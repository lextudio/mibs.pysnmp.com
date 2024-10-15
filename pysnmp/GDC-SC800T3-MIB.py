# SNMP MIB module (GDC-SC800T3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GDC-SC800T3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:10 2024
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

(gdc,) = mibBuilder.importSymbols(
    "GDCCMN-MIB",
    "gdc")

(SCinstance,) = mibBuilder.importSymbols(
    "GDCMACRO-MIB",
    "SCinstance")

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

_Ds3_ObjectIdentity = ObjectIdentity
ds3 = _Ds3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19)
)
_Sc800t3_ObjectIdentity = ObjectIdentity
sc800t3 = _Sc800t3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1)
)
_Sc800t3Version_ObjectIdentity = ObjectIdentity
sc800t3Version = _Sc800t3Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 1)
)


class _Sc800t3MIBversion_Type(DisplayString):
    """Custom type sc800t3MIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Sc800t3MIBversion_Type.__name__ = "DisplayString"
_Sc800t3MIBversion_Object = MibScalar
sc800t3MIBversion = _Sc800t3MIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 1, 1),
    _Sc800t3MIBversion_Type()
)
sc800t3MIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3MIBversion.setStatus("mandatory")
_Sc800t3VersionTable_Object = MibTable
sc800t3VersionTable = _Sc800t3VersionTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sc800t3VersionTable.setStatus("mandatory")
_Sc800t3VersionEntry_Object = MibTableRow
sc800t3VersionEntry = _Sc800t3VersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 1, 2, 1)
)
sc800t3VersionEntry.setIndexNames(
    (0, "GDC-SC800T3-MIB", "sc800t3VersionIndex"),
)
if mibBuilder.loadTexts:
    sc800t3VersionEntry.setStatus("mandatory")
_Sc800t3VersionIndex_Type = SCinstance
_Sc800t3VersionIndex_Object = MibTableColumn
sc800t3VersionIndex = _Sc800t3VersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 1, 2, 1, 1),
    _Sc800t3VersionIndex_Type()
)
sc800t3VersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3VersionIndex.setStatus("mandatory")


class _Sc800t3ActiveFirmwareRev_Type(DisplayString):
    """Custom type sc800t3ActiveFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Sc800t3ActiveFirmwareRev_Type.__name__ = "DisplayString"
_Sc800t3ActiveFirmwareRev_Object = MibTableColumn
sc800t3ActiveFirmwareRev = _Sc800t3ActiveFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 1, 2, 1, 2),
    _Sc800t3ActiveFirmwareRev_Type()
)
sc800t3ActiveFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3ActiveFirmwareRev.setStatus("mandatory")


class _Sc800t3StandbyFirmwareRev_Type(DisplayString):
    """Custom type sc800t3StandbyFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Sc800t3StandbyFirmwareRev_Type.__name__ = "DisplayString"
_Sc800t3StandbyFirmwareRev_Object = MibTableColumn
sc800t3StandbyFirmwareRev = _Sc800t3StandbyFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 1, 2, 1, 3),
    _Sc800t3StandbyFirmwareRev_Type()
)
sc800t3StandbyFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3StandbyFirmwareRev.setStatus("mandatory")


class _Sc800t3StoredFirmwareStatus_Type(Integer32):
    """Custom type sc800t3StoredFirmwareStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("statBadUnZip", 6),
          ("statBlank", 1),
          ("statCheckSumBad", 4),
          ("statDownLoading", 2),
          ("statDownloadAborted", 7),
          ("statOK", 3),
          ("statUnZipping", 5))
    )


_Sc800t3StoredFirmwareStatus_Type.__name__ = "Integer32"
_Sc800t3StoredFirmwareStatus_Object = MibTableColumn
sc800t3StoredFirmwareStatus = _Sc800t3StoredFirmwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 1, 2, 1, 4),
    _Sc800t3StoredFirmwareStatus_Type()
)
sc800t3StoredFirmwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3StoredFirmwareStatus.setStatus("mandatory")


class _Sc800t3SwitchActiveFirmware_Type(Integer32):
    """Custom type sc800t3SwitchActiveFirmware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switchActive", 2),
          ("switchNorm", 1))
    )


_Sc800t3SwitchActiveFirmware_Type.__name__ = "Integer32"
_Sc800t3SwitchActiveFirmware_Object = MibTableColumn
sc800t3SwitchActiveFirmware = _Sc800t3SwitchActiveFirmware_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 1, 2, 1, 5),
    _Sc800t3SwitchActiveFirmware_Type()
)
sc800t3SwitchActiveFirmware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3SwitchActiveFirmware.setStatus("mandatory")


class _Sc800t3DownloadingMode_Type(Integer32):
    """Custom type sc800t3DownloadingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disableAll", 1),
          ("enableAndSwitch", 3),
          ("enableAndWait", 2))
    )


_Sc800t3DownloadingMode_Type.__name__ = "Integer32"
_Sc800t3DownloadingMode_Object = MibTableColumn
sc800t3DownloadingMode = _Sc800t3DownloadingMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 1, 2, 1, 6),
    _Sc800t3DownloadingMode_Type()
)
sc800t3DownloadingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3DownloadingMode.setStatus("mandatory")


class _Sc800t3EraseFlash_Type(Integer32):
    """Custom type sc800t3EraseFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("erase", 2),
          ("normal", 1))
    )


_Sc800t3EraseFlash_Type.__name__ = "Integer32"
_Sc800t3EraseFlash_Object = MibTableColumn
sc800t3EraseFlash = _Sc800t3EraseFlash_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 1, 2, 1, 7),
    _Sc800t3EraseFlash_Type()
)
sc800t3EraseFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3EraseFlash.setStatus("mandatory")
_Sc800t3Configuration_ObjectIdentity = ObjectIdentity
sc800t3Configuration = _Sc800t3Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 2)
)
_Sc800t3ChannelConfigTable_Object = MibTable
sc800t3ChannelConfigTable = _Sc800t3ChannelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sc800t3ChannelConfigTable.setStatus("mandatory")
_Sc800t3ChannelConfigEntry_Object = MibTableRow
sc800t3ChannelConfigEntry = _Sc800t3ChannelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 2, 1, 1)
)
sc800t3ChannelConfigEntry.setIndexNames(
    (0, "GDC-SC800T3-MIB", "sc800t3ChannelConfigIndex"),
)
if mibBuilder.loadTexts:
    sc800t3ChannelConfigEntry.setStatus("mandatory")
_Sc800t3ChannelConfigIndex_Type = SCinstance
_Sc800t3ChannelConfigIndex_Object = MibTableColumn
sc800t3ChannelConfigIndex = _Sc800t3ChannelConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 2, 1, 1, 1),
    _Sc800t3ChannelConfigIndex_Type()
)
sc800t3ChannelConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3ChannelConfigIndex.setStatus("mandatory")


class _Sc800t3ForcedDCE_Type(Integer32):
    """Custom type sc800t3ForcedDCE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("followsDte", 1),
          ("forcedOn", 2))
    )


_Sc800t3ForcedDCE_Type.__name__ = "Integer32"
_Sc800t3ForcedDCE_Object = MibTableColumn
sc800t3ForcedDCE = _Sc800t3ForcedDCE_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 2, 1, 1, 2),
    _Sc800t3ForcedDCE_Type()
)
sc800t3ForcedDCE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3ForcedDCE.setStatus("mandatory")


class _Sc800t3ChannelDTEtest_Type(Integer32):
    """Custom type sc800t3ChannelDTEtest based on Integer32"""
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


_Sc800t3ChannelDTEtest_Type.__name__ = "Integer32"
_Sc800t3ChannelDTEtest_Object = MibTableColumn
sc800t3ChannelDTEtest = _Sc800t3ChannelDTEtest_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 2, 1, 1, 3),
    _Sc800t3ChannelDTEtest_Type()
)
sc800t3ChannelDTEtest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3ChannelDTEtest.setStatus("mandatory")


class _Sc800t3DTELoopTimeout_Type(Integer32):
    """Custom type sc800t3DTELoopTimeout based on Integer32"""
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


_Sc800t3DTELoopTimeout_Type.__name__ = "Integer32"
_Sc800t3DTELoopTimeout_Object = MibTableColumn
sc800t3DTELoopTimeout = _Sc800t3DTELoopTimeout_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 2, 1, 1, 4),
    _Sc800t3DTELoopTimeout_Type()
)
sc800t3DTELoopTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3DTELoopTimeout.setStatus("mandatory")
_Sc800t3NetworkConfigTable_Object = MibTable
sc800t3NetworkConfigTable = _Sc800t3NetworkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 2, 2)
)
if mibBuilder.loadTexts:
    sc800t3NetworkConfigTable.setStatus("mandatory")
_Sc800t3NetworkConfigEntry_Object = MibTableRow
sc800t3NetworkConfigEntry = _Sc800t3NetworkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 2, 2, 1)
)
sc800t3NetworkConfigEntry.setIndexNames(
    (0, "GDC-SC800T3-MIB", "sc800t3NetworkConfigIndex"),
)
if mibBuilder.loadTexts:
    sc800t3NetworkConfigEntry.setStatus("mandatory")
