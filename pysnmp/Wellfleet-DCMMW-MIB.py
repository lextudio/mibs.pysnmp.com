# SNMP MIB module (Wellfleet-DCMMW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-DCMMW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:00 2024
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

(wfDCMmwGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfDCMmwGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfDCMmw_ObjectIdentity = ObjectIdentity
wfDCMmw = _WfDCMmw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 1)
)


class _WfDCMmwDelete_Type(Integer32):
    """Custom type wfDCMmwDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDCMmwDelete_Type.__name__ = "Integer32"
_WfDCMmwDelete_Object = MibScalar
wfDCMmwDelete = _WfDCMmwDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 1, 1),
    _WfDCMmwDelete_Type()
)
wfDCMmwDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDCMmwDelete.setStatus("obsolete")


class _WfDCMmwDisable_Type(Integer32):
    """Custom type wfDCMmwDisable based on Integer32"""
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


_WfDCMmwDisable_Type.__name__ = "Integer32"
_WfDCMmwDisable_Object = MibScalar
wfDCMmwDisable = _WfDCMmwDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 1, 2),
    _WfDCMmwDisable_Type()
)
wfDCMmwDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDCMmwDisable.setStatus("obsolete")


class _WfDCMmwImageName_Type(DisplayString):
    """Custom type wfDCMmwImageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_WfDCMmwImageName_Type.__name__ = "DisplayString"
_WfDCMmwImageName_Object = MibScalar
wfDCMmwImageName = _WfDCMmwImageName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 1, 3),
    _WfDCMmwImageName_Type()
)
wfDCMmwImageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDCMmwImageName.setStatus("obsolete")


class _WfDCMmwBootOption_Type(Integer32):
    """Custom type wfDCMmwBootOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 2),
          ("local", 1))
    )


_WfDCMmwBootOption_Type.__name__ = "Integer32"
_WfDCMmwBootOption_Object = MibScalar
wfDCMmwBootOption = _WfDCMmwBootOption_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 1, 4),
    _WfDCMmwBootOption_Type()
)
wfDCMmwBootOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDCMmwBootOption.setStatus("obsolete")


class _WfDCMmwImageSaveMode_Type(Integer32):
    """Custom type wfDCMmwImageSaveMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nosave", 2),
          ("save", 1))
    )


_WfDCMmwImageSaveMode_Type.__name__ = "Integer32"
_WfDCMmwImageSaveMode_Object = MibScalar
wfDCMmwImageSaveMode = _WfDCMmwImageSaveMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 1, 5),
    _WfDCMmwImageSaveMode_Type()
)
wfDCMmwImageSaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDCMmwImageSaveMode.setStatus("obsolete")


class _WfDCMmwCfgMode_Type(Integer32):
    """Custom type wfDCMmwCfgMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("shmem", 2))
    )


_WfDCMmwCfgMode_Type.__name__ = "Integer32"
_WfDCMmwCfgMode_Object = MibScalar
wfDCMmwCfgMode = _WfDCMmwCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 1, 6),
    _WfDCMmwCfgMode_Type()
)
wfDCMmwCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDCMmwCfgMode.setStatus("obsolete")


class _WfDCMmwWriteConfigInfo_Type(Integer32):
    """Custom type wfDCMmwWriteConfigInfo based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nosave", 2),
          ("save", 1))
    )


_WfDCMmwWriteConfigInfo_Type.__name__ = "Integer32"
_WfDCMmwWriteConfigInfo_Object = MibScalar
wfDCMmwWriteConfigInfo = _WfDCMmwWriteConfigInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 1, 7),
    _WfDCMmwWriteConfigInfo_Type()
)
wfDCMmwWriteConfigInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDCMmwWriteConfigInfo.setStatus("obsolete")


