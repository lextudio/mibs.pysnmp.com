# SNMP MIB module (CTRON-APPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-APPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:32 2024
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

(nwRtrProtoSuites,) = mibBuilder.importSymbols(
    "ROUTER-OIDS",
    "nwRtrProtoSuites")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NwAppnRouter_ObjectIdentity = ObjectIdentity
nwAppnRouter = _NwAppnRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5)
)
_NwAppnMibs_ObjectIdentity = ObjectIdentity
nwAppnMibs = _NwAppnMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 1)
)
_NwAppnMibRevText_Type = DisplayString
_NwAppnMibRevText_Object = MibScalar
nwAppnMibRevText = _NwAppnMibRevText_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 1, 1),
    _NwAppnMibRevText_Type()
)
nwAppnMibRevText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnMibRevText.setStatus("mandatory")
_NwAppnComponents_ObjectIdentity = ObjectIdentity
nwAppnComponents = _NwAppnComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2)
)
_NwAppnSystem_ObjectIdentity = ObjectIdentity
nwAppnSystem = _NwAppnSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1)
)
_NwAppnSysConfig_ObjectIdentity = ObjectIdentity
nwAppnSysConfig = _NwAppnSysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1)
)


class _NwAppnSysRouterId_Type(DisplayString):
    """Custom type nwAppnSysRouterId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_NwAppnSysRouterId_Type.__name__ = "DisplayString"
_NwAppnSysRouterId_Object = MibScalar
nwAppnSysRouterId = _NwAppnSysRouterId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 1),
    _NwAppnSysRouterId_Type()
)
nwAppnSysRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysRouterId.setStatus("mandatory")
_NwAppnSysCfgLocalNode_ObjectIdentity = ObjectIdentity
nwAppnSysCfgLocalNode = _NwAppnSysCfgLocalNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 2)
)


class _NwAppnSysNodeType_Type(Integer32):
    """Custom type nwAppnSysNodeType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("networknode", 1)
    )


_NwAppnSysNodeType_Type.__name__ = "Integer32"
_NwAppnSysNodeType_Object = MibScalar
nwAppnSysNodeType = _NwAppnSysNodeType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 2, 1),
    _NwAppnSysNodeType_Type()
)
nwAppnSysNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnSysNodeType.setStatus("mandatory")


class _NwAppnSysCpAlias_Type(DisplayString):
    """Custom type nwAppnSysCpAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_NwAppnSysCpAlias_Type.__name__ = "DisplayString"
_NwAppnSysCpAlias_Object = MibScalar
nwAppnSysCpAlias = _NwAppnSysCpAlias_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 2, 2),
    _NwAppnSysCpAlias_Type()
)
nwAppnSysCpAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysCpAlias.setStatus("mandatory")


class _NwAppnSysModeCosMap_Type(Integer32):
    """Custom type nwAppnSysModeCosMap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_NwAppnSysModeCosMap_Type.__name__ = "Integer32"
_NwAppnSysModeCosMap_Object = MibScalar
nwAppnSysModeCosMap = _NwAppnSysModeCosMap_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 2, 3),
    _NwAppnSysModeCosMap_Type()
)
nwAppnSysModeCosMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysModeCosMap.setStatus("mandatory")


class _NwAppnSysMdsSupport_Type(Integer32):
    """Custom type nwAppnSysMdsSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_NwAppnSysMdsSupport_Type.__name__ = "Integer32"
_NwAppnSysMdsSupport_Object = MibScalar
nwAppnSysMdsSupport = _NwAppnSysMdsSupport_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 2, 4),
    _NwAppnSysMdsSupport_Type()
)
nwAppnSysMdsSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysMdsSupport.setStatus("mandatory")


class _NwAppnSysMaxLocates_Type(Integer32):
    """Custom type nwAppnSysMaxLocates based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NwAppnSysMaxLocates_Type.__name__ = "Integer32"
_NwAppnSysMaxLocates_Object = MibScalar
nwAppnSysMaxLocates = _NwAppnSysMaxLocates_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 2, 6),
    _NwAppnSysMaxLocates_Type()
)
nwAppnSysMaxLocates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysMaxLocates.setStatus("mandatory")


class _NwAppnSysDirCacheSize_Type(Integer32):
    """Custom type nwAppnSysDirCacheSize based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NwAppnSysDirCacheSize_Type.__name__ = "Integer32"
_NwAppnSysDirCacheSize_Object = MibScalar
nwAppnSysDirCacheSize = _NwAppnSysDirCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 2, 7),
    _NwAppnSysDirCacheSize_Type()
)
nwAppnSysDirCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysDirCacheSize.setStatus("mandatory")


class _NwAppnSysMaxDirEntries_Type(Integer32):
    """Custom type nwAppnSysMaxDirEntries based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NwAppnSysMaxDirEntries_Type.__name__ = "Integer32"
_NwAppnSysMaxDirEntries_Object = MibScalar
nwAppnSysMaxDirEntries = _NwAppnSysMaxDirEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 2, 8),
    _NwAppnSysMaxDirEntries_Type()
)
nwAppnSysMaxDirEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysMaxDirEntries.setStatus("mandatory")


class _NwAppnSysLocateTimeout_Type(Integer32):
    """Custom type nwAppnSysLocateTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NwAppnSysLocateTimeout_Type.__name__ = "Integer32"
_NwAppnSysLocateTimeout_Object = MibScalar
nwAppnSysLocateTimeout = _NwAppnSysLocateTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 2, 9),
    _NwAppnSysLocateTimeout_Type()
)
nwAppnSysLocateTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysLocateTimeout.setStatus("mandatory")


class _NwAppnSysRegCds_Type(Integer32):
    """Custom type nwAppnSysRegCds based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_NwAppnSysRegCds_Type.__name__ = "Integer32"
_NwAppnSysRegCds_Object = MibScalar
nwAppnSysRegCds = _NwAppnSysRegCds_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 2, 10),
    _NwAppnSysRegCds_Type()
)
nwAppnSysRegCds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysRegCds.setStatus("mandatory")


class _NwAppnSysMdsSendQSize_Type(Integer32):
    """Custom type nwAppnSysMdsSendQSize based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NwAppnSysMdsSendQSize_Type.__name__ = "Integer32"
_NwAppnSysMdsSendQSize_Object = MibScalar
nwAppnSysMdsSendQSize = _NwAppnSysMdsSendQSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 2, 11),
    _NwAppnSysMdsSendQSize_Type()
)
nwAppnSysMdsSendQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysMdsSendQSize.setStatus("mandatory")


class _NwAppnSysCosSize_Type(Integer32):
    """Custom type nwAppnSysCosSize based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NwAppnSysCosSize_Type.__name__ = "Integer32"
_NwAppnSysCosSize_Object = MibScalar
nwAppnSysCosSize = _NwAppnSysCosSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 2, 12),
    _NwAppnSysCosSize_Type()
)
nwAppnSysCosSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysCosSize.setStatus("mandatory")


class _NwAppnSysTreeSize_Type(Integer32):
    """Custom type nwAppnSysTreeSize based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NwAppnSysTreeSize_Type.__name__ = "Integer32"
_NwAppnSysTreeSize_Object = MibScalar
nwAppnSysTreeSize = _NwAppnSysTreeSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 2, 13),
    _NwAppnSysTreeSize_Type()
)
nwAppnSysTreeSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysTreeSize.setStatus("mandatory")


class _NwAppnSysTreeUseLimit_Type(Integer32):
    """Custom type nwAppnSysTreeUseLimit based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NwAppnSysTreeUseLimit_Type.__name__ = "Integer32"
_NwAppnSysTreeUseLimit_Object = MibScalar
nwAppnSysTreeUseLimit = _NwAppnSysTreeUseLimit_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 2, 14),
    _NwAppnSysTreeUseLimit_Type()
)
nwAppnSysTreeUseLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysTreeUseLimit.setStatus("mandatory")


class _NwAppnSysMaxTdmNodes_Type(Integer32):
    """Custom type nwAppnSysMaxTdmNodes based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NwAppnSysMaxTdmNodes_Type.__name__ = "Integer32"
_NwAppnSysMaxTdmNodes_Object = MibScalar
nwAppnSysMaxTdmNodes = _NwAppnSysMaxTdmNodes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 2, 15),
    _NwAppnSysMaxTdmNodes_Type()
)
nwAppnSysMaxTdmNodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysMaxTdmNodes.setStatus("mandatory")


class _NwAppnSysMaxTdmTGs_Type(Integer32):
    """Custom type nwAppnSysMaxTdmTGs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NwAppnSysMaxTdmTGs_Type.__name__ = "Integer32"
_NwAppnSysMaxTdmTGs_Object = MibScalar
nwAppnSysMaxTdmTGs = _NwAppnSysMaxTdmTGs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 2, 16),
    _NwAppnSysMaxTdmTGs_Type()
)
nwAppnSysMaxTdmTGs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysMaxTdmTGs.setStatus("mandatory")


class _NwAppnSysMaxIsrSessions_Type(Integer32):
    """Custom type nwAppnSysMaxIsrSessions based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NwAppnSysMaxIsrSessions_Type.__name__ = "Integer32"
_NwAppnSysMaxIsrSessions_Object = MibScalar
nwAppnSysMaxIsrSessions = _NwAppnSysMaxIsrSessions_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 2, 18),
    _NwAppnSysMaxIsrSessions_Type()
)
nwAppnSysMaxIsrSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysMaxIsrSessions.setStatus("mandatory")


class _NwAppnSysIsrUpperThresh_Type(Integer32):
    """Custom type nwAppnSysIsrUpperThresh based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NwAppnSysIsrUpperThresh_Type.__name__ = "Integer32"
_NwAppnSysIsrUpperThresh_Object = MibScalar
nwAppnSysIsrUpperThresh = _NwAppnSysIsrUpperThresh_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 2, 19),
    _NwAppnSysIsrUpperThresh_Type()
)
nwAppnSysIsrUpperThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysIsrUpperThresh.setStatus("mandatory")


class _NwAppnSysIsrLowerThresh_Type(Integer32):
    """Custom type nwAppnSysIsrLowerThresh based on Integer32"""
    defaultValue = 800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NwAppnSysIsrLowerThresh_Type.__name__ = "Integer32"
_NwAppnSysIsrLowerThresh_Object = MibScalar
nwAppnSysIsrLowerThresh = _NwAppnSysIsrLowerThresh_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 2, 20),
    _NwAppnSysIsrLowerThresh_Type()
)
nwAppnSysIsrLowerThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysIsrLowerThresh.setStatus("mandatory")


class _NwAppnSysIsrMaxRuSize_Type(Integer32):
    """Custom type nwAppnSysIsrMaxRuSize based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NwAppnSysIsrMaxRuSize_Type.__name__ = "Integer32"
_NwAppnSysIsrMaxRuSize_Object = MibScalar
nwAppnSysIsrMaxRuSize = _NwAppnSysIsrMaxRuSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 2, 21),
    _NwAppnSysIsrMaxRuSize_Type()
)
nwAppnSysIsrMaxRuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysIsrMaxRuSize.setStatus("mandatory")


class _NwAppnSysIsrRcvPaceWind_Type(Integer32):
    """Custom type nwAppnSysIsrRcvPaceWind based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_NwAppnSysIsrRcvPaceWind_Type.__name__ = "Integer32"
_NwAppnSysIsrRcvPaceWind_Object = MibScalar
nwAppnSysIsrRcvPaceWind = _NwAppnSysIsrRcvPaceWind_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 2, 22),
    _NwAppnSysIsrRcvPaceWind_Type()
)
nwAppnSysIsrRcvPaceWind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysIsrRcvPaceWind.setStatus("mandatory")


class _NwAppnSysRtAddResist_Type(Integer32):
    """Custom type nwAppnSysRtAddResist based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NwAppnSysRtAddResist_Type.__name__ = "Integer32"
_NwAppnSysRtAddResist_Object = MibScalar
nwAppnSysRtAddResist = _NwAppnSysRtAddResist_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 2, 23),
    _NwAppnSysRtAddResist_Type()
)
nwAppnSysRtAddResist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysRtAddResist.setStatus("mandatory")


class _NwAppnSysStopType_Type(Integer32):
    """Custom type nwAppnSysStopType based on Integer32"""
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
        *(("abort", 1),
          ("immediate", 2),
          ("quiesce", 3),
          ("quiesceIsr", 4))
    )


_NwAppnSysStopType_Type.__name__ = "Integer32"
_NwAppnSysStopType_Object = MibScalar
nwAppnSysStopType = _NwAppnSysStopType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 2, 24),
    _NwAppnSysStopType_Type()
)
nwAppnSysStopType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysStopType.setStatus("mandatory")


class _NwAppnSysBlockNum_Type(DisplayString):
    """Custom type nwAppnSysBlockNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_NwAppnSysBlockNum_Type.__name__ = "DisplayString"
_NwAppnSysBlockNum_Object = MibScalar
nwAppnSysBlockNum = _NwAppnSysBlockNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 2, 25),
    _NwAppnSysBlockNum_Type()
)
nwAppnSysBlockNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysBlockNum.setStatus("mandatory")


class _NwAppnSysIdNum_Type(DisplayString):
    """Custom type nwAppnSysIdNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_NwAppnSysIdNum_Type.__name__ = "DisplayString"
_NwAppnSysIdNum_Object = MibScalar
nwAppnSysIdNum = _NwAppnSysIdNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 2, 26),
    _NwAppnSysIdNum_Type()
)
nwAppnSysIdNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysIdNum.setStatus("mandatory")
_NwAppnSysCfgTables_ObjectIdentity = ObjectIdentity
nwAppnSysCfgTables = _NwAppnSysCfgTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 3)
)
_NwAppnSysLuTable_Object = MibTable
nwAppnSysLuTable = _NwAppnSysLuTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    nwAppnSysLuTable.setStatus("mandatory")
_NwAppnSysLuEntry_Object = MibTableRow
nwAppnSysLuEntry = _NwAppnSysLuEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 3, 1, 1)
)
nwAppnSysLuEntry.setIndexNames(
    (0, "CTRON-APPN-MIB", "nwAppnSysCpName"),
    (0, "CTRON-APPN-MIB", "nwAppnSysLuName"),
)
if mibBuilder.loadTexts:
    nwAppnSysLuEntry.setStatus("mandatory")


class _NwAppnSysCpName_Type(DisplayString):
    """Custom type nwAppnSysCpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_NwAppnSysCpName_Type.__name__ = "DisplayString"
_NwAppnSysCpName_Object = MibTableColumn
nwAppnSysCpName = _NwAppnSysCpName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 3, 1, 1, 1),
    _NwAppnSysCpName_Type()
)
nwAppnSysCpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysCpName.setStatus("mandatory")


class _NwAppnSysLuName_Type(DisplayString):
    """Custom type nwAppnSysLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_NwAppnSysLuName_Type.__name__ = "DisplayString"
_NwAppnSysLuName_Object = MibTableColumn
nwAppnSysLuName = _NwAppnSysLuName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 3, 1, 1, 2),
    _NwAppnSysLuName_Type()
)
nwAppnSysLuName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysLuName.setStatus("mandatory")


class _NwAppnSysLuControl_Type(Integer32):
    """Custom type nwAppnSysLuControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("other", 1))
    )


_NwAppnSysLuControl_Type.__name__ = "Integer32"
_NwAppnSysLuControl_Object = MibTableColumn
nwAppnSysLuControl = _NwAppnSysLuControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 1, 3, 1, 1, 3),
    _NwAppnSysLuControl_Type()
)
nwAppnSysLuControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysLuControl.setStatus("mandatory")
_NwAppnSysAdministration_ObjectIdentity = ObjectIdentity
nwAppnSysAdministration = _NwAppnSysAdministration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 2)
)


class _NwAppnSysAdminStatus_Type(Integer32):
    """Custom type nwAppnSysAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwAppnSysAdminStatus_Type.__name__ = "Integer32"
_NwAppnSysAdminStatus_Object = MibScalar
nwAppnSysAdminStatus = _NwAppnSysAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 2, 1),
    _NwAppnSysAdminStatus_Type()
)
nwAppnSysAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysAdminStatus.setStatus("mandatory")


class _NwAppnSysOperStatus_Type(Integer32):
    """Custom type nwAppnSysOperStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1),
          ("pendingDisable", 4),
          ("pendingEnable", 5))
    )


_NwAppnSysOperStatus_Type.__name__ = "Integer32"
_NwAppnSysOperStatus_Object = MibScalar
nwAppnSysOperStatus = _NwAppnSysOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 2, 2),
    _NwAppnSysOperStatus_Type()
)
nwAppnSysOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnSysOperStatus.setStatus("mandatory")