_Sc800t3NetworkConfigIndex_Type = SCinstance
_Sc800t3NetworkConfigIndex_Object = MibTableColumn
sc800t3NetworkConfigIndex = _Sc800t3NetworkConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 2, 2, 1, 1),
    _Sc800t3NetworkConfigIndex_Type()
)
sc800t3NetworkConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3NetworkConfigIndex.setStatus("mandatory")


class _Sc800t3NetworkFrameType_Type(Integer32):
    """Custom type sc800t3NetworkFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cbitParity", 2),
          ("m13", 1))
    )


_Sc800t3NetworkFrameType_Type.__name__ = "Integer32"
_Sc800t3NetworkFrameType_Object = MibTableColumn
sc800t3NetworkFrameType = _Sc800t3NetworkFrameType_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 2, 2, 1, 2),
    _Sc800t3NetworkFrameType_Type()
)
sc800t3NetworkFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3NetworkFrameType.setStatus("mandatory")


class _Sc800t3NetworkTransmitClockSource_Type(Integer32):
    """Custom type sc800t3NetworkTransmitClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("receive", 2))
    )


_Sc800t3NetworkTransmitClockSource_Type.__name__ = "Integer32"
_Sc800t3NetworkTransmitClockSource_Object = MibTableColumn
sc800t3NetworkTransmitClockSource = _Sc800t3NetworkTransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 2, 2, 1, 3),
    _Sc800t3NetworkTransmitClockSource_Type()
)
sc800t3NetworkTransmitClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3NetworkTransmitClockSource.setStatus("mandatory")


class _Sc800t3NetworkAISLoopdown_Type(Integer32):
    """Custom type sc800t3NetworkAISLoopdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_Sc800t3NetworkAISLoopdown_Type.__name__ = "Integer32"
_Sc800t3NetworkAISLoopdown_Object = MibTableColumn
sc800t3NetworkAISLoopdown = _Sc800t3NetworkAISLoopdown_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 2, 2, 1, 4),
    _Sc800t3NetworkAISLoopdown_Type()
)
sc800t3NetworkAISLoopdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3NetworkAISLoopdown.setStatus("mandatory")


class _Sc800t3NetworkLineType_Type(Integer32):
    """Custom type sc800t3NetworkLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("longCable", 1),
          ("shortCable", 2))
    )


_Sc800t3NetworkLineType_Type.__name__ = "Integer32"
_Sc800t3NetworkLineType_Object = MibTableColumn
sc800t3NetworkLineType = _Sc800t3NetworkLineType_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 2, 2, 1, 5),
    _Sc800t3NetworkLineType_Type()
)
sc800t3NetworkLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3NetworkLineType.setStatus("mandatory")


class _Sc800t3NetworkIdleStatus_Type(Integer32):
    """Custom type sc800t3NetworkIdleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notReceived", 1),
          ("received", 2))
    )


_Sc800t3NetworkIdleStatus_Type.__name__ = "Integer32"
_Sc800t3NetworkIdleStatus_Object = MibTableColumn
sc800t3NetworkIdleStatus = _Sc800t3NetworkIdleStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 2, 2, 1, 6),
    _Sc800t3NetworkIdleStatus_Type()
)
sc800t3NetworkIdleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3NetworkIdleStatus.setStatus("mandatory")


class _Sc800t3NetworkTransmitIdleStatus_Type(Integer32):
    """Custom type sc800t3NetworkTransmitIdleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_Sc800t3NetworkTransmitIdleStatus_Type.__name__ = "Integer32"
_Sc800t3NetworkTransmitIdleStatus_Object = MibTableColumn
sc800t3NetworkTransmitIdleStatus = _Sc800t3NetworkTransmitIdleStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 2, 2, 1, 7),
    _Sc800t3NetworkTransmitIdleStatus_Type()
)
sc800t3NetworkTransmitIdleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3NetworkTransmitIdleStatus.setStatus("mandatory")


class _Sc800t3NetworkSesBERThreshold_Type(Integer32):
    """Custom type sc800t3NetworkSesBERThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("thresone", 1),
          ("thresseven", 2))
    )


_Sc800t3NetworkSesBERThreshold_Type.__name__ = "Integer32"
_Sc800t3NetworkSesBERThreshold_Object = MibTableColumn
sc800t3NetworkSesBERThreshold = _Sc800t3NetworkSesBERThreshold_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 2, 2, 1, 8),
    _Sc800t3NetworkSesBERThreshold_Type()
)
sc800t3NetworkSesBERThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3NetworkSesBERThreshold.setStatus("mandatory")


class _Sc800t3InbandLoopback_Type(Integer32):
    """Custom type sc800t3InbandLoopback based on Integer32"""
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


_Sc800t3InbandLoopback_Type.__name__ = "Integer32"
_Sc800t3InbandLoopback_Object = MibTableColumn
sc800t3InbandLoopback = _Sc800t3InbandLoopback_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 2, 2, 1, 9),
    _Sc800t3InbandLoopback_Type()
)
sc800t3InbandLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3InbandLoopback.setStatus("mandatory")
_Sc800t3Diagnostics_ObjectIdentity = ObjectIdentity
sc800t3Diagnostics = _Sc800t3Diagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 3)
)
_Sc800t3DiagTable_Object = MibTable
sc800t3DiagTable = _Sc800t3DiagTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sc800t3DiagTable.setStatus("mandatory")
_Sc800t3DiagEntry_Object = MibTableRow
sc800t3DiagEntry = _Sc800t3DiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 3, 1, 1)
)
sc800t3DiagEntry.setIndexNames(
    (0, "GDC-SC800T3-MIB", "sc800t3DiagIndex"),
)
if mibBuilder.loadTexts:
    sc800t3DiagEntry.setStatus("mandatory")
_Sc800t3DiagIndex_Type = SCinstance
_Sc800t3DiagIndex_Object = MibTableColumn
sc800t3DiagIndex = _Sc800t3DiagIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 3, 1, 1, 1),
    _Sc800t3DiagIndex_Type()
)
sc800t3DiagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3DiagIndex.setStatus("mandatory")


class _Sc800t3DiagTestDuration_Type(Integer32):
    """Custom type sc800t3DiagTestDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("testTime10Mins", 11),
          ("testTime15Mins", 12),
          ("testTime1Min", 2),
          ("testTime20Mins", 13),
          ("testTime25Mins", 14),
          ("testTime2Mins", 3),
          ("testTime30Mins", 15),
          ("testTime30Secs", 1),
          ("testTime3Mins", 4),
          ("testTime4Mins", 5),
          ("testTime5Mins", 6),
          ("testTime6Mins", 7),
          ("testTime7Mins", 8),
          ("testTime8Mins", 9),
          ("testTime9Mins", 10),
          ("testTimeInfinite", 16))
    )


_Sc800t3DiagTestDuration_Type.__name__ = "Integer32"
_Sc800t3DiagTestDuration_Object = MibTableColumn
sc800t3DiagTestDuration = _Sc800t3DiagTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 3, 1, 1, 2),
    _Sc800t3DiagTestDuration_Type()
)
sc800t3DiagTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3DiagTestDuration.setStatus("mandatory")


class _Sc800t3InsertBitError_Type(Integer32):
    """Custom type sc800t3InsertBitError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("insertBitErrorNorm", 1),
          ("insertOneBitError", 2))
    )


_Sc800t3InsertBitError_Type.__name__ = "Integer32"
_Sc800t3InsertBitError_Object = MibTableColumn
sc800t3InsertBitError = _Sc800t3InsertBitError_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 3, 1, 1, 3),
    _Sc800t3InsertBitError_Type()
)
sc800t3InsertBitError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3InsertBitError.setStatus("mandatory")


class _Sc800t3DiagT3Test_Type(Integer32):
    """Custom type sc800t3DiagT3Test based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("t3DTELoopback", 6),
          ("t3EndToEndST", 11),
          ("t3LineLoopback", 2),
          ("t3LocalLoopback", 4),
          ("t3LocalLoopbackST", 5),
          ("t3NoTest", 1),
          ("t3PayLoadLoopback", 3),
          ("t3RemoteLineLoopback", 7),
          ("t3RemoteLineLoopbackST", 8),
          ("t3RemotePayload", 9),
          ("t3RemotePayloadST", 10))
    )


_Sc800t3DiagT3Test_Type.__name__ = "Integer32"
_Sc800t3DiagT3Test_Object = MibTableColumn
sc800t3DiagT3Test = _Sc800t3DiagT3Test_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 3, 1, 1, 4),
    _Sc800t3DiagT3Test_Type()
)
sc800t3DiagT3Test.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3DiagT3Test.setStatus("mandatory")


class _Sc800t3DiagTestResults_Type(OctetString):
    """Custom type sc800t3DiagTestResults based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Sc800t3DiagTestResults_Type.__name__ = "OctetString"
_Sc800t3DiagTestResults_Object = MibTableColumn
sc800t3DiagTestResults = _Sc800t3DiagTestResults_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 3, 1, 1, 5),
    _Sc800t3DiagTestResults_Type()
)
sc800t3DiagTestResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3DiagTestResults.setStatus("mandatory")


class _Sc800t3DiagResetTestResults_Type(Integer32):
    """Custom type sc800t3DiagResetTestResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("resetTestResult", 2))
    )