class _WfDCMmwRMONMaxHost_Type(Integer32):
    """Custom type wfDCMmwRMONMaxHost based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 8128),
    )


_WfDCMmwRMONMaxHost_Type.__name__ = "Integer32"
_WfDCMmwRMONMaxHost_Object = MibScalar
wfDCMmwRMONMaxHost = _WfDCMmwRMONMaxHost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 1, 8),
    _WfDCMmwRMONMaxHost_Type()
)
wfDCMmwRMONMaxHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDCMmwRMONMaxHost.setStatus("obsolete")


class _WfDCMmwRMONDfltHost_Type(Integer32):
    """Custom type wfDCMmwRMONDfltHost based on Integer32"""
    defaultValue = 2

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


_WfDCMmwRMONDfltHost_Type.__name__ = "Integer32"
_WfDCMmwRMONDfltHost_Object = MibScalar
wfDCMmwRMONDfltHost = _WfDCMmwRMONDfltHost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 1, 9),
    _WfDCMmwRMONDfltHost_Type()
)
wfDCMmwRMONDfltHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDCMmwRMONDfltHost.setStatus("obsolete")


class _WfDCMmwRMONDfltMtrix_Type(Integer32):
    """Custom type wfDCMmwRMONDfltMtrix based on Integer32"""
    defaultValue = 2

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


_WfDCMmwRMONDfltMtrix_Type.__name__ = "Integer32"
_WfDCMmwRMONDfltMtrix_Object = MibScalar
wfDCMmwRMONDfltMtrix = _WfDCMmwRMONDfltMtrix_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 1, 10),
    _WfDCMmwRMONDfltMtrix_Type()
)
wfDCMmwRMONDfltMtrix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDCMmwRMONDfltMtrix.setStatus("obsolete")
_WfDCMmwRMONHost_Type = Integer32
_WfDCMmwRMONHost_Object = MibScalar
wfDCMmwRMONHost = _WfDCMmwRMONHost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 1, 11),
    _WfDCMmwRMONHost_Type()
)
wfDCMmwRMONHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDCMmwRMONHost.setStatus("obsolete")


class _WfDCMRmonAgent_Type(Integer32):
    """Custom type wfDCMRmonAgent based on Integer32"""
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
          ("ready", 1))
    )


_WfDCMRmonAgent_Type.__name__ = "Integer32"
_WfDCMRmonAgent_Object = MibScalar
wfDCMRmonAgent = _WfDCMRmonAgent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 1, 12),
    _WfDCMRmonAgent_Type()
)
wfDCMRmonAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDCMRmonAgent.setStatus("obsolete")
_WfDCMMemSize_Type = Integer32
_WfDCMMemSize_Object = MibScalar
wfDCMMemSize = _WfDCMMemSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 1, 13),
    _WfDCMMemSize_Type()
)
wfDCMMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDCMMemSize.setStatus("obsolete")


class _WfDCMHwRev_Type(DisplayString):
    """Custom type wfDCMHwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_WfDCMHwRev_Type.__name__ = "DisplayString"
_WfDCMHwRev_Object = MibScalar
wfDCMHwRev = _WfDCMHwRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 1, 14),
    _WfDCMHwRev_Type()
)
wfDCMHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDCMHwRev.setStatus("obsolete")


class _WfDCMFwRev_Type(DisplayString):
    """Custom type wfDCMFwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_WfDCMFwRev_Type.__name__ = "DisplayString"
_WfDCMFwRev_Object = MibScalar
wfDCMFwRev = _WfDCMFwRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 1, 15),
    _WfDCMFwRev_Type()
)
wfDCMFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDCMFwRev.setStatus("obsolete")


class _WfDCMAgentImageVersion_Type(DisplayString):
    """Custom type wfDCMAgentImageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_WfDCMAgentImageVersion_Type.__name__ = "DisplayString"
_WfDCMAgentImageVersion_Object = MibScalar
wfDCMAgentImageVersion = _WfDCMAgentImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 1, 16),
    _WfDCMAgentImageVersion_Type()
)
wfDCMAgentImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDCMAgentImageVersion.setStatus("obsolete")
_WfDCMmwNumDCM_Type = Integer32
_WfDCMmwNumDCM_Object = MibScalar
wfDCMmwNumDCM = _WfDCMmwNumDCM_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 1, 17),
    _WfDCMmwNumDCM_Type()
)
wfDCMmwNumDCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDCMmwNumDCM.setStatus("obsolete")
_WfDCMTable_Object = MibTable
wfDCMTable = _WfDCMTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 2)
)
if mibBuilder.loadTexts:
    wfDCMTable.setStatus("mandatory")
_WfDCMEntry_Object = MibTableRow
wfDCMEntry = _WfDCMEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 2, 1)
)
wfDCMEntry.setIndexNames(
    (0, "Wellfleet-DCMMW-MIB", "wfDCMIndex"),
)
if mibBuilder.loadTexts:
    wfDCMEntry.setStatus("mandatory")