class _NwAppnSysAdminReset_Type(Integer32):
    """Custom type nwAppnSysAdminReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_NwAppnSysAdminReset_Type.__name__ = "Integer32"
_NwAppnSysAdminReset_Object = MibScalar
nwAppnSysAdminReset = _NwAppnSysAdminReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 2, 3),
    _NwAppnSysAdminReset_Type()
)
nwAppnSysAdminReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnSysAdminReset.setStatus("mandatory")
_NwAppnSysOperationalTime_Type = TimeTicks
_NwAppnSysOperationalTime_Object = MibScalar
nwAppnSysOperationalTime = _NwAppnSysOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 2, 4),
    _NwAppnSysOperationalTime_Type()
)
nwAppnSysOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnSysOperationalTime.setStatus("mandatory")
_NwAppnSysVersion_Type = DisplayString
_NwAppnSysVersion_Object = MibScalar
nwAppnSysVersion = _NwAppnSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 1, 2, 5),
    _NwAppnSysVersion_Type()
)
nwAppnSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnSysVersion.setStatus("mandatory")
_NwAppnForwarding_ObjectIdentity = ObjectIdentity
nwAppnForwarding = _NwAppnForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2)
)
_NwAppnFwdSystem_ObjectIdentity = ObjectIdentity
nwAppnFwdSystem = _NwAppnFwdSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 1)
)
_NwAppnFwdCounters_ObjectIdentity = ObjectIdentity
nwAppnFwdCounters = _NwAppnFwdCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 1, 1)
)


class _NwAppnFwdCtrAdminStatus_Type(Integer32):
    """Custom type nwAppnFwdCtrAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwAppnFwdCtrAdminStatus_Type.__name__ = "Integer32"
_NwAppnFwdCtrAdminStatus_Object = MibScalar
nwAppnFwdCtrAdminStatus = _NwAppnFwdCtrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 1, 1, 1),
    _NwAppnFwdCtrAdminStatus_Type()
)
nwAppnFwdCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdCtrAdminStatus.setStatus("mandatory")


class _NwAppnFwdCtrReset_Type(Integer32):
    """Custom type nwAppnFwdCtrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_NwAppnFwdCtrReset_Type.__name__ = "Integer32"
_NwAppnFwdCtrReset_Object = MibScalar
nwAppnFwdCtrReset = _NwAppnFwdCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 1, 1, 2),
    _NwAppnFwdCtrReset_Type()
)
nwAppnFwdCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdCtrReset.setStatus("mandatory")
_NwAppnFwdCtrOperationalTime_Type = TimeTicks
_NwAppnFwdCtrOperationalTime_Object = MibScalar
nwAppnFwdCtrOperationalTime = _NwAppnFwdCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 1, 1, 3),
    _NwAppnFwdCtrOperationalTime_Type()
)
nwAppnFwdCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdCtrOperationalTime.setStatus("mandatory")
_NwAppnFwdCtrInMus_Type = Counter32
_NwAppnFwdCtrInMus_Object = MibScalar
nwAppnFwdCtrInMus = _NwAppnFwdCtrInMus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 1, 1, 4),
    _NwAppnFwdCtrInMus_Type()
)
nwAppnFwdCtrInMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdCtrInMus.setStatus("mandatory")
_NwAppnFwdCtrOutMus_Type = Counter32
_NwAppnFwdCtrOutMus_Object = MibScalar
nwAppnFwdCtrOutMus = _NwAppnFwdCtrOutMus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 1, 1, 5),
    _NwAppnFwdCtrOutMus_Type()
)
nwAppnFwdCtrOutMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdCtrOutMus.setStatus("mandatory")
_NwAppnFwdCtrFwdMus_Type = Counter32
_NwAppnFwdCtrFwdMus_Object = MibScalar
nwAppnFwdCtrFwdMus = _NwAppnFwdCtrFwdMus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 1, 1, 6),
    _NwAppnFwdCtrFwdMus_Type()
)
nwAppnFwdCtrFwdMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdCtrFwdMus.setStatus("mandatory")
_NwAppnFwdCtrFilteredMus_Type = Counter32
_NwAppnFwdCtrFilteredMus_Object = MibScalar
nwAppnFwdCtrFilteredMus = _NwAppnFwdCtrFilteredMus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 1, 1, 7),
    _NwAppnFwdCtrFilteredMus_Type()
)
nwAppnFwdCtrFilteredMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdCtrFilteredMus.setStatus("mandatory")
_NwAppnFwdCtrDiscardMus_Type = Counter32
_NwAppnFwdCtrDiscardMus_Object = MibScalar
nwAppnFwdCtrDiscardMus = _NwAppnFwdCtrDiscardMus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 1, 1, 8),
    _NwAppnFwdCtrDiscardMus_Type()
)
nwAppnFwdCtrDiscardMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdCtrDiscardMus.setStatus("mandatory")
_NwAppnFwdCtrAddrErrMus_Type = Counter32
_NwAppnFwdCtrAddrErrMus_Object = MibScalar
nwAppnFwdCtrAddrErrMus = _NwAppnFwdCtrAddrErrMus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 1, 1, 9),
    _NwAppnFwdCtrAddrErrMus_Type()
)
nwAppnFwdCtrAddrErrMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdCtrAddrErrMus.setStatus("mandatory")
_NwAppnFwdCtrLenErrMus_Type = Counter32
_NwAppnFwdCtrLenErrMus_Object = MibScalar
nwAppnFwdCtrLenErrMus = _NwAppnFwdCtrLenErrMus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 1, 1, 10),
    _NwAppnFwdCtrLenErrMus_Type()
)
nwAppnFwdCtrLenErrMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdCtrLenErrMus.setStatus("mandatory")
_NwAppnFwdCtrHdrErrMus_Type = Counter32
_NwAppnFwdCtrHdrErrMus_Object = MibScalar
nwAppnFwdCtrHdrErrMus = _NwAppnFwdCtrHdrErrMus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 1, 1, 11),
    _NwAppnFwdCtrHdrErrMus_Type()
)
nwAppnFwdCtrHdrErrMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdCtrHdrErrMus.setStatus("mandatory")
_NwAppnFwdCtrInBytes_Type = Counter32
_NwAppnFwdCtrInBytes_Object = MibScalar
nwAppnFwdCtrInBytes = _NwAppnFwdCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 1, 1, 12),
    _NwAppnFwdCtrInBytes_Type()
)
nwAppnFwdCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdCtrInBytes.setStatus("mandatory")
_NwAppnFwdCtrOutBytes_Type = Counter32
_NwAppnFwdCtrOutBytes_Object = MibScalar
nwAppnFwdCtrOutBytes = _NwAppnFwdCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 1, 1, 13),
    _NwAppnFwdCtrOutBytes_Type()
)
nwAppnFwdCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdCtrOutBytes.setStatus("mandatory")
_NwAppnFwdCtrFwdBytes_Type = Counter32
_NwAppnFwdCtrFwdBytes_Object = MibScalar
nwAppnFwdCtrFwdBytes = _NwAppnFwdCtrFwdBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 1, 1, 14),
    _NwAppnFwdCtrFwdBytes_Type()
)
nwAppnFwdCtrFwdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdCtrFwdBytes.setStatus("mandatory")
_NwAppnFwdCtrFilteredBytes_Type = Counter32
_NwAppnFwdCtrFilteredBytes_Object = MibScalar
nwAppnFwdCtrFilteredBytes = _NwAppnFwdCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 1, 1, 15),
    _NwAppnFwdCtrFilteredBytes_Type()
)
nwAppnFwdCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdCtrFilteredBytes.setStatus("mandatory")
_NwAppnFwdCtrDiscardBytes_Type = Counter32
_NwAppnFwdCtrDiscardBytes_Object = MibScalar
nwAppnFwdCtrDiscardBytes = _NwAppnFwdCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 1, 1, 16),
    _NwAppnFwdCtrDiscardBytes_Type()
)
nwAppnFwdCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdCtrDiscardBytes.setStatus("mandatory")
_NwAppnFwdCtrHostInMus_Type = Counter32
_NwAppnFwdCtrHostInMus_Object = MibScalar
nwAppnFwdCtrHostInMus = _NwAppnFwdCtrHostInMus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 1, 1, 17),
    _NwAppnFwdCtrHostInMus_Type()
)
nwAppnFwdCtrHostInMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdCtrHostInMus.setStatus("mandatory")
_NwAppnFwdCtrHostOutMus_Type = Counter32
_NwAppnFwdCtrHostOutMus_Object = MibScalar
nwAppnFwdCtrHostOutMus = _NwAppnFwdCtrHostOutMus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 1, 1, 18),
    _NwAppnFwdCtrHostOutMus_Type()
)
nwAppnFwdCtrHostOutMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdCtrHostOutMus.setStatus("mandatory")
_NwAppnFwdCtrHostDiscardMus_Type = Counter32
_NwAppnFwdCtrHostDiscardMus_Object = MibScalar
nwAppnFwdCtrHostDiscardMus = _NwAppnFwdCtrHostDiscardMus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 1, 1, 19),
    _NwAppnFwdCtrHostDiscardMus_Type()
)
nwAppnFwdCtrHostDiscardMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdCtrHostDiscardMus.setStatus("mandatory")
_NwAppnFwdCtrHostInBytes_Type = Counter32
_NwAppnFwdCtrHostInBytes_Object = MibScalar
nwAppnFwdCtrHostInBytes = _NwAppnFwdCtrHostInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 1, 1, 20),
    _NwAppnFwdCtrHostInBytes_Type()
)
nwAppnFwdCtrHostInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdCtrHostInBytes.setStatus("mandatory")
_NwAppnFwdCtrHostOutBytes_Type = Counter32
_NwAppnFwdCtrHostOutBytes_Object = MibScalar
nwAppnFwdCtrHostOutBytes = _NwAppnFwdCtrHostOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 1, 1, 21),
    _NwAppnFwdCtrHostOutBytes_Type()
)
nwAppnFwdCtrHostOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdCtrHostOutBytes.setStatus("mandatory")
_NwAppnFwdCtrHostDiscardBytes_Type = Counter32
_NwAppnFwdCtrHostDiscardBytes_Object = MibScalar
nwAppnFwdCtrHostDiscardBytes = _NwAppnFwdCtrHostDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 1, 1, 22),
    _NwAppnFwdCtrHostDiscardBytes_Type()
)
nwAppnFwdCtrHostDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdCtrHostDiscardBytes.setStatus("mandatory")
_NwAppnFwdInterfaces_ObjectIdentity = ObjectIdentity
nwAppnFwdInterfaces = _NwAppnFwdInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2)
)
_NwAppnFwdIfConfig_ObjectIdentity = ObjectIdentity
nwAppnFwdIfConfig = _NwAppnFwdIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1)
)
_NwAppnFwdIfTable_Object = MibTable
nwAppnFwdIfTable = _NwAppnFwdIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nwAppnFwdIfTable.setStatus("mandatory")
_NwAppnFwdIfEntry_Object = MibTableRow
nwAppnFwdIfEntry = _NwAppnFwdIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 1, 1)
)
nwAppnFwdIfEntry.setIndexNames(
    (0, "CTRON-APPN-MIB", "nwAppnFwdIfIndex"),
)
if mibBuilder.loadTexts:
    nwAppnFwdIfEntry.setStatus("mandatory")
_NwAppnFwdIfIndex_Type = Integer32
_NwAppnFwdIfIndex_Object = MibTableColumn
nwAppnFwdIfIndex = _NwAppnFwdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 1, 1, 1),
    _NwAppnFwdIfIndex_Type()
)
nwAppnFwdIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfIndex.setStatus("mandatory")


class _NwAppnFwdIfAdminStatus_Type(Integer32):
    """Custom type nwAppnFwdIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwAppnFwdIfAdminStatus_Type.__name__ = "Integer32"
_NwAppnFwdIfAdminStatus_Object = MibTableColumn
nwAppnFwdIfAdminStatus = _NwAppnFwdIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 1, 1, 2),
    _NwAppnFwdIfAdminStatus_Type()
)
nwAppnFwdIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdIfAdminStatus.setStatus("mandatory")


class _NwAppnFwdIfOperStatus_Type(Integer32):
    """Custom type nwAppnFwdIfOperStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1),
          ("pendingDisable", 4),
          ("pendingEnable", 5))
    )


_NwAppnFwdIfOperStatus_Type.__name__ = "Integer32"
_NwAppnFwdIfOperStatus_Object = MibTableColumn
nwAppnFwdIfOperStatus = _NwAppnFwdIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 1, 1, 3),
    _NwAppnFwdIfOperStatus_Type()
)
nwAppnFwdIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfOperStatus.setStatus("mandatory")
_NwAppnFwdIfOperationalTime_Type = TimeTicks
_NwAppnFwdIfOperationalTime_Object = MibTableColumn
nwAppnFwdIfOperationalTime = _NwAppnFwdIfOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 1, 1, 4),
    _NwAppnFwdIfOperationalTime_Type()
)
nwAppnFwdIfOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfOperationalTime.setStatus("mandatory")


class _NwAppnFwdIfControl_Type(Integer32):
    """Custom type nwAppnFwdIfControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("other", 1)
    )


_NwAppnFwdIfControl_Type.__name__ = "Integer32"
_NwAppnFwdIfControl_Object = MibTableColumn
nwAppnFwdIfControl = _NwAppnFwdIfControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 1, 1, 5),
    _NwAppnFwdIfControl_Type()
)
nwAppnFwdIfControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdIfControl.setStatus("mandatory")
_NwAppnFwdIfMtu_Type = Integer32
_NwAppnFwdIfMtu_Object = MibTableColumn
nwAppnFwdIfMtu = _NwAppnFwdIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 1, 1, 6),
    _NwAppnFwdIfMtu_Type()
)
nwAppnFwdIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdIfMtu.setStatus("mandatory")


class _NwAppnFwdIfForwarding_Type(Integer32):
    """Custom type nwAppnFwdIfForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwAppnFwdIfForwarding_Type.__name__ = "Integer32"
_NwAppnFwdIfForwarding_Object = MibTableColumn
nwAppnFwdIfForwarding = _NwAppnFwdIfForwarding_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 1, 1, 7),
    _NwAppnFwdIfForwarding_Type()
)
nwAppnFwdIfForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdIfForwarding.setStatus("mandatory")


class _NwAppnFwdIfFrameType_Type(Integer32):
    """Custom type nwAppnFwdIfFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("i8022", 4),
          ("other", 1),
          ("sync", 8))
    )


_NwAppnFwdIfFrameType_Type.__name__ = "Integer32"
_NwAppnFwdIfFrameType_Object = MibTableColumn
nwAppnFwdIfFrameType = _NwAppnFwdIfFrameType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 1, 1, 8),
    _NwAppnFwdIfFrameType_Type()
)
nwAppnFwdIfFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdIfFrameType.setStatus("mandatory")
_NwAppnFwdIfAclIdentifier_Type = Integer32
_NwAppnFwdIfAclIdentifier_Object = MibTableColumn
nwAppnFwdIfAclIdentifier = _NwAppnFwdIfAclIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 1, 1, 9),
    _NwAppnFwdIfAclIdentifier_Type()
)
nwAppnFwdIfAclIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdIfAclIdentifier.setStatus("mandatory")


class _NwAppnFwdIfAclStatus_Type(Integer32):
    """Custom type nwAppnFwdIfAclStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwAppnFwdIfAclStatus_Type.__name__ = "Integer32"
_NwAppnFwdIfAclStatus_Object = MibTableColumn
nwAppnFwdIfAclStatus = _NwAppnFwdIfAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 1, 1, 10),
    _NwAppnFwdIfAclStatus_Type()
)
nwAppnFwdIfAclStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdIfAclStatus.setStatus("mandatory")


class _NwAppnFwdIfCacheControl_Type(Integer32):
    """Custom type nwAppnFwdIfCacheControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_NwAppnFwdIfCacheControl_Type.__name__ = "Integer32"
_NwAppnFwdIfCacheControl_Object = MibTableColumn
nwAppnFwdIfCacheControl = _NwAppnFwdIfCacheControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 1, 1, 11),
    _NwAppnFwdIfCacheControl_Type()
)
nwAppnFwdIfCacheControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdIfCacheControl.setStatus("mandatory")
_NwAppnFwdIfCacheEntries_Type = Counter32
_NwAppnFwdIfCacheEntries_Object = MibTableColumn
nwAppnFwdIfCacheEntries = _NwAppnFwdIfCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 1, 1, 12),
    _NwAppnFwdIfCacheEntries_Type()
)
nwAppnFwdIfCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfCacheEntries.setStatus("mandatory")
_NwAppnFwdIfCacheHits_Type = Counter32
_NwAppnFwdIfCacheHits_Object = MibTableColumn
nwAppnFwdIfCacheHits = _NwAppnFwdIfCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 1, 1, 13),
    _NwAppnFwdIfCacheHits_Type()
)
nwAppnFwdIfCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfCacheHits.setStatus("mandatory")
_NwAppnFwdIfCacheMisses_Type = Counter32
_NwAppnFwdIfCacheMisses_Object = MibTableColumn
nwAppnFwdIfCacheMisses = _NwAppnFwdIfCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 1, 1, 14),
    _NwAppnFwdIfCacheMisses_Type()
)
nwAppnFwdIfCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfCacheMisses.setStatus("mandatory")
_NwAppnExtensionTable_Object = MibTable
nwAppnExtensionTable = _NwAppnExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    nwAppnExtensionTable.setStatus("mandatory")
_NwAppnExtEntry_Object = MibTableRow
nwAppnExtEntry = _NwAppnExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1)
)
nwAppnExtEntry.setIndexNames(
    (0, "CTRON-APPN-MIB", "nwAppnExtIfIndex"),
)
if mibBuilder.loadTexts:
    nwAppnExtEntry.setStatus("mandatory")