_Sc800t3DiagResetTestResults_Type.__name__ = "Integer32"
_Sc800t3DiagResetTestResults_Object = MibTableColumn
sc800t3DiagResetTestResults = _Sc800t3DiagResetTestResults_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 3, 1, 1, 6),
    _Sc800t3DiagResetTestResults_Type()
)
sc800t3DiagResetTestResults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3DiagResetTestResults.setStatus("mandatory")
_Sc800t3Maintenance_ObjectIdentity = ObjectIdentity
sc800t3Maintenance = _Sc800t3Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 4)
)
_Sc800t3MaintenanceTable_Object = MibTable
sc800t3MaintenanceTable = _Sc800t3MaintenanceTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 4, 1)
)
if mibBuilder.loadTexts:
    sc800t3MaintenanceTable.setStatus("mandatory")
_Sc800t3MaintenanceEntry_Object = MibTableRow
sc800t3MaintenanceEntry = _Sc800t3MaintenanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 4, 1, 1)
)
sc800t3MaintenanceEntry.setIndexNames(
    (0, "GDC-SC800T3-MIB", "sc800t3MaintenanceIndex"),
)
if mibBuilder.loadTexts:
    sc800t3MaintenanceEntry.setStatus("mandatory")
_Sc800t3MaintenanceIndex_Type = SCinstance
_Sc800t3MaintenanceIndex_Object = MibTableColumn
sc800t3MaintenanceIndex = _Sc800t3MaintenanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 4, 1, 1, 1),
    _Sc800t3MaintenanceIndex_Type()
)
sc800t3MaintenanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3MaintenanceIndex.setStatus("mandatory")


class _Sc800t3LedStatus_Type(OctetString):
    """Custom type sc800t3LedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Sc800t3LedStatus_Type.__name__ = "OctetString"
_Sc800t3LedStatus_Object = MibTableColumn
sc800t3LedStatus = _Sc800t3LedStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 4, 1, 1, 2),
    _Sc800t3LedStatus_Type()
)
sc800t3LedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3LedStatus.setStatus("mandatory")


class _Sc800t3SoftReset_Type(Integer32):
    """Custom type sc800t3SoftReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norm", 1),
          ("reset", 2))
    )


_Sc800t3SoftReset_Type.__name__ = "Integer32"
_Sc800t3SoftReset_Object = MibTableColumn
sc800t3SoftReset = _Sc800t3SoftReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 4, 1, 1, 3),
    _Sc800t3SoftReset_Type()
)
sc800t3SoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3SoftReset.setStatus("mandatory")


class _Sc800t3DefaultInit_Type(Integer32):
    """Custom type sc800t3DefaultInit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("factoryDefault", 2),
          ("normal", 1))
    )


_Sc800t3DefaultInit_Type.__name__ = "Integer32"
_Sc800t3DefaultInit_Object = MibTableColumn
sc800t3DefaultInit = _Sc800t3DefaultInit_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 4, 1, 1, 4),
    _Sc800t3DefaultInit_Type()
)
sc800t3DefaultInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3DefaultInit.setStatus("mandatory")


class _Sc800t3ValidNearEndIntervals_Type(Integer32):
    """Custom type sc800t3ValidNearEndIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Sc800t3ValidNearEndIntervals_Type.__name__ = "Integer32"
_Sc800t3ValidNearEndIntervals_Object = MibTableColumn
sc800t3ValidNearEndIntervals = _Sc800t3ValidNearEndIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 4, 1, 1, 5),
    _Sc800t3ValidNearEndIntervals_Type()
)
sc800t3ValidNearEndIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3ValidNearEndIntervals.setStatus("mandatory")


class _Sc800t3ValidFarEndIntervals_Type(Integer32):
    """Custom type sc800t3ValidFarEndIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Sc800t3ValidFarEndIntervals_Type.__name__ = "Integer32"
_Sc800t3ValidFarEndIntervals_Object = MibTableColumn
sc800t3ValidFarEndIntervals = _Sc800t3ValidFarEndIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 4, 1, 1, 6),
    _Sc800t3ValidFarEndIntervals_Type()
)
sc800t3ValidFarEndIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3ValidFarEndIntervals.setStatus("mandatory")


class _Sc800t3ShelfType_Type(Integer32):
    """Custom type sc800t3ShelfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("spectracomm", 1),
          ("twinPack", 2))
    )


_Sc800t3ShelfType_Type.__name__ = "Integer32"
_Sc800t3ShelfType_Object = MibTableColumn
sc800t3ShelfType = _Sc800t3ShelfType_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 4, 1, 1, 7),
    _Sc800t3ShelfType_Type()
)
sc800t3ShelfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3ShelfType.setStatus("mandatory")


class _Sc800t3TwinPackPowerSupply_Type(Integer32):
    """Custom type sc800t3TwinPackPowerSupply based on Integer32"""
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
        *(("both", 4),
          ("bottomOnly", 2),
          ("none", 1),
          ("topOnly", 3))
    )


_Sc800t3TwinPackPowerSupply_Type.__name__ = "Integer32"
_Sc800t3TwinPackPowerSupply_Object = MibTableColumn
sc800t3TwinPackPowerSupply = _Sc800t3TwinPackPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 4, 1, 1, 8),
    _Sc800t3TwinPackPowerSupply_Type()
)
sc800t3TwinPackPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3TwinPackPowerSupply.setStatus("mandatory")


class _Sc800t3TestAllLeds_Type(Integer32):
    """Custom type sc800t3TestAllLeds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allLedsOFF", 2),
          ("allLedsON", 1))
    )


_Sc800t3TestAllLeds_Type.__name__ = "Integer32"
_Sc800t3TestAllLeds_Object = MibTableColumn
sc800t3TestAllLeds = _Sc800t3TestAllLeds_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 4, 1, 1, 9),
    _Sc800t3TestAllLeds_Type()
)
sc800t3TestAllLeds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3TestAllLeds.setStatus("mandatory")


class _Sc800t3NearEndResetStats_Type(Integer32):
    """Custom type sc800t3NearEndResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norm", 1),
          ("reset", 2))
    )


_Sc800t3NearEndResetStats_Type.__name__ = "Integer32"
_Sc800t3NearEndResetStats_Object = MibTableColumn
sc800t3NearEndResetStats = _Sc800t3NearEndResetStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 4, 1, 1, 10),
    _Sc800t3NearEndResetStats_Type()
)
sc800t3NearEndResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3NearEndResetStats.setStatus("mandatory")


class _Sc800t3FarEndResetStats_Type(Integer32):
    """Custom type sc800t3FarEndResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norm", 1),
          ("reset", 2))
    )


_Sc800t3FarEndResetStats_Type.__name__ = "Integer32"
_Sc800t3FarEndResetStats_Object = MibTableColumn
sc800t3FarEndResetStats = _Sc800t3FarEndResetStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 4, 1, 1, 11),
    _Sc800t3FarEndResetStats_Type()
)
sc800t3FarEndResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3FarEndResetStats.setStatus("mandatory")


class _Sc800t3NearEndStatLastInitial_Type(Integer32):
    """Custom type sc800t3NearEndStatLastInitial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sc800t3NearEndStatLastInitial_Type.__name__ = "Integer32"
_Sc800t3NearEndStatLastInitial_Object = MibTableColumn
sc800t3NearEndStatLastInitial = _Sc800t3NearEndStatLastInitial_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 4, 1, 1, 12),
    _Sc800t3NearEndStatLastInitial_Type()
)
sc800t3NearEndStatLastInitial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3NearEndStatLastInitial.setStatus("mandatory")