class _WfDCMDelete_Type(Integer32):
    """Custom type wfDCMDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDCMDelete_Type.__name__ = "Integer32"
_WfDCMDelete_Object = MibTableColumn
wfDCMDelete = _WfDCMDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 2, 1, 1),
    _WfDCMDelete_Type()
)
wfDCMDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDCMDelete.setStatus("mandatory")
_WfDCMIndex_Type = Integer32
_WfDCMIndex_Object = MibTableColumn
wfDCMIndex = _WfDCMIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 2, 1, 2),
    _WfDCMIndex_Type()
)
wfDCMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDCMIndex.setStatus("mandatory")


class _WfDCMDisable_Type(Integer32):
    """Custom type wfDCMDisable based on Integer32"""
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


_WfDCMDisable_Type.__name__ = "Integer32"
_WfDCMDisable_Object = MibTableColumn
wfDCMDisable = _WfDCMDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 2, 1, 3),
    _WfDCMDisable_Type()
)
wfDCMDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDCMDisable.setStatus("mandatory")


class _WfDCMOperStatus_Type(Integer32):
    """Custom type wfDCMOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("init", 3),
          ("up", 1))
    )


_WfDCMOperStatus_Type.__name__ = "Integer32"
_WfDCMOperStatus_Object = MibTableColumn
wfDCMOperStatus = _WfDCMOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 2, 1, 4),
    _WfDCMOperStatus_Type()
)
wfDCMOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDCMOperStatus.setStatus("mandatory")


class _WfDCMStreamCount_Type(Integer32):
    """Custom type wfDCMStreamCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WfDCMStreamCount_Type.__name__ = "Integer32"
_WfDCMStreamCount_Object = MibTableColumn
wfDCMStreamCount = _WfDCMStreamCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 2, 1, 5),
    _WfDCMStreamCount_Type()
)
wfDCMStreamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDCMStreamCount.setStatus("mandatory")


class _WfDCMIntfType_Type(Integer32):
    """Custom type wfDCMIntfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ether", 6),
          ("tokenring", 9))
    )


_WfDCMIntfType_Type.__name__ = "Integer32"
_WfDCMIntfType_Object = MibTableColumn
wfDCMIntfType = _WfDCMIntfType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 2, 1, 6),
    _WfDCMIntfType_Type()
)
wfDCMIntfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDCMIntfType.setStatus("mandatory")
_WfDCMImageName_Type = DisplayString
_WfDCMImageName_Object = MibTableColumn
wfDCMImageName = _WfDCMImageName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 2, 1, 7),
    _WfDCMImageName_Type()
)
wfDCMImageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDCMImageName.setStatus("mandatory")


class _WfDCMBootOption_Type(Integer32):
    """Custom type wfDCMBootOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 2),
          ("local", 1))
    )


_WfDCMBootOption_Type.__name__ = "Integer32"
_WfDCMBootOption_Object = MibTableColumn
wfDCMBootOption = _WfDCMBootOption_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 2, 1, 8),
    _WfDCMBootOption_Type()
)
wfDCMBootOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDCMBootOption.setStatus("mandatory")


class _WfDCMImageSaveMode_Type(Integer32):
    """Custom type wfDCMImageSaveMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nosave", 2),
          ("save", 1))
    )


_WfDCMImageSaveMode_Type.__name__ = "Integer32"
_WfDCMImageSaveMode_Object = MibTableColumn
wfDCMImageSaveMode = _WfDCMImageSaveMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 2, 1, 9),
    _WfDCMImageSaveMode_Type()
)
wfDCMImageSaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDCMImageSaveMode.setStatus("mandatory")


class _WfDCMCfgMode_Type(Integer32):
    """Custom type wfDCMCfgMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("shmem", 2))
    )


_WfDCMCfgMode_Type.__name__ = "Integer32"
_WfDCMCfgMode_Object = MibTableColumn
wfDCMCfgMode = _WfDCMCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 2, 1, 10),
    _WfDCMCfgMode_Type()
)
wfDCMCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDCMCfgMode.setStatus("mandatory")


class _WfDCMSaveConfigInfo_Type(Integer32):
    """Custom type wfDCMSaveConfigInfo based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nosave", 2),
          ("save", 1))
    )


_WfDCMSaveConfigInfo_Type.__name__ = "Integer32"
_WfDCMSaveConfigInfo_Object = MibTableColumn
wfDCMSaveConfigInfo = _WfDCMSaveConfigInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 2, 1, 11),
    _WfDCMSaveConfigInfo_Type()
)
wfDCMSaveConfigInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDCMSaveConfigInfo.setStatus("mandatory")