_NwAppnExtIfIndex_Type = Integer32
_NwAppnExtIfIndex_Object = MibTableColumn
nwAppnExtIfIndex = _NwAppnExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 1),
    _NwAppnExtIfIndex_Type()
)
nwAppnExtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnExtIfIndex.setStatus("mandatory")


class _NwAppnExtIfPortName_Type(DisplayString):
    """Custom type nwAppnExtIfPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_NwAppnExtIfPortName_Type.__name__ = "DisplayString"
_NwAppnExtIfPortName_Object = MibTableColumn
nwAppnExtIfPortName = _NwAppnExtIfPortName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 2),
    _NwAppnExtIfPortName_Type()
)
nwAppnExtIfPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnExtIfPortName.setStatus("mandatory")


class _NwAppnExtIfPortType_Type(Integer32):
    """Custom type nwAppnExtIfPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonswitched", 1),
          ("satf", 3),
          ("switched", 2))
    )


_NwAppnExtIfPortType_Type.__name__ = "Integer32"
_NwAppnExtIfPortType_Object = MibTableColumn
nwAppnExtIfPortType = _NwAppnExtIfPortType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 4),
    _NwAppnExtIfPortType_Type()
)
nwAppnExtIfPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnExtIfPortType.setStatus("mandatory")


class _NwAppnExtIfDlcType_Type(Integer32):
    """Custom type nwAppnExtIfDlcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("llc2", 1),
          ("sdlc", 2),
          ("x25", 3))
    )


_NwAppnExtIfDlcType_Type.__name__ = "Integer32"
_NwAppnExtIfDlcType_Object = MibTableColumn
nwAppnExtIfDlcType = _NwAppnExtIfDlcType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 5),
    _NwAppnExtIfDlcType_Type()
)
nwAppnExtIfDlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnExtIfDlcType.setStatus("mandatory")


class _NwAppnExtIfMaxRBtuSize_Type(Integer32):
    """Custom type nwAppnExtIfMaxRBtuSize based on Integer32"""
    defaultValue = 2048

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(99, 65535),
    )


_NwAppnExtIfMaxRBtuSize_Type.__name__ = "Integer32"
_NwAppnExtIfMaxRBtuSize_Object = MibTableColumn
nwAppnExtIfMaxRBtuSize = _NwAppnExtIfMaxRBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 6),
    _NwAppnExtIfMaxRBtuSize_Type()
)
nwAppnExtIfMaxRBtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnExtIfMaxRBtuSize.setStatus("mandatory")


class _NwAppnExtIfTotLsActLim_Type(Integer32):
    """Custom type nwAppnExtIfTotLsActLim based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_NwAppnExtIfTotLsActLim_Type.__name__ = "Integer32"
_NwAppnExtIfTotLsActLim_Object = MibTableColumn
nwAppnExtIfTotLsActLim = _NwAppnExtIfTotLsActLim_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 7),
    _NwAppnExtIfTotLsActLim_Type()
)
nwAppnExtIfTotLsActLim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnExtIfTotLsActLim.setStatus("mandatory")


class _NwAppnExtIfInbLsActLim_Type(Integer32):
    """Custom type nwAppnExtIfInbLsActLim based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_NwAppnExtIfInbLsActLim_Type.__name__ = "Integer32"
_NwAppnExtIfInbLsActLim_Object = MibTableColumn
nwAppnExtIfInbLsActLim = _NwAppnExtIfInbLsActLim_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 8),
    _NwAppnExtIfInbLsActLim_Type()
)
nwAppnExtIfInbLsActLim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnExtIfInbLsActLim.setStatus("mandatory")


class _NwAppnExtIfOutbLsActLim_Type(Integer32):
    """Custom type nwAppnExtIfOutbLsActLim based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_NwAppnExtIfOutbLsActLim_Type.__name__ = "Integer32"
_NwAppnExtIfOutbLsActLim_Object = MibTableColumn
nwAppnExtIfOutbLsActLim = _NwAppnExtIfOutbLsActLim_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 9),
    _NwAppnExtIfOutbLsActLim_Type()
)
nwAppnExtIfOutbLsActLim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnExtIfOutbLsActLim.setStatus("mandatory")


class _NwAppnExtIfLocalLsRole_Type(Integer32):
    """Custom type nwAppnExtIfLocalLsRole based on Integer32"""
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
        *(("negotiable", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_NwAppnExtIfLocalLsRole_Type.__name__ = "Integer32"
_NwAppnExtIfLocalLsRole_Object = MibTableColumn
nwAppnExtIfLocalLsRole = _NwAppnExtIfLocalLsRole_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 10),
    _NwAppnExtIfLocalLsRole_Type()
)
nwAppnExtIfLocalLsRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnExtIfLocalLsRole.setStatus("mandatory")


class _NwAppnExtIfActXidXchgLimit_Type(Integer32):
    """Custom type nwAppnExtIfActXidXchgLimit based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NwAppnExtIfActXidXchgLimit_Type.__name__ = "Integer32"
_NwAppnExtIfActXidXchgLimit_Object = MibTableColumn
nwAppnExtIfActXidXchgLimit = _NwAppnExtIfActXidXchgLimit_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 11),
    _NwAppnExtIfActXidXchgLimit_Type()
)
nwAppnExtIfActXidXchgLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnExtIfActXidXchgLimit.setStatus("mandatory")


class _NwAppnExtIfNonActXidXchgLimit_Type(Integer32):
    """Custom type nwAppnExtIfNonActXidXchgLimit based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NwAppnExtIfNonActXidXchgLimit_Type.__name__ = "Integer32"
_NwAppnExtIfNonActXidXchgLimit_Object = MibTableColumn
nwAppnExtIfNonActXidXchgLimit = _NwAppnExtIfNonActXidXchgLimit_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 12),
    _NwAppnExtIfNonActXidXchgLimit_Type()
)
nwAppnExtIfNonActXidXchgLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnExtIfNonActXidXchgLimit.setStatus("mandatory")


class _NwAppnExtIfLsXmitRcvCap_Type(Integer32):
    """Custom type nwAppnExtIfLsXmitRcvCap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twowayalternating", 2),
          ("twowaysimultaneous", 1))
    )


_NwAppnExtIfLsXmitRcvCap_Type.__name__ = "Integer32"
_NwAppnExtIfLsXmitRcvCap_Object = MibTableColumn
nwAppnExtIfLsXmitRcvCap = _NwAppnExtIfLsXmitRcvCap_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 13),
    _NwAppnExtIfLsXmitRcvCap_Type()
)
nwAppnExtIfLsXmitRcvCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnExtIfLsXmitRcvCap.setStatus("mandatory")


class _NwAppnExtIfMaxIfrmRcvd_Type(Integer32):
    """Custom type nwAppnExtIfMaxIfrmRcvd based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_NwAppnExtIfMaxIfrmRcvd_Type.__name__ = "Integer32"
_NwAppnExtIfMaxIfrmRcvd_Object = MibTableColumn
nwAppnExtIfMaxIfrmRcvd = _NwAppnExtIfMaxIfrmRcvd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 14),
    _NwAppnExtIfMaxIfrmRcvd_Type()
)
nwAppnExtIfMaxIfrmRcvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnExtIfMaxIfrmRcvd.setStatus("mandatory")


class _NwAppnExtIfDfltTargetPacing_Type(Integer32):
    """Custom type nwAppnExtIfDfltTargetPacing based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_NwAppnExtIfDfltTargetPacing_Type.__name__ = "Integer32"
_NwAppnExtIfDfltTargetPacing_Object = MibTableColumn
nwAppnExtIfDfltTargetPacing = _NwAppnExtIfDfltTargetPacing_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 15),
    _NwAppnExtIfDfltTargetPacing_Type()
)
nwAppnExtIfDfltTargetPacing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnExtIfDfltTargetPacing.setStatus("mandatory")


class _NwAppnExtIfDfltMaxSBtuSize_Type(Integer32):
    """Custom type nwAppnExtIfDfltMaxSBtuSize based on Integer32"""
    defaultValue = 2048

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(99, 65535),
    )


_NwAppnExtIfDfltMaxSBtuSize_Type.__name__ = "Integer32"
_NwAppnExtIfDfltMaxSBtuSize_Object = MibTableColumn
nwAppnExtIfDfltMaxSBtuSize = _NwAppnExtIfDfltMaxSBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 16),
    _NwAppnExtIfDfltMaxSBtuSize_Type()
)
nwAppnExtIfDfltMaxSBtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnExtIfDfltMaxSBtuSize.setStatus("mandatory")


class _NwAppnExtIfDfltEffectCap_Type(Integer32):
    """Custom type nwAppnExtIfDfltEffectCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 603979776),
    )


_NwAppnExtIfDfltEffectCap_Type.__name__ = "Integer32"
_NwAppnExtIfDfltEffectCap_Object = MibTableColumn
nwAppnExtIfDfltEffectCap = _NwAppnExtIfDfltEffectCap_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 17),
    _NwAppnExtIfDfltEffectCap_Type()
)
nwAppnExtIfDfltEffectCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnExtIfDfltEffectCap.setStatus("mandatory")


class _NwAppnExtIfDfltConnectCost_Type(Integer32):
    """Custom type nwAppnExtIfDfltConnectCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NwAppnExtIfDfltConnectCost_Type.__name__ = "Integer32"
_NwAppnExtIfDfltConnectCost_Object = MibTableColumn
nwAppnExtIfDfltConnectCost = _NwAppnExtIfDfltConnectCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 18),
    _NwAppnExtIfDfltConnectCost_Type()
)
nwAppnExtIfDfltConnectCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnExtIfDfltConnectCost.setStatus("mandatory")


class _NwAppnExtIfDfltByteCost_Type(Integer32):
    """Custom type nwAppnExtIfDfltByteCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NwAppnExtIfDfltByteCost_Type.__name__ = "Integer32"
_NwAppnExtIfDfltByteCost_Object = MibTableColumn
nwAppnExtIfDfltByteCost = _NwAppnExtIfDfltByteCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 19),
    _NwAppnExtIfDfltByteCost_Type()
)
nwAppnExtIfDfltByteCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnExtIfDfltByteCost.setStatus("mandatory")


class _NwAppnExtIfDfltSecurity_Type(Integer32):
    """Custom type nwAppnExtIfDfltSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32,
              64,
              96,
              128,
              160,
              192)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 160),
          ("guardedConduit", 128),
          ("guardedRadiation", 192),
          ("nonsecure", 1),
          ("publicSwitchNw", 32),
          ("secureConduit", 96),
          ("undergroundCable", 64))
    )


_NwAppnExtIfDfltSecurity_Type.__name__ = "Integer32"
_NwAppnExtIfDfltSecurity_Object = MibTableColumn
nwAppnExtIfDfltSecurity = _NwAppnExtIfDfltSecurity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 20),
    _NwAppnExtIfDfltSecurity_Type()
)
nwAppnExtIfDfltSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnExtIfDfltSecurity.setStatus("mandatory")


class _NwAppnExtIfDfltPropDelay_Type(Integer32):
    """Custom type nwAppnExtIfDfltPropDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              384,
              9216,
              147456,
              294912,
              2013265920)
        )
    )
    namedValues = NamedValues(
        *(("long", 294912),
          ("maximum", 2013265920),
          ("minimum", 0),
          ("negligible", 384),
          ("packetswitched", 147456),
          ("terrestrial", 9216))
    )


_NwAppnExtIfDfltPropDelay_Type.__name__ = "Integer32"
_NwAppnExtIfDfltPropDelay_Object = MibTableColumn
nwAppnExtIfDfltPropDelay = _NwAppnExtIfDfltPropDelay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 21),
    _NwAppnExtIfDfltPropDelay_Type()
)
nwAppnExtIfDfltPropDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnExtIfDfltPropDelay.setStatus("mandatory")


class _NwAppnExtIfDfltUsrDef1_Type(Integer32):
    """Custom type nwAppnExtIfDfltUsrDef1 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NwAppnExtIfDfltUsrDef1_Type.__name__ = "Integer32"
_NwAppnExtIfDfltUsrDef1_Object = MibTableColumn
nwAppnExtIfDfltUsrDef1 = _NwAppnExtIfDfltUsrDef1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 22),
    _NwAppnExtIfDfltUsrDef1_Type()
)
nwAppnExtIfDfltUsrDef1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnExtIfDfltUsrDef1.setStatus("mandatory")


class _NwAppnExtIfDfltUsrDef2_Type(Integer32):
    """Custom type nwAppnExtIfDfltUsrDef2 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NwAppnExtIfDfltUsrDef2_Type.__name__ = "Integer32"
_NwAppnExtIfDfltUsrDef2_Object = MibTableColumn
nwAppnExtIfDfltUsrDef2 = _NwAppnExtIfDfltUsrDef2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 23),
    _NwAppnExtIfDfltUsrDef2_Type()
)
nwAppnExtIfDfltUsrDef2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnExtIfDfltUsrDef2.setStatus("mandatory")


class _NwAppnExtIfDfltUsrDef3_Type(Integer32):
    """Custom type nwAppnExtIfDfltUsrDef3 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NwAppnExtIfDfltUsrDef3_Type.__name__ = "Integer32"
_NwAppnExtIfDfltUsrDef3_Object = MibTableColumn
nwAppnExtIfDfltUsrDef3 = _NwAppnExtIfDfltUsrDef3_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 24),
    _NwAppnExtIfDfltUsrDef3_Type()
)
nwAppnExtIfDfltUsrDef3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnExtIfDfltUsrDef3.setStatus("mandatory")


class _NwAppnExtIfStopType_Type(Integer32):
    """Custom type nwAppnExtIfStopType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("immediate", 1),
          ("orderly", 2))
    )


_NwAppnExtIfStopType_Type.__name__ = "Integer32"
_NwAppnExtIfStopType_Object = MibTableColumn
nwAppnExtIfStopType = _NwAppnExtIfStopType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 25),
    _NwAppnExtIfStopType_Type()
)
nwAppnExtIfStopType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnExtIfStopType.setStatus("mandatory")


class _NwAppnExtIfCpCpSupp_Type(Integer32):
    """Custom type nwAppnExtIfCpCpSupp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_NwAppnExtIfCpCpSupp_Type.__name__ = "Integer32"
_NwAppnExtIfCpCpSupp_Object = MibTableColumn
nwAppnExtIfCpCpSupp = _NwAppnExtIfCpCpSupp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 26),
    _NwAppnExtIfCpCpSupp_Type()
)
nwAppnExtIfCpCpSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnExtIfCpCpSupp.setStatus("mandatory")


class _NwAppnExtIfLimitedRsrc_Type(Integer32):
    """Custom type nwAppnExtIfLimitedRsrc based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_NwAppnExtIfLimitedRsrc_Type.__name__ = "Integer32"
_NwAppnExtIfLimitedRsrc_Object = MibTableColumn
nwAppnExtIfLimitedRsrc = _NwAppnExtIfLimitedRsrc_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 27),
    _NwAppnExtIfLimitedRsrc_Type()
)
nwAppnExtIfLimitedRsrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnExtIfLimitedRsrc.setStatus("mandatory")


class _NwAppnExtIfAddress_Type(OctetString):
    """Custom type nwAppnExtIfAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NwAppnExtIfAddress_Type.__name__ = "OctetString"
_NwAppnExtIfAddress_Object = MibTableColumn
nwAppnExtIfAddress = _NwAppnExtIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 28),
    _NwAppnExtIfAddress_Type()
)
nwAppnExtIfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnExtIfAddress.setStatus("mandatory")


class _NwAppnExtIfSsap_Type(OctetString):
    """Custom type nwAppnExtIfSsap based on OctetString"""
    defaultHexValue = "04"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_NwAppnExtIfSsap_Type.__name__ = "OctetString"
_NwAppnExtIfSsap_Object = MibTableColumn
nwAppnExtIfSsap = _NwAppnExtIfSsap_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 2, 1, 29),
    _NwAppnExtIfSsap_Type()
)
nwAppnExtIfSsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnExtIfSsap.setStatus("mandatory")
_NwAppnIfCn_ObjectIdentity = ObjectIdentity
nwAppnIfCn = _NwAppnIfCn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 3)
)
_NwAppnIfCnPortTable_Object = MibTable
nwAppnIfCnPortTable = _NwAppnIfCnPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    nwAppnIfCnPortTable.setStatus("mandatory")
_NwAppnIfCnPortEntry_Object = MibTableRow
nwAppnIfCnPortEntry = _NwAppnIfCnPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 3, 1, 1)
)
nwAppnIfCnPortEntry.setIndexNames(
    (0, "CTRON-APPN-MIB", "nwAppnIfCnPtFqName"),
    (0, "CTRON-APPN-MIB", "nwAppnIfCnPtName"),
)
if mibBuilder.loadTexts:
    nwAppnIfCnPortEntry.setStatus("mandatory")


class _NwAppnIfCnPtFqName_Type(DisplayString):
    """Custom type nwAppnIfCnPtFqName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_NwAppnIfCnPtFqName_Type.__name__ = "DisplayString"