class _Sc800t3FarEndStatLastInitial_Type(Integer32):
    """Custom type sc800t3FarEndStatLastInitial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sc800t3FarEndStatLastInitial_Type.__name__ = "Integer32"
_Sc800t3FarEndStatLastInitial_Object = MibTableColumn
sc800t3FarEndStatLastInitial = _Sc800t3FarEndStatLastInitial_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 4, 1, 1, 13),
    _Sc800t3FarEndStatLastInitial_Type()
)
sc800t3FarEndStatLastInitial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3FarEndStatLastInitial.setStatus("mandatory")
_Sc800t3Alarms_ObjectIdentity = ObjectIdentity
sc800t3Alarms = _Sc800t3Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5)
)
_Sc800t3NoResponse_ObjectIdentity = ObjectIdentity
sc800t3NoResponse = _Sc800t3NoResponse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5, 1)
)
_Sc800t3DiagRxErrAlm_ObjectIdentity = ObjectIdentity
sc800t3DiagRxErrAlm = _Sc800t3DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5, 2)
)
_Sc800t3PowerUpAlm_ObjectIdentity = ObjectIdentity
sc800t3PowerUpAlm = _Sc800t3PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5, 3)
)
_Sc800t3POSTFail_ObjectIdentity = ObjectIdentity
sc800t3POSTFail = _Sc800t3POSTFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5, 4)
)
_Sc800t3UnsolicitedTest_ObjectIdentity = ObjectIdentity
sc800t3UnsolicitedTest = _Sc800t3UnsolicitedTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5, 5)
)
_Sc800t3ConfigChange_ObjectIdentity = ObjectIdentity
sc800t3ConfigChange = _Sc800t3ConfigChange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5, 6)
)
_Sc800t3TimingLoss_ObjectIdentity = ObjectIdentity
sc800t3TimingLoss = _Sc800t3TimingLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5, 7)
)
_Sc800t3LossOfSignal_ObjectIdentity = ObjectIdentity
sc800t3LossOfSignal = _Sc800t3LossOfSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5, 8)
)
_Sc800t3OutOfFrame_ObjectIdentity = ObjectIdentity
sc800t3OutOfFrame = _Sc800t3OutOfFrame_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5, 9)
)
_Sc800t3AIS_ObjectIdentity = ObjectIdentity
sc800t3AIS = _Sc800t3AIS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5, 10)
)
_Sc800t3DTEReadyLoss_ObjectIdentity = ObjectIdentity
sc800t3DTEReadyLoss = _Sc800t3DTEReadyLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5, 11)
)
_Sc800t3DTETXCLKLoss_ObjectIdentity = ObjectIdentity
sc800t3DTETXCLKLoss = _Sc800t3DTETXCLKLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5, 12)
)
_Sc800t3RXDNoTrans_ObjectIdentity = ObjectIdentity
sc800t3RXDNoTrans = _Sc800t3RXDNoTrans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5, 13)
)
_Sc800t3TXDNoTrans_ObjectIdentity = ObjectIdentity
sc800t3TXDNoTrans = _Sc800t3TXDNoTrans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5, 14)
)
_Sc800t3RemoteNotResponding_ObjectIdentity = ObjectIdentity
sc800t3RemoteNotResponding = _Sc800t3RemoteNotResponding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5, 15)
)
_Sc800t3TopPowerSupplyFail_ObjectIdentity = ObjectIdentity
sc800t3TopPowerSupplyFail = _Sc800t3TopPowerSupplyFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5, 16)
)
_Sc800t3BottomPowerSupplyFail_ObjectIdentity = ObjectIdentity
sc800t3BottomPowerSupplyFail = _Sc800t3BottomPowerSupplyFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5, 17)
)
_Sc800t3DTETest_ObjectIdentity = ObjectIdentity
sc800t3DTETest = _Sc800t3DTETest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5, 18)
)
_Sc800t3RAI_ObjectIdentity = ObjectIdentity
sc800t3RAI = _Sc800t3RAI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5, 19)
)
_Sc800t3ES_ObjectIdentity = ObjectIdentity
sc800t3ES = _Sc800t3ES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5, 20)
)
_Sc800t3SES_ObjectIdentity = ObjectIdentity
sc800t3SES = _Sc800t3SES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5, 21)
)
_Sc800t3SAS_ObjectIdentity = ObjectIdentity
sc800t3SAS = _Sc800t3SAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5, 22)
)
_Sc800t3UAS_ObjectIdentity = ObjectIdentity
sc800t3UAS = _Sc800t3UAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5, 23)
)
_Sc800t3CodeViolations_ObjectIdentity = ObjectIdentity
sc800t3CodeViolations = _Sc800t3CodeViolations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5, 24)
)
_Sc800t3ESline_ObjectIdentity = ObjectIdentity
sc800t3ESline = _Sc800t3ESline_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 5, 25)
)
_Sc800t3Performance_ObjectIdentity = ObjectIdentity
sc800t3Performance = _Sc800t3Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6)
)
_Sc800t3CurrentNearEndTable_Object = MibTable
sc800t3CurrentNearEndTable = _Sc800t3CurrentNearEndTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 1)
)
if mibBuilder.loadTexts:
    sc800t3CurrentNearEndTable.setStatus("mandatory")
_Sc800t3CurrentNearEndEntry_Object = MibTableRow
sc800t3CurrentNearEndEntry = _Sc800t3CurrentNearEndEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 1, 1)
)
sc800t3CurrentNearEndEntry.setIndexNames(
    (0, "GDC-SC800T3-MIB", "sc800t3CurrentNearEndIndex"),
)
if mibBuilder.loadTexts:
    sc800t3CurrentNearEndEntry.setStatus("mandatory")
_Sc800t3CurrentNearEndIndex_Type = SCinstance
_Sc800t3CurrentNearEndIndex_Object = MibTableColumn
sc800t3CurrentNearEndIndex = _Sc800t3CurrentNearEndIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 1, 1, 1),
    _Sc800t3CurrentNearEndIndex_Type()
)
sc800t3CurrentNearEndIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3CurrentNearEndIndex.setStatus("mandatory")


class _Sc800t3CurrentNearEndStat_Type(OctetString):
    """Custom type sc800t3CurrentNearEndStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_Sc800t3CurrentNearEndStat_Type.__name__ = "OctetString"
_Sc800t3CurrentNearEndStat_Object = MibTableColumn
sc800t3CurrentNearEndStat = _Sc800t3CurrentNearEndStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 1, 1, 2),
    _Sc800t3CurrentNearEndStat_Type()
)
sc800t3CurrentNearEndStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3CurrentNearEndStat.setStatus("mandatory")
_Sc800t3PreviousDayNearEndTable_Object = MibTable
sc800t3PreviousDayNearEndTable = _Sc800t3PreviousDayNearEndTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 2)
)
if mibBuilder.loadTexts:
    sc800t3PreviousDayNearEndTable.setStatus("mandatory")
_Sc800t3PreviousDayNearEndEntry_Object = MibTableRow
sc800t3PreviousDayNearEndEntry = _Sc800t3PreviousDayNearEndEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 2, 1)
)
sc800t3PreviousDayNearEndEntry.setIndexNames(
    (0, "GDC-SC800T3-MIB", "sc800t3PreviousDayNearEndIndex"),
)
if mibBuilder.loadTexts:
    sc800t3PreviousDayNearEndEntry.setStatus("mandatory")
_Sc800t3PreviousDayNearEndIndex_Type = SCinstance
_Sc800t3PreviousDayNearEndIndex_Object = MibTableColumn
sc800t3PreviousDayNearEndIndex = _Sc800t3PreviousDayNearEndIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 2, 1, 1),
    _Sc800t3PreviousDayNearEndIndex_Type()
)
sc800t3PreviousDayNearEndIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3PreviousDayNearEndIndex.setStatus("mandatory")


class _Sc800t3PreviousDayNearEndStat_Type(OctetString):
    """Custom type sc800t3PreviousDayNearEndStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_Sc800t3PreviousDayNearEndStat_Type.__name__ = "OctetString"
_Sc800t3PreviousDayNearEndStat_Object = MibTableColumn
sc800t3PreviousDayNearEndStat = _Sc800t3PreviousDayNearEndStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 2, 1, 2),
    _Sc800t3PreviousDayNearEndStat_Type()
)
sc800t3PreviousDayNearEndStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3PreviousDayNearEndStat.setStatus("mandatory")
_Sc800t3CurrentFarEndTable_Object = MibTable
sc800t3CurrentFarEndTable = _Sc800t3CurrentFarEndTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 3)
)
if mibBuilder.loadTexts:
    sc800t3CurrentFarEndTable.setStatus("mandatory")
_Sc800t3CurrentFarEndEntry_Object = MibTableRow
sc800t3CurrentFarEndEntry = _Sc800t3CurrentFarEndEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 3, 1)
)
sc800t3CurrentFarEndEntry.setIndexNames(
    (0, "GDC-SC800T3-MIB", "sc800t3CurrentFarEndIndex"),
)
if mibBuilder.loadTexts:
    sc800t3CurrentFarEndEntry.setStatus("mandatory")
_Sc800t3CurrentFarEndIndex_Type = SCinstance
_Sc800t3CurrentFarEndIndex_Object = MibTableColumn
sc800t3CurrentFarEndIndex = _Sc800t3CurrentFarEndIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 3, 1, 1),
    _Sc800t3CurrentFarEndIndex_Type()
)
sc800t3CurrentFarEndIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3CurrentFarEndIndex.setStatus("mandatory")


class _Sc800t3CurrentFarEndStat_Type(OctetString):
    """Custom type sc800t3CurrentFarEndStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_Sc800t3CurrentFarEndStat_Type.__name__ = "OctetString"
_Sc800t3CurrentFarEndStat_Object = MibTableColumn
sc800t3CurrentFarEndStat = _Sc800t3CurrentFarEndStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 3, 1, 2),
    _Sc800t3CurrentFarEndStat_Type()
)
sc800t3CurrentFarEndStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3CurrentFarEndStat.setStatus("mandatory")
_Sc800t3CurrentDayNearEndTable_Object = MibTable
sc800t3CurrentDayNearEndTable = _Sc800t3CurrentDayNearEndTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 4)
)
if mibBuilder.loadTexts:
    sc800t3CurrentDayNearEndTable.setStatus("mandatory")
_Sc800t3CurrentDayNearEndEntry_Object = MibTableRow
sc800t3CurrentDayNearEndEntry = _Sc800t3CurrentDayNearEndEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 4, 1)
)
sc800t3CurrentDayNearEndEntry.setIndexNames(
    (0, "GDC-SC800T3-MIB", "sc800t3CurrentDayNearEndIndex"),
)
if mibBuilder.loadTexts:
    sc800t3CurrentDayNearEndEntry.setStatus("mandatory")