class _WfDCMRMONMaxHost_Type(Integer32):
    """Custom type wfDCMRMONMaxHost based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 8128),
    )


_WfDCMRMONMaxHost_Type.__name__ = "Integer32"
_WfDCMRMONMaxHost_Object = MibTableColumn
wfDCMRMONMaxHost = _WfDCMRMONMaxHost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 2, 1, 12),
    _WfDCMRMONMaxHost_Type()
)
wfDCMRMONMaxHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDCMRMONMaxHost.setStatus("mandatory")


class _WfDCMRMONDfltHost_Type(Integer32):
    """Custom type wfDCMRMONDfltHost based on Integer32"""
    defaultValue = 2

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


_WfDCMRMONDfltHost_Type.__name__ = "Integer32"
_WfDCMRMONDfltHost_Object = MibTableColumn
wfDCMRMONDfltHost = _WfDCMRMONDfltHost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 2, 1, 13),
    _WfDCMRMONDfltHost_Type()
)
wfDCMRMONDfltHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDCMRMONDfltHost.setStatus("mandatory")


class _WfDCMRMONDfltMtrix_Type(Integer32):
    """Custom type wfDCMRMONDfltMtrix based on Integer32"""
    defaultValue = 2

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


_WfDCMRMONDfltMtrix_Type.__name__ = "Integer32"
_WfDCMRMONDfltMtrix_Object = MibTableColumn
wfDCMRMONDfltMtrix = _WfDCMRMONDfltMtrix_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 2, 1, 14),
    _WfDCMRMONDfltMtrix_Type()
)
wfDCMRMONDfltMtrix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDCMRMONDfltMtrix.setStatus("mandatory")
_WfDCMRMONHost_Type = Integer32
_WfDCMRMONHost_Object = MibTableColumn
wfDCMRMONHost = _WfDCMRMONHost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 2, 1, 15),
    _WfDCMRMONHost_Type()
)
wfDCMRMONHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDCMRMONHost.setStatus("mandatory")
_WfDCMmemSize_Type = Integer32
_WfDCMmemSize_Object = MibTableColumn
wfDCMmemSize = _WfDCMmemSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 2, 1, 16),
    _WfDCMmemSize_Type()
)
wfDCMmemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDCMmemSize.setStatus("mandatory")
_WfDCMhwRev_Type = DisplayString
_WfDCMhwRev_Object = MibTableColumn
wfDCMhwRev = _WfDCMhwRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 2, 1, 17),
    _WfDCMhwRev_Type()
)
wfDCMhwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDCMhwRev.setStatus("mandatory")
_WfDCMfwRev_Type = DisplayString
_WfDCMfwRev_Object = MibTableColumn
wfDCMfwRev = _WfDCMfwRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 2, 1, 18),
    _WfDCMfwRev_Type()
)
wfDCMfwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDCMfwRev.setStatus("mandatory")
_WfDCMagentImageVersion_Type = DisplayString
_WfDCMagentImageVersion_Object = MibTableColumn
wfDCMagentImageVersion = _WfDCMagentImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 2, 1, 19),
    _WfDCMagentImageVersion_Type()
)
wfDCMagentImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDCMagentImageVersion.setStatus("mandatory")


class _WfDCMRmonObjectSupport_Type(Integer32):
    """Custom type wfDCMRmonObjectSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rmon", 1),
          ("rmon2", 2))
    )


_WfDCMRmonObjectSupport_Type.__name__ = "Integer32"
_WfDCMRmonObjectSupport_Object = MibTableColumn
wfDCMRmonObjectSupport = _WfDCMRmonObjectSupport_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 2, 1, 20),
    _WfDCMRmonObjectSupport_Type()
)
wfDCMRmonObjectSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDCMRmonObjectSupport.setStatus("mandatory")
_WfDCMStreamTable_Object = MibTable
wfDCMStreamTable = _WfDCMStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 3)
)
if mibBuilder.loadTexts:
    wfDCMStreamTable.setStatus("obsolete")
_WfDCMStreamEntry_Object = MibTableRow
wfDCMStreamEntry = _WfDCMStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 3, 1)
)
wfDCMStreamEntry.setIndexNames(
    (0, "Wellfleet-DCMMW-MIB", "wfDCMStreamDCMIndex"),
    (0, "Wellfleet-DCMMW-MIB", "wfDCMStreamIndex"),
)
if mibBuilder.loadTexts:
    wfDCMStreamEntry.setStatus("obsolete")
_WfDCMStreamDCMIndex_Type = Integer32
_WfDCMStreamDCMIndex_Object = MibTableColumn
wfDCMStreamDCMIndex = _WfDCMStreamDCMIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 3, 1, 1),
    _WfDCMStreamDCMIndex_Type()
)
wfDCMStreamDCMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDCMStreamDCMIndex.setStatus("obsolete")