_NwAppnIfCnPtFqName_Object = MibTableColumn
nwAppnIfCnPtFqName = _NwAppnIfCnPtFqName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 3, 1, 1, 1),
    _NwAppnIfCnPtFqName_Type()
)
nwAppnIfCnPtFqName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnIfCnPtFqName.setStatus("mandatory")


class _NwAppnIfCnPtName_Type(DisplayString):
    """Custom type nwAppnIfCnPtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_NwAppnIfCnPtName_Type.__name__ = "DisplayString"
_NwAppnIfCnPtName_Object = MibTableColumn
nwAppnIfCnPtName = _NwAppnIfCnPtName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 3, 1, 1, 2),
    _NwAppnIfCnPtName_Type()
)
nwAppnIfCnPtName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnIfCnPtName.setStatus("mandatory")


class _NwAppnIfCnPtControl_Type(Integer32):
    """Custom type nwAppnIfCnPtControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("other", 1))
    )


_NwAppnIfCnPtControl_Type.__name__ = "Integer32"
_NwAppnIfCnPtControl_Object = MibTableColumn
nwAppnIfCnPtControl = _NwAppnIfCnPtControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 3, 1, 1, 3),
    _NwAppnIfCnPtControl_Type()
)
nwAppnIfCnPtControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnIfCnPtControl.setStatus("mandatory")
_NwAppnIfCnTgCharTable_Object = MibTable
nwAppnIfCnTgCharTable = _NwAppnIfCnTgCharTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    nwAppnIfCnTgCharTable.setStatus("mandatory")
_NwAppnIfCnTgCharEntry_Object = MibTableRow
nwAppnIfCnTgCharEntry = _NwAppnIfCnTgCharEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 3, 2, 1)
)
nwAppnIfCnTgCharEntry.setIndexNames(
    (0, "CTRON-APPN-MIB", "nwAppnIfCnTgFqName"),
)
if mibBuilder.loadTexts:
    nwAppnIfCnTgCharEntry.setStatus("mandatory")


class _NwAppnIfCnTgFqName_Type(DisplayString):
    """Custom type nwAppnIfCnTgFqName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_NwAppnIfCnTgFqName_Type.__name__ = "DisplayString"
_NwAppnIfCnTgFqName_Object = MibTableColumn
nwAppnIfCnTgFqName = _NwAppnIfCnTgFqName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 3, 2, 1, 1),
    _NwAppnIfCnTgFqName_Type()
)
nwAppnIfCnTgFqName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnIfCnTgFqName.setStatus("mandatory")


class _NwAppnIfCnTgEffectCap_Type(Integer32):
    """Custom type nwAppnIfCnTgEffectCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 603979776),
    )


_NwAppnIfCnTgEffectCap_Type.__name__ = "Integer32"
_NwAppnIfCnTgEffectCap_Object = MibTableColumn
nwAppnIfCnTgEffectCap = _NwAppnIfCnTgEffectCap_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 3, 2, 1, 2),
    _NwAppnIfCnTgEffectCap_Type()
)
nwAppnIfCnTgEffectCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnIfCnTgEffectCap.setStatus("mandatory")


class _NwAppnIfCnTgConnectCost_Type(Integer32):
    """Custom type nwAppnIfCnTgConnectCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NwAppnIfCnTgConnectCost_Type.__name__ = "Integer32"
_NwAppnIfCnTgConnectCost_Object = MibTableColumn
nwAppnIfCnTgConnectCost = _NwAppnIfCnTgConnectCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 3, 2, 1, 3),
    _NwAppnIfCnTgConnectCost_Type()
)
nwAppnIfCnTgConnectCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnIfCnTgConnectCost.setStatus("mandatory")


class _NwAppnIfCnTgByteCost_Type(Integer32):
    """Custom type nwAppnIfCnTgByteCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NwAppnIfCnTgByteCost_Type.__name__ = "Integer32"
_NwAppnIfCnTgByteCost_Object = MibTableColumn
nwAppnIfCnTgByteCost = _NwAppnIfCnTgByteCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 3, 2, 1, 4),
    _NwAppnIfCnTgByteCost_Type()
)
nwAppnIfCnTgByteCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnIfCnTgByteCost.setStatus("mandatory")


class _NwAppnIfCnTgSecurity_Type(Integer32):
    """Custom type nwAppnIfCnTgSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32,
              64,
              96,
              128,
              160,
              192)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 160),
          ("guardedConduit", 128),
          ("guardedRadiation", 192),
          ("nonsecure", 1),
          ("publicSwitchNw", 32),
          ("secureConduit", 96),
          ("undergroundCable", 64))
    )


_NwAppnIfCnTgSecurity_Type.__name__ = "Integer32"
_NwAppnIfCnTgSecurity_Object = MibTableColumn
nwAppnIfCnTgSecurity = _NwAppnIfCnTgSecurity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 3, 2, 1, 5),
    _NwAppnIfCnTgSecurity_Type()
)
nwAppnIfCnTgSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnIfCnTgSecurity.setStatus("mandatory")


class _NwAppnIfCnTgPropDelay_Type(Integer32):
    """Custom type nwAppnIfCnTgPropDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              384,
              9216,
              147456,
              294912,
              2013265920)
        )
    )
    namedValues = NamedValues(
        *(("long", 294912),
          ("maximum", 2013265920),
          ("minimum", 0),
          ("negligible", 384),
          ("packetswitched", 147456),
          ("terrestrial", 9216))
    )


_NwAppnIfCnTgPropDelay_Type.__name__ = "Integer32"
_NwAppnIfCnTgPropDelay_Object = MibTableColumn
nwAppnIfCnTgPropDelay = _NwAppnIfCnTgPropDelay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 3, 2, 1, 6),
    _NwAppnIfCnTgPropDelay_Type()
)
nwAppnIfCnTgPropDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnIfCnTgPropDelay.setStatus("mandatory")


class _NwAppnIfCnTgUsrDef1_Type(Integer32):
    """Custom type nwAppnIfCnTgUsrDef1 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NwAppnIfCnTgUsrDef1_Type.__name__ = "Integer32"
_NwAppnIfCnTgUsrDef1_Object = MibTableColumn
nwAppnIfCnTgUsrDef1 = _NwAppnIfCnTgUsrDef1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 3, 2, 1, 7),
    _NwAppnIfCnTgUsrDef1_Type()
)
nwAppnIfCnTgUsrDef1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnIfCnTgUsrDef1.setStatus("mandatory")


class _NwAppnIfCnTgUsrDef2_Type(Integer32):
    """Custom type nwAppnIfCnTgUsrDef2 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NwAppnIfCnTgUsrDef2_Type.__name__ = "Integer32"
_NwAppnIfCnTgUsrDef2_Object = MibTableColumn
nwAppnIfCnTgUsrDef2 = _NwAppnIfCnTgUsrDef2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 3, 2, 1, 8),
    _NwAppnIfCnTgUsrDef2_Type()
)
nwAppnIfCnTgUsrDef2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnIfCnTgUsrDef2.setStatus("mandatory")


class _NwAppnIfCnTgUsrDef3_Type(Integer32):
    """Custom type nwAppnIfCnTgUsrDef3 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NwAppnIfCnTgUsrDef3_Type.__name__ = "Integer32"
_NwAppnIfCnTgUsrDef3_Object = MibTableColumn
nwAppnIfCnTgUsrDef3 = _NwAppnIfCnTgUsrDef3_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 1, 3, 2, 1, 9),
    _NwAppnIfCnTgUsrDef3_Type()
)
nwAppnIfCnTgUsrDef3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnIfCnTgUsrDef3.setStatus("mandatory")
_NwAppnFwdIfCounters_ObjectIdentity = ObjectIdentity
nwAppnFwdIfCounters = _NwAppnFwdIfCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2)
)
_NwAppnFwdIfCtrTable_Object = MibTable
nwAppnFwdIfCtrTable = _NwAppnFwdIfCtrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nwAppnFwdIfCtrTable.setStatus("mandatory")
_NwAppnFwdIfCtrEntry_Object = MibTableRow
nwAppnFwdIfCtrEntry = _NwAppnFwdIfCtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2, 1, 1)
)
nwAppnFwdIfCtrEntry.setIndexNames(
    (0, "CTRON-APPN-MIB", "nwAppnFwdIfCtrIfIndex"),
)
if mibBuilder.loadTexts:
    nwAppnFwdIfCtrEntry.setStatus("mandatory")
_NwAppnFwdIfCtrIfIndex_Type = Integer32
_NwAppnFwdIfCtrIfIndex_Object = MibTableColumn
nwAppnFwdIfCtrIfIndex = _NwAppnFwdIfCtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2, 1, 1, 1),
    _NwAppnFwdIfCtrIfIndex_Type()
)
nwAppnFwdIfCtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfCtrIfIndex.setStatus("mandatory")


class _NwAppnFwdIfCtrAdminStatus_Type(Integer32):
    """Custom type nwAppnFwdIfCtrAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwAppnFwdIfCtrAdminStatus_Type.__name__ = "Integer32"
_NwAppnFwdIfCtrAdminStatus_Object = MibTableColumn
nwAppnFwdIfCtrAdminStatus = _NwAppnFwdIfCtrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2, 1, 1, 2),
    _NwAppnFwdIfCtrAdminStatus_Type()
)
nwAppnFwdIfCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdIfCtrAdminStatus.setStatus("mandatory")


class _NwAppnFwdIfCtrReset_Type(Integer32):
    """Custom type nwAppnFwdIfCtrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_NwAppnFwdIfCtrReset_Type.__name__ = "Integer32"
_NwAppnFwdIfCtrReset_Object = MibTableColumn
nwAppnFwdIfCtrReset = _NwAppnFwdIfCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2, 1, 1, 3),
    _NwAppnFwdIfCtrReset_Type()
)
nwAppnFwdIfCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdIfCtrReset.setStatus("mandatory")
_NwAppnFwdIfCtrOperationalTime_Type = TimeTicks
_NwAppnFwdIfCtrOperationalTime_Object = MibTableColumn
nwAppnFwdIfCtrOperationalTime = _NwAppnFwdIfCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2, 1, 1, 4),
    _NwAppnFwdIfCtrOperationalTime_Type()
)
nwAppnFwdIfCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfCtrOperationalTime.setStatus("mandatory")
_NwAppnFwdIfCtrInMus_Type = Counter32
_NwAppnFwdIfCtrInMus_Object = MibTableColumn
nwAppnFwdIfCtrInMus = _NwAppnFwdIfCtrInMus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2, 1, 1, 5),
    _NwAppnFwdIfCtrInMus_Type()
)
nwAppnFwdIfCtrInMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfCtrInMus.setStatus("mandatory")
_NwAppnFwdIfCtrOutMus_Type = Counter32
_NwAppnFwdIfCtrOutMus_Object = MibTableColumn
nwAppnFwdIfCtrOutMus = _NwAppnFwdIfCtrOutMus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2, 1, 1, 6),
    _NwAppnFwdIfCtrOutMus_Type()
)
nwAppnFwdIfCtrOutMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfCtrOutMus.setStatus("mandatory")
_NwAppnFwdIfCtrFwdMus_Type = Counter32
_NwAppnFwdIfCtrFwdMus_Object = MibTableColumn
nwAppnFwdIfCtrFwdMus = _NwAppnFwdIfCtrFwdMus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2, 1, 1, 7),
    _NwAppnFwdIfCtrFwdMus_Type()
)
nwAppnFwdIfCtrFwdMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfCtrFwdMus.setStatus("mandatory")
_NwAppnFwdIfCtrFilteredMus_Type = Counter32
_NwAppnFwdIfCtrFilteredMus_Object = MibTableColumn
nwAppnFwdIfCtrFilteredMus = _NwAppnFwdIfCtrFilteredMus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2, 1, 1, 8),
    _NwAppnFwdIfCtrFilteredMus_Type()
)
nwAppnFwdIfCtrFilteredMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfCtrFilteredMus.setStatus("mandatory")
_NwAppnFwdIfCtrDiscardMus_Type = Counter32
_NwAppnFwdIfCtrDiscardMus_Object = MibTableColumn
nwAppnFwdIfCtrDiscardMus = _NwAppnFwdIfCtrDiscardMus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2, 1, 1, 9),
    _NwAppnFwdIfCtrDiscardMus_Type()
)
nwAppnFwdIfCtrDiscardMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfCtrDiscardMus.setStatus("mandatory")
_NwAppnFwdIfCtrAddrErrMus_Type = Counter32
_NwAppnFwdIfCtrAddrErrMus_Object = MibTableColumn
nwAppnFwdIfCtrAddrErrMus = _NwAppnFwdIfCtrAddrErrMus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2, 1, 1, 10),
    _NwAppnFwdIfCtrAddrErrMus_Type()
)
nwAppnFwdIfCtrAddrErrMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfCtrAddrErrMus.setStatus("mandatory")
_NwAppnFwdIfCtrLenErrMus_Type = Counter32
_NwAppnFwdIfCtrLenErrMus_Object = MibTableColumn
nwAppnFwdIfCtrLenErrMus = _NwAppnFwdIfCtrLenErrMus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2, 1, 1, 11),
    _NwAppnFwdIfCtrLenErrMus_Type()
)
nwAppnFwdIfCtrLenErrMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfCtrLenErrMus.setStatus("mandatory")
_NwAppnFwdIfCtrHdrErrMus_Type = Counter32
_NwAppnFwdIfCtrHdrErrMus_Object = MibTableColumn
nwAppnFwdIfCtrHdrErrMus = _NwAppnFwdIfCtrHdrErrMus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2, 1, 1, 12),
    _NwAppnFwdIfCtrHdrErrMus_Type()
)
nwAppnFwdIfCtrHdrErrMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfCtrHdrErrMus.setStatus("mandatory")
_NwAppnFwdIfCtrInBytes_Type = Counter32
_NwAppnFwdIfCtrInBytes_Object = MibTableColumn
nwAppnFwdIfCtrInBytes = _NwAppnFwdIfCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2, 1, 1, 13),
    _NwAppnFwdIfCtrInBytes_Type()
)
nwAppnFwdIfCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfCtrInBytes.setStatus("mandatory")
_NwAppnFwdIfCtrOutBytes_Type = Counter32
_NwAppnFwdIfCtrOutBytes_Object = MibTableColumn
nwAppnFwdIfCtrOutBytes = _NwAppnFwdIfCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2, 1, 1, 14),
    _NwAppnFwdIfCtrOutBytes_Type()
)
nwAppnFwdIfCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfCtrOutBytes.setStatus("mandatory")
_NwAppnFwdIfCtrFwdBytes_Type = Counter32
_NwAppnFwdIfCtrFwdBytes_Object = MibTableColumn
nwAppnFwdIfCtrFwdBytes = _NwAppnFwdIfCtrFwdBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2, 1, 1, 15),
    _NwAppnFwdIfCtrFwdBytes_Type()
)
nwAppnFwdIfCtrFwdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfCtrFwdBytes.setStatus("mandatory")
_NwAppnFwdIfCtrFilteredBytes_Type = Counter32
_NwAppnFwdIfCtrFilteredBytes_Object = MibTableColumn
nwAppnFwdIfCtrFilteredBytes = _NwAppnFwdIfCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2, 1, 1, 16),
    _NwAppnFwdIfCtrFilteredBytes_Type()
)
nwAppnFwdIfCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfCtrFilteredBytes.setStatus("mandatory")
_NwAppnFwdIfCtrDiscardBytes_Type = Counter32
_NwAppnFwdIfCtrDiscardBytes_Object = MibTableColumn
nwAppnFwdIfCtrDiscardBytes = _NwAppnFwdIfCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2, 1, 1, 17),
    _NwAppnFwdIfCtrDiscardBytes_Type()
)
nwAppnFwdIfCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfCtrDiscardBytes.setStatus("mandatory")
_NwAppnFwdIfCtrHostInMus_Type = Counter32
_NwAppnFwdIfCtrHostInMus_Object = MibTableColumn
nwAppnFwdIfCtrHostInMus = _NwAppnFwdIfCtrHostInMus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2, 1, 1, 18),
    _NwAppnFwdIfCtrHostInMus_Type()
)
nwAppnFwdIfCtrHostInMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfCtrHostInMus.setStatus("mandatory")
_NwAppnFwdIfCtrHostOutMus_Type = Counter32
_NwAppnFwdIfCtrHostOutMus_Object = MibTableColumn
nwAppnFwdIfCtrHostOutMus = _NwAppnFwdIfCtrHostOutMus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2, 1, 1, 19),
    _NwAppnFwdIfCtrHostOutMus_Type()
)
nwAppnFwdIfCtrHostOutMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfCtrHostOutMus.setStatus("mandatory")
_NwAppnFwdIfCtrHostDiscardMus_Type = Counter32
_NwAppnFwdIfCtrHostDiscardMus_Object = MibTableColumn
nwAppnFwdIfCtrHostDiscardMus = _NwAppnFwdIfCtrHostDiscardMus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2, 1, 1, 20),
    _NwAppnFwdIfCtrHostDiscardMus_Type()
)
nwAppnFwdIfCtrHostDiscardMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfCtrHostDiscardMus.setStatus("mandatory")
_NwAppnFwdIfCtrHostInBytes_Type = Counter32
_NwAppnFwdIfCtrHostInBytes_Object = MibTableColumn
nwAppnFwdIfCtrHostInBytes = _NwAppnFwdIfCtrHostInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2, 1, 1, 21),
    _NwAppnFwdIfCtrHostInBytes_Type()
)
nwAppnFwdIfCtrHostInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfCtrHostInBytes.setStatus("mandatory")
_NwAppnFwdIfCtrHostOutBytes_Type = Counter32
_NwAppnFwdIfCtrHostOutBytes_Object = MibTableColumn
nwAppnFwdIfCtrHostOutBytes = _NwAppnFwdIfCtrHostOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2, 1, 1, 22),
    _NwAppnFwdIfCtrHostOutBytes_Type()
)
nwAppnFwdIfCtrHostOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfCtrHostOutBytes.setStatus("mandatory")
_NwAppnFwdIfCtrHostDiscardBytes_Type = Counter32
_NwAppnFwdIfCtrHostDiscardBytes_Object = MibTableColumn
nwAppnFwdIfCtrHostDiscardBytes = _NwAppnFwdIfCtrHostDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 2, 2, 1, 1, 23),
    _NwAppnFwdIfCtrHostDiscardBytes_Type()
)
nwAppnFwdIfCtrHostDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdIfCtrHostDiscardBytes.setStatus("mandatory")
_NwAppnFwdLinks_ObjectIdentity = ObjectIdentity
nwAppnFwdLinks = _NwAppnFwdLinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3)
)
_NwAppnFwdLsConfig_ObjectIdentity = ObjectIdentity
nwAppnFwdLsConfig = _NwAppnFwdLsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1)
)
_NwAppnFwdLsTable_Object = MibTable
nwAppnFwdLsTable = _NwAppnFwdLsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    nwAppnFwdLsTable.setStatus("mandatory")
_NwAppnFwdLsEntry_Object = MibTableRow
nwAppnFwdLsEntry = _NwAppnFwdLsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1)
)
nwAppnFwdLsEntry.setIndexNames(
    (0, "CTRON-APPN-MIB", "nwAppnFwdLsName"),
)
if mibBuilder.loadTexts:
    nwAppnFwdLsEntry.setStatus("mandatory")


class _NwAppnFwdLsName_Type(DisplayString):
    """Custom type nwAppnFwdLsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_NwAppnFwdLsName_Type.__name__ = "DisplayString"