_Sc800t3CurrentDayNearEndIndex_Type = SCinstance
_Sc800t3CurrentDayNearEndIndex_Object = MibTableColumn
sc800t3CurrentDayNearEndIndex = _Sc800t3CurrentDayNearEndIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 4, 1, 1),
    _Sc800t3CurrentDayNearEndIndex_Type()
)
sc800t3CurrentDayNearEndIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3CurrentDayNearEndIndex.setStatus("mandatory")


class _Sc800t3CurrentDayNearEndStat_Type(OctetString):
    """Custom type sc800t3CurrentDayNearEndStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_Sc800t3CurrentDayNearEndStat_Type.__name__ = "OctetString"
_Sc800t3CurrentDayNearEndStat_Object = MibTableColumn
sc800t3CurrentDayNearEndStat = _Sc800t3CurrentDayNearEndStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 4, 1, 2),
    _Sc800t3CurrentDayNearEndStat_Type()
)
sc800t3CurrentDayNearEndStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3CurrentDayNearEndStat.setStatus("mandatory")
_Sc800t3PreviousDayFarEndTable_Object = MibTable
sc800t3PreviousDayFarEndTable = _Sc800t3PreviousDayFarEndTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 5)
)
if mibBuilder.loadTexts:
    sc800t3PreviousDayFarEndTable.setStatus("mandatory")
_Sc800t3PreviousDayFarEndEntry_Object = MibTableRow
sc800t3PreviousDayFarEndEntry = _Sc800t3PreviousDayFarEndEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 5, 1)
)
sc800t3PreviousDayFarEndEntry.setIndexNames(
    (0, "GDC-SC800T3-MIB", "sc800t3PreviousDayFarEndIndex"),
)
if mibBuilder.loadTexts:
    sc800t3PreviousDayFarEndEntry.setStatus("mandatory")
_Sc800t3PreviousDayFarEndIndex_Type = SCinstance
_Sc800t3PreviousDayFarEndIndex_Object = MibTableColumn
sc800t3PreviousDayFarEndIndex = _Sc800t3PreviousDayFarEndIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 5, 1, 1),
    _Sc800t3PreviousDayFarEndIndex_Type()
)
sc800t3PreviousDayFarEndIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3PreviousDayFarEndIndex.setStatus("mandatory")


class _Sc800t3PreviousDayFarEndStat_Type(OctetString):
    """Custom type sc800t3PreviousDayFarEndStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_Sc800t3PreviousDayFarEndStat_Type.__name__ = "OctetString"
_Sc800t3PreviousDayFarEndStat_Object = MibTableColumn
sc800t3PreviousDayFarEndStat = _Sc800t3PreviousDayFarEndStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 5, 1, 2),
    _Sc800t3PreviousDayFarEndStat_Type()
)
sc800t3PreviousDayFarEndStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3PreviousDayFarEndStat.setStatus("mandatory")
_Sc800t3CurrentDayFarEndTable_Object = MibTable
sc800t3CurrentDayFarEndTable = _Sc800t3CurrentDayFarEndTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 6)
)
if mibBuilder.loadTexts:
    sc800t3CurrentDayFarEndTable.setStatus("mandatory")
_Sc800t3CurrentDayFarEndEntry_Object = MibTableRow
sc800t3CurrentDayFarEndEntry = _Sc800t3CurrentDayFarEndEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 6, 1)
)
sc800t3CurrentDayFarEndEntry.setIndexNames(
    (0, "GDC-SC800T3-MIB", "sc800t3CurrentDayFarEndIndex"),
)
if mibBuilder.loadTexts:
    sc800t3CurrentDayFarEndEntry.setStatus("mandatory")
_Sc800t3CurrentDayFarEndIndex_Type = SCinstance
_Sc800t3CurrentDayFarEndIndex_Object = MibTableColumn
sc800t3CurrentDayFarEndIndex = _Sc800t3CurrentDayFarEndIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 6, 1, 1),
    _Sc800t3CurrentDayFarEndIndex_Type()
)
sc800t3CurrentDayFarEndIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3CurrentDayFarEndIndex.setStatus("mandatory")


class _Sc800t3CurrentDayFarEndStat_Type(OctetString):
    """Custom type sc800t3CurrentDayFarEndStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_Sc800t3CurrentDayFarEndStat_Type.__name__ = "OctetString"
_Sc800t3CurrentDayFarEndStat_Object = MibTableColumn
sc800t3CurrentDayFarEndStat = _Sc800t3CurrentDayFarEndStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 6, 1, 2),
    _Sc800t3CurrentDayFarEndStat_Type()
)
sc800t3CurrentDayFarEndStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3CurrentDayFarEndStat.setStatus("mandatory")
_Sc800t3NearEndIntervalTable_Object = MibTable
sc800t3NearEndIntervalTable = _Sc800t3NearEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 7)
)
if mibBuilder.loadTexts:
    sc800t3NearEndIntervalTable.setStatus("mandatory")
_Sc800t3NearEndIntervalEntry_Object = MibTableRow
sc800t3NearEndIntervalEntry = _Sc800t3NearEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 7, 1)
)
sc800t3NearEndIntervalEntry.setIndexNames(
    (0, "GDC-SC800T3-MIB", "sc800t3NearEndIntervalIndex"),
    (0, "GDC-SC800T3-MIB", "sc800t3NearEndIntervalNumber"),
)
if mibBuilder.loadTexts:
    sc800t3NearEndIntervalEntry.setStatus("mandatory")
_Sc800t3NearEndIntervalIndex_Type = SCinstance
_Sc800t3NearEndIntervalIndex_Object = MibTableColumn
sc800t3NearEndIntervalIndex = _Sc800t3NearEndIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 7, 1, 1),
    _Sc800t3NearEndIntervalIndex_Type()
)
sc800t3NearEndIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3NearEndIntervalIndex.setStatus("mandatory")


class _Sc800t3NearEndIntervalNumber_Type(Integer32):
    """Custom type sc800t3NearEndIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_Sc800t3NearEndIntervalNumber_Type.__name__ = "Integer32"
_Sc800t3NearEndIntervalNumber_Object = MibTableColumn
sc800t3NearEndIntervalNumber = _Sc800t3NearEndIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 7, 1, 2),
    _Sc800t3NearEndIntervalNumber_Type()
)
sc800t3NearEndIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3NearEndIntervalNumber.setStatus("mandatory")


class _Sc800t3NearEndIntervalStats_Type(OctetString):
    """Custom type sc800t3NearEndIntervalStats based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_Sc800t3NearEndIntervalStats_Type.__name__ = "OctetString"
_Sc800t3NearEndIntervalStats_Object = MibTableColumn
sc800t3NearEndIntervalStats = _Sc800t3NearEndIntervalStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 7, 1, 3),
    _Sc800t3NearEndIntervalStats_Type()
)
sc800t3NearEndIntervalStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3NearEndIntervalStats.setStatus("mandatory")
_Sc800t3FarEndIntervalTable_Object = MibTable
sc800t3FarEndIntervalTable = _Sc800t3FarEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 9)
)
if mibBuilder.loadTexts:
    sc800t3FarEndIntervalTable.setStatus("mandatory")
_Sc800t3FarEndIntervalEntry_Object = MibTableRow
sc800t3FarEndIntervalEntry = _Sc800t3FarEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 9, 1)
)
sc800t3FarEndIntervalEntry.setIndexNames(
    (0, "GDC-SC800T3-MIB", "sc800t3FarEndIntervalIndex"),
    (0, "GDC-SC800T3-MIB", "sc800t3FarEndIntervalNumber"),
)
if mibBuilder.loadTexts:
    sc800t3FarEndIntervalEntry.setStatus("mandatory")
_Sc800t3FarEndIntervalIndex_Type = SCinstance
_Sc800t3FarEndIntervalIndex_Object = MibTableColumn
sc800t3FarEndIntervalIndex = _Sc800t3FarEndIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 9, 1, 1),
    _Sc800t3FarEndIntervalIndex_Type()
)
sc800t3FarEndIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3FarEndIntervalIndex.setStatus("mandatory")


class _Sc800t3FarEndIntervalNumber_Type(Integer32):
    """Custom type sc800t3FarEndIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_Sc800t3FarEndIntervalNumber_Type.__name__ = "Integer32"
_Sc800t3FarEndIntervalNumber_Object = MibTableColumn
sc800t3FarEndIntervalNumber = _Sc800t3FarEndIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 9, 1, 2),
    _Sc800t3FarEndIntervalNumber_Type()
)
sc800t3FarEndIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3FarEndIntervalNumber.setStatus("mandatory")