class _WfDCMStreamIndex_Type(Integer32):
    """Custom type wfDCMStreamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WfDCMStreamIndex_Type.__name__ = "Integer32"
_WfDCMStreamIndex_Object = MibTableColumn
wfDCMStreamIndex = _WfDCMStreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 3, 1, 2),
    _WfDCMStreamIndex_Type()
)
wfDCMStreamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDCMStreamIndex.setStatus("obsolete")


class _WfDCMStreamDisable_Type(Integer32):
    """Custom type wfDCMStreamDisable based on Integer32"""
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


_WfDCMStreamDisable_Type.__name__ = "Integer32"
_WfDCMStreamDisable_Object = MibTableColumn
wfDCMStreamDisable = _WfDCMStreamDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 3, 1, 3),
    _WfDCMStreamDisable_Type()
)
wfDCMStreamDisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDCMStreamDisable.setStatus("obsolete")
_WfDCMStreamDataSource_Type = ObjectIdentifier
_WfDCMStreamDataSource_Object = MibTableColumn
wfDCMStreamDataSource = _WfDCMStreamDataSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16, 3, 1, 4),
    _WfDCMStreamDataSource_Type()
)
wfDCMStreamDataSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDCMStreamDataSource.setStatus("obsolete")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-DCMMW-MIB",
    **{"wfDCMmw": wfDCMmw,
       "wfDCMmwDelete": wfDCMmwDelete,
       "wfDCMmwDisable": wfDCMmwDisable,
       "wfDCMmwImageName": wfDCMmwImageName,
       "wfDCMmwBootOption": wfDCMmwBootOption,
       "wfDCMmwImageSaveMode": wfDCMmwImageSaveMode,
       "wfDCMmwCfgMode": wfDCMmwCfgMode,
       "wfDCMmwWriteConfigInfo": wfDCMmwWriteConfigInfo,
       "wfDCMmwRMONMaxHost": wfDCMmwRMONMaxHost,
       "wfDCMmwRMONDfltHost": wfDCMmwRMONDfltHost,
       "wfDCMmwRMONDfltMtrix": wfDCMmwRMONDfltMtrix,
       "wfDCMmwRMONHost": wfDCMmwRMONHost,
       "wfDCMRmonAgent": wfDCMRmonAgent,
       "wfDCMMemSize": wfDCMMemSize,
       "wfDCMHwRev": wfDCMHwRev,
       "wfDCMFwRev": wfDCMFwRev,
       "wfDCMAgentImageVersion": wfDCMAgentImageVersion,
       "wfDCMmwNumDCM": wfDCMmwNumDCM,
       "wfDCMTable": wfDCMTable,
       "wfDCMEntry": wfDCMEntry,
       "wfDCMDelete": wfDCMDelete,
       "wfDCMIndex": wfDCMIndex,
       "wfDCMDisable": wfDCMDisable,
       "wfDCMOperStatus": wfDCMOperStatus,
       "wfDCMStreamCount": wfDCMStreamCount,
       "wfDCMIntfType": wfDCMIntfType,
       "wfDCMImageName": wfDCMImageName,
       "wfDCMBootOption": wfDCMBootOption,
       "wfDCMImageSaveMode": wfDCMImageSaveMode,
       "wfDCMCfgMode": wfDCMCfgMode,
       "wfDCMSaveConfigInfo": wfDCMSaveConfigInfo,
       "wfDCMRMONMaxHost": wfDCMRMONMaxHost,
       "wfDCMRMONDfltHost": wfDCMRMONDfltHost,
       "wfDCMRMONDfltMtrix": wfDCMRMONDfltMtrix,
       "wfDCMRMONHost": wfDCMRMONHost,
       "wfDCMmemSize": wfDCMmemSize,
       "wfDCMhwRev": wfDCMhwRev,
       "wfDCMfwRev": wfDCMfwRev,
       "wfDCMagentImageVersion": wfDCMagentImageVersion,
       "wfDCMRmonObjectSupport": wfDCMRmonObjectSupport,
       "wfDCMStreamTable": wfDCMStreamTable,
       "wfDCMStreamEntry": wfDCMStreamEntry,
       "wfDCMStreamDCMIndex": wfDCMStreamDCMIndex,
       "wfDCMStreamIndex": wfDCMStreamIndex,
       "wfDCMStreamDisable": wfDCMStreamDisable,
       "wfDCMStreamDataSource": wfDCMStreamDataSource}
)