_NwAppnFwdLsName_Object = MibTableColumn
nwAppnFwdLsName = _NwAppnFwdLsName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 1),
    _NwAppnFwdLsName_Type()
)
nwAppnFwdLsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsName.setStatus("mandatory")


class _NwAppnFwdLsAdminStatus_Type(Integer32):
    """Custom type nwAppnFwdLsAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_NwAppnFwdLsAdminStatus_Type.__name__ = "Integer32"
_NwAppnFwdLsAdminStatus_Object = MibTableColumn
nwAppnFwdLsAdminStatus = _NwAppnFwdLsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 2),
    _NwAppnFwdLsAdminStatus_Type()
)
nwAppnFwdLsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsAdminStatus.setStatus("mandatory")


class _NwAppnFwdLsOperStatus_Type(Integer32):
    """Custom type nwAppnFwdLsOperStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1),
          ("pendingDisable", 4),
          ("pendingEnable", 5))
    )


_NwAppnFwdLsOperStatus_Type.__name__ = "Integer32"
_NwAppnFwdLsOperStatus_Object = MibTableColumn
nwAppnFwdLsOperStatus = _NwAppnFwdLsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 3),
    _NwAppnFwdLsOperStatus_Type()
)
nwAppnFwdLsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsOperStatus.setStatus("mandatory")
_NwAppnFwdLsOperationalTime_Type = TimeTicks
_NwAppnFwdLsOperationalTime_Object = MibTableColumn
nwAppnFwdLsOperationalTime = _NwAppnFwdLsOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 4),
    _NwAppnFwdLsOperationalTime_Type()
)
nwAppnFwdLsOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsOperationalTime.setStatus("mandatory")


class _NwAppnFwdLsControl_Type(Integer32):
    """Custom type nwAppnFwdLsControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("other", 1))
    )


_NwAppnFwdLsControl_Type.__name__ = "Integer32"
_NwAppnFwdLsControl_Object = MibTableColumn
nwAppnFwdLsControl = _NwAppnFwdLsControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 5),
    _NwAppnFwdLsControl_Type()
)
nwAppnFwdLsControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsControl.setStatus("mandatory")


class _NwAppnFwdLsPortName_Type(DisplayString):
    """Custom type nwAppnFwdLsPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_NwAppnFwdLsPortName_Type.__name__ = "DisplayString"
_NwAppnFwdLsPortName_Object = MibTableColumn
nwAppnFwdLsPortName = _NwAppnFwdLsPortName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 6),
    _NwAppnFwdLsPortName_Type()
)
nwAppnFwdLsPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsPortName.setStatus("mandatory")


class _NwAppnFwdLsAdjCpName_Type(DisplayString):
    """Custom type nwAppnFwdLsAdjCpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_NwAppnFwdLsAdjCpName_Type.__name__ = "DisplayString"
_NwAppnFwdLsAdjCpName_Object = MibTableColumn
nwAppnFwdLsAdjCpName = _NwAppnFwdLsAdjCpName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 7),
    _NwAppnFwdLsAdjCpName_Type()
)
nwAppnFwdLsAdjCpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsAdjCpName.setStatus("mandatory")


class _NwAppnFwdLsAdjCpType_Type(Integer32):
    """Custom type nwAppnFwdLsAdjCpType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("endnode", 1),
          ("networknode", 2))
    )


_NwAppnFwdLsAdjCpType_Type.__name__ = "Integer32"
_NwAppnFwdLsAdjCpType_Object = MibTableColumn
nwAppnFwdLsAdjCpType = _NwAppnFwdLsAdjCpType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 8),
    _NwAppnFwdLsAdjCpType_Type()
)
nwAppnFwdLsAdjCpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsAdjCpType.setStatus("mandatory")


class _NwAppnFwdLsAutoActSupport_Type(Integer32):
    """Custom type nwAppnFwdLsAutoActSupport based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_NwAppnFwdLsAutoActSupport_Type.__name__ = "Integer32"
_NwAppnFwdLsAutoActSupport_Object = MibTableColumn
nwAppnFwdLsAutoActSupport = _NwAppnFwdLsAutoActSupport_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 10),
    _NwAppnFwdLsAutoActSupport_Type()
)
nwAppnFwdLsAutoActSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsAutoActSupport.setStatus("mandatory")


class _NwAppnFwdLsLimitedRsrc_Type(Integer32):
    """Custom type nwAppnFwdLsLimitedRsrc based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_NwAppnFwdLsLimitedRsrc_Type.__name__ = "Integer32"
_NwAppnFwdLsLimitedRsrc_Object = MibTableColumn
nwAppnFwdLsLimitedRsrc = _NwAppnFwdLsLimitedRsrc_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 11),
    _NwAppnFwdLsLimitedRsrc_Type()
)
nwAppnFwdLsLimitedRsrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsLimitedRsrc.setStatus("mandatory")


class _NwAppnFwdLsSscpSession_Type(Integer32):
    """Custom type nwAppnFwdLsSscpSession based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_NwAppnFwdLsSscpSession_Type.__name__ = "Integer32"
_NwAppnFwdLsSscpSession_Object = MibTableColumn
nwAppnFwdLsSscpSession = _NwAppnFwdLsSscpSession_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 12),
    _NwAppnFwdLsSscpSession_Type()
)
nwAppnFwdLsSscpSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsSscpSession.setStatus("mandatory")


class _NwAppnFwdLsPuName_Type(DisplayString):
    """Custom type nwAppnFwdLsPuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_NwAppnFwdLsPuName_Type.__name__ = "DisplayString"
_NwAppnFwdLsPuName_Object = MibTableColumn
nwAppnFwdLsPuName = _NwAppnFwdLsPuName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 13),
    _NwAppnFwdLsPuName_Type()
)
nwAppnFwdLsPuName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsPuName.setStatus("mandatory")


class _NwAppnFwdLsBackLvlLenEN_Type(Integer32):
    """Custom type nwAppnFwdLsBackLvlLenEN based on Integer32"""
    defaultValue = 1

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
        *(("no", 1),
          ("noxid", 4),
          ("xid0", 3),
          ("xid3", 2))
    )


_NwAppnFwdLsBackLvlLenEN_Type.__name__ = "Integer32"
_NwAppnFwdLsBackLvlLenEN_Object = MibTableColumn
nwAppnFwdLsBackLvlLenEN = _NwAppnFwdLsBackLvlLenEN_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 14),
    _NwAppnFwdLsBackLvlLenEN_Type()
)
nwAppnFwdLsBackLvlLenEN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsBackLvlLenEN.setStatus("mandatory")


class _NwAppnFwdLsCpCpSessSupp_Type(Integer32):
    """Custom type nwAppnFwdLsCpCpSessSupp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_NwAppnFwdLsCpCpSessSupp_Type.__name__ = "Integer32"
_NwAppnFwdLsCpCpSessSupp_Object = MibTableColumn
nwAppnFwdLsCpCpSessSupp = _NwAppnFwdLsCpCpSessSupp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 16),
    _NwAppnFwdLsCpCpSessSupp_Type()
)
nwAppnFwdLsCpCpSessSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsCpCpSessSupp.setStatus("mandatory")


class _NwAppnFwdLsEffectCap_Type(Integer32):
    """Custom type nwAppnFwdLsEffectCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 603979776),
    )


_NwAppnFwdLsEffectCap_Type.__name__ = "Integer32"
_NwAppnFwdLsEffectCap_Object = MibTableColumn
nwAppnFwdLsEffectCap = _NwAppnFwdLsEffectCap_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 17),
    _NwAppnFwdLsEffectCap_Type()
)
nwAppnFwdLsEffectCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsEffectCap.setStatus("mandatory")


class _NwAppnFwdLsConnectCost_Type(Integer32):
    """Custom type nwAppnFwdLsConnectCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NwAppnFwdLsConnectCost_Type.__name__ = "Integer32"
_NwAppnFwdLsConnectCost_Object = MibTableColumn
nwAppnFwdLsConnectCost = _NwAppnFwdLsConnectCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 18),
    _NwAppnFwdLsConnectCost_Type()
)
nwAppnFwdLsConnectCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsConnectCost.setStatus("mandatory")


class _NwAppnFwdLsByteCost_Type(Integer32):
    """Custom type nwAppnFwdLsByteCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NwAppnFwdLsByteCost_Type.__name__ = "Integer32"
_NwAppnFwdLsByteCost_Object = MibTableColumn
nwAppnFwdLsByteCost = _NwAppnFwdLsByteCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 19),
    _NwAppnFwdLsByteCost_Type()
)
nwAppnFwdLsByteCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsByteCost.setStatus("mandatory")


class _NwAppnFwdLsSecurity_Type(Integer32):
    """Custom type nwAppnFwdLsSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32,
              64,
              96,
              128,
              160,
              192)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 160),
          ("guardedConduit", 128),
          ("guardedRadiation", 192),
          ("nonsecure", 1),
          ("publicSwitchNw", 32),
          ("secureConduit", 96),
          ("undergroundCable", 64))
    )


_NwAppnFwdLsSecurity_Type.__name__ = "Integer32"
_NwAppnFwdLsSecurity_Object = MibTableColumn
nwAppnFwdLsSecurity = _NwAppnFwdLsSecurity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 20),
    _NwAppnFwdLsSecurity_Type()
)
nwAppnFwdLsSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsSecurity.setStatus("mandatory")


class _NwAppnFwdLsPropDelay_Type(Integer32):
    """Custom type nwAppnFwdLsPropDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              384,
              9216,
              147456,
              294912,
              2013265920)
        )
    )
    namedValues = NamedValues(
        *(("long", 294912),
          ("maximum", 2013265920),
          ("minimum", 0),
          ("negligible", 384),
          ("packetswitched", 147456),
          ("terrestrial", 9216))
    )


_NwAppnFwdLsPropDelay_Type.__name__ = "Integer32"
_NwAppnFwdLsPropDelay_Object = MibTableColumn
nwAppnFwdLsPropDelay = _NwAppnFwdLsPropDelay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 21),
    _NwAppnFwdLsPropDelay_Type()
)
nwAppnFwdLsPropDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsPropDelay.setStatus("mandatory")


class _NwAppnFwdLsUsrDef1_Type(Integer32):
    """Custom type nwAppnFwdLsUsrDef1 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NwAppnFwdLsUsrDef1_Type.__name__ = "Integer32"
_NwAppnFwdLsUsrDef1_Object = MibTableColumn
nwAppnFwdLsUsrDef1 = _NwAppnFwdLsUsrDef1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 22),
    _NwAppnFwdLsUsrDef1_Type()
)
nwAppnFwdLsUsrDef1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsUsrDef1.setStatus("mandatory")


class _NwAppnFwdLsUsrDef2_Type(Integer32):
    """Custom type nwAppnFwdLsUsrDef2 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NwAppnFwdLsUsrDef2_Type.__name__ = "Integer32"
_NwAppnFwdLsUsrDef2_Object = MibTableColumn
nwAppnFwdLsUsrDef2 = _NwAppnFwdLsUsrDef2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 23),
    _NwAppnFwdLsUsrDef2_Type()
)
nwAppnFwdLsUsrDef2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsUsrDef2.setStatus("mandatory")


class _NwAppnFwdLsUsrDef3_Type(Integer32):
    """Custom type nwAppnFwdLsUsrDef3 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NwAppnFwdLsUsrDef3_Type.__name__ = "Integer32"
_NwAppnFwdLsUsrDef3_Object = MibTableColumn
nwAppnFwdLsUsrDef3 = _NwAppnFwdLsUsrDef3_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 24),
    _NwAppnFwdLsUsrDef3_Type()
)
nwAppnFwdLsUsrDef3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsUsrDef3.setStatus("mandatory")


class _NwAppnFwdLsTrgtPacingCount_Type(Integer32):
    """Custom type nwAppnFwdLsTrgtPacingCount based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_NwAppnFwdLsTrgtPacingCount_Type.__name__ = "Integer32"
_NwAppnFwdLsTrgtPacingCount_Object = MibTableColumn
nwAppnFwdLsTrgtPacingCount = _NwAppnFwdLsTrgtPacingCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 25),
    _NwAppnFwdLsTrgtPacingCount_Type()
)
nwAppnFwdLsTrgtPacingCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsTrgtPacingCount.setStatus("mandatory")


class _NwAppnFwdLsMaxSendBtu_Type(Integer32):
    """Custom type nwAppnFwdLsMaxSendBtu based on Integer32"""
    defaultValue = 2048

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(99, 65535),
    )


_NwAppnFwdLsMaxSendBtu_Type.__name__ = "Integer32"
_NwAppnFwdLsMaxSendBtu_Object = MibTableColumn
nwAppnFwdLsMaxSendBtu = _NwAppnFwdLsMaxSendBtu_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 26),
    _NwAppnFwdLsMaxSendBtu_Type()
)
nwAppnFwdLsMaxSendBtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsMaxSendBtu.setStatus("mandatory")
_NwAppnFwdLsNumActiveSession_Type = Integer32
_NwAppnFwdLsNumActiveSession_Object = MibTableColumn
nwAppnFwdLsNumActiveSession = _NwAppnFwdLsNumActiveSession_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 27),
    _NwAppnFwdLsNumActiveSession_Type()
)
nwAppnFwdLsNumActiveSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsNumActiveSession.setStatus("mandatory")


class _NwAppnFwdLsdynamicLs_Type(Integer32):
    """Custom type nwAppnFwdLsdynamicLs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_NwAppnFwdLsdynamicLs_Type.__name__ = "Integer32"
_NwAppnFwdLsdynamicLs_Object = MibTableColumn
nwAppnFwdLsdynamicLs = _NwAppnFwdLsdynamicLs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 28),
    _NwAppnFwdLsdynamicLs_Type()
)
nwAppnFwdLsdynamicLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsdynamicLs.setStatus("mandatory")


class _NwAppnFwdLsStopType_Type(Integer32):
    """Custom type nwAppnFwdLsStopType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("immediate", 1),
          ("orderly", 2))
    )