class _Sc800t3FarEndIntervalStats_Type(OctetString):
    """Custom type sc800t3FarEndIntervalStats based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_Sc800t3FarEndIntervalStats_Type.__name__ = "OctetString"
_Sc800t3FarEndIntervalStats_Object = MibTableColumn
sc800t3FarEndIntervalStats = _Sc800t3FarEndIntervalStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 9, 1, 3),
    _Sc800t3FarEndIntervalStats_Type()
)
sc800t3FarEndIntervalStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3FarEndIntervalStats.setStatus("mandatory")
_Sc800t3PreviousNearEndTable_Object = MibTable
sc800t3PreviousNearEndTable = _Sc800t3PreviousNearEndTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 10)
)
if mibBuilder.loadTexts:
    sc800t3PreviousNearEndTable.setStatus("mandatory")
_Sc800t3PreviousNearEndEntry_Object = MibTableRow
sc800t3PreviousNearEndEntry = _Sc800t3PreviousNearEndEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 10, 1)
)
sc800t3PreviousNearEndEntry.setIndexNames(
    (0, "GDC-SC800T3-MIB", "sc800t3PreviousNearEndIndex"),
)
if mibBuilder.loadTexts:
    sc800t3PreviousNearEndEntry.setStatus("mandatory")
_Sc800t3PreviousNearEndIndex_Type = SCinstance
_Sc800t3PreviousNearEndIndex_Object = MibTableColumn
sc800t3PreviousNearEndIndex = _Sc800t3PreviousNearEndIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 10, 1, 1),
    _Sc800t3PreviousNearEndIndex_Type()
)
sc800t3PreviousNearEndIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3PreviousNearEndIndex.setStatus("mandatory")


class _Sc800t3PreviousNearEndStat_Type(OctetString):
    """Custom type sc800t3PreviousNearEndStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_Sc800t3PreviousNearEndStat_Type.__name__ = "OctetString"
_Sc800t3PreviousNearEndStat_Object = MibTableColumn
sc800t3PreviousNearEndStat = _Sc800t3PreviousNearEndStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 10, 1, 2),
    _Sc800t3PreviousNearEndStat_Type()
)
sc800t3PreviousNearEndStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3PreviousNearEndStat.setStatus("mandatory")
_Sc800t3PreviousFarEndTable_Object = MibTable
sc800t3PreviousFarEndTable = _Sc800t3PreviousFarEndTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 11)
)
if mibBuilder.loadTexts:
    sc800t3PreviousFarEndTable.setStatus("mandatory")
_Sc800t3PreviousFarEndEntry_Object = MibTableRow
sc800t3PreviousFarEndEntry = _Sc800t3PreviousFarEndEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 11, 1)
)
sc800t3PreviousFarEndEntry.setIndexNames(
    (0, "GDC-SC800T3-MIB", "sc800t3PreviousFarEndIndex"),
)
if mibBuilder.loadTexts:
    sc800t3PreviousFarEndEntry.setStatus("mandatory")
_Sc800t3PreviousFarEndIndex_Type = SCinstance
_Sc800t3PreviousFarEndIndex_Object = MibTableColumn
sc800t3PreviousFarEndIndex = _Sc800t3PreviousFarEndIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 11, 1, 1),
    _Sc800t3PreviousFarEndIndex_Type()
)
sc800t3PreviousFarEndIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3PreviousFarEndIndex.setStatus("mandatory")


class _Sc800t3PreviousFarEndStat_Type(OctetString):
    """Custom type sc800t3PreviousFarEndStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Sc800t3PreviousFarEndStat_Type.__name__ = "OctetString"
_Sc800t3PreviousFarEndStat_Object = MibTableColumn
sc800t3PreviousFarEndStat = _Sc800t3PreviousFarEndStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 6, 11, 1, 2),
    _Sc800t3PreviousFarEndStat_Type()
)
sc800t3PreviousFarEndStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3PreviousFarEndStat.setStatus("mandatory")
_Sc800t3AlarmConfig_ObjectIdentity = ObjectIdentity
sc800t3AlarmConfig = _Sc800t3AlarmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 7)
)
_Sc800t3AlarmConfigTable_Object = MibTable
sc800t3AlarmConfigTable = _Sc800t3AlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 7, 1)
)
if mibBuilder.loadTexts:
    sc800t3AlarmConfigTable.setStatus("mandatory")
_Sc800t3AlarmConfigEntry_Object = MibTableRow
sc800t3AlarmConfigEntry = _Sc800t3AlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 7, 1, 1)
)
sc800t3AlarmConfigEntry.setIndexNames(
    (0, "GDC-SC800T3-MIB", "sc800t3AlarmConfigIndex"),
    (0, "GDC-SC800T3-MIB", "sc800t3AlarmConfigIdentifier"),
)
if mibBuilder.loadTexts:
    sc800t3AlarmConfigEntry.setStatus("mandatory")
_Sc800t3AlarmConfigIndex_Type = SCinstance
_Sc800t3AlarmConfigIndex_Object = MibTableColumn
sc800t3AlarmConfigIndex = _Sc800t3AlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 7, 1, 1, 1),
    _Sc800t3AlarmConfigIndex_Type()
)
sc800t3AlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3AlarmConfigIndex.setStatus("mandatory")
_Sc800t3AlarmConfigIdentifier_Type = ObjectIdentifier
_Sc800t3AlarmConfigIdentifier_Object = MibTableColumn
sc800t3AlarmConfigIdentifier = _Sc800t3AlarmConfigIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 7, 1, 1, 2),
    _Sc800t3AlarmConfigIdentifier_Type()
)
sc800t3AlarmConfigIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3AlarmConfigIdentifier.setStatus("mandatory")


class _Sc800t3AlarmCountWindow_Type(Integer32):
    """Custom type sc800t3AlarmCountWindow based on Integer32"""
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
        *(("last1hr", 4),
          ("last1min", 3),
          ("last1sec", 2),
          ("reportAll", 1),
          ("reportWhen", 5))
    )


_Sc800t3AlarmCountWindow_Type.__name__ = "Integer32"
_Sc800t3AlarmCountWindow_Object = MibTableColumn
sc800t3AlarmCountWindow = _Sc800t3AlarmCountWindow_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 7, 1, 1, 3),
    _Sc800t3AlarmCountWindow_Type()
)
sc800t3AlarmCountWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3AlarmCountWindow.setStatus("mandatory")


class _Sc800t3AlarmCountThreshold_Type(Integer32):
    """Custom type sc800t3AlarmCountThreshold based on Integer32"""
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
        *(("thresGT10", 1),
          ("thresGT100", 2),
          ("thresGT1000", 3),
          ("thresGT10000", 4),
          ("thresGT100000", 5),
          ("thresGT1000000", 6))
    )


_Sc800t3AlarmCountThreshold_Type.__name__ = "Integer32"
_Sc800t3AlarmCountThreshold_Object = MibTableColumn
sc800t3AlarmCountThreshold = _Sc800t3AlarmCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 7, 1, 1, 4),
    _Sc800t3AlarmCountThreshold_Type()
)
sc800t3AlarmCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3AlarmCountThreshold.setStatus("mandatory")
_Sc800t3LocalAlarms_ObjectIdentity = ObjectIdentity
sc800t3LocalAlarms = _Sc800t3LocalAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 8)
)
_Sc800t3LocalAlarmConfigTable_Object = MibTable
sc800t3LocalAlarmConfigTable = _Sc800t3LocalAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 8, 1)
)
if mibBuilder.loadTexts:
    sc800t3LocalAlarmConfigTable.setStatus("mandatory")
_Sc800t3LocalAlarmConfigEntry_Object = MibTableRow
sc800t3LocalAlarmConfigEntry = _Sc800t3LocalAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 8, 1, 1)
)
sc800t3LocalAlarmConfigEntry.setIndexNames(
    (0, "GDC-SC800T3-MIB", "sc800t3LocalAlarmConfigIndex"),
)
if mibBuilder.loadTexts:
    sc800t3LocalAlarmConfigEntry.setStatus("mandatory")
_Sc800t3LocalAlarmConfigIndex_Type = SCinstance
_Sc800t3LocalAlarmConfigIndex_Object = MibTableColumn
sc800t3LocalAlarmConfigIndex = _Sc800t3LocalAlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 8, 1, 1, 1),
    _Sc800t3LocalAlarmConfigIndex_Type()
)
sc800t3LocalAlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc800t3LocalAlarmConfigIndex.setStatus("mandatory")


class _Sc800t3OOF_Type(Integer32):
    """Custom type sc800t3OOF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Sc800t3OOF_Type.__name__ = "Integer32"
_Sc800t3OOF_Object = MibTableColumn
sc800t3OOF = _Sc800t3OOF_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 8, 1, 1, 2),
    _Sc800t3OOF_Type()
)
sc800t3OOF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3OOF.setStatus("mandatory")


class _Sc800t3AISLOCAL_Type(Integer32):
    """Custom type sc800t3AISLOCAL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Sc800t3AISLOCAL_Type.__name__ = "Integer32"
_Sc800t3AISLOCAL_Object = MibTableColumn
sc800t3AISLOCAL = _Sc800t3AISLOCAL_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 8, 1, 1, 3),
    _Sc800t3AISLOCAL_Type()
)
sc800t3AISLOCAL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3AISLOCAL.setStatus("mandatory")


class _Sc800t3TIMLOS_Type(Integer32):
    """Custom type sc800t3TIMLOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Sc800t3TIMLOS_Type.__name__ = "Integer32"
_Sc800t3TIMLOS_Object = MibTableColumn
sc800t3TIMLOS = _Sc800t3TIMLOS_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 8, 1, 1, 4),
    _Sc800t3TIMLOS_Type()
)
sc800t3TIMLOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3TIMLOS.setStatus("mandatory")