_NwAppnFwdLsStopType_Type.__name__ = "Integer32"
_NwAppnFwdLsStopType_Object = MibTableColumn
nwAppnFwdLsStopType = _NwAppnFwdLsStopType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 29),
    _NwAppnFwdLsStopType_Type()
)
nwAppnFwdLsStopType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsStopType.setStatus("mandatory")
_NwAppnFwdLsPortNbr_Type = Integer32
_NwAppnFwdLsPortNbr_Object = MibTableColumn
nwAppnFwdLsPortNbr = _NwAppnFwdLsPortNbr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 30),
    _NwAppnFwdLsPortNbr_Type()
)
nwAppnFwdLsPortNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsPortNbr.setStatus("mandatory")


class _NwAppnFwdLsDestAddr_Type(OctetString):
    """Custom type nwAppnFwdLsDestAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NwAppnFwdLsDestAddr_Type.__name__ = "OctetString"
_NwAppnFwdLsDestAddr_Object = MibTableColumn
nwAppnFwdLsDestAddr = _NwAppnFwdLsDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 31),
    _NwAppnFwdLsDestAddr_Type()
)
nwAppnFwdLsDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsDestAddr.setStatus("mandatory")


class _NwAppnFwdLsDsap_Type(OctetString):
    """Custom type nwAppnFwdLsDsap based on OctetString"""
    defaultHexValue = "04"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_NwAppnFwdLsDsap_Type.__name__ = "OctetString"
_NwAppnFwdLsDsap_Object = MibTableColumn
nwAppnFwdLsDsap = _NwAppnFwdLsDsap_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 32),
    _NwAppnFwdLsDsap_Type()
)
nwAppnFwdLsDsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsDsap.setStatus("mandatory")


class _NwAppnFwdLsBlockNum_Type(DisplayString):
    """Custom type nwAppnFwdLsBlockNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_NwAppnFwdLsBlockNum_Type.__name__ = "DisplayString"
_NwAppnFwdLsBlockNum_Object = MibTableColumn
nwAppnFwdLsBlockNum = _NwAppnFwdLsBlockNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 33),
    _NwAppnFwdLsBlockNum_Type()
)
nwAppnFwdLsBlockNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsBlockNum.setStatus("mandatory")


class _NwAppnFwdLsIdNum_Type(DisplayString):
    """Custom type nwAppnFwdLsIdNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_NwAppnFwdLsIdNum_Type.__name__ = "DisplayString"
_NwAppnFwdLsIdNum_Object = MibTableColumn
nwAppnFwdLsIdNum = _NwAppnFwdLsIdNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 1, 1, 1, 34),
    _NwAppnFwdLsIdNum_Type()
)
nwAppnFwdLsIdNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsIdNum.setStatus("mandatory")
_NwAppnFwdLsCounters_ObjectIdentity = ObjectIdentity
nwAppnFwdLsCounters = _NwAppnFwdLsCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2)
)
_NwAppnFwdLsCtrTable_Object = MibTable
nwAppnFwdLsCtrTable = _NwAppnFwdLsCtrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    nwAppnFwdLsCtrTable.setStatus("mandatory")
_NwAppnFwdLsCtrEntry_Object = MibTableRow
nwAppnFwdLsCtrEntry = _NwAppnFwdLsCtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2, 1, 1)
)
nwAppnFwdLsCtrEntry.setIndexNames(
    (0, "CTRON-APPN-MIB", "nwAppnFwdLsCtrLsName"),
)
if mibBuilder.loadTexts:
    nwAppnFwdLsCtrEntry.setStatus("mandatory")


class _NwAppnFwdLsCtrLsName_Type(DisplayString):
    """Custom type nwAppnFwdLsCtrLsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_NwAppnFwdLsCtrLsName_Type.__name__ = "DisplayString"
_NwAppnFwdLsCtrLsName_Object = MibTableColumn
nwAppnFwdLsCtrLsName = _NwAppnFwdLsCtrLsName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2, 1, 1, 1),
    _NwAppnFwdLsCtrLsName_Type()
)
nwAppnFwdLsCtrLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsCtrLsName.setStatus("mandatory")


class _NwAppnFwdLsCtrAdminStatus_Type(Integer32):
    """Custom type nwAppnFwdLsCtrAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwAppnFwdLsCtrAdminStatus_Type.__name__ = "Integer32"
_NwAppnFwdLsCtrAdminStatus_Object = MibTableColumn
nwAppnFwdLsCtrAdminStatus = _NwAppnFwdLsCtrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2, 1, 1, 2),
    _NwAppnFwdLsCtrAdminStatus_Type()
)
nwAppnFwdLsCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsCtrAdminStatus.setStatus("mandatory")


class _NwAppnFwdLsCtrReset_Type(Integer32):
    """Custom type nwAppnFwdLsCtrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_NwAppnFwdLsCtrReset_Type.__name__ = "Integer32"
_NwAppnFwdLsCtrReset_Object = MibTableColumn
nwAppnFwdLsCtrReset = _NwAppnFwdLsCtrReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2, 1, 1, 3),
    _NwAppnFwdLsCtrReset_Type()
)
nwAppnFwdLsCtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnFwdLsCtrReset.setStatus("mandatory")
_NwAppnFwdLsCtrOperationalTime_Type = TimeTicks
_NwAppnFwdLsCtrOperationalTime_Object = MibTableColumn
nwAppnFwdLsCtrOperationalTime = _NwAppnFwdLsCtrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2, 1, 1, 4),
    _NwAppnFwdLsCtrOperationalTime_Type()
)
nwAppnFwdLsCtrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsCtrOperationalTime.setStatus("mandatory")
_NwAppnFwdLsCtrInBlus_Type = Counter32
_NwAppnFwdLsCtrInBlus_Object = MibTableColumn
nwAppnFwdLsCtrInBlus = _NwAppnFwdLsCtrInBlus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2, 1, 1, 5),
    _NwAppnFwdLsCtrInBlus_Type()
)
nwAppnFwdLsCtrInBlus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsCtrInBlus.setStatus("mandatory")
_NwAppnFwdLsCtrOutBlus_Type = Counter32
_NwAppnFwdLsCtrOutBlus_Object = MibTableColumn
nwAppnFwdLsCtrOutBlus = _NwAppnFwdLsCtrOutBlus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2, 1, 1, 6),
    _NwAppnFwdLsCtrOutBlus_Type()
)
nwAppnFwdLsCtrOutBlus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsCtrOutBlus.setStatus("mandatory")
_NwAppnFwdLsCtrFwdBlus_Type = Counter32
_NwAppnFwdLsCtrFwdBlus_Object = MibTableColumn
nwAppnFwdLsCtrFwdBlus = _NwAppnFwdLsCtrFwdBlus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2, 1, 1, 7),
    _NwAppnFwdLsCtrFwdBlus_Type()
)
nwAppnFwdLsCtrFwdBlus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsCtrFwdBlus.setStatus("mandatory")
_NwAppnFwdLsCtrFilteredBlus_Type = Counter32
_NwAppnFwdLsCtrFilteredBlus_Object = MibTableColumn
nwAppnFwdLsCtrFilteredBlus = _NwAppnFwdLsCtrFilteredBlus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2, 1, 1, 8),
    _NwAppnFwdLsCtrFilteredBlus_Type()
)
nwAppnFwdLsCtrFilteredBlus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsCtrFilteredBlus.setStatus("mandatory")
_NwAppnFwdLsCtrDiscardBlus_Type = Counter32
_NwAppnFwdLsCtrDiscardBlus_Object = MibTableColumn
nwAppnFwdLsCtrDiscardBlus = _NwAppnFwdLsCtrDiscardBlus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2, 1, 1, 9),
    _NwAppnFwdLsCtrDiscardBlus_Type()
)
nwAppnFwdLsCtrDiscardBlus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsCtrDiscardBlus.setStatus("mandatory")
_NwAppnFwdLsCtrAddrErrBlus_Type = Counter32
_NwAppnFwdLsCtrAddrErrBlus_Object = MibTableColumn
nwAppnFwdLsCtrAddrErrBlus = _NwAppnFwdLsCtrAddrErrBlus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2, 1, 1, 10),
    _NwAppnFwdLsCtrAddrErrBlus_Type()
)
nwAppnFwdLsCtrAddrErrBlus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsCtrAddrErrBlus.setStatus("mandatory")
_NwAppnFwdLsCtrLenErrBlus_Type = Counter32
_NwAppnFwdLsCtrLenErrBlus_Object = MibTableColumn
nwAppnFwdLsCtrLenErrBlus = _NwAppnFwdLsCtrLenErrBlus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2, 1, 1, 11),
    _NwAppnFwdLsCtrLenErrBlus_Type()
)
nwAppnFwdLsCtrLenErrBlus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsCtrLenErrBlus.setStatus("mandatory")
_NwAppnFwdLsCtrHdrErrBlus_Type = Counter32
_NwAppnFwdLsCtrHdrErrBlus_Object = MibTableColumn
nwAppnFwdLsCtrHdrErrBlus = _NwAppnFwdLsCtrHdrErrBlus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2, 1, 1, 12),
    _NwAppnFwdLsCtrHdrErrBlus_Type()
)
nwAppnFwdLsCtrHdrErrBlus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsCtrHdrErrBlus.setStatus("mandatory")
_NwAppnFwdLsCtrInBytes_Type = Counter32
_NwAppnFwdLsCtrInBytes_Object = MibTableColumn
nwAppnFwdLsCtrInBytes = _NwAppnFwdLsCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2, 1, 1, 13),
    _NwAppnFwdLsCtrInBytes_Type()
)
nwAppnFwdLsCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsCtrInBytes.setStatus("mandatory")
_NwAppnFwdLsCtrOutBytes_Type = Counter32
_NwAppnFwdLsCtrOutBytes_Object = MibTableColumn
nwAppnFwdLsCtrOutBytes = _NwAppnFwdLsCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2, 1, 1, 14),
    _NwAppnFwdLsCtrOutBytes_Type()
)
nwAppnFwdLsCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsCtrOutBytes.setStatus("mandatory")
_NwAppnFwdLsCtrFwdBytes_Type = Counter32
_NwAppnFwdLsCtrFwdBytes_Object = MibTableColumn
nwAppnFwdLsCtrFwdBytes = _NwAppnFwdLsCtrFwdBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2, 1, 1, 15),
    _NwAppnFwdLsCtrFwdBytes_Type()
)
nwAppnFwdLsCtrFwdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsCtrFwdBytes.setStatus("mandatory")
_NwAppnFwdLsCtrFilteredBytes_Type = Counter32
_NwAppnFwdLsCtrFilteredBytes_Object = MibTableColumn
nwAppnFwdLsCtrFilteredBytes = _NwAppnFwdLsCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2, 1, 1, 16),
    _NwAppnFwdLsCtrFilteredBytes_Type()
)
nwAppnFwdLsCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsCtrFilteredBytes.setStatus("mandatory")
_NwAppnFwdLsCtrDiscardBytes_Type = Counter32
_NwAppnFwdLsCtrDiscardBytes_Object = MibTableColumn
nwAppnFwdLsCtrDiscardBytes = _NwAppnFwdLsCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2, 1, 1, 17),
    _NwAppnFwdLsCtrDiscardBytes_Type()
)
nwAppnFwdLsCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsCtrDiscardBytes.setStatus("mandatory")
_NwAppnFwdLsCtrHostInBlus_Type = Counter32
_NwAppnFwdLsCtrHostInBlus_Object = MibTableColumn
nwAppnFwdLsCtrHostInBlus = _NwAppnFwdLsCtrHostInBlus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2, 1, 1, 18),
    _NwAppnFwdLsCtrHostInBlus_Type()
)
nwAppnFwdLsCtrHostInBlus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsCtrHostInBlus.setStatus("mandatory")
_NwAppnFwdLsCtrHostOutBlus_Type = Counter32
_NwAppnFwdLsCtrHostOutBlus_Object = MibTableColumn
nwAppnFwdLsCtrHostOutBlus = _NwAppnFwdLsCtrHostOutBlus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2, 1, 1, 19),
    _NwAppnFwdLsCtrHostOutBlus_Type()
)
nwAppnFwdLsCtrHostOutBlus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsCtrHostOutBlus.setStatus("mandatory")
_NwAppnFwdLsCtrHostDiscardBlus_Type = Counter32
_NwAppnFwdLsCtrHostDiscardBlus_Object = MibTableColumn
nwAppnFwdLsCtrHostDiscardBlus = _NwAppnFwdLsCtrHostDiscardBlus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2, 1, 1, 20),
    _NwAppnFwdLsCtrHostDiscardBlus_Type()
)
nwAppnFwdLsCtrHostDiscardBlus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsCtrHostDiscardBlus.setStatus("mandatory")
_NwAppnFwdLsCtrHostInBytes_Type = Counter32
_NwAppnFwdLsCtrHostInBytes_Object = MibTableColumn
nwAppnFwdLsCtrHostInBytes = _NwAppnFwdLsCtrHostInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2, 1, 1, 21),
    _NwAppnFwdLsCtrHostInBytes_Type()
)
nwAppnFwdLsCtrHostInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsCtrHostInBytes.setStatus("mandatory")
_NwAppnFwdLsCtrHostOutBytes_Type = Counter32
_NwAppnFwdLsCtrHostOutBytes_Object = MibTableColumn
nwAppnFwdLsCtrHostOutBytes = _NwAppnFwdLsCtrHostOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2, 1, 1, 22),
    _NwAppnFwdLsCtrHostOutBytes_Type()
)
nwAppnFwdLsCtrHostOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsCtrHostOutBytes.setStatus("mandatory")
_NwAppnFwdLsCtrHostDiscardBytes_Type = Counter32
_NwAppnFwdLsCtrHostDiscardBytes_Object = MibTableColumn
nwAppnFwdLsCtrHostDiscardBytes = _NwAppnFwdLsCtrHostDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 2, 3, 2, 1, 1, 23),
    _NwAppnFwdLsCtrHostDiscardBytes_Type()
)
nwAppnFwdLsCtrHostDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnFwdLsCtrHostDiscardBytes.setStatus("mandatory")
_NwAppnTopology_ObjectIdentity = ObjectIdentity
nwAppnTopology = _NwAppnTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 4)
)
_NwAppnDistanceVector_ObjectIdentity = ObjectIdentity
nwAppnDistanceVector = _NwAppnDistanceVector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 4, 1)
)
_NwAppnLinkState_ObjectIdentity = ObjectIdentity
nwAppnLinkState = _NwAppnLinkState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 4, 2)
)
_NwAppnIsr_ObjectIdentity = ObjectIdentity
nwAppnIsr = _NwAppnIsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 4, 2, 1)
)
_NwAppnIsrSystem_ObjectIdentity = ObjectIdentity
nwAppnIsrSystem = _NwAppnIsrSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 4, 2, 1, 1)
)
_NwAppnIsrConfig_ObjectIdentity = ObjectIdentity
nwAppnIsrConfig = _NwAppnIsrConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 4, 2, 1, 1, 1)
)


class _NwAppnIsrAdminStatus_Type(Integer32):
    """Custom type nwAppnIsrAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_NwAppnIsrAdminStatus_Type.__name__ = "Integer32"
_NwAppnIsrAdminStatus_Object = MibScalar
nwAppnIsrAdminStatus = _NwAppnIsrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 4, 2, 1, 1, 1, 1),
    _NwAppnIsrAdminStatus_Type()
)
nwAppnIsrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnIsrAdminStatus.setStatus("mandatory")


class _NwAppnIsrOperStatus_Type(Integer32):
    """Custom type nwAppnIsrOperStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1),
          ("pendingDisable", 4),
          ("pendingEnable", 5))
    )


_NwAppnIsrOperStatus_Type.__name__ = "Integer32"
_NwAppnIsrOperStatus_Object = MibScalar
nwAppnIsrOperStatus = _NwAppnIsrOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 4, 2, 1, 1, 1, 2),
    _NwAppnIsrOperStatus_Type()
)
nwAppnIsrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnIsrOperStatus.setStatus("mandatory")


class _NwAppnIsrAdminReset_Type(Integer32):
    """Custom type nwAppnIsrAdminReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("other", 1)
    )


_NwAppnIsrAdminReset_Type.__name__ = "Integer32"
_NwAppnIsrAdminReset_Object = MibScalar
nwAppnIsrAdminReset = _NwAppnIsrAdminReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 4, 2, 1, 1, 1, 3),
    _NwAppnIsrAdminReset_Type()
)
nwAppnIsrAdminReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnIsrAdminReset.setStatus("mandatory")
_NwAppnIsrOperationalTime_Type = TimeTicks
_NwAppnIsrOperationalTime_Object = MibScalar
nwAppnIsrOperationalTime = _NwAppnIsrOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 4, 2, 1, 1, 1, 4),
    _NwAppnIsrOperationalTime_Type()
)
nwAppnIsrOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnIsrOperationalTime.setStatus("mandatory")
_NwAppnIsrVersion_Type = DisplayString
_NwAppnIsrVersion_Object = MibScalar
nwAppnIsrVersion = _NwAppnIsrVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 4, 2, 1, 1, 1, 5),
    _NwAppnIsrVersion_Type()
)
nwAppnIsrVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnIsrVersion.setStatus("mandatory")
_NwAppnIsrCounters_ObjectIdentity = ObjectIdentity
nwAppnIsrCounters = _NwAppnIsrCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 4, 2, 1, 1, 2)
)
_NwAppnIsrInterfaces_ObjectIdentity = ObjectIdentity
nwAppnIsrInterfaces = _NwAppnIsrInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 4, 2, 1, 2)
)
_NwAppnIsrIfConfig_ObjectIdentity = ObjectIdentity
nwAppnIsrIfConfig = _NwAppnIsrIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 4, 2, 1, 2, 1)
)
_NwAppnIsrIfCounters_ObjectIdentity = ObjectIdentity
nwAppnIsrIfCounters = _NwAppnIsrIfCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 4, 2, 1, 2, 2)
)
_NwAppnIsrDatabase_ObjectIdentity = ObjectIdentity
nwAppnIsrDatabase = _NwAppnIsrDatabase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 4, 2, 1, 3)
)
_NwAppnIsrFilters_ObjectIdentity = ObjectIdentity
nwAppnIsrFilters = _NwAppnIsrFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 4, 2, 1, 4)
)
_NwAppnFib_ObjectIdentity = ObjectIdentity
nwAppnFib = _NwAppnFib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 5)
)
_NwAppnEndSystems_ObjectIdentity = ObjectIdentity
nwAppnEndSystems = _NwAppnEndSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 6)
)
_NwAppnHostsSystem_ObjectIdentity = ObjectIdentity
nwAppnHostsSystem = _NwAppnHostsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 6, 1)
)
_NwAppnHostsInterfaces_ObjectIdentity = ObjectIdentity
nwAppnHostsInterfaces = _NwAppnHostsInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 6, 2)
)
_NwAppnAccessControl_ObjectIdentity = ObjectIdentity
nwAppnAccessControl = _NwAppnAccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 7)
)
_NwAppnFilters_ObjectIdentity = ObjectIdentity
nwAppnFilters = _NwAppnFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 8)
)
_NwAppnRedirector_ObjectIdentity = ObjectIdentity
nwAppnRedirector = _NwAppnRedirector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 9)
)
_NwAppnEvent_ObjectIdentity = ObjectIdentity
nwAppnEvent = _NwAppnEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 10)
)
_NwAppnEventLogConfig_ObjectIdentity = ObjectIdentity
nwAppnEventLogConfig = _NwAppnEventLogConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 10, 1)
)


class _NwAppnEventAdminStatus_Type(Integer32):
    """Custom type nwAppnEventAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwAppnEventAdminStatus_Type.__name__ = "Integer32"
_NwAppnEventAdminStatus_Object = MibScalar
nwAppnEventAdminStatus = _NwAppnEventAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 10, 1, 1),
    _NwAppnEventAdminStatus_Type()
)
nwAppnEventAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnEventAdminStatus.setStatus("mandatory")
_NwAppnEventMaxEntries_Type = Integer32
_NwAppnEventMaxEntries_Object = MibScalar
nwAppnEventMaxEntries = _NwAppnEventMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 10, 1, 2),
    _NwAppnEventMaxEntries_Type()
)
nwAppnEventMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnEventMaxEntries.setStatus("mandatory")


class _NwAppnEventTraceAll_Type(Integer32):
    """Custom type nwAppnEventTraceAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwAppnEventTraceAll_Type.__name__ = "Integer32"
_NwAppnEventTraceAll_Object = MibScalar
nwAppnEventTraceAll = _NwAppnEventTraceAll_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 10, 1, 3),
    _NwAppnEventTraceAll_Type()
)
nwAppnEventTraceAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnEventTraceAll.setStatus("mandatory")
_NwAppnEventLogFilterTable_ObjectIdentity = ObjectIdentity
nwAppnEventLogFilterTable = _NwAppnEventLogFilterTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 10, 2)
)
_NwAppnEventFilterTable_Object = MibTable
nwAppnEventFilterTable = _NwAppnEventFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 10, 2, 1)
)
if mibBuilder.loadTexts:
    nwAppnEventFilterTable.setStatus("mandatory")
_NwAppnEventFilterEntry_Object = MibTableRow
nwAppnEventFilterEntry = _NwAppnEventFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 10, 2, 1, 1)
)
nwAppnEventFilterEntry.setIndexNames(
    (0, "CTRON-APPN-MIB", "nwAppnEventFltrProtocol"),
    (0, "CTRON-APPN-MIB", "nwAppnEventFltrIfNum"),
)
if mibBuilder.loadTexts:
    nwAppnEventFilterEntry.setStatus("mandatory")
_NwAppnEventFltrProtocol_Type = Integer32
_NwAppnEventFltrProtocol_Object = MibTableColumn
nwAppnEventFltrProtocol = _NwAppnEventFltrProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 10, 2, 1, 1, 1),
    _NwAppnEventFltrProtocol_Type()
)
nwAppnEventFltrProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnEventFltrProtocol.setStatus("mandatory")
_NwAppnEventFltrIfNum_Type = Integer32
_NwAppnEventFltrIfNum_Object = MibTableColumn
nwAppnEventFltrIfNum = _NwAppnEventFltrIfNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 10, 2, 1, 1, 2),
    _NwAppnEventFltrIfNum_Type()
)
nwAppnEventFltrIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnEventFltrIfNum.setStatus("mandatory")


class _NwAppnEventFltrControl_Type(Integer32):
    """Custom type nwAppnEventFltrControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 3),
          ("delete", 2),
          ("other", 1))
    )


_NwAppnEventFltrControl_Type.__name__ = "Integer32"
_NwAppnEventFltrControl_Object = MibTableColumn
nwAppnEventFltrControl = _NwAppnEventFltrControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 10, 2, 1, 1, 3),
    _NwAppnEventFltrControl_Type()
)
nwAppnEventFltrControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnEventFltrControl.setStatus("mandatory")


class _NwAppnEventFltrType_Type(Integer32):
    """Custom type nwAppnEventFltrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("error", 32),
          ("event", 16),
          ("misc", 1),
          ("rcv", 4),
          ("timer", 2),
          ("xmit", 8))
    )


_NwAppnEventFltrType_Type.__name__ = "Integer32"
_NwAppnEventFltrType_Object = MibTableColumn
nwAppnEventFltrType = _NwAppnEventFltrType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 10, 2, 1, 1, 4),
    _NwAppnEventFltrType_Type()
)
nwAppnEventFltrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnEventFltrType.setStatus("mandatory")


class _NwAppnEventFltrSeverity_Type(Integer32):
    """Custom type nwAppnEventFltrSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("highest", 1),
          ("highlow", 3),
          ("highmed", 2))
    )


_NwAppnEventFltrSeverity_Type.__name__ = "Integer32"
_NwAppnEventFltrSeverity_Object = MibTableColumn
nwAppnEventFltrSeverity = _NwAppnEventFltrSeverity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 10, 2, 1, 1, 5),
    _NwAppnEventFltrSeverity_Type()
)
nwAppnEventFltrSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnEventFltrSeverity.setStatus("mandatory")


class _NwAppnEventFltrAction_Type(Integer32):
    """Custom type nwAppnEventFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("log", 1),
          ("logTrap", 3),
          ("trap", 2))
    )


_NwAppnEventFltrAction_Type.__name__ = "Integer32"
_NwAppnEventFltrAction_Object = MibTableColumn
nwAppnEventFltrAction = _NwAppnEventFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 10, 2, 1, 1, 6),
    _NwAppnEventFltrAction_Type()
)
nwAppnEventFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAppnEventFltrAction.setStatus("mandatory")
_NwAppnEventLogTable_ObjectIdentity = ObjectIdentity
nwAppnEventLogTable = _NwAppnEventLogTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 10, 3)
)
_NwAppnEventTable_Object = MibTable
nwAppnEventTable = _NwAppnEventTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 10, 3, 1)
)
if mibBuilder.loadTexts:
    nwAppnEventTable.setStatus("mandatory")
_NwAppnEventEntry_Object = MibTableRow
nwAppnEventEntry = _NwAppnEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 10, 3, 1, 1)
)
nwAppnEventEntry.setIndexNames(
    (0, "CTRON-APPN-MIB", "nwAppnEventNumber"),
)
if mibBuilder.loadTexts:
    nwAppnEventEntry.setStatus("mandatory")
_NwAppnEventNumber_Type = Integer32
_NwAppnEventNumber_Object = MibTableColumn
nwAppnEventNumber = _NwAppnEventNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 10, 3, 1, 1, 1),
    _NwAppnEventNumber_Type()
)
nwAppnEventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnEventNumber.setStatus("mandatory")
_NwAppnEventTime_Type = TimeTicks
_NwAppnEventTime_Object = MibTableColumn
nwAppnEventTime = _NwAppnEventTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 10, 3, 1, 1, 2),
    _NwAppnEventTime_Type()
)
nwAppnEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnEventTime.setStatus("mandatory")


class _NwAppnEventType_Type(Integer32):
    """Custom type nwAppnEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64)
        )
    )
    namedValues = NamedValues(
        *(("diags", 32),
          ("error", 64),
          ("event", 16),
          ("misc", 1),
          ("rcv", 4),
          ("timer", 2),
          ("xmit", 8))
    )


_NwAppnEventType_Type.__name__ = "Integer32"
_NwAppnEventType_Object = MibTableColumn
nwAppnEventType = _NwAppnEventType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 10, 3, 1, 1, 3),
    _NwAppnEventType_Type()
)
nwAppnEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnEventType.setStatus("mandatory")