class _Sc800t3TXDLOS_Type(Integer32):
    """Custom type sc800t3TXDLOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Sc800t3TXDLOS_Type.__name__ = "Integer32"
_Sc800t3TXDLOS_Object = MibTableColumn
sc800t3TXDLOS = _Sc800t3TXDLOS_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 8, 1, 1, 5),
    _Sc800t3TXDLOS_Type()
)
sc800t3TXDLOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3TXDLOS.setStatus("mandatory")


class _Sc800t3RXDLOS_Type(Integer32):
    """Custom type sc800t3RXDLOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Sc800t3RXDLOS_Type.__name__ = "Integer32"
_Sc800t3RXDLOS_Object = MibTableColumn
sc800t3RXDLOS = _Sc800t3RXDLOS_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 8, 1, 1, 6),
    _Sc800t3RXDLOS_Type()
)
sc800t3RXDLOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3RXDLOS.setStatus("mandatory")


class _Sc800t3LOS_Type(Integer32):
    """Custom type sc800t3LOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Sc800t3LOS_Type.__name__ = "Integer32"
_Sc800t3LOS_Object = MibTableColumn
sc800t3LOS = _Sc800t3LOS_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 8, 1, 1, 7),
    _Sc800t3LOS_Type()
)
sc800t3LOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3LOS.setStatus("mandatory")


class _Sc800t3TPSFAIL_Type(Integer32):
    """Custom type sc800t3TPSFAIL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Sc800t3TPSFAIL_Type.__name__ = "Integer32"
_Sc800t3TPSFAIL_Object = MibTableColumn
sc800t3TPSFAIL = _Sc800t3TPSFAIL_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 8, 1, 1, 8),
    _Sc800t3TPSFAIL_Type()
)
sc800t3TPSFAIL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3TPSFAIL.setStatus("mandatory")


class _Sc800t3BPSFAIL_Type(Integer32):
    """Custom type sc800t3BPSFAIL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Sc800t3BPSFAIL_Type.__name__ = "Integer32"
_Sc800t3BPSFAIL_Object = MibTableColumn
sc800t3BPSFAIL = _Sc800t3BPSFAIL_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 8, 1, 1, 9),
    _Sc800t3BPSFAIL_Type()
)
sc800t3BPSFAIL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3BPSFAIL.setStatus("mandatory")


class _Sc800t3DTECLKLOS_Type(Integer32):
    """Custom type sc800t3DTECLKLOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Sc800t3DTECLKLOS_Type.__name__ = "Integer32"
_Sc800t3DTECLKLOS_Object = MibTableColumn
sc800t3DTECLKLOS = _Sc800t3DTECLKLOS_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 8, 1, 1, 10),
    _Sc800t3DTECLKLOS_Type()
)
sc800t3DTECLKLOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3DTECLKLOS.setStatus("mandatory")


class _Sc800t3DTERDYLOS_Type(Integer32):
    """Custom type sc800t3DTERDYLOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Sc800t3DTERDYLOS_Type.__name__ = "Integer32"
_Sc800t3DTERDYLOS_Object = MibTableColumn
sc800t3DTERDYLOS = _Sc800t3DTERDYLOS_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 8, 1, 1, 11),
    _Sc800t3DTERDYLOS_Type()
)
sc800t3DTERDYLOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3DTERDYLOS.setStatus("mandatory")


class _Sc800t3RAILOCAL_Type(Integer32):
    """Custom type sc800t3RAILOCAL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Sc800t3RAILOCAL_Type.__name__ = "Integer32"
_Sc800t3RAILOCAL_Object = MibTableColumn
sc800t3RAILOCAL = _Sc800t3RAILOCAL_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 8, 1, 1, 12),
    _Sc800t3RAILOCAL_Type()
)
sc800t3RAILOCAL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3RAILOCAL.setStatus("mandatory")


class _Sc800t3THRESHESL_Type(Integer32):
    """Custom type sc800t3THRESHESL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Sc800t3THRESHESL_Type.__name__ = "Integer32"
_Sc800t3THRESHESL_Object = MibTableColumn
sc800t3THRESHESL = _Sc800t3THRESHESL_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 8, 1, 1, 13),
    _Sc800t3THRESHESL_Type()
)
sc800t3THRESHESL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3THRESHESL.setStatus("mandatory")


class _Sc800t3THRESHES_Type(Integer32):
    """Custom type sc800t3THRESHES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Sc800t3THRESHES_Type.__name__ = "Integer32"
_Sc800t3THRESHES_Object = MibTableColumn
sc800t3THRESHES = _Sc800t3THRESHES_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 8, 1, 1, 14),
    _Sc800t3THRESHES_Type()
)
sc800t3THRESHES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3THRESHES.setStatus("mandatory")


class _Sc800t3THRESHSES_Type(Integer32):
    """Custom type sc800t3THRESHSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Sc800t3THRESHSES_Type.__name__ = "Integer32"
_Sc800t3THRESHSES_Object = MibTableColumn
sc800t3THRESHSES = _Sc800t3THRESHSES_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 8, 1, 1, 15),
    _Sc800t3THRESHSES_Type()
)
sc800t3THRESHSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3THRESHSES.setStatus("mandatory")


class _Sc800t3THRESHSAS_Type(Integer32):
    """Custom type sc800t3THRESHSAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Sc800t3THRESHSAS_Type.__name__ = "Integer32"
_Sc800t3THRESHSAS_Object = MibTableColumn
sc800t3THRESHSAS = _Sc800t3THRESHSAS_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 8, 1, 1, 16),
    _Sc800t3THRESHSAS_Type()
)
sc800t3THRESHSAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3THRESHSAS.setStatus("mandatory")


class _Sc800t3THRESHUAS_Type(Integer32):
    """Custom type sc800t3THRESHUAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Sc800t3THRESHUAS_Type.__name__ = "Integer32"
_Sc800t3THRESHUAS_Object = MibTableColumn
sc800t3THRESHUAS = _Sc800t3THRESHUAS_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 8, 1, 1, 17),
    _Sc800t3THRESHUAS_Type()
)
sc800t3THRESHUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3THRESHUAS.setStatus("mandatory")


class _Sc800t3THRESHCV_Type(Integer32):
    """Custom type sc800t3THRESHCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Sc800t3THRESHCV_Type.__name__ = "Integer32"