class _NwAppnEventSeverity_Type(Integer32):
    """Custom type nwAppnEventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("highest", 1),
          ("highlow", 3),
          ("highmed", 2))
    )


_NwAppnEventSeverity_Type.__name__ = "Integer32"
_NwAppnEventSeverity_Object = MibTableColumn
nwAppnEventSeverity = _NwAppnEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 10, 3, 1, 1, 4),
    _NwAppnEventSeverity_Type()
)
nwAppnEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnEventSeverity.setStatus("mandatory")
_NwAppnEventProtocol_Type = Integer32
_NwAppnEventProtocol_Object = MibTableColumn
nwAppnEventProtocol = _NwAppnEventProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 10, 3, 1, 1, 5),
    _NwAppnEventProtocol_Type()
)
nwAppnEventProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnEventProtocol.setStatus("mandatory")
_NwAppnEventIfNum_Type = Integer32
_NwAppnEventIfNum_Object = MibTableColumn
nwAppnEventIfNum = _NwAppnEventIfNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 10, 3, 1, 1, 6),
    _NwAppnEventIfNum_Type()
)
nwAppnEventIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnEventIfNum.setStatus("mandatory")
_NwAppnEventTextString_Type = OctetString
_NwAppnEventTextString_Object = MibTableColumn
nwAppnEventTextString = _NwAppnEventTextString_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 10, 3, 1, 1, 7),
    _NwAppnEventTextString_Type()
)
nwAppnEventTextString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppnEventTextString.setStatus("mandatory")
_NwAppnWorkGroup_ObjectIdentity = ObjectIdentity
nwAppnWorkGroup = _NwAppnWorkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 5, 2, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-APPN-MIB",
    **{"nwAppnRouter": nwAppnRouter,
       "nwAppnMibs": nwAppnMibs,
       "nwAppnMibRevText": nwAppnMibRevText,
       "nwAppnComponents": nwAppnComponents,
       "nwAppnSystem": nwAppnSystem,
       "nwAppnSysConfig": nwAppnSysConfig,
       "nwAppnSysRouterId": nwAppnSysRouterId,
       "nwAppnSysCfgLocalNode": nwAppnSysCfgLocalNode,
       "nwAppnSysNodeType": nwAppnSysNodeType,
       "nwAppnSysCpAlias": nwAppnSysCpAlias,
       "nwAppnSysModeCosMap": nwAppnSysModeCosMap,
       "nwAppnSysMdsSupport": nwAppnSysMdsSupport,
       "nwAppnSysMaxLocates": nwAppnSysMaxLocates,
       "nwAppnSysDirCacheSize": nwAppnSysDirCacheSize,
       "nwAppnSysMaxDirEntries": nwAppnSysMaxDirEntries,
       "nwAppnSysLocateTimeout": nwAppnSysLocateTimeout,
       "nwAppnSysRegCds": nwAppnSysRegCds,
       "nwAppnSysMdsSendQSize": nwAppnSysMdsSendQSize,
       "nwAppnSysCosSize": nwAppnSysCosSize,
       "nwAppnSysTreeSize": nwAppnSysTreeSize,
       "nwAppnSysTreeUseLimit": nwAppnSysTreeUseLimit,
       "nwAppnSysMaxTdmNodes": nwAppnSysMaxTdmNodes,
       "nwAppnSysMaxTdmTGs": nwAppnSysMaxTdmTGs,
       "nwAppnSysMaxIsrSessions": nwAppnSysMaxIsrSessions,
       "nwAppnSysIsrUpperThresh": nwAppnSysIsrUpperThresh,
       "nwAppnSysIsrLowerThresh": nwAppnSysIsrLowerThresh,
       "nwAppnSysIsrMaxRuSize": nwAppnSysIsrMaxRuSize,
       "nwAppnSysIsrRcvPaceWind": nwAppnSysIsrRcvPaceWind,
       "nwAppnSysRtAddResist": nwAppnSysRtAddResist,
       "nwAppnSysStopType": nwAppnSysStopType,
       "nwAppnSysBlockNum": nwAppnSysBlockNum,
       "nwAppnSysIdNum": nwAppnSysIdNum,
       "nwAppnSysCfgTables": nwAppnSysCfgTables,
       "nwAppnSysLuTable": nwAppnSysLuTable,
       "nwAppnSysLuEntry": nwAppnSysLuEntry,
       "nwAppnSysCpName": nwAppnSysCpName,
       "nwAppnSysLuName": nwAppnSysLuName,
       "nwAppnSysLuControl": nwAppnSysLuControl,
       "nwAppnSysAdministration": nwAppnSysAdministration,
       "nwAppnSysAdminStatus": nwAppnSysAdminStatus,
       "nwAppnSysOperStatus": nwAppnSysOperStatus,
       "nwAppnSysAdminReset": nwAppnSysAdminReset,
       "nwAppnSysOperationalTime": nwAppnSysOperationalTime,
       "nwAppnSysVersion": nwAppnSysVersion,
       "nwAppnForwarding": nwAppnForwarding,
       "nwAppnFwdSystem": nwAppnFwdSystem,
       "nwAppnFwdCounters": nwAppnFwdCounters,
       "nwAppnFwdCtrAdminStatus": nwAppnFwdCtrAdminStatus,
       "nwAppnFwdCtrReset": nwAppnFwdCtrReset,
       "nwAppnFwdCtrOperationalTime": nwAppnFwdCtrOperationalTime,
       "nwAppnFwdCtrInMus": nwAppnFwdCtrInMus,
       "nwAppnFwdCtrOutMus": nwAppnFwdCtrOutMus,
       "nwAppnFwdCtrFwdMus": nwAppnFwdCtrFwdMus,
       "nwAppnFwdCtrFilteredMus": nwAppnFwdCtrFilteredMus,
       "nwAppnFwdCtrDiscardMus": nwAppnFwdCtrDiscardMus,
       "nwAppnFwdCtrAddrErrMus": nwAppnFwdCtrAddrErrMus,
       "nwAppnFwdCtrLenErrMus": nwAppnFwdCtrLenErrMus,
       "nwAppnFwdCtrHdrErrMus": nwAppnFwdCtrHdrErrMus,
       "nwAppnFwdCtrInBytes": nwAppnFwdCtrInBytes,
       "nwAppnFwdCtrOutBytes": nwAppnFwdCtrOutBytes,
       "nwAppnFwdCtrFwdBytes": nwAppnFwdCtrFwdBytes,
       "nwAppnFwdCtrFilteredBytes": nwAppnFwdCtrFilteredBytes,
       "nwAppnFwdCtrDiscardBytes": nwAppnFwdCtrDiscardBytes,
       "nwAppnFwdCtrHostInMus": nwAppnFwdCtrHostInMus,
       "nwAppnFwdCtrHostOutMus": nwAppnFwdCtrHostOutMus,
       "nwAppnFwdCtrHostDiscardMus": nwAppnFwdCtrHostDiscardMus,
       "nwAppnFwdCtrHostInBytes": nwAppnFwdCtrHostInBytes,
       "nwAppnFwdCtrHostOutBytes": nwAppnFwdCtrHostOutBytes,
       "nwAppnFwdCtrHostDiscardBytes": nwAppnFwdCtrHostDiscardBytes,
       "nwAppnFwdInterfaces": nwAppnFwdInterfaces,
       "nwAppnFwdIfConfig": nwAppnFwdIfConfig,
       "nwAppnFwdIfTable": nwAppnFwdIfTable,
       "nwAppnFwdIfEntry": nwAppnFwdIfEntry,
       "nwAppnFwdIfIndex": nwAppnFwdIfIndex,
       "nwAppnFwdIfAdminStatus": nwAppnFwdIfAdminStatus,
       "nwAppnFwdIfOperStatus": nwAppnFwdIfOperStatus,
       "nwAppnFwdIfOperationalTime": nwAppnFwdIfOperationalTime,
       "nwAppnFwdIfControl": nwAppnFwdIfControl,
       "nwAppnFwdIfMtu": nwAppnFwdIfMtu,
       "nwAppnFwdIfForwarding": nwAppnFwdIfForwarding,
       "nwAppnFwdIfFrameType": nwAppnFwdIfFrameType,
       "nwAppnFwdIfAclIdentifier": nwAppnFwdIfAclIdentifier,
       "nwAppnFwdIfAclStatus": nwAppnFwdIfAclStatus,
       "nwAppnFwdIfCacheControl": nwAppnFwdIfCacheControl,
       "nwAppnFwdIfCacheEntries": nwAppnFwdIfCacheEntries,
       "nwAppnFwdIfCacheHits": nwAppnFwdIfCacheHits,
       "nwAppnFwdIfCacheMisses": nwAppnFwdIfCacheMisses,
       "nwAppnExtensionTable": nwAppnExtensionTable,
       "nwAppnExtEntry": nwAppnExtEntry,
       "nwAppnExtIfIndex": nwAppnExtIfIndex,
       "nwAppnExtIfPortName": nwAppnExtIfPortName,
       "nwAppnExtIfPortType": nwAppnExtIfPortType,
       "nwAppnExtIfDlcType": nwAppnExtIfDlcType,
       "nwAppnExtIfMaxRBtuSize": nwAppnExtIfMaxRBtuSize,
       "nwAppnExtIfTotLsActLim": nwAppnExtIfTotLsActLim,
       "nwAppnExtIfInbLsActLim": nwAppnExtIfInbLsActLim,
       "nwAppnExtIfOutbLsActLim": nwAppnExtIfOutbLsActLim,
       "nwAppnExtIfLocalLsRole": nwAppnExtIfLocalLsRole,
       "nwAppnExtIfActXidXchgLimit": nwAppnExtIfActXidXchgLimit,
       "nwAppnExtIfNonActXidXchgLimit": nwAppnExtIfNonActXidXchgLimit,
       "nwAppnExtIfLsXmitRcvCap": nwAppnExtIfLsXmitRcvCap,
       "nwAppnExtIfMaxIfrmRcvd": nwAppnExtIfMaxIfrmRcvd,
       "nwAppnExtIfDfltTargetPacing": nwAppnExtIfDfltTargetPacing,
       "nwAppnExtIfDfltMaxSBtuSize": nwAppnExtIfDfltMaxSBtuSize,
       "nwAppnExtIfDfltEffectCap": nwAppnExtIfDfltEffectCap,
       "nwAppnExtIfDfltConnectCost": nwAppnExtIfDfltConnectCost,
       "nwAppnExtIfDfltByteCost": nwAppnExtIfDfltByteCost,
       "nwAppnExtIfDfltSecurity": nwAppnExtIfDfltSecurity,
       "nwAppnExtIfDfltPropDelay": nwAppnExtIfDfltPropDelay,
       "nwAppnExtIfDfltUsrDef1": nwAppnExtIfDfltUsrDef1,
       "nwAppnExtIfDfltUsrDef2": nwAppnExtIfDfltUsrDef2,
       "nwAppnExtIfDfltUsrDef3": nwAppnExtIfDfltUsrDef3,
       "nwAppnExtIfStopType": nwAppnExtIfStopType,
       "nwAppnExtIfCpCpSupp": nwAppnExtIfCpCpSupp,
       "nwAppnExtIfLimitedRsrc": nwAppnExtIfLimitedRsrc,
       "nwAppnExtIfAddress": nwAppnExtIfAddress,
       "nwAppnExtIfSsap": nwAppnExtIfSsap,
       "nwAppnIfCn": nwAppnIfCn,
       "nwAppnIfCnPortTable": nwAppnIfCnPortTable,
       "nwAppnIfCnPortEntry": nwAppnIfCnPortEntry,
       "nwAppnIfCnPtFqName": nwAppnIfCnPtFqName,
       "nwAppnIfCnPtName": nwAppnIfCnPtName,
       "nwAppnIfCnPtControl": nwAppnIfCnPtControl,
       "nwAppnIfCnTgCharTable": nwAppnIfCnTgCharTable,
       "nwAppnIfCnTgCharEntry": nwAppnIfCnTgCharEntry,
       "nwAppnIfCnTgFqName": nwAppnIfCnTgFqName,
       "nwAppnIfCnTgEffectCap": nwAppnIfCnTgEffectCap,
       "nwAppnIfCnTgConnectCost": nwAppnIfCnTgConnectCost,
       "nwAppnIfCnTgByteCost": nwAppnIfCnTgByteCost,
       "nwAppnIfCnTgSecurity": nwAppnIfCnTgSecurity,
       "nwAppnIfCnTgPropDelay": nwAppnIfCnTgPropDelay,
       "nwAppnIfCnTgUsrDef1": nwAppnIfCnTgUsrDef1,
       "nwAppnIfCnTgUsrDef2": nwAppnIfCnTgUsrDef2,
       "nwAppnIfCnTgUsrDef3": nwAppnIfCnTgUsrDef3,
       "nwAppnFwdIfCounters": nwAppnFwdIfCounters,
       "nwAppnFwdIfCtrTable": nwAppnFwdIfCtrTable,
       "nwAppnFwdIfCtrEntry": nwAppnFwdIfCtrEntry,
       "nwAppnFwdIfCtrIfIndex": nwAppnFwdIfCtrIfIndex,
       "nwAppnFwdIfCtrAdminStatus": nwAppnFwdIfCtrAdminStatus,
       "nwAppnFwdIfCtrReset": nwAppnFwdIfCtrReset,
       "nwAppnFwdIfCtrOperationalTime": nwAppnFwdIfCtrOperationalTime,
       "nwAppnFwdIfCtrInMus": nwAppnFwdIfCtrInMus,
       "nwAppnFwdIfCtrOutMus": nwAppnFwdIfCtrOutMus,
       "nwAppnFwdIfCtrFwdMus": nwAppnFwdIfCtrFwdMus,
       "nwAppnFwdIfCtrFilteredMus": nwAppnFwdIfCtrFilteredMus,
       "nwAppnFwdIfCtrDiscardMus": nwAppnFwdIfCtrDiscardMus,
       "nwAppnFwdIfCtrAddrErrMus": nwAppnFwdIfCtrAddrErrMus,
       "nwAppnFwdIfCtrLenErrMus": nwAppnFwdIfCtrLenErrMus,
       "nwAppnFwdIfCtrHdrErrMus": nwAppnFwdIfCtrHdrErrMus,
       "nwAppnFwdIfCtrInBytes": nwAppnFwdIfCtrInBytes,
       "nwAppnFwdIfCtrOutBytes": nwAppnFwdIfCtrOutBytes,
       "nwAppnFwdIfCtrFwdBytes": nwAppnFwdIfCtrFwdBytes,
       "nwAppnFwdIfCtrFilteredBytes": nwAppnFwdIfCtrFilteredBytes,
       "nwAppnFwdIfCtrDiscardBytes": nwAppnFwdIfCtrDiscardBytes,
       "nwAppnFwdIfCtrHostInMus": nwAppnFwdIfCtrHostInMus,
       "nwAppnFwdIfCtrHostOutMus": nwAppnFwdIfCtrHostOutMus,
       "nwAppnFwdIfCtrHostDiscardMus": nwAppnFwdIfCtrHostDiscardMus,
       "nwAppnFwdIfCtrHostInBytes": nwAppnFwdIfCtrHostInBytes,
       "nwAppnFwdIfCtrHostOutBytes": nwAppnFwdIfCtrHostOutBytes,
       "nwAppnFwdIfCtrHostDiscardBytes": nwAppnFwdIfCtrHostDiscardBytes,
       "nwAppnFwdLinks": nwAppnFwdLinks,
       "nwAppnFwdLsConfig": nwAppnFwdLsConfig,
       "nwAppnFwdLsTable": nwAppnFwdLsTable,
       "nwAppnFwdLsEntry": nwAppnFwdLsEntry,
       "nwAppnFwdLsName": nwAppnFwdLsName,
       "nwAppnFwdLsAdminStatus": nwAppnFwdLsAdminStatus,
       "nwAppnFwdLsOperStatus": nwAppnFwdLsOperStatus,
       "nwAppnFwdLsOperationalTime": nwAppnFwdLsOperationalTime,
       "nwAppnFwdLsControl": nwAppnFwdLsControl,
       "nwAppnFwdLsPortName": nwAppnFwdLsPortName,
       "nwAppnFwdLsAdjCpName": nwAppnFwdLsAdjCpName,
       "nwAppnFwdLsAdjCpType": nwAppnFwdLsAdjCpType,
       "nwAppnFwdLsAutoActSupport": nwAppnFwdLsAutoActSupport,
       "nwAppnFwdLsLimitedRsrc": nwAppnFwdLsLimitedRsrc,
       "nwAppnFwdLsSscpSession": nwAppnFwdLsSscpSession,
       "nwAppnFwdLsPuName": nwAppnFwdLsPuName,
       "nwAppnFwdLsBackLvlLenEN": nwAppnFwdLsBackLvlLenEN,
       "nwAppnFwdLsCpCpSessSupp": nwAppnFwdLsCpCpSessSupp,
       "nwAppnFwdLsEffectCap": nwAppnFwdLsEffectCap,
       "nwAppnFwdLsConnectCost": nwAppnFwdLsConnectCost,
       "nwAppnFwdLsByteCost": nwAppnFwdLsByteCost,
       "nwAppnFwdLsSecurity": nwAppnFwdLsSecurity,
       "nwAppnFwdLsPropDelay": nwAppnFwdLsPropDelay,
       "nwAppnFwdLsUsrDef1": nwAppnFwdLsUsrDef1,
       "nwAppnFwdLsUsrDef2": nwAppnFwdLsUsrDef2,
       "nwAppnFwdLsUsrDef3": nwAppnFwdLsUsrDef3,
       "nwAppnFwdLsTrgtPacingCount": nwAppnFwdLsTrgtPacingCount,
       "nwAppnFwdLsMaxSendBtu": nwAppnFwdLsMaxSendBtu,
       "nwAppnFwdLsNumActiveSession": nwAppnFwdLsNumActiveSession,
       "nwAppnFwdLsdynamicLs": nwAppnFwdLsdynamicLs,
       "nwAppnFwdLsStopType": nwAppnFwdLsStopType,
       "nwAppnFwdLsPortNbr": nwAppnFwdLsPortNbr,
       "nwAppnFwdLsDestAddr": nwAppnFwdLsDestAddr,
       "nwAppnFwdLsDsap": nwAppnFwdLsDsap,
       "nwAppnFwdLsBlockNum": nwAppnFwdLsBlockNum,
       "nwAppnFwdLsIdNum": nwAppnFwdLsIdNum,
       "nwAppnFwdLsCounters": nwAppnFwdLsCounters,
       "nwAppnFwdLsCtrTable": nwAppnFwdLsCtrTable,
       "nwAppnFwdLsCtrEntry": nwAppnFwdLsCtrEntry,
       "nwAppnFwdLsCtrLsName": nwAppnFwdLsCtrLsName,
       "nwAppnFwdLsCtrAdminStatus": nwAppnFwdLsCtrAdminStatus,
       "nwAppnFwdLsCtrReset": nwAppnFwdLsCtrReset,
       "nwAppnFwdLsCtrOperationalTime": nwAppnFwdLsCtrOperationalTime,
       "nwAppnFwdLsCtrInBlus": nwAppnFwdLsCtrInBlus,
       "nwAppnFwdLsCtrOutBlus": nwAppnFwdLsCtrOutBlus,
       "nwAppnFwdLsCtrFwdBlus": nwAppnFwdLsCtrFwdBlus,
       "nwAppnFwdLsCtrFilteredBlus": nwAppnFwdLsCtrFilteredBlus,
       "nwAppnFwdLsCtrDiscardBlus": nwAppnFwdLsCtrDiscardBlus,
       "nwAppnFwdLsCtrAddrErrBlus": nwAppnFwdLsCtrAddrErrBlus,
       "nwAppnFwdLsCtrLenErrBlus": nwAppnFwdLsCtrLenErrBlus,
       "nwAppnFwdLsCtrHdrErrBlus": nwAppnFwdLsCtrHdrErrBlus,
       "nwAppnFwdLsCtrInBytes": nwAppnFwdLsCtrInBytes,
       "nwAppnFwdLsCtrOutBytes": nwAppnFwdLsCtrOutBytes,
       "nwAppnFwdLsCtrFwdBytes": nwAppnFwdLsCtrFwdBytes,
       "nwAppnFwdLsCtrFilteredBytes": nwAppnFwdLsCtrFilteredBytes,
       "nwAppnFwdLsCtrDiscardBytes": nwAppnFwdLsCtrDiscardBytes,
       "nwAppnFwdLsCtrHostInBlus": nwAppnFwdLsCtrHostInBlus,
       "nwAppnFwdLsCtrHostOutBlus": nwAppnFwdLsCtrHostOutBlus,
       "nwAppnFwdLsCtrHostDiscardBlus": nwAppnFwdLsCtrHostDiscardBlus,
       "nwAppnFwdLsCtrHostInBytes": nwAppnFwdLsCtrHostInBytes,
       "nwAppnFwdLsCtrHostOutBytes": nwAppnFwdLsCtrHostOutBytes,
       "nwAppnFwdLsCtrHostDiscardBytes": nwAppnFwdLsCtrHostDiscardBytes,
       "nwAppnTopology": nwAppnTopology,
       "nwAppnDistanceVector": nwAppnDistanceVector,
       "nwAppnLinkState": nwAppnLinkState,
       "nwAppnIsr": nwAppnIsr,
       "nwAppnIsrSystem": nwAppnIsrSystem,
       "nwAppnIsrConfig": nwAppnIsrConfig,
       "nwAppnIsrAdminStatus": nwAppnIsrAdminStatus,
       "nwAppnIsrOperStatus": nwAppnIsrOperStatus,
       "nwAppnIsrAdminReset": nwAppnIsrAdminReset,
       "nwAppnIsrOperationalTime": nwAppnIsrOperationalTime,
       "nwAppnIsrVersion": nwAppnIsrVersion,
       "nwAppnIsrCounters": nwAppnIsrCounters,
       "nwAppnIsrInterfaces": nwAppnIsrInterfaces,
       "nwAppnIsrIfConfig": nwAppnIsrIfConfig,
       "nwAppnIsrIfCounters": nwAppnIsrIfCounters,
       "nwAppnIsrDatabase": nwAppnIsrDatabase,
       "nwAppnIsrFilters": nwAppnIsrFilters,
       "nwAppnFib": nwAppnFib,
       "nwAppnEndSystems": nwAppnEndSystems,
       "nwAppnHostsSystem": nwAppnHostsSystem,
       "nwAppnHostsInterfaces": nwAppnHostsInterfaces,
       "nwAppnAccessControl": nwAppnAccessControl,
       "nwAppnFilters": nwAppnFilters,
       "nwAppnRedirector": nwAppnRedirector,
       "nwAppnEvent": nwAppnEvent,
       "nwAppnEventLogConfig": nwAppnEventLogConfig,
       "nwAppnEventAdminStatus": nwAppnEventAdminStatus,
       "nwAppnEventMaxEntries": nwAppnEventMaxEntries,
       "nwAppnEventTraceAll": nwAppnEventTraceAll,
       "nwAppnEventLogFilterTable": nwAppnEventLogFilterTable,
       "nwAppnEventFilterTable": nwAppnEventFilterTable,
       "nwAppnEventFilterEntry": nwAppnEventFilterEntry,
       "nwAppnEventFltrProtocol": nwAppnEventFltrProtocol,
       "nwAppnEventFltrIfNum": nwAppnEventFltrIfNum,
       "nwAppnEventFltrControl": nwAppnEventFltrControl,
       "nwAppnEventFltrType": nwAppnEventFltrType,
       "nwAppnEventFltrSeverity": nwAppnEventFltrSeverity,
       "nwAppnEventFltrAction": nwAppnEventFltrAction,
       "nwAppnEventLogTable": nwAppnEventLogTable,
       "nwAppnEventTable": nwAppnEventTable,
       "nwAppnEventEntry": nwAppnEventEntry,
       "nwAppnEventNumber": nwAppnEventNumber,
       "nwAppnEventTime": nwAppnEventTime,
       "nwAppnEventType": nwAppnEventType,
       "nwAppnEventSeverity": nwAppnEventSeverity,
       "nwAppnEventProtocol": nwAppnEventProtocol,
       "nwAppnEventIfNum": nwAppnEventIfNum,
       "nwAppnEventTextString": nwAppnEventTextString,
       "nwAppnWorkGroup": nwAppnWorkGroup}
)