_Sc800t3THRESHCV_Object = MibTableColumn
sc800t3THRESHCV = _Sc800t3THRESHCV_Object(
    (1, 3, 6, 1, 4, 1, 498, 19, 1, 8, 1, 1, 18),
    _Sc800t3THRESHCV_Type()
)
sc800t3THRESHCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc800t3THRESHCV.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GDC-SC800T3-MIB",
    **{"ds3": ds3,
       "sc800t3": sc800t3,
       "sc800t3Version": sc800t3Version,
       "sc800t3MIBversion": sc800t3MIBversion,
       "sc800t3VersionTable": sc800t3VersionTable,
       "sc800t3VersionEntry": sc800t3VersionEntry,
       "sc800t3VersionIndex": sc800t3VersionIndex,
       "sc800t3ActiveFirmwareRev": sc800t3ActiveFirmwareRev,
       "sc800t3StandbyFirmwareRev": sc800t3StandbyFirmwareRev,
       "sc800t3StoredFirmwareStatus": sc800t3StoredFirmwareStatus,
       "sc800t3SwitchActiveFirmware": sc800t3SwitchActiveFirmware,
       "sc800t3DownloadingMode": sc800t3DownloadingMode,
       "sc800t3EraseFlash": sc800t3EraseFlash,
       "sc800t3Configuration": sc800t3Configuration,
       "sc800t3ChannelConfigTable": sc800t3ChannelConfigTable,
       "sc800t3ChannelConfigEntry": sc800t3ChannelConfigEntry,
       "sc800t3ChannelConfigIndex": sc800t3ChannelConfigIndex,
       "sc800t3ForcedDCE": sc800t3ForcedDCE,
       "sc800t3ChannelDTEtest": sc800t3ChannelDTEtest,
       "sc800t3DTELoopTimeout": sc800t3DTELoopTimeout,
       "sc800t3NetworkConfigTable": sc800t3NetworkConfigTable,
       "sc800t3NetworkConfigEntry": sc800t3NetworkConfigEntry,
       "sc800t3NetworkConfigIndex": sc800t3NetworkConfigIndex,
       "sc800t3NetworkFrameType": sc800t3NetworkFrameType,
       "sc800t3NetworkTransmitClockSource": sc800t3NetworkTransmitClockSource,
       "sc800t3NetworkAISLoopdown": sc800t3NetworkAISLoopdown,
       "sc800t3NetworkLineType": sc800t3NetworkLineType,
       "sc800t3NetworkIdleStatus": sc800t3NetworkIdleStatus,
       "sc800t3NetworkTransmitIdleStatus": sc800t3NetworkTransmitIdleStatus,
       "sc800t3NetworkSesBERThreshold": sc800t3NetworkSesBERThreshold,
       "sc800t3InbandLoopback": sc800t3InbandLoopback,
       "sc800t3Diagnostics": sc800t3Diagnostics,
       "sc800t3DiagTable": sc800t3DiagTable,
       "sc800t3DiagEntry": sc800t3DiagEntry,
       "sc800t3DiagIndex": sc800t3DiagIndex,
       "sc800t3DiagTestDuration": sc800t3DiagTestDuration,
       "sc800t3InsertBitError": sc800t3InsertBitError,
       "sc800t3DiagT3Test": sc800t3DiagT3Test,
       "sc800t3DiagTestResults": sc800t3DiagTestResults,
       "sc800t3DiagResetTestResults": sc800t3DiagResetTestResults,
       "sc800t3Maintenance": sc800t3Maintenance,
       "sc800t3MaintenanceTable": sc800t3MaintenanceTable,
       "sc800t3MaintenanceEntry": sc800t3MaintenanceEntry,
       "sc800t3MaintenanceIndex": sc800t3MaintenanceIndex,
       "sc800t3LedStatus": sc800t3LedStatus,
       "sc800t3SoftReset": sc800t3SoftReset,
       "sc800t3DefaultInit": sc800t3DefaultInit,
       "sc800t3ValidNearEndIntervals": sc800t3ValidNearEndIntervals,
       "sc800t3ValidFarEndIntervals": sc800t3ValidFarEndIntervals,
       "sc800t3ShelfType": sc800t3ShelfType,
       "sc800t3TwinPackPowerSupply": sc800t3TwinPackPowerSupply,
       "sc800t3TestAllLeds": sc800t3TestAllLeds,
       "sc800t3NearEndResetStats": sc800t3NearEndResetStats,
       "sc800t3FarEndResetStats": sc800t3FarEndResetStats,
       "sc800t3NearEndStatLastInitial": sc800t3NearEndStatLastInitial,
       "sc800t3FarEndStatLastInitial": sc800t3FarEndStatLastInitial,
       "sc800t3Alarms": sc800t3Alarms,
       "sc800t3NoResponse": sc800t3NoResponse,
       "sc800t3DiagRxErrAlm": sc800t3DiagRxErrAlm,
       "sc800t3PowerUpAlm": sc800t3PowerUpAlm,
       "sc800t3POSTFail": sc800t3POSTFail,
       "sc800t3UnsolicitedTest": sc800t3UnsolicitedTest,
       "sc800t3ConfigChange": sc800t3ConfigChange,
       "sc800t3TimingLoss": sc800t3TimingLoss,
       "sc800t3LossOfSignal": sc800t3LossOfSignal,
       "sc800t3OutOfFrame": sc800t3OutOfFrame,
       "sc800t3AIS": sc800t3AIS,
       "sc800t3DTEReadyLoss": sc800t3DTEReadyLoss,
       "sc800t3DTETXCLKLoss": sc800t3DTETXCLKLoss,
       "sc800t3RXDNoTrans": sc800t3RXDNoTrans,
       "sc800t3TXDNoTrans": sc800t3TXDNoTrans,
       "sc800t3RemoteNotResponding": sc800t3RemoteNotResponding,
       "sc800t3TopPowerSupplyFail": sc800t3TopPowerSupplyFail,
       "sc800t3BottomPowerSupplyFail": sc800t3BottomPowerSupplyFail,
       "sc800t3DTETest": sc800t3DTETest,
       "sc800t3RAI": sc800t3RAI,
       "sc800t3ES": sc800t3ES,
       "sc800t3SES": sc800t3SES,
       "sc800t3SAS": sc800t3SAS,
       "sc800t3UAS": sc800t3UAS,
       "sc800t3CodeViolations": sc800t3CodeViolations,
       "sc800t3ESline": sc800t3ESline,
       "sc800t3Performance": sc800t3Performance,
       "sc800t3CurrentNearEndTable": sc800t3CurrentNearEndTable,
       "sc800t3CurrentNearEndEntry": sc800t3CurrentNearEndEntry,
       "sc800t3CurrentNearEndIndex": sc800t3CurrentNearEndIndex,
       "sc800t3CurrentNearEndStat": sc800t3CurrentNearEndStat,
       "sc800t3PreviousDayNearEndTable": sc800t3PreviousDayNearEndTable,
       "sc800t3PreviousDayNearEndEntry": sc800t3PreviousDayNearEndEntry,
       "sc800t3PreviousDayNearEndIndex": sc800t3PreviousDayNearEndIndex,
       "sc800t3PreviousDayNearEndStat": sc800t3PreviousDayNearEndStat,
       "sc800t3CurrentFarEndTable": sc800t3CurrentFarEndTable,
       "sc800t3CurrentFarEndEntry": sc800t3CurrentFarEndEntry,
       "sc800t3CurrentFarEndIndex": sc800t3CurrentFarEndIndex,
       "sc800t3CurrentFarEndStat": sc800t3CurrentFarEndStat,
       "sc800t3CurrentDayNearEndTable": sc800t3CurrentDayNearEndTable,
       "sc800t3CurrentDayNearEndEntry": sc800t3CurrentDayNearEndEntry,
       "sc800t3CurrentDayNearEndIndex": sc800t3CurrentDayNearEndIndex,
       "sc800t3CurrentDayNearEndStat": sc800t3CurrentDayNearEndStat,
       "sc800t3PreviousDayFarEndTable": sc800t3PreviousDayFarEndTable,
       "sc800t3PreviousDayFarEndEntry": sc800t3PreviousDayFarEndEntry,
       "sc800t3PreviousDayFarEndIndex": sc800t3PreviousDayFarEndIndex,
       "sc800t3PreviousDayFarEndStat": sc800t3PreviousDayFarEndStat,
       "sc800t3CurrentDayFarEndTable": sc800t3CurrentDayFarEndTable,
       "sc800t3CurrentDayFarEndEntry": sc800t3CurrentDayFarEndEntry,
       "sc800t3CurrentDayFarEndIndex": sc800t3CurrentDayFarEndIndex,
       "sc800t3CurrentDayFarEndStat": sc800t3CurrentDayFarEndStat,
       "sc800t3NearEndIntervalTable": sc800t3NearEndIntervalTable,
       "sc800t3NearEndIntervalEntry": sc800t3NearEndIntervalEntry,
       "sc800t3NearEndIntervalIndex": sc800t3NearEndIntervalIndex,
       "sc800t3NearEndIntervalNumber": sc800t3NearEndIntervalNumber,
       "sc800t3NearEndIntervalStats": sc800t3NearEndIntervalStats,
       "sc800t3FarEndIntervalTable": sc800t3FarEndIntervalTable,
       "sc800t3FarEndIntervalEntry": sc800t3FarEndIntervalEntry,
       "sc800t3FarEndIntervalIndex": sc800t3FarEndIntervalIndex,
       "sc800t3FarEndIntervalNumber": sc800t3FarEndIntervalNumber,
       "sc800t3FarEndIntervalStats": sc800t3FarEndIntervalStats,
       "sc800t3PreviousNearEndTable": sc800t3PreviousNearEndTable,
       "sc800t3PreviousNearEndEntry": sc800t3PreviousNearEndEntry,
       "sc800t3PreviousNearEndIndex": sc800t3PreviousNearEndIndex,
       "sc800t3PreviousNearEndStat": sc800t3PreviousNearEndStat,
       "sc800t3PreviousFarEndTable": sc800t3PreviousFarEndTable,
       "sc800t3PreviousFarEndEntry": sc800t3PreviousFarEndEntry,
       "sc800t3PreviousFarEndIndex": sc800t3PreviousFarEndIndex,
       "sc800t3PreviousFarEndStat": sc800t3PreviousFarEndStat,
       "sc800t3AlarmConfig": sc800t3AlarmConfig,
       "sc800t3AlarmConfigTable": sc800t3AlarmConfigTable,
       "sc800t3AlarmConfigEntry": sc800t3AlarmConfigEntry,
       "sc800t3AlarmConfigIndex": sc800t3AlarmConfigIndex,
       "sc800t3AlarmConfigIdentifier": sc800t3AlarmConfigIdentifier,
       "sc800t3AlarmCountWindow": sc800t3AlarmCountWindow,
       "sc800t3AlarmCountThreshold": sc800t3AlarmCountThreshold,
       "sc800t3LocalAlarms": sc800t3LocalAlarms,
       "sc800t3LocalAlarmConfigTable": sc800t3LocalAlarmConfigTable,
       "sc800t3LocalAlarmConfigEntry": sc800t3LocalAlarmConfigEntry,
       "sc800t3LocalAlarmConfigIndex": sc800t3LocalAlarmConfigIndex,
       "sc800t3OOF": sc800t3OOF,
       "sc800t3AISLOCAL": sc800t3AISLOCAL,
       "sc800t3TIMLOS": sc800t3TIMLOS,
       "sc800t3TXDLOS": sc800t3TXDLOS,
       "sc800t3RXDLOS": sc800t3RXDLOS,
       "sc800t3LOS": sc800t3LOS,
       "sc800t3TPSFAIL": sc800t3TPSFAIL,
       "sc800t3BPSFAIL": sc800t3BPSFAIL,
       "sc800t3DTECLKLOS": sc800t3DTECLKLOS,
       "sc800t3DTERDYLOS": sc800t3DTERDYLOS,
       "sc800t3RAILOCAL": sc800t3RAILOCAL,
       "sc800t3THRESHESL": sc800t3THRESHESL,
       "sc800t3THRESHES": sc800t3THRESHES,
       "sc800t3THRESHSES": sc800t3THRESHSES,
       "sc800t3THRESHSAS": sc800t3THRESHSAS,
       "sc800t3THRESHUAS": sc800t3THRESHUAS,
       "sc800t3THRESHCV": sc800t3THRESHCV}
)
