# SNMP MIB module (PROBE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PROBE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:46 2024
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

(EntryStatus,
 OwnerString) = mibBuilder.importSymbols(
    "RMON-MIB",
    "EntryStatus",
    "OwnerString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class AccessLevel(Integer32):
    """Custom type AccessLevel based on Integer32"""
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
        *(("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4))
    )





class ControlString(DisplayString):
    """Custom type ControlString based on DisplayString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_HpExperimental_ObjectIdentity = ObjectIdentity
hpExperimental = _HpExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 1)
)
_Ntd_ObjectIdentity = ObjectIdentity
ntd = _Ntd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 1, 5)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3)
)
_NetElement_ObjectIdentity = ObjectIdentity
netElement = _NetElement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7)
)
_Lanprobe_ObjectIdentity = ObjectIdentity
lanprobe = _Lanprobe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6)
)
_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1)
)
_ProbeAdmin_ObjectIdentity = ObjectIdentity
probeAdmin = _ProbeAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 1)
)


class _ProbeIdentification_Type(DisplayString):
    """Custom type probeIdentification based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ProbeIdentification_Type.__name__ = "DisplayString"
_ProbeIdentification_Object = MibScalar
probeIdentification = _ProbeIdentification_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 1, 1),
    _ProbeIdentification_Type()
)
probeIdentification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probeIdentification.setStatus("mandatory")


class _ProbeFirmwareRev_Type(DisplayString):
    """Custom type probeFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProbeFirmwareRev_Type.__name__ = "DisplayString"
_ProbeFirmwareRev_Object = MibScalar
probeFirmwareRev = _ProbeFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 1, 2),
    _ProbeFirmwareRev_Type()
)
probeFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeFirmwareRev.setStatus("mandatory")


class _ProbeHardwareRev_Type(DisplayString):
    """Custom type probeHardwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ProbeHardwareRev_Type.__name__ = "DisplayString"
_ProbeHardwareRev_Object = MibScalar
probeHardwareRev = _ProbeHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 1, 3),
    _ProbeHardwareRev_Type()
)
probeHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeHardwareRev.setStatus("mandatory")


class _ProbeDateTime_Type(DisplayString):
    """Custom type probeDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(26, 40),
    )


_ProbeDateTime_Type.__name__ = "DisplayString"
_ProbeDateTime_Object = MibScalar
probeDateTime = _ProbeDateTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 1, 4),
    _ProbeDateTime_Type()
)
probeDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probeDateTime.setStatus("mandatory")


class _ProbeResetControl_Type(Integer32):
    """Custom type probeResetControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coldBoot", 3),
          ("running", 1),
          ("warmBoot", 2))
    )


_ProbeResetControl_Type.__name__ = "Integer32"
_ProbeResetControl_Object = MibScalar
probeResetControl = _ProbeResetControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 1, 5),
    _ProbeResetControl_Type()
)
probeResetControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probeResetControl.setStatus("mandatory")


class _ProbeDownloadFile_Type(DisplayString):
    """Custom type probeDownloadFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ProbeDownloadFile_Type.__name__ = "DisplayString"
_ProbeDownloadFile_Object = MibScalar
probeDownloadFile = _ProbeDownloadFile_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 1, 6),
    _ProbeDownloadFile_Type()
)
probeDownloadFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probeDownloadFile.setStatus("mandatory")
_ProbeDownloadTFTPServer_Type = IpAddress
_ProbeDownloadTFTPServer_Object = MibScalar
probeDownloadTFTPServer = _ProbeDownloadTFTPServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 1, 7),
    _ProbeDownloadTFTPServer_Type()
)
probeDownloadTFTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probeDownloadTFTPServer.setStatus("mandatory")


class _ProbeDownloadAction_Type(Integer32):
    """Custom type probeDownloadAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("downloadToPROM", 2),
          ("downloadToRAM", 3),
          ("imageValid", 1))
    )


_ProbeDownloadAction_Type.__name__ = "Integer32"
_ProbeDownloadAction_Object = MibScalar
probeDownloadAction = _ProbeDownloadAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 1, 8),
    _ProbeDownloadAction_Type()
)
probeDownloadAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probeDownloadAction.setStatus("mandatory")


class _ProbeDownloadStatus_Type(Integer32):
    """Custom type probeDownloadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("downloadFailed", 2),
          ("downloadStatusUnknown", 3),
          ("downloadSuccess", 1))
    )


_ProbeDownloadStatus_Type.__name__ = "Integer32"
_ProbeDownloadStatus_Object = MibScalar
probeDownloadStatus = _ProbeDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 1, 9),
    _ProbeDownloadStatus_Type()
)
probeDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeDownloadStatus.setStatus("mandatory")


class _ProbeEchoInterval_Type(Integer32):
    """Custom type probeEchoInterval based on Integer32"""
    defaultValue = 1800


_ProbeEchoInterval_Object = MibScalar
probeEchoInterval = _ProbeEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 1, 10),
    _ProbeEchoInterval_Type()
)
probeEchoInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probeEchoInterval.setStatus("mandatory")


class _ProbeFeatureDeactivate_Type(Integer32):
    """Custom type probeFeatureDeactivate based on Integer32"""
    defaultValue = 0


_ProbeFeatureDeactivate_Object = MibScalar
probeFeatureDeactivate = _ProbeFeatureDeactivate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 1, 12),
    _ProbeFeatureDeactivate_Type()
)
probeFeatureDeactivate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeFeatureDeactivate.setStatus("mandatory")
_CableTest_ObjectIdentity = ObjectIdentity
cableTest = _CableTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 2)
)
_NodeLocation_ObjectIdentity = ObjectIdentity
nodeLocation = _NodeLocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 3)
)
_ProbeView_ObjectIdentity = ObjectIdentity
probeView = _ProbeView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 4)
)
_RmonExtension_ObjectIdentity = ObjectIdentity
rmonExtension = _RmonExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5)
)
_StatsExtension_ObjectIdentity = ObjectIdentity
statsExtension = _StatsExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1)
)


class _CurrentUtilizationPeriod_Type(Integer32):
    """Custom type currentUtilizationPeriod based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_CurrentUtilizationPeriod_Type.__name__ = "Integer32"
_CurrentUtilizationPeriod_Object = MibScalar
currentUtilizationPeriod = _CurrentUtilizationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 1),
    _CurrentUtilizationPeriod_Type()
)
currentUtilizationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentUtilizationPeriod.setStatus("mandatory")
_CurrentUtilization_Type = Integer32
_CurrentUtilization_Object = MibScalar
currentUtilization = _CurrentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 2),
    _CurrentUtilization_Type()
)
currentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentUtilization.setStatus("mandatory")
_CurrentUtilizationTable_Object = MibTable
currentUtilizationTable = _CurrentUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 7)
)
if mibBuilder.loadTexts:
    currentUtilizationTable.setStatus("mandatory")
_CurrentUtilizationEntry_Object = MibTableRow
currentUtilizationEntry = _CurrentUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 7, 1)
)
currentUtilizationEntry.setIndexNames(
    (0, "PROBE-MIB", "curUtilIfIndex"),
)
if mibBuilder.loadTexts:
    currentUtilizationEntry.setStatus("mandatory")


class _CurUtilIfIndex_Type(Integer32):
    """Custom type curUtilIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CurUtilIfIndex_Type.__name__ = "Integer32"
_CurUtilIfIndex_Object = MibTableColumn
curUtilIfIndex = _CurUtilIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 7, 1, 1),
    _CurUtilIfIndex_Type()
)
curUtilIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curUtilIfIndex.setStatus("mandatory")


class _CurUtilPeriod_Type(Integer32):
    """Custom type curUtilPeriod based on Integer32"""
    defaultValue = 5


_CurUtilPeriod_Object = MibTableColumn
curUtilPeriod = _CurUtilPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 7, 1, 2),
    _CurUtilPeriod_Type()
)
curUtilPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    curUtilPeriod.setStatus("mandatory")
_CurUtil_Type = Integer32
_CurUtil_Object = MibTableColumn
curUtil = _CurUtil_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 7, 1, 3),
    _CurUtil_Type()
)
curUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curUtil.setStatus("mandatory")
_CurUtilReceive_Type = Integer32
_CurUtilReceive_Object = MibTableColumn
curUtilReceive = _CurUtilReceive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 7, 1, 4),
    _CurUtilReceive_Type()
)
curUtilReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curUtilReceive.setStatus("mandatory")
_CurUtilTransmit_Type = Integer32
_CurUtilTransmit_Object = MibTableColumn
curUtilTransmit = _CurUtilTransmit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 7, 1, 5),
    _CurUtilTransmit_Type()
)
curUtilTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curUtilTransmit.setStatus("mandatory")
_HostsExtension_ObjectIdentity = ObjectIdentity
hostsExtension = _HostsExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4)
)
_HostExtDuplicateNetAddresses_Type = Counter32
_HostExtDuplicateNetAddresses_Object = MibScalar
hostExtDuplicateNetAddresses = _HostExtDuplicateNetAddresses_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 1),
    _HostExtDuplicateNetAddresses_Type()
)
hostExtDuplicateNetAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostExtDuplicateNetAddresses.setStatus("mandatory")


class _HostExtDuplicateNetEvent_Type(Integer32):
    """Custom type hostExtDuplicateNetEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HostExtDuplicateNetEvent_Type.__name__ = "Integer32"
_HostExtDuplicateNetEvent_Object = MibScalar
hostExtDuplicateNetEvent = _HostExtDuplicateNetEvent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 2),
    _HostExtDuplicateNetEvent_Type()
)
hostExtDuplicateNetEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostExtDuplicateNetEvent.setStatus("mandatory")
_HostExtLastDuplicateNetAddress_Type = OctetString
_HostExtLastDuplicateNetAddress_Object = MibScalar
hostExtLastDuplicateNetAddress = _HostExtLastDuplicateNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 3),
    _HostExtLastDuplicateNetAddress_Type()
)
hostExtLastDuplicateNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostExtLastDuplicateNetAddress.setStatus("mandatory")
_HostExtLastDuplicateHost1_Type = OctetString
_HostExtLastDuplicateHost1_Object = MibScalar
hostExtLastDuplicateHost1 = _HostExtLastDuplicateHost1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 4),
    _HostExtLastDuplicateHost1_Type()
)
hostExtLastDuplicateHost1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostExtLastDuplicateHost1.setStatus("mandatory")
_HostExtLastDuplicateHost2_Type = OctetString
_HostExtLastDuplicateHost2_Object = MibScalar
hostExtLastDuplicateHost2 = _HostExtLastDuplicateHost2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 5),
    _HostExtLastDuplicateHost2_Type()
)
hostExtLastDuplicateHost2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostExtLastDuplicateHost2.setStatus("mandatory")
_HostExtChangedNetAddresses_Type = Counter32
_HostExtChangedNetAddresses_Object = MibScalar
hostExtChangedNetAddresses = _HostExtChangedNetAddresses_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 6),
    _HostExtChangedNetAddresses_Type()
)
hostExtChangedNetAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostExtChangedNetAddresses.setStatus("mandatory")


class _HostExtChangedNetEvent_Type(Integer32):
    """Custom type hostExtChangedNetEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HostExtChangedNetEvent_Type.__name__ = "Integer32"
_HostExtChangedNetEvent_Object = MibScalar
hostExtChangedNetEvent = _HostExtChangedNetEvent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 7),
    _HostExtChangedNetEvent_Type()
)
hostExtChangedNetEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostExtChangedNetEvent.setStatus("mandatory")
_HostExtLastChangedHost_Type = OctetString
_HostExtLastChangedHost_Object = MibScalar
hostExtLastChangedHost = _HostExtLastChangedHost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 8),
    _HostExtLastChangedHost_Type()
)
hostExtLastChangedHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostExtLastChangedHost.setStatus("mandatory")
_HostExtLastOldNetAddress_Type = OctetString
_HostExtLastOldNetAddress_Object = MibScalar
hostExtLastOldNetAddress = _HostExtLastOldNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 9),
    _HostExtLastOldNetAddress_Type()
)
hostExtLastOldNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostExtLastOldNetAddress.setStatus("mandatory")
_HostExtLastNewNetAddress_Type = OctetString
_HostExtLastNewNetAddress_Object = MibScalar
hostExtLastNewNetAddress = _HostExtLastNewNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 10),
    _HostExtLastNewNetAddress_Type()
)
hostExtLastNewNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostExtLastNewNetAddress.setStatus("mandatory")
_HostExtTable_Object = MibTable
hostExtTable = _HostExtTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 11)
)
if mibBuilder.loadTexts:
    hostExtTable.setStatus("mandatory")
_HostExtEntry_Object = MibTableRow
hostExtEntry = _HostExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 11, 1)
)
hostExtEntry.setIndexNames(
    (0, "PROBE-MIB", "hostExtIndex"),
    (0, "PROBE-MIB", "hostExtMacAddress"),
)
if mibBuilder.loadTexts:
    hostExtEntry.setStatus("mandatory")


class _HostExtIndex_Type(Integer32):
    """Custom type hostExtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostExtIndex_Type.__name__ = "Integer32"
_HostExtIndex_Object = MibTableColumn
hostExtIndex = _HostExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 11, 1, 1),
    _HostExtIndex_Type()
)
hostExtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostExtIndex.setStatus("mandatory")
_HostExtMacAddress_Type = OctetString
_HostExtMacAddress_Object = MibTableColumn
hostExtMacAddress = _HostExtMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 11, 1, 2),
    _HostExtMacAddress_Type()
)
hostExtMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostExtMacAddress.setStatus("mandatory")


class _HostExtNetAddrType_Type(Integer32):
    """Custom type hostExtNetAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ip", 1)
    )


_HostExtNetAddrType_Type.__name__ = "Integer32"
_HostExtNetAddrType_Object = MibTableColumn
hostExtNetAddrType = _HostExtNetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 11, 1, 3),
    _HostExtNetAddrType_Type()
)
hostExtNetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostExtNetAddrType.setStatus("mandatory")


class _HostExtNetAddrStatus_Type(Integer32):
    """Custom type hostExtNetAddrStatus based on Integer32"""
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
        *(("changedOnce", 3),
          ("known", 2),
          ("multipleChanges", 4),
          ("unknown", 1))
    )


_HostExtNetAddrStatus_Type.__name__ = "Integer32"
_HostExtNetAddrStatus_Object = MibTableColumn
hostExtNetAddrStatus = _HostExtNetAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 11, 1, 4),
    _HostExtNetAddrStatus_Type()
)
hostExtNetAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostExtNetAddrStatus.setStatus("mandatory")
_HostExtNetAddress_Type = OctetString
_HostExtNetAddress_Object = MibTableColumn
hostExtNetAddress = _HostExtNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 11, 1, 5),
    _HostExtNetAddress_Type()
)
hostExtNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostExtNetAddress.setStatus("mandatory")


class _HostExtCreationOrder_Type(Integer32):
    """Custom type hostExtCreationOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostExtCreationOrder_Type.__name__ = "Integer32"
_HostExtCreationOrder_Object = MibTableColumn
hostExtCreationOrder = _HostExtCreationOrder_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 11, 1, 6),
    _HostExtCreationOrder_Type()
)
hostExtCreationOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostExtCreationOrder.setStatus("mandatory")
_HostExtLastUpdateTime_Type = TimeTicks
_HostExtLastUpdateTime_Object = MibTableColumn
hostExtLastUpdateTime = _HostExtLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 11, 1, 7),
    _HostExtLastUpdateTime_Type()
)
hostExtLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostExtLastUpdateTime.setStatus("mandatory")
_HostTimeExtTable_Object = MibTable
hostTimeExtTable = _HostTimeExtTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 12)
)
if mibBuilder.loadTexts:
    hostTimeExtTable.setStatus("mandatory")
_HostTimeExtEntry_Object = MibTableRow
hostTimeExtEntry = _HostTimeExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 12, 1)
)
hostTimeExtEntry.setIndexNames(
    (0, "PROBE-MIB", "hostTimeExtIndex"),
    (0, "PROBE-MIB", "hostTimeExtCreationOrder"),
)
if mibBuilder.loadTexts:
    hostTimeExtEntry.setStatus("mandatory")


class _HostTimeExtIndex_Type(Integer32):
    """Custom type hostTimeExtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostTimeExtIndex_Type.__name__ = "Integer32"
_HostTimeExtIndex_Object = MibTableColumn
hostTimeExtIndex = _HostTimeExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 12, 1, 1),
    _HostTimeExtIndex_Type()
)
hostTimeExtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeExtIndex.setStatus("mandatory")
_HostTimeExtMacAddress_Type = OctetString
_HostTimeExtMacAddress_Object = MibTableColumn
hostTimeExtMacAddress = _HostTimeExtMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 12, 1, 2),
    _HostTimeExtMacAddress_Type()
)
hostTimeExtMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeExtMacAddress.setStatus("mandatory")


class _HostTimeExtNetAddrType_Type(Integer32):
    """Custom type hostTimeExtNetAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ip", 1)
    )


_HostTimeExtNetAddrType_Type.__name__ = "Integer32"
_HostTimeExtNetAddrType_Object = MibTableColumn
hostTimeExtNetAddrType = _HostTimeExtNetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 12, 1, 3),
    _HostTimeExtNetAddrType_Type()
)
hostTimeExtNetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeExtNetAddrType.setStatus("mandatory")


class _HostTimeExtNetAddrStatus_Type(Integer32):
    """Custom type hostTimeExtNetAddrStatus based on Integer32"""
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
        *(("changedOnce", 3),
          ("known", 2),
          ("multipleChanges", 4),
          ("unknown", 1))
    )


_HostTimeExtNetAddrStatus_Type.__name__ = "Integer32"
_HostTimeExtNetAddrStatus_Object = MibTableColumn
hostTimeExtNetAddrStatus = _HostTimeExtNetAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 12, 1, 4),
    _HostTimeExtNetAddrStatus_Type()
)
hostTimeExtNetAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeExtNetAddrStatus.setStatus("mandatory")
_HostTimeExtNetAddress_Type = OctetString
_HostTimeExtNetAddress_Object = MibTableColumn
hostTimeExtNetAddress = _HostTimeExtNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 12, 1, 5),
    _HostTimeExtNetAddress_Type()
)
hostTimeExtNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeExtNetAddress.setStatus("mandatory")


class _HostTimeExtCreationOrder_Type(Integer32):
    """Custom type hostTimeExtCreationOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostTimeExtCreationOrder_Type.__name__ = "Integer32"
_HostTimeExtCreationOrder_Object = MibTableColumn
hostTimeExtCreationOrder = _HostTimeExtCreationOrder_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 12, 1, 6),
    _HostTimeExtCreationOrder_Type()
)
hostTimeExtCreationOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeExtCreationOrder.setStatus("mandatory")
_HostTimeExtLastUpdateTime_Type = TimeTicks
_HostTimeExtLastUpdateTime_Object = MibTableColumn
hostTimeExtLastUpdateTime = _HostTimeExtLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 4, 12, 1, 7),
    _HostTimeExtLastUpdateTime_Type()
)
hostTimeExtLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeExtLastUpdateTime.setStatus("mandatory")
_FilterExtension_ObjectIdentity = ObjectIdentity
filterExtension = _FilterExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 7)
)
_ChannelExtTable_Object = MibTable
channelExtTable = _ChannelExtTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 7, 2)
)
if mibBuilder.loadTexts:
    channelExtTable.setStatus("mandatory")
_ChannelExtEntry_Object = MibTableRow
channelExtEntry = _ChannelExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 7, 2, 1)
)
channelExtEntry.setIndexNames(
    (0, "PROBE-MIB", "channelExtIndex"),
)
if mibBuilder.loadTexts:
    channelExtEntry.setStatus("mandatory")


class _ChannelExtIndex_Type(Integer32):
    """Custom type channelExtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChannelExtIndex_Type.__name__ = "Integer32"
_ChannelExtIndex_Object = MibTableColumn
channelExtIndex = _ChannelExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 7, 2, 1, 1),
    _ChannelExtIndex_Type()
)
channelExtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelExtIndex.setStatus("mandatory")


class _ChannelExtSelfPktCapture_Type(Integer32):
    """Custom type channelExtSelfPktCapture based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("captureMyOwn", 1),
          ("ignoreMyOwn", 2))
    )


_ChannelExtSelfPktCapture_Type.__name__ = "Integer32"
_ChannelExtSelfPktCapture_Object = MibTableColumn
channelExtSelfPktCapture = _ChannelExtSelfPktCapture_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 7, 2, 1, 2),
    _ChannelExtSelfPktCapture_Type()
)
channelExtSelfPktCapture.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelExtSelfPktCapture.setStatus("mandatory")
_ChannelExtDropEvents_Type = Integer32
_ChannelExtDropEvents_Object = MibScalar
channelExtDropEvents = _ChannelExtDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 7, 3),
    _ChannelExtDropEvents_Type()
)
channelExtDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelExtDropEvents.setStatus("mandatory")
_EchoTest_ObjectIdentity = ObjectIdentity
echoTest = _EchoTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6)
)
_EchoTestSSTable_Object = MibTable
echoTestSSTable = _EchoTestSSTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 1)
)
if mibBuilder.loadTexts:
    echoTestSSTable.setStatus("mandatory")
_EchoTestSSEntry_Object = MibTableRow
echoTestSSEntry = _EchoTestSSEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 1, 1)
)
echoTestSSEntry.setIndexNames(
    (0, "PROBE-MIB", "echoTestSSIndex"),
)
if mibBuilder.loadTexts:
    echoTestSSEntry.setStatus("mandatory")


class _EchoTestSSIndex_Type(Integer32):
    """Custom type echoTestSSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EchoTestSSIndex_Type.__name__ = "Integer32"
_EchoTestSSIndex_Object = MibTableColumn
echoTestSSIndex = _EchoTestSSIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 1, 1, 1),
    _EchoTestSSIndex_Type()
)
echoTestSSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoTestSSIndex.setStatus("mandatory")


class _EchoTestSSIfIndex_Type(Integer32):
    """Custom type echoTestSSIfIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EchoTestSSIfIndex_Type.__name__ = "Integer32"
_EchoTestSSIfIndex_Object = MibTableColumn
echoTestSSIfIndex = _EchoTestSSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 1, 1, 2),
    _EchoTestSSIfIndex_Type()
)
echoTestSSIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoTestSSIfIndex.setStatus("mandatory")
_EchoTestSSMacAddress_Type = OctetString
_EchoTestSSMacAddress_Object = MibTableColumn
echoTestSSMacAddress = _EchoTestSSMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 1, 1, 3),
    _EchoTestSSMacAddress_Type()
)
echoTestSSMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoTestSSMacAddress.setStatus("mandatory")
_EchoTestSSNetAddress_Type = OctetString
_EchoTestSSNetAddress_Object = MibTableColumn
echoTestSSNetAddress = _EchoTestSSNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 1, 1, 4),
    _EchoTestSSNetAddress_Type()
)
echoTestSSNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoTestSSNetAddress.setStatus("mandatory")


class _EchoTestSSProtocol_Type(Integer32):
    """Custom type echoTestSSProtocol based on Integer32"""
    defaultValue = 1

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("appleTalk", 7),
          ("ethernet-ctp", 3),
          ("icmp-echo", 1),
          ("ieee-802-2", 2),
          ("novell-802-2", 8),
          ("novell-802-3", 4),
          ("novell-ethernet", 5),
          ("vines-datalink", 6))
    )


_EchoTestSSProtocol_Type.__name__ = "Integer32"
_EchoTestSSProtocol_Object = MibTableColumn
echoTestSSProtocol = _EchoTestSSProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 1, 1, 5),
    _EchoTestSSProtocol_Type()
)
echoTestSSProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoTestSSProtocol.setStatus("mandatory")


class _EchoTestSSTimeout_Type(Integer32):
    """Custom type echoTestSSTimeout based on Integer32"""
    defaultValue = 100


_EchoTestSSTimeout_Object = MibTableColumn
echoTestSSTimeout = _EchoTestSSTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 1, 1, 6),
    _EchoTestSSTimeout_Type()
)
echoTestSSTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoTestSSTimeout.setStatus("mandatory")


class _EchoTestSSRetryAttempts_Type(Integer32):
    """Custom type echoTestSSRetryAttempts based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_EchoTestSSRetryAttempts_Type.__name__ = "Integer32"
_EchoTestSSRetryAttempts_Object = MibTableColumn
echoTestSSRetryAttempts = _EchoTestSSRetryAttempts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 1, 1, 7),
    _EchoTestSSRetryAttempts_Type()
)
echoTestSSRetryAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoTestSSRetryAttempts.setStatus("mandatory")


class _EchoTestSSLastEchoStatus_Type(Integer32):
    """Custom type echoTestSSLastEchoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-results-available", 1),
          ("response-received", 2),
          ("response-timed-out", 3))
    )


_EchoTestSSLastEchoStatus_Type.__name__ = "Integer32"
_EchoTestSSLastEchoStatus_Object = MibTableColumn
echoTestSSLastEchoStatus = _EchoTestSSLastEchoStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 1, 1, 8),
    _EchoTestSSLastEchoStatus_Type()
)
echoTestSSLastEchoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoTestSSLastEchoStatus.setStatus("mandatory")
_EchoTestSSResponseNumber_Type = Integer32
_EchoTestSSResponseNumber_Object = MibTableColumn
echoTestSSResponseNumber = _EchoTestSSResponseNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 1, 1, 9),
    _EchoTestSSResponseNumber_Type()
)
echoTestSSResponseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoTestSSResponseNumber.setStatus("mandatory")
_EchoTestSSResponseTime_Type = Integer32
_EchoTestSSResponseTime_Object = MibTableColumn
echoTestSSResponseTime = _EchoTestSSResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 1, 1, 10),
    _EchoTestSSResponseTime_Type()
)
echoTestSSResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoTestSSResponseTime.setStatus("mandatory")
_EchoTestSSOwner_Type = OwnerString
_EchoTestSSOwner_Object = MibTableColumn
echoTestSSOwner = _EchoTestSSOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 1, 1, 11),
    _EchoTestSSOwner_Type()
)
echoTestSSOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoTestSSOwner.setStatus("mandatory")
_EchoTestSSStatus_Type = EntryStatus
_EchoTestSSStatus_Object = MibTableColumn
echoTestSSStatus = _EchoTestSSStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 1, 1, 12),
    _EchoTestSSStatus_Type()
)
echoTestSSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoTestSSStatus.setStatus("mandatory")
_EchoTestPeriodicTable_Object = MibTable
echoTestPeriodicTable = _EchoTestPeriodicTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2)
)
if mibBuilder.loadTexts:
    echoTestPeriodicTable.setStatus("mandatory")
_EchoTestPeriodicEntry_Object = MibTableRow
echoTestPeriodicEntry = _EchoTestPeriodicEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1)
)
echoTestPeriodicEntry.setIndexNames(
    (0, "PROBE-MIB", "echoTestPeriodicIndex"),
)
if mibBuilder.loadTexts:
    echoTestPeriodicEntry.setStatus("mandatory")


class _EchoTestPeriodicIndex_Type(Integer32):
    """Custom type echoTestPeriodicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EchoTestPeriodicIndex_Type.__name__ = "Integer32"
_EchoTestPeriodicIndex_Object = MibTableColumn
echoTestPeriodicIndex = _EchoTestPeriodicIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 1),
    _EchoTestPeriodicIndex_Type()
)
echoTestPeriodicIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoTestPeriodicIndex.setStatus("mandatory")


class _EchoTestPeriodicIfIndex_Type(Integer32):
    """Custom type echoTestPeriodicIfIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EchoTestPeriodicIfIndex_Type.__name__ = "Integer32"
_EchoTestPeriodicIfIndex_Object = MibTableColumn
echoTestPeriodicIfIndex = _EchoTestPeriodicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 2),
    _EchoTestPeriodicIfIndex_Type()
)
echoTestPeriodicIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoTestPeriodicIfIndex.setStatus("mandatory")
_EchoTestPeriodicMacAddress_Type = OctetString
_EchoTestPeriodicMacAddress_Object = MibTableColumn
echoTestPeriodicMacAddress = _EchoTestPeriodicMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 3),
    _EchoTestPeriodicMacAddress_Type()
)
echoTestPeriodicMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoTestPeriodicMacAddress.setStatus("mandatory")
_EchoTestPeriodicNetAddress_Type = OctetString
_EchoTestPeriodicNetAddress_Object = MibTableColumn
echoTestPeriodicNetAddress = _EchoTestPeriodicNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 4),
    _EchoTestPeriodicNetAddress_Type()
)
echoTestPeriodicNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoTestPeriodicNetAddress.setStatus("mandatory")


class _EchoTestPeriodicProtocol_Type(Integer32):
    """Custom type echoTestPeriodicProtocol based on Integer32"""
    defaultValue = 1

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("appleTalk", 7),
          ("ethernet-ctp", 3),
          ("icmp-echo", 1),
          ("ieee-802-2", 2),
          ("novell-802-2", 8),
          ("novell-802-3", 4),
          ("novell-ethernet", 5),
          ("vines-datalink", 6))
    )


_EchoTestPeriodicProtocol_Type.__name__ = "Integer32"
_EchoTestPeriodicProtocol_Object = MibTableColumn
echoTestPeriodicProtocol = _EchoTestPeriodicProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 5),
    _EchoTestPeriodicProtocol_Type()
)
echoTestPeriodicProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoTestPeriodicProtocol.setStatus("mandatory")


class _EchoTestPeriodicTimeout_Type(Integer32):
    """Custom type echoTestPeriodicTimeout based on Integer32"""
    defaultValue = 500


_EchoTestPeriodicTimeout_Object = MibTableColumn
echoTestPeriodicTimeout = _EchoTestPeriodicTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 6),
    _EchoTestPeriodicTimeout_Type()
)
echoTestPeriodicTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoTestPeriodicTimeout.setStatus("mandatory")


class _EchoTestPeriodicRetryAttempts_Type(Integer32):
    """Custom type echoTestPeriodicRetryAttempts based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_EchoTestPeriodicRetryAttempts_Type.__name__ = "Integer32"
_EchoTestPeriodicRetryAttempts_Object = MibTableColumn
echoTestPeriodicRetryAttempts = _EchoTestPeriodicRetryAttempts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 7),
    _EchoTestPeriodicRetryAttempts_Type()
)
echoTestPeriodicRetryAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoTestPeriodicRetryAttempts.setStatus("mandatory")


class _EchoTestPeriodicNoResponseEventIndex_Type(Integer32):
    """Custom type echoTestPeriodicNoResponseEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EchoTestPeriodicNoResponseEventIndex_Type.__name__ = "Integer32"
_EchoTestPeriodicNoResponseEventIndex_Object = MibTableColumn
echoTestPeriodicNoResponseEventIndex = _EchoTestPeriodicNoResponseEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 8),
    _EchoTestPeriodicNoResponseEventIndex_Type()
)
echoTestPeriodicNoResponseEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoTestPeriodicNoResponseEventIndex.setStatus("mandatory")


class _EchoTestPeriodicRespondedEventIndex_Type(Integer32):
    """Custom type echoTestPeriodicRespondedEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EchoTestPeriodicRespondedEventIndex_Type.__name__ = "Integer32"
_EchoTestPeriodicRespondedEventIndex_Object = MibTableColumn
echoTestPeriodicRespondedEventIndex = _EchoTestPeriodicRespondedEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 9),
    _EchoTestPeriodicRespondedEventIndex_Type()
)
echoTestPeriodicRespondedEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoTestPeriodicRespondedEventIndex.setStatus("mandatory")


class _EchoTestPeriodicEchoState_Type(Integer32):
    """Custom type echoTestPeriodicEchoState based on Integer32"""
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
        *(("no-echo-sent", 1),
          ("waiting-for-initial-response", 2),
          ("waiting-for-subsequent-response", 4),
          ("waiting-to-echo", 3))
    )


_EchoTestPeriodicEchoState_Type.__name__ = "Integer32"
_EchoTestPeriodicEchoState_Object = MibTableColumn
echoTestPeriodicEchoState = _EchoTestPeriodicEchoState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 10),
    _EchoTestPeriodicEchoState_Type()
)
echoTestPeriodicEchoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoTestPeriodicEchoState.setStatus("mandatory")


class _EchoTestPeriodicLastEchoStatus_Type(Integer32):
    """Custom type echoTestPeriodicLastEchoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-results-available", 1),
          ("response-received", 2),
          ("response-timed-out", 3))
    )


_EchoTestPeriodicLastEchoStatus_Type.__name__ = "Integer32"
_EchoTestPeriodicLastEchoStatus_Object = MibTableColumn
echoTestPeriodicLastEchoStatus = _EchoTestPeriodicLastEchoStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 11),
    _EchoTestPeriodicLastEchoStatus_Type()
)
echoTestPeriodicLastEchoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoTestPeriodicLastEchoStatus.setStatus("mandatory")
_EchoTestPeriodicTotalOperations_Type = Integer32
_EchoTestPeriodicTotalOperations_Object = MibTableColumn
echoTestPeriodicTotalOperations = _EchoTestPeriodicTotalOperations_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 12),
    _EchoTestPeriodicTotalOperations_Type()
)
echoTestPeriodicTotalOperations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoTestPeriodicTotalOperations.setStatus("mandatory")
_EchoTestPeriodicSuccessfulOperations_Type = Integer32
_EchoTestPeriodicSuccessfulOperations_Object = MibTableColumn
echoTestPeriodicSuccessfulOperations = _EchoTestPeriodicSuccessfulOperations_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 13),
    _EchoTestPeriodicSuccessfulOperations_Type()
)
echoTestPeriodicSuccessfulOperations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoTestPeriodicSuccessfulOperations.setStatus("mandatory")
_EchoTestPeriodicMinRespTime_Type = Integer32
_EchoTestPeriodicMinRespTime_Object = MibTableColumn
echoTestPeriodicMinRespTime = _EchoTestPeriodicMinRespTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 14),
    _EchoTestPeriodicMinRespTime_Type()
)
echoTestPeriodicMinRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoTestPeriodicMinRespTime.setStatus("mandatory")
_EchoTestPeriodicMaxRespTime_Type = Integer32
_EchoTestPeriodicMaxRespTime_Object = MibTableColumn
echoTestPeriodicMaxRespTime = _EchoTestPeriodicMaxRespTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 15),
    _EchoTestPeriodicMaxRespTime_Type()
)
echoTestPeriodicMaxRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoTestPeriodicMaxRespTime.setStatus("mandatory")
_EchoTestPeriodicLastRespTime_Type = Integer32
_EchoTestPeriodicLastRespTime_Object = MibTableColumn
echoTestPeriodicLastRespTime = _EchoTestPeriodicLastRespTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 16),
    _EchoTestPeriodicLastRespTime_Type()
)
echoTestPeriodicLastRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoTestPeriodicLastRespTime.setStatus("mandatory")
_EchoTestPeriodicTotalRespTime_Type = Integer32
_EchoTestPeriodicTotalRespTime_Object = MibTableColumn
echoTestPeriodicTotalRespTime = _EchoTestPeriodicTotalRespTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 17),
    _EchoTestPeriodicTotalRespTime_Type()
)
echoTestPeriodicTotalRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoTestPeriodicTotalRespTime.setStatus("mandatory")
_EchoTestPeriodicOwner_Type = OwnerString
_EchoTestPeriodicOwner_Object = MibTableColumn
echoTestPeriodicOwner = _EchoTestPeriodicOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 18),
    _EchoTestPeriodicOwner_Type()
)
echoTestPeriodicOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoTestPeriodicOwner.setStatus("mandatory")
_EchoTestPeriodicStatus_Type = EntryStatus
_EchoTestPeriodicStatus_Object = MibTableColumn
echoTestPeriodicStatus = _EchoTestPeriodicStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 19),
    _EchoTestPeriodicStatus_Type()
)
echoTestPeriodicStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoTestPeriodicStatus.setStatus("mandatory")
_EchoTestPeriodicSumOfSquaresTimeLo_Type = Integer32
_EchoTestPeriodicSumOfSquaresTimeLo_Object = MibTableColumn
echoTestPeriodicSumOfSquaresTimeLo = _EchoTestPeriodicSumOfSquaresTimeLo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 20),
    _EchoTestPeriodicSumOfSquaresTimeLo_Type()
)
echoTestPeriodicSumOfSquaresTimeLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoTestPeriodicSumOfSquaresTimeLo.setStatus("mandatory")
_EchoTestPeriodicSumOfSquaresTimeHi_Type = Integer32
_EchoTestPeriodicSumOfSquaresTimeHi_Object = MibTableColumn
echoTestPeriodicSumOfSquaresTimeHi = _EchoTestPeriodicSumOfSquaresTimeHi_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 21),
    _EchoTestPeriodicSumOfSquaresTimeHi_Type()
)
echoTestPeriodicSumOfSquaresTimeHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoTestPeriodicSumOfSquaresTimeHi.setStatus("mandatory")
_EchoTestPeriodicFailedAttemptCount_Type = Integer32
_EchoTestPeriodicFailedAttemptCount_Object = MibTableColumn
echoTestPeriodicFailedAttemptCount = _EchoTestPeriodicFailedAttemptCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 22),
    _EchoTestPeriodicFailedAttemptCount_Type()
)
echoTestPeriodicFailedAttemptCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoTestPeriodicFailedAttemptCount.setStatus("mandatory")
_EchoTestPeriodicMinRespTime30MinInt_Type = Integer32
_EchoTestPeriodicMinRespTime30MinInt_Object = MibTableColumn
echoTestPeriodicMinRespTime30MinInt = _EchoTestPeriodicMinRespTime30MinInt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 23),
    _EchoTestPeriodicMinRespTime30MinInt_Type()
)
echoTestPeriodicMinRespTime30MinInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoTestPeriodicMinRespTime30MinInt.setStatus("mandatory")
_EchoTestPeriodicMaxRespTime30MinInt_Type = Integer32
_EchoTestPeriodicMaxRespTime30MinInt_Object = MibTableColumn
echoTestPeriodicMaxRespTime30MinInt = _EchoTestPeriodicMaxRespTime30MinInt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 24),
    _EchoTestPeriodicMaxRespTime30MinInt_Type()
)
echoTestPeriodicMaxRespTime30MinInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoTestPeriodicMaxRespTime30MinInt.setStatus("mandatory")
_EchoTestPeriodicMinRespTime5MinInt_Type = Integer32
_EchoTestPeriodicMinRespTime5MinInt_Object = MibTableColumn
echoTestPeriodicMinRespTime5MinInt = _EchoTestPeriodicMinRespTime5MinInt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 25),
    _EchoTestPeriodicMinRespTime5MinInt_Type()
)
echoTestPeriodicMinRespTime5MinInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoTestPeriodicMinRespTime5MinInt.setStatus("mandatory")
_EchoTestPeriodicMaxRespTime5MinInt_Type = Integer32
_EchoTestPeriodicMaxRespTime5MinInt_Object = MibTableColumn
echoTestPeriodicMaxRespTime5MinInt = _EchoTestPeriodicMaxRespTime5MinInt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 2, 1, 26),
    _EchoTestPeriodicMaxRespTime5MinInt_Type()
)
echoTestPeriodicMaxRespTime5MinInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoTestPeriodicMaxRespTime5MinInt.setStatus("mandatory")


class _EchoTestPeriod_Type(Integer32):
    """Custom type echoTestPeriod based on Integer32"""
    defaultValue = 0


_EchoTestPeriod_Object = MibScalar
echoTestPeriod = _EchoTestPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 3),
    _EchoTestPeriod_Type()
)
echoTestPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoTestPeriod.setStatus("mandatory")
_EchoTestPeriodicCount_Type = Integer32
_EchoTestPeriodicCount_Object = MibScalar
echoTestPeriodicCount = _EchoTestPeriodicCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 4),
    _EchoTestPeriodicCount_Type()
)
echoTestPeriodicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoTestPeriodicCount.setStatus("mandatory")


class _EchoTestResetSSTable_Type(Integer32):
    """Custom type echoTestResetSSTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("reset-the-table", 3),
          ("table-in-use", 2),
          ("table-is-empty", 1))
    )


_EchoTestResetSSTable_Type.__name__ = "Integer32"
_EchoTestResetSSTable_Object = MibScalar
echoTestResetSSTable = _EchoTestResetSSTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 5),
    _EchoTestResetSSTable_Type()
)
echoTestResetSSTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoTestResetSSTable.setStatus("mandatory")


class _EchoTestResetPeriodicTable_Type(Integer32):
    """Custom type echoTestResetPeriodicTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("reset-the-table", 3),
          ("table-in-use", 2),
          ("table-is-empty", 1))
    )


_EchoTestResetPeriodicTable_Type.__name__ = "Integer32"
_EchoTestResetPeriodicTable_Object = MibScalar
echoTestResetPeriodicTable = _EchoTestResetPeriodicTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 6),
    _EchoTestResetPeriodicTable_Type()
)
echoTestResetPeriodicTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoTestResetPeriodicTable.setStatus("mandatory")
_EchoTestPeriodicTableLastEdit_Type = TimeTicks
_EchoTestPeriodicTableLastEdit_Object = MibScalar
echoTestPeriodicTableLastEdit = _EchoTestPeriodicTableLastEdit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 7),
    _EchoTestPeriodicTableLastEdit_Type()
)
echoTestPeriodicTableLastEdit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoTestPeriodicTableLastEdit.setStatus("mandatory")


class _EchoTestPeriodicTableStatus_Type(Integer32):
    """Custom type echoTestPeriodicTableStatus based on Integer32"""
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
        *(("beingModified", 4),
          ("recoveryRequest", 2),
          ("underRecovery", 3),
          ("valid", 1))
    )


_EchoTestPeriodicTableStatus_Type.__name__ = "Integer32"
_EchoTestPeriodicTableStatus_Object = MibScalar
echoTestPeriodicTableStatus = _EchoTestPeriodicTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 8),
    _EchoTestPeriodicTableStatus_Type()
)
echoTestPeriodicTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoTestPeriodicTableStatus.setStatus("mandatory")
_EchoTestNovellDefaultGateway_Type = OctetString
_EchoTestNovellDefaultGateway_Object = MibScalar
echoTestNovellDefaultGateway = _EchoTestNovellDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 6, 9),
    _EchoTestNovellDefaultGateway_Type()
)
echoTestNovellDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoTestNovellDefaultGateway.setStatus("mandatory")
_Cable_ObjectIdentity = ObjectIdentity
cable = _Cable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 7)
)
_NodeLocatorII_ObjectIdentity = ObjectIdentity
nodeLocatorII = _NodeLocatorII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 8)
)
_Lp1_ObjectIdentity = ObjectIdentity
lp1 = _Lp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 2)
)
_LpEther_ObjectIdentity = ObjectIdentity
lpEther = _LpEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 3)
)
_Lp2EtherV1_ObjectIdentity = ObjectIdentity
lp2EtherV1 = _Lp2EtherV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 3, 1)
)
_Lp2EtherV2_ObjectIdentity = ObjectIdentity
lp2EtherV2 = _Lp2EtherV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 3, 2)
)
_Lp3Ether_ObjectIdentity = ObjectIdentity
lp3Ether = _Lp3Ether_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 3, 3)
)
_Pview_ObjectIdentity = ObjectIdentity
pview = _Pview_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 4)
)
_Lp2TokenRing_ObjectIdentity = ObjectIdentity
lp2TokenRing = _Lp2TokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 5)
)
_Lp2TokenRingV2_ObjectIdentity = ObjectIdentity
lp2TokenRingV2 = _Lp2TokenRingV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 5, 2)
)
_LpFDDI_ObjectIdentity = ObjectIdentity
lpFDDI = _LpFDDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 6)
)
_LpFDDIV1_ObjectIdentity = ObjectIdentity
lpFDDIV1 = _LpFDDIV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 6, 1)
)
_LpFDDIV2_ObjectIdentity = ObjectIdentity
lpFDDIV2 = _LpFDDIV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 6, 2)
)
_LpQ_ObjectIdentity = ObjectIdentity
lpQ = _LpQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 7)
)
_LpQuadEther_ObjectIdentity = ObjectIdentity
lpQuadEther = _LpQuadEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 7, 2)
)
_LpQuadEtherV1_ObjectIdentity = ObjectIdentity
lpQuadEtherV1 = _LpQuadEtherV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 7, 2, 1)
)
_LpFE_ObjectIdentity = ObjectIdentity
lpFE = _LpFE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 9)
)
_LpFastEther_ObjectIdentity = ObjectIdentity
lpFastEther = _LpFastEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 9, 1)
)
_LpFastEtherV1_ObjectIdentity = ObjectIdentity
lpFastEtherV1 = _LpFastEtherV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 9, 1, 1)
)
_LpMultiport_ObjectIdentity = ObjectIdentity
lpMultiport = _LpMultiport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 10)
)
_LpMultiportTokenRing_ObjectIdentity = ObjectIdentity
lpMultiportTokenRing = _LpMultiportTokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 10, 1)
)
_LpMultiportTokenRingV1_ObjectIdentity = ObjectIdentity
lpMultiportTokenRingV1 = _LpMultiportTokenRingV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 10, 1, 1)
)
_LpMultiportEther_ObjectIdentity = ObjectIdentity
lpMultiportEther = _LpMultiportEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 10, 2)
)
_LpMultiportEtherV1_ObjectIdentity = ObjectIdentity
lpMultiportEtherV1 = _LpMultiportEtherV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 10, 2, 1)
)
_LpT1_ObjectIdentity = ObjectIdentity
lpT1 = _LpT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 11)
)
_LpT1Multiport_ObjectIdentity = ObjectIdentity
lpT1Multiport = _LpT1Multiport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 11, 1)
)
_LpT1MultiportV1_ObjectIdentity = ObjectIdentity
lpT1MultiportV1 = _LpT1MultiportV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 11, 1, 1)
)
_LpE1_ObjectIdentity = ObjectIdentity
lpE1 = _LpE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 12)
)
_LpE1Multiport_ObjectIdentity = ObjectIdentity
lpE1Multiport = _LpE1Multiport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 12, 1)
)
_LpE1MultiportV1_ObjectIdentity = ObjectIdentity
lpE1MultiportV1 = _LpE1MultiportV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 12, 1, 1)
)
_LpVSeries_ObjectIdentity = ObjectIdentity
lpVSeries = _LpVSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 13)
)
_LpVSeriesMultiport_ObjectIdentity = ObjectIdentity
lpVSeriesMultiport = _LpVSeriesMultiport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 13, 1)
)
_LpVSeriesMultiportV1_ObjectIdentity = ObjectIdentity
lpVSeriesMultiportV1 = _LpVSeriesMultiportV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 13, 1, 1)
)
_LpHSSerial_ObjectIdentity = ObjectIdentity
lpHSSerial = _LpHSSerial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 14)
)
_LpHSSI_ObjectIdentity = ObjectIdentity
lpHSSI = _LpHSSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 14, 1)
)
_LpHSSIV1_ObjectIdentity = ObjectIdentity
lpHSSIV1 = _LpHSSIV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 14, 1, 1)
)
_LpT3_ObjectIdentity = ObjectIdentity
lpT3 = _LpT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 15)
)
_LpT3Multiport_ObjectIdentity = ObjectIdentity
lpT3Multiport = _LpT3Multiport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 15, 1)
)
_LpT3MultiportV1_ObjectIdentity = ObjectIdentity
lpT3MultiportV1 = _LpT3MultiportV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 15, 1, 1)
)
_LpATMUTP_ObjectIdentity = ObjectIdentity
lpATMUTP = _LpATMUTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 16)
)
_LpATMUTPMultiport_ObjectIdentity = ObjectIdentity
lpATMUTPMultiport = _LpATMUTPMultiport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 16, 1)
)
_LpATMUTPMultiportV1_ObjectIdentity = ObjectIdentity
lpATMUTPMultiportV1 = _LpATMUTPMultiportV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 16, 1, 1)
)
_LpATMOC3_ObjectIdentity = ObjectIdentity
lpATMOC3 = _LpATMOC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 17)
)
_LpATMOC3Multiport_ObjectIdentity = ObjectIdentity
lpATMOC3Multiport = _LpATMOC3Multiport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 17, 1)
)
_LpATMOC3MultiportV1_ObjectIdentity = ObjectIdentity
lpATMOC3MultiportV1 = _LpATMOC3MultiportV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 17, 1, 1)
)
_LpATMT3_ObjectIdentity = ObjectIdentity
lpATMT3 = _LpATMT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 18)
)
_LpATMT3Multiport_ObjectIdentity = ObjectIdentity
lpATMT3Multiport = _LpATMT3Multiport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 18, 1)
)
_LpATMT3MultiportV1_ObjectIdentity = ObjectIdentity
lpATMT3MultiportV1 = _LpATMT3MultiportV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 18, 1, 1)
)
_LpATME3_ObjectIdentity = ObjectIdentity
lpATME3 = _LpATME3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 19)
)
_LpATME3Multiport_ObjectIdentity = ObjectIdentity
lpATME3Multiport = _LpATME3Multiport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 19, 1)
)
_LpATME3MultiportV1_ObjectIdentity = ObjectIdentity
lpATME3MultiportV1 = _LpATME3MultiportV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 19, 1, 1)
)
_LpATMOC12_ObjectIdentity = ObjectIdentity
lpATMOC12 = _LpATMOC12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 20)
)
_LpATMOC12Multiport_ObjectIdentity = ObjectIdentity
lpATMOC12Multiport = _LpATMOC12Multiport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 20, 1)
)
_LpATMOC12MultiportV1_ObjectIdentity = ObjectIdentity
lpATMOC12MultiportV1 = _LpATMOC12MultiportV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 20, 1, 1)
)
_LpATMGigabit_ObjectIdentity = ObjectIdentity
lpATMGigabit = _LpATMGigabit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 21)
)
_LpATMGigabitMultiport_ObjectIdentity = ObjectIdentity
lpATMGigabitMultiport = _LpATMGigabitMultiport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 21, 1)
)
_LpATMGigabitMultiportV1_ObjectIdentity = ObjectIdentity
lpATMGigabitMultiportV1 = _LpATMGigabitMultiportV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 21, 1, 1)
)
_LpE3_ObjectIdentity = ObjectIdentity
lpE3 = _LpE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 22)
)
_LpE3Multiport_ObjectIdentity = ObjectIdentity
lpE3Multiport = _LpE3Multiport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 22, 1)
)
_LpE3MultiportV1_ObjectIdentity = ObjectIdentity
lpE3MultiportV1 = _LpE3MultiportV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 22, 1, 1)
)
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4)
)
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 4)
)
_Serial_ObjectIdentity = ObjectIdentity
serial = _Serial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 5)
)
_SerialConfigTable_Object = MibTable
serialConfigTable = _SerialConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 5, 1)
)
if mibBuilder.loadTexts:
    serialConfigTable.setStatus("mandatory")
_SerialConfigEntry_Object = MibTableRow
serialConfigEntry = _SerialConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 5, 1, 1)
)
serialConfigEntry.setIndexNames(
    (0, "PROBE-MIB", "serialIfIndex"),
)
if mibBuilder.loadTexts:
    serialConfigEntry.setStatus("mandatory")


class _SerialIfIndex_Type(Integer32):
    """Custom type serialIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SerialIfIndex_Type.__name__ = "Integer32"
_SerialIfIndex_Object = MibTableColumn
serialIfIndex = _SerialIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 5, 1, 1, 1),
    _SerialIfIndex_Type()
)
serialIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialIfIndex.setStatus("mandatory")
_SerialIpAddress_Type = IpAddress
_SerialIpAddress_Object = MibTableColumn
serialIpAddress = _SerialIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 5, 1, 1, 2),
    _SerialIpAddress_Type()
)
serialIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialIpAddress.setStatus("mandatory")
_SerialSubnetMask_Type = IpAddress
_SerialSubnetMask_Object = MibTableColumn
serialSubnetMask = _SerialSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 5, 1, 1, 3),
    _SerialSubnetMask_Type()
)
serialSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialSubnetMask.setStatus("mandatory")


class _SerialMode_Type(Integer32):
    """Custom type serialMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("modem", 2))
    )


_SerialMode_Type.__name__ = "Integer32"
_SerialMode_Object = MibTableColumn
serialMode = _SerialMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 5, 1, 1, 4),
    _SerialMode_Type()
)
serialMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialMode.setStatus("mandatory")


class _SerialProtocol_Type(Integer32):
    """Custom type serialProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("slip", 1)
    )


_SerialProtocol_Type.__name__ = "Integer32"
_SerialProtocol_Object = MibTableColumn
serialProtocol = _SerialProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 5, 1, 1, 5),
    _SerialProtocol_Type()
)
serialProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialProtocol.setStatus("mandatory")


class _SerialSpeed_Type(Integer32):
    """Custom type serialSpeed based on Integer32"""
    defaultValue = 5

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("speed-1200bps", 2),
          ("speed-14400bps", 6),
          ("speed-19200bps", 7),
          ("speed-2400bps", 3),
          ("speed-300bps", 1),
          ("speed-38400bps", 8),
          ("speed-4800bps", 4),
          ("speed-9600bps", 5))
    )


_SerialSpeed_Type.__name__ = "Integer32"
_SerialSpeed_Object = MibTableColumn
serialSpeed = _SerialSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 5, 1, 1, 6),
    _SerialSpeed_Type()
)
serialSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialSpeed.setStatus("mandatory")


class _SerialTimeout_Type(Integer32):
    """Custom type serialTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SerialTimeout_Type.__name__ = "Integer32"
_SerialTimeout_Object = MibTableColumn
serialTimeout = _SerialTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 5, 1, 1, 7),
    _SerialTimeout_Type()
)
serialTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialTimeout.setStatus("mandatory")


class _SerialModemInitString_Type(ControlString):
    """Custom type serialModemInitString based on ControlString"""
    defaultValue = OctetString("^s^MATE0Q0V1X4 S0=1 S2=43^M")

    subtypeSpec = ControlString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SerialModemInitString_Type.__name__ = "ControlString"
_SerialModemInitString_Object = MibTableColumn
serialModemInitString = _SerialModemInitString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 5, 1, 1, 8),
    _SerialModemInitString_Type()
)
serialModemInitString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialModemInitString.setStatus("mandatory")


class _SerialModemHangUpString_Type(ControlString):
    """Custom type serialModemHangUpString based on ControlString"""
    defaultValue = OctetString("^d2^s+++^d2^sATH0^M^d2")

    subtypeSpec = ControlString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SerialModemHangUpString_Type.__name__ = "ControlString"
_SerialModemHangUpString_Object = MibTableColumn
serialModemHangUpString = _SerialModemHangUpString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 5, 1, 1, 9),
    _SerialModemHangUpString_Type()
)
serialModemHangUpString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialModemHangUpString.setStatus("mandatory")


class _SerialModemConnectResp_Type(DisplayString):
    """Custom type serialModemConnectResp based on DisplayString"""
    defaultValue = OctetString("""\
/CONNECT/300/CONNECT 1200/1200/CONNECT 2400/2400/
              CONNECT 4800/4800/CONNECT 9600/9600/CONNECT 14400/14400/
              CONNECT 19200/19200/CONNECT 38400/38400/""")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SerialModemConnectResp_Type.__name__ = "DisplayString"
_SerialModemConnectResp_Object = MibTableColumn
serialModemConnectResp = _SerialModemConnectResp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 5, 1, 1, 10),
    _SerialModemConnectResp_Type()
)
serialModemConnectResp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialModemConnectResp.setStatus("mandatory")


class _SerialModemNoConnectResp_Type(DisplayString):
    """Custom type serialModemNoConnectResp based on DisplayString"""
    defaultValue = OctetString("/NO CARRIER/BUSY/NO DIALTONE/NO ANSWER/ERROR/")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SerialModemNoConnectResp_Type.__name__ = "DisplayString"
_SerialModemNoConnectResp_Object = MibTableColumn
serialModemNoConnectResp = _SerialModemNoConnectResp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 5, 1, 1, 11),
    _SerialModemNoConnectResp_Type()
)
serialModemNoConnectResp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialModemNoConnectResp.setStatus("mandatory")


class _SerialFlowControl_Type(Integer32):
    """Custom type serialFlowControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardwareFlowControl", 2),
          ("noFlowControl", 1))
    )


_SerialFlowControl_Type.__name__ = "Integer32"
_SerialFlowControl_Object = MibTableColumn
serialFlowControl = _SerialFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 5, 1, 1, 12),
    _SerialFlowControl_Type()
)
serialFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialFlowControl.setStatus("mandatory")


class _SerialTrapTimeout_Type(Integer32):
    """Custom type serialTrapTimeout based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SerialTrapTimeout_Type.__name__ = "Integer32"
_SerialTrapTimeout_Object = MibTableColumn
serialTrapTimeout = _SerialTrapTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 5, 1, 1, 13),
    _SerialTrapTimeout_Type()
)
serialTrapTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialTrapTimeout.setStatus("mandatory")
_Net_ObjectIdentity = ObjectIdentity
net = _Net_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 6)
)
_NetConfigTable_Object = MibTable
netConfigTable = _NetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 6, 1)
)
if mibBuilder.loadTexts:
    netConfigTable.setStatus("mandatory")
_NetConfigEntry_Object = MibTableRow
netConfigEntry = _NetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 6, 1, 1)
)
netConfigEntry.setIndexNames(
    (0, "PROBE-MIB", "netConfigIfIndex"),
)
if mibBuilder.loadTexts:
    netConfigEntry.setStatus("mandatory")


class _NetConfigIfIndex_Type(Integer32):
    """Custom type netConfigIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NetConfigIfIndex_Type.__name__ = "Integer32"
_NetConfigIfIndex_Object = MibTableColumn
netConfigIfIndex = _NetConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 6, 1, 1, 1),
    _NetConfigIfIndex_Type()
)
netConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netConfigIfIndex.setStatus("mandatory")


class _NetConfigIfSpeed_Type(Integer32):
    """Custom type netConfigIfSpeed based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183)
        )
    )
    namedValues = NamedValues(
        *(("ifsp-10000kbps", 97),
          ("ifsp-1000kbps", 79),
          ("ifsp-1008000bps", 56),
          ("ifsp-100Mb", 3),
          ("ifsp-1024000bps", 25),
          ("ifsp-10500kbps", 98),
          ("ifsp-1064000bps", 57),
          ("ifsp-1088000bps", 26),
          ("ifsp-10Mb", 2),
          ("ifsp-11000kbps", 99),
          ("ifsp-1120000bps", 58),
          ("ifsp-112000bps", 42),
          ("ifsp-11500kbps", 100),
          ("ifsp-1152000bps", 27),
          ("ifsp-115200bps", 73),
          ("ifsp-1176000bps", 59),
          ("ifsp-12000bps", 68),
          ("ifsp-12000kbps", 101),
          ("ifsp-1200bps", 63),
          ("ifsp-1216000bps", 28),
          ("ifsp-1232000bps", 60),
          ("ifsp-12500kbps", 102),
          ("ifsp-1280000bps", 29),
          ("ifsp-128000bps", 11),
          ("ifsp-1288000bps", 61),
          ("ifsp-13000kbps", 103),
          ("ifsp-1344000bps", 30),
          ("ifsp-13500kbps", 104),
          ("ifsp-14000kbps", 105),
          ("ifsp-1408000bps", 31),
          ("ifsp-14400bps", 69),
          ("ifsp-14500kbps", 106),
          ("ifsp-1472000bps", 32),
          ("ifsp-15000kbps", 107),
          ("ifsp-1500kbps", 80),
          ("ifsp-1536000bps", 33),
          ("ifsp-15500kbps", 108),
          ("ifsp-155520kbps", 76),
          ("ifsp-1600000bps", 34),
          ("ifsp-16000kbps", 109),
          ("ifsp-16500kbps", 110),
          ("ifsp-1664000bps", 35),
          ("ifsp-168000bps", 43),
          ("ifsp-16Mb", 5),
          ("ifsp-17000kbps", 111),
          ("ifsp-1728000bps", 36),
          ("ifsp-17500kbps", 112),
          ("ifsp-1792000bps", 37),
          ("ifsp-18000kbps", 113),
          ("ifsp-18500kbps", 114),
          ("ifsp-1856000bps", 38),
          ("ifsp-19000kbps", 115),
          ("ifsp-1920000bps", 39),
          ("ifsp-192000bps", 12),
          ("ifsp-19200bps", 70),
          ("ifsp-19500kbps", 116),
          ("ifsp-1984000bps", 40),
          ("ifsp-1Gb", 9),
          ("ifsp-1Mb", 1),
          ("ifsp-20000kbps", 117),
          ("ifsp-2000kbps", 81),
          ("ifsp-200Mb", 8),
          ("ifsp-2048000bps", 78),
          ("ifsp-20500kbps", 118),
          ("ifsp-20Mb", 7),
          ("ifsp-21000kbps", 119),
          ("ifsp-21500kbps", 120),
          ("ifsp-22000kbps", 121),
          ("ifsp-224000bps", 44),
          ("ifsp-22500kbps", 122),
          ("ifsp-23000kbps", 123),
          ("ifsp-23500kbps", 124),
          ("ifsp-24000kbps", 125),
          ("ifsp-2400bps", 64),
          ("ifsp-24500kbps", 126),
          ("ifsp-25000kbps", 127),
          ("ifsp-2500kbps", 82),
          ("ifsp-25500kbps", 128),
          ("ifsp-256000bps", 13),
          ("ifsp-26000kbps", 129),
          ("ifsp-26500kbps", 130),
          ("ifsp-27000kbps", 131),
          ("ifsp-27500kbps", 132),
          ("ifsp-280000bps", 45),
          ("ifsp-28000kbps", 133),
          ("ifsp-28500kbps", 134),
          ("ifsp-29000kbps", 135),
          ("ifsp-29500kbps", 136),
          ("ifsp-30000kbps", 137),
          ("ifsp-3000kbps", 83),
          ("ifsp-300bps", 62),
          ("ifsp-30500kbps", 138),
          ("ifsp-31000kbps", 139),
          ("ifsp-31500kbps", 140),
          ("ifsp-320000bps", 14),
          ("ifsp-32000kbps", 141),
          ("ifsp-32500kbps", 142),
          ("ifsp-33000kbps", 143),
          ("ifsp-33500kbps", 144),
          ("ifsp-336000bps", 46),
          ("ifsp-34000kbps", 145),
          ("ifsp-34100kbps", 146),
          ("ifsp-34368kbps", 74),
          ("ifsp-34500kbps", 147),
          ("ifsp-35000kbps", 148),
          ("ifsp-3500kbps", 84),
          ("ifsp-35500kbps", 149),
          ("ifsp-36000kbps", 150),
          ("ifsp-36500kbps", 151),
          ("ifsp-37000kbps", 152),
          ("ifsp-37500kbps", 153),
          ("ifsp-38000kbps", 154),
          ("ifsp-384000bps", 15),
          ("ifsp-38400bps", 71),
          ("ifsp-38500kbps", 155),
          ("ifsp-39000kbps", 156),
          ("ifsp-392000bps", 47),
          ("ifsp-39500kbps", 157),
          ("ifsp-40000kbps", 158),
          ("ifsp-4000kbps", 85),
          ("ifsp-40500kbps", 159),
          ("ifsp-41000kbps", 160),
          ("ifsp-41500kbps", 161),
          ("ifsp-42000kbps", 162),
          ("ifsp-42500kbps", 163),
          ("ifsp-43000kbps", 164),
          ("ifsp-43500kbps", 165),
          ("ifsp-44000kbps", 166),
          ("ifsp-44210kbps", 167),
          ("ifsp-44500kbps", 168),
          ("ifsp-44736kbps", 75),
          ("ifsp-448000bps", 16),
          ("ifsp-45000kbps", 169),
          ("ifsp-4500kbps", 86),
          ("ifsp-45500kbps", 170),
          ("ifsp-46000kbps", 171),
          ("ifsp-46500kbps", 172),
          ("ifsp-47000kbps", 173),
          ("ifsp-47500kbps", 174),
          ("ifsp-48000kbps", 175),
          ("ifsp-4800bps", 65),
          ("ifsp-48500kbps", 176),
          ("ifsp-49000kbps", 177),
          ("ifsp-49500kbps", 178),
          ("ifsp-4Mb", 4),
          ("ifsp-50000kbps", 179),
          ("ifsp-5000kbps", 87),
          ("ifsp-504000bps", 48),
          ("ifsp-50500kbps", 180),
          ("ifsp-51000kbps", 181),
          ("ifsp-512000bps", 17),
          ("ifsp-51500kbps", 182),
          ("ifsp-52000kbps", 183),
          ("ifsp-5500kbps", 88),
          ("ifsp-560000bps", 49),
          ("ifsp-56000bps", 41),
          ("ifsp-576000bps", 18),
          ("ifsp-57600bps", 72),
          ("ifsp-6000kbps", 89),
          ("ifsp-616000bps", 50),
          ("ifsp-622000kbps", 77),
          ("ifsp-640000bps", 19),
          ("ifsp-64000bps", 10),
          ("ifsp-6500kbps", 90),
          ("ifsp-672000bps", 51),
          ("ifsp-7000kbps", 91),
          ("ifsp-704000bps", 20),
          ("ifsp-7200bps", 66),
          ("ifsp-728000bps", 52),
          ("ifsp-7500kbps", 92),
          ("ifsp-768000bps", 21),
          ("ifsp-784000bps", 53),
          ("ifsp-8000kbps", 93),
          ("ifsp-832000bps", 22),
          ("ifsp-840000bps", 54),
          ("ifsp-8500kbps", 94),
          ("ifsp-896000bps", 23),
          ("ifsp-9000kbps", 95),
          ("ifsp-9500kbps", 96),
          ("ifsp-952000bps", 55),
          ("ifsp-960000bps", 24),
          ("ifsp-9600bps", 67),
          ("ifsp-unspecified", 6))
    )


_NetConfigIfSpeed_Type.__name__ = "Integer32"
_NetConfigIfSpeed_Object = MibTableColumn
netConfigIfSpeed = _NetConfigIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 6, 1, 1, 2),
    _NetConfigIfSpeed_Type()
)
netConfigIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netConfigIfSpeed.setStatus("mandatory")
_NetConfigIPAddress_Type = IpAddress
_NetConfigIPAddress_Object = MibTableColumn
netConfigIPAddress = _NetConfigIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 6, 1, 1, 3),
    _NetConfigIPAddress_Type()
)
netConfigIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigIPAddress.setStatus("mandatory")
_NetConfigSubnetMask_Type = IpAddress
_NetConfigSubnetMask_Object = MibTableColumn
netConfigSubnetMask = _NetConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 6, 1, 1, 4),
    _NetConfigSubnetMask_Type()
)
netConfigSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigSubnetMask.setStatus("mandatory")


class _NetConfigRingNumber_Type(Integer32):
    """Custom type netConfigRingNumber based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4095),
    )


_NetConfigRingNumber_Type.__name__ = "Integer32"
_NetConfigRingNumber_Object = MibTableColumn
netConfigRingNumber = _NetConfigRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 6, 1, 1, 5),
    _NetConfigRingNumber_Type()
)
netConfigRingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigRingNumber.setStatus("mandatory")


class _NetConfigPortType_Type(Integer32):
    """Custom type netConfigPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("monitorOnly", 1),
          ("monitorTransmit", 3),
          ("telemetry", 2))
    )


_NetConfigPortType_Type.__name__ = "Integer32"
_NetConfigPortType_Object = MibTableColumn
netConfigPortType = _NetConfigPortType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 6, 1, 1, 6),
    _NetConfigPortType_Type()
)
netConfigPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigPortType.setStatus("mandatory")
_NetConfigDefaultGateway_Type = IpAddress
_NetConfigDefaultGateway_Object = MibTableColumn
netConfigDefaultGateway = _NetConfigDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 6, 1, 1, 7),
    _NetConfigDefaultGateway_Type()
)
netConfigDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigDefaultGateway.setStatus("mandatory")


class _NetConfigPhysicalConnector_Type(Integer32):
    """Custom type netConfigPhysicalConnector based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("aui", 2),
          ("bnc", 4),
          ("br-2", 10),
          ("db-25", 6),
          ("db-37", 9),
          ("db-9", 5),
          ("fiber", 3),
          ("hssi", 11),
          ("mini-bantam", 7),
          ("rj-45", 1),
          ("rj-48c", 8),
          ("unknown", 12))
    )


_NetConfigPhysicalConnector_Type.__name__ = "Integer32"
_NetConfigPhysicalConnector_Object = MibTableColumn
netConfigPhysicalConnector = _NetConfigPhysicalConnector_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 6, 1, 1, 8),
    _NetConfigPhysicalConnector_Type()
)
netConfigPhysicalConnector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigPhysicalConnector.setStatus("mandatory")


class _NetConfigLinkSpeed_Type(Integer32):
    """Custom type netConfigLinkSpeed based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183)
        )
    )
    namedValues = NamedValues(
        *(("lksp-10000kbps", 97),
          ("lksp-1000kbps", 79),
          ("lksp-1008000bps", 56),
          ("lksp-100Mb", 3),
          ("lksp-1024000bps", 25),
          ("lksp-10500kbps", 98),
          ("lksp-1064000bps", 57),
          ("lksp-1088000bps", 26),
          ("lksp-10Mb", 2),
          ("lksp-11000kbps", 99),
          ("lksp-1120000bps", 58),
          ("lksp-112000bps", 42),
          ("lksp-11500kbps", 100),
          ("lksp-1152000bps", 27),
          ("lksp-115200bps", 73),
          ("lksp-1176000bps", 59),
          ("lksp-12000bps", 68),
          ("lksp-12000kbps", 101),
          ("lksp-1200bps", 63),
          ("lksp-1216000bps", 28),
          ("lksp-1232000bps", 60),
          ("lksp-12500kbps", 102),
          ("lksp-1280000bps", 29),
          ("lksp-128000bps", 11),
          ("lksp-1288000bps", 61),
          ("lksp-13000kbps", 103),
          ("lksp-1344000bps", 30),
          ("lksp-13500kbps", 104),
          ("lksp-14000kbps", 105),
          ("lksp-1408000bps", 31),
          ("lksp-14400bps", 69),
          ("lksp-14500kbps", 106),
          ("lksp-1472000bps", 32),
          ("lksp-15000kbps", 107),
          ("lksp-1500kbps", 80),
          ("lksp-1536000bps", 33),
          ("lksp-15500kbps", 108),
          ("lksp-155520kbps", 76),
          ("lksp-1600000bps", 34),
          ("lksp-16000kbps", 109),
          ("lksp-16500kbps", 110),
          ("lksp-1664000bps", 35),
          ("lksp-168000bps", 43),
          ("lksp-16Mb", 5),
          ("lksp-17000kbps", 111),
          ("lksp-1728000bps", 36),
          ("lksp-17500kbps", 112),
          ("lksp-1792000bps", 37),
          ("lksp-18000kbps", 113),
          ("lksp-18500kbps", 114),
          ("lksp-1856000bps", 38),
          ("lksp-19000kbps", 115),
          ("lksp-1920000bps", 39),
          ("lksp-192000bps", 12),
          ("lksp-19200bps", 70),
          ("lksp-19500kbps", 116),
          ("lksp-1984000bps", 40),
          ("lksp-1Gb", 9),
          ("lksp-1Mb", 1),
          ("lksp-20000kbps", 117),
          ("lksp-2000kbps", 81),
          ("lksp-200Mb", 8),
          ("lksp-2048000bps", 78),
          ("lksp-20500kbps", 118),
          ("lksp-20Mb", 7),
          ("lksp-21000kbps", 119),
          ("lksp-21500kbps", 120),
          ("lksp-22000kbps", 121),
          ("lksp-224000bps", 44),
          ("lksp-22500kbps", 122),
          ("lksp-23000kbps", 123),
          ("lksp-23500kbps", 124),
          ("lksp-24000kbps", 125),
          ("lksp-2400bps", 64),
          ("lksp-24500kbps", 126),
          ("lksp-25000kbps", 127),
          ("lksp-2500kbps", 82),
          ("lksp-25500kbps", 128),
          ("lksp-256000bps", 13),
          ("lksp-26000kbps", 129),
          ("lksp-26500kbps", 130),
          ("lksp-27000kbps", 131),
          ("lksp-27500kbps", 132),
          ("lksp-280000bps", 45),
          ("lksp-28000kbps", 133),
          ("lksp-28500kbps", 134),
          ("lksp-29000kbps", 135),
          ("lksp-29500kbps", 136),
          ("lksp-30000kbps", 137),
          ("lksp-3000kbps", 83),
          ("lksp-300bps", 62),
          ("lksp-30500kbps", 138),
          ("lksp-31000kbps", 139),
          ("lksp-31500kbps", 140),
          ("lksp-320000bps", 14),
          ("lksp-32000kbps", 141),
          ("lksp-32500kbps", 142),
          ("lksp-33000kbps", 143),
          ("lksp-33500kbps", 144),
          ("lksp-336000bps", 46),
          ("lksp-34000kbps", 145),
          ("lksp-34100kbps", 146),
          ("lksp-34368kbps", 74),
          ("lksp-34500kbps", 147),
          ("lksp-35000kbps", 148),
          ("lksp-3500kbps", 84),
          ("lksp-35500kbps", 149),
          ("lksp-36000kbps", 150),
          ("lksp-36500kbps", 151),
          ("lksp-37000kbps", 152),
          ("lksp-37500kbps", 153),
          ("lksp-38000kbps", 154),
          ("lksp-384000bps", 15),
          ("lksp-38400bps", 71),
          ("lksp-38500kbps", 155),
          ("lksp-39000kbps", 156),
          ("lksp-392000bps", 47),
          ("lksp-39500kbps", 157),
          ("lksp-40000kbps", 158),
          ("lksp-4000kbps", 85),
          ("lksp-40500kbps", 159),
          ("lksp-41000kbps", 160),
          ("lksp-41500kbps", 161),
          ("lksp-42000kbps", 162),
          ("lksp-42500kbps", 163),
          ("lksp-43000kbps", 164),
          ("lksp-43500kbps", 165),
          ("lksp-44000kbps", 166),
          ("lksp-44210kbps", 167),
          ("lksp-44500kbps", 168),
          ("lksp-44736kbps", 75),
          ("lksp-448000bps", 16),
          ("lksp-45000kbps", 169),
          ("lksp-4500kbps", 86),
          ("lksp-45500kbps", 170),
          ("lksp-46000kbps", 171),
          ("lksp-46500kbps", 172),
          ("lksp-47000kbps", 173),
          ("lksp-47500kbps", 174),
          ("lksp-48000kbps", 175),
          ("lksp-4800bps", 65),
          ("lksp-48500kbps", 176),
          ("lksp-49000kbps", 177),
          ("lksp-49500kbps", 178),
          ("lksp-4Mb", 4),
          ("lksp-50000kbps", 179),
          ("lksp-5000kbps", 87),
          ("lksp-504000bps", 48),
          ("lksp-50500kbps", 180),
          ("lksp-51000kbps", 181),
          ("lksp-512000bps", 17),
          ("lksp-51500kbps", 182),
          ("lksp-52000kbps", 183),
          ("lksp-5500kbps", 88),
          ("lksp-560000bps", 49),
          ("lksp-56000bps", 41),
          ("lksp-576000bps", 18),
          ("lksp-57600bps", 72),
          ("lksp-6000kbps", 89),
          ("lksp-616000bps", 50),
          ("lksp-622000kbps", 77),
          ("lksp-640000bps", 19),
          ("lksp-64000bps", 10),
          ("lksp-6500kbps", 90),
          ("lksp-672000bps", 51),
          ("lksp-7000kbps", 91),
          ("lksp-704000bps", 20),
          ("lksp-7200bps", 66),
          ("lksp-728000bps", 52),
          ("lksp-7500kbps", 92),
          ("lksp-768000bps", 21),
          ("lksp-784000bps", 53),
          ("lksp-8000kbps", 93),
          ("lksp-832000bps", 22),
          ("lksp-840000bps", 54),
          ("lksp-8500kbps", 94),
          ("lksp-896000bps", 23),
          ("lksp-9000kbps", 95),
          ("lksp-9500kbps", 96),
          ("lksp-952000bps", 55),
          ("lksp-960000bps", 24),
          ("lksp-9600bps", 67),
          ("lksp-auto-negotiate", 6))
    )


_NetConfigLinkSpeed_Type.__name__ = "Integer32"
_NetConfigLinkSpeed_Object = MibTableColumn
netConfigLinkSpeed = _NetConfigLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 6, 1, 1, 9),
    _NetConfigLinkSpeed_Type()
)
netConfigLinkSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigLinkSpeed.setStatus("mandatory")


class _NetConfigDuplex_Type(Integer32):
    """Custom type netConfigDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 2),
          ("half-duplex", 1))
    )


_NetConfigDuplex_Type.__name__ = "Integer32"
_NetConfigDuplex_Object = MibTableColumn
netConfigDuplex = _NetConfigDuplex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 6, 1, 1, 10),
    _NetConfigDuplex_Type()
)
netConfigDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigDuplex.setStatus("mandatory")


class _NetConfigLineCode_Type(Integer32):
    """Custom type netConfigLineCode based on Integer32"""
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
        *(("ami", 2),
          ("b3zs", 4),
          ("b8zs", 1),
          ("hdb3", 3))
    )


_NetConfigLineCode_Type.__name__ = "Integer32"
_NetConfigLineCode_Object = MibTableColumn
netConfigLineCode = _NetConfigLineCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 6, 1, 1, 11),
    _NetConfigLineCode_Type()
)
netConfigLineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigLineCode.setStatus("mandatory")


class _NetConfigFramingType_Type(Integer32):
    """Custom type netConfigFramingType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("cbitParity", 6),
          ("d4", 2),
          ("esf", 1),
          ("g751", 8),
          ("g804", 7),
          ("m13", 5),
          ("slic96", 10),
          ("t1dm", 9),
          ("withCRC4", 3),
          ("withoutCRC4", 4))
    )


_NetConfigFramingType_Type.__name__ = "Integer32"
_NetConfigFramingType_Object = MibTableColumn
netConfigFramingType = _NetConfigFramingType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 6, 1, 1, 12),
    _NetConfigFramingType_Type()
)
netConfigFramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigFramingType.setStatus("mandatory")


class _NetConfigChannelRate_Type(Integer32):
    """Custom type netConfigChannelRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chnrt-1536000bps", 3),
          ("chnrt-56K", 1),
          ("chnrt-64K", 2))
    )


_NetConfigChannelRate_Type.__name__ = "Integer32"
_NetConfigChannelRate_Object = MibTableColumn
netConfigChannelRate = _NetConfigChannelRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 6, 1, 1, 13),
    _NetConfigChannelRate_Type()
)
netConfigChannelRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigChannelRate.setStatus("mandatory")
_NetConfigDataChannel_Type = Integer32
_NetConfigDataChannel_Object = MibTableColumn
netConfigDataChannel = _NetConfigDataChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 6, 1, 1, 14),
    _NetConfigDataChannel_Type()
)
netConfigDataChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigDataChannel.setStatus("mandatory")


class _NetConfigDataSense_Type(Integer32):
    """Custom type netConfigDataSense based on Integer32"""
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
        *(("inverted", 2),
          ("normal", 1),
          ("nrzi", 3))
    )


_NetConfigDataSense_Type.__name__ = "Integer32"
_NetConfigDataSense_Object = MibTableColumn
netConfigDataSense = _NetConfigDataSense_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 6, 1, 1, 15),
    _NetConfigDataSense_Type()
)
netConfigDataSense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigDataSense.setStatus("mandatory")


class _NetConfigLinkLayerType_Type(Integer32):
    """Custom type netConfigLinkLayerType based on Integer32"""
    defaultValue = 1

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
        *(("aal5", 5),
          ("frameRelay", 1),
          ("hdlc", 3),
          ("ppp", 6),
          ("sdlc", 4),
          ("x25", 2))
    )


_NetConfigLinkLayerType_Type.__name__ = "Integer32"
_NetConfigLinkLayerType_Object = MibTableColumn
netConfigLinkLayerType = _NetConfigLinkLayerType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 6, 1, 1, 16),
    _NetConfigLinkLayerType_Type()
)
netConfigLinkLayerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigLinkLayerType.setStatus("mandatory")


class _NetConfigNetworkInterface_Type(Integer32):
    """Custom type netConfigNetworkInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nni", 2),
          ("uni", 1))
    )


_NetConfigNetworkInterface_Type.__name__ = "Integer32"
_NetConfigNetworkInterface_Object = MibTableColumn
netConfigNetworkInterface = _NetConfigNetworkInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 6, 1, 1, 17),
    _NetConfigNetworkInterface_Type()
)
netConfigNetworkInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigNetworkInterface.setStatus("mandatory")


class _NetConfigCellSynchronization_Type(Integer32):
    """Custom type netConfigCellSynchronization based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hec", 1),
          ("plcp", 2))
    )


_NetConfigCellSynchronization_Type.__name__ = "Integer32"
_NetConfigCellSynchronization_Object = MibTableColumn
netConfigCellSynchronization = _NetConfigCellSynchronization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 6, 1, 1, 18),
    _NetConfigCellSynchronization_Type()
)
netConfigCellSynchronization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigCellSynchronization.setStatus("mandatory")


class _NetConfigReceiverMode_Type(Integer32):
    """Custom type netConfigReceiverMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("line", 1),
          ("monitor-jack", 2))
    )


_NetConfigReceiverMode_Type.__name__ = "Integer32"
_NetConfigReceiverMode_Object = MibTableColumn
netConfigReceiverMode = _NetConfigReceiverMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 6, 1, 1, 19),
    _NetConfigReceiverMode_Type()
)
netConfigReceiverMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigReceiverMode.setStatus("mandatory")


class _NetConfigMaximumFrameSize_Type(Integer32):
    """Custom type netConfigMaximumFrameSize based on Integer32"""
    defaultValue = 8192


_NetConfigMaximumFrameSize_Object = MibTableColumn
netConfigMaximumFrameSize = _NetConfigMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 6, 1, 1, 20),
    _NetConfigMaximumFrameSize_Type()
)
netConfigMaximumFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigMaximumFrameSize.setStatus("mandatory")
_NetDefaultGateway_Type = IpAddress
_NetDefaultGateway_Object = MibScalar
netDefaultGateway = _NetDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 6, 2),
    _NetDefaultGateway_Type()
)
netDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDefaultGateway.setStatus("mandatory")
_TokenRing_ObjectIdentity = ObjectIdentity
tokenRing = _TokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 7)
)


class _TokenRingSpeed_Type(Integer32):
    """Custom type tokenRingSpeed based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoDetect", 1),
          ("ringsp-16Mbps", 3),
          ("ringsp-4Mbps", 2))
    )


_TokenRingSpeed_Type.__name__ = "Integer32"
_TokenRingSpeed_Object = MibScalar
tokenRingSpeed = _TokenRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 7, 1),
    _TokenRingSpeed_Type()
)
tokenRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingSpeed.setStatus("mandatory")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 13)
)
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 1)
)
_Delivery_ObjectIdentity = ObjectIdentity
delivery = _Delivery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 1, 3)
)
_TrapDestTable_Object = MibTable
trapDestTable = _TrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 1, 3, 3)
)
if mibBuilder.loadTexts:
    trapDestTable.setStatus("mandatory")
_TrapDestEntry_Object = MibTableRow
trapDestEntry = _TrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 1, 3, 3, 1)
)
trapDestEntry.setIndexNames(
    (0, "PROBE-MIB", "trapDestIndex"),
)
if mibBuilder.loadTexts:
    trapDestEntry.setStatus("mandatory")


class _TrapDestIndex_Type(Integer32):
    """Custom type trapDestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TrapDestIndex_Type.__name__ = "Integer32"
_TrapDestIndex_Object = MibTableColumn
trapDestIndex = _TrapDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 1, 3, 3, 1, 1),
    _TrapDestIndex_Type()
)
trapDestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDestIndex.setStatus("mandatory")


class _TrapDestCommunity_Type(DisplayString):
    """Custom type trapDestCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TrapDestCommunity_Type.__name__ = "DisplayString"
_TrapDestCommunity_Object = MibTableColumn
trapDestCommunity = _TrapDestCommunity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 1, 3, 3, 1, 2),
    _TrapDestCommunity_Type()
)
trapDestCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestCommunity.setStatus("mandatory")


class _TrapDestDeliveryType_Type(Integer32):
    """Custom type trapDestDeliveryType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("one-shot", 1)
    )


_TrapDestDeliveryType_Type.__name__ = "Integer32"
_TrapDestDeliveryType_Object = MibTableColumn
trapDestDeliveryType = _TrapDestDeliveryType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 1, 3, 3, 1, 3),
    _TrapDestDeliveryType_Type()
)
trapDestDeliveryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestDeliveryType.setStatus("mandatory")
_TrapDestPrimaryIpAddress_Type = IpAddress
_TrapDestPrimaryIpAddress_Object = MibTableColumn
trapDestPrimaryIpAddress = _TrapDestPrimaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 1, 3, 3, 1, 4),
    _TrapDestPrimaryIpAddress_Type()
)
trapDestPrimaryIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestPrimaryIpAddress.setStatus("mandatory")


class _TrapDestPrimaryIfIndex_Type(Integer32):
    """Custom type trapDestPrimaryIfIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TrapDestPrimaryIfIndex_Type.__name__ = "Integer32"
_TrapDestPrimaryIfIndex_Object = MibTableColumn
trapDestPrimaryIfIndex = _TrapDestPrimaryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 1, 3, 3, 1, 5),
    _TrapDestPrimaryIfIndex_Type()
)
trapDestPrimaryIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestPrimaryIfIndex.setStatus("mandatory")
_TrapDestOwner_Type = OwnerString
_TrapDestOwner_Object = MibTableColumn
trapDestOwner = _TrapDestOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 1, 3, 3, 1, 8),
    _TrapDestOwner_Type()
)
trapDestOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestOwner.setStatus("mandatory")
_TrapDestStatus_Type = EntryStatus
_TrapDestStatus_Object = MibTableColumn
trapDestStatus = _TrapDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 1, 3, 3, 1, 9),
    _TrapDestStatus_Type()
)
trapDestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestStatus.setStatus("mandatory")
_Community_ObjectIdentity = ObjectIdentity
community = _Community_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 5)
)
_AccessControl_ObjectIdentity = ObjectIdentity
accessControl = _AccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 5, 1)
)
_CommAccessTable_Object = MibTable
commAccessTable = _CommAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 5, 1, 1)
)
if mibBuilder.loadTexts:
    commAccessTable.setStatus("mandatory")
_CommAccessEntry_Object = MibTableRow
commAccessEntry = _CommAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 5, 1, 1, 1)
)
commAccessEntry.setIndexNames(
    (0, "PROBE-MIB", "commAccessIndex"),
)
if mibBuilder.loadTexts:
    commAccessEntry.setStatus("mandatory")


class _CommAccessIndex_Type(Integer32):
    """Custom type commAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CommAccessIndex_Type.__name__ = "Integer32"
_CommAccessIndex_Object = MibTableColumn
commAccessIndex = _CommAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 5, 1, 1, 1, 1),
    _CommAccessIndex_Type()
)
commAccessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commAccessIndex.setStatus("mandatory")


class _CommAccessCommunity_Type(DisplayString):
    """Custom type commAccessCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CommAccessCommunity_Type.__name__ = "DisplayString"
_CommAccessCommunity_Object = MibTableColumn
commAccessCommunity = _CommAccessCommunity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 5, 1, 1, 1, 2),
    _CommAccessCommunity_Type()
)
commAccessCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commAccessCommunity.setStatus("mandatory")
_CommAccessLevel_Type = AccessLevel
_CommAccessLevel_Object = MibTableColumn
commAccessLevel = _CommAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 5, 1, 1, 1, 3),
    _CommAccessLevel_Type()
)
commAccessLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commAccessLevel.setStatus("mandatory")
_CommAccessOwner_Type = OwnerString
_CommAccessOwner_Object = MibTableColumn
commAccessOwner = _CommAccessOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 5, 1, 1, 1, 4),
    _CommAccessOwner_Type()
)
commAccessOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commAccessOwner.setStatus("mandatory")
_CommAccessStatus_Type = EntryStatus
_CommAccessStatus_Object = MibTableColumn
commAccessStatus = _CommAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 5, 1, 1, 1, 5),
    _CommAccessStatus_Type()
)
commAccessStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commAccessStatus.setStatus("mandatory")
_ClientTable_Object = MibTable
clientTable = _ClientTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 5, 1, 2)
)
if mibBuilder.loadTexts:
    clientTable.setStatus("mandatory")
_ClientEntry_Object = MibTableRow
clientEntry = _ClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 5, 1, 2, 1)
)
clientEntry.setIndexNames(
    (0, "PROBE-MIB", "clientIndex"),
)
if mibBuilder.loadTexts:
    clientEntry.setStatus("mandatory")


class _ClientIndex_Type(Integer32):
    """Custom type clientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ClientIndex_Type.__name__ = "Integer32"
_ClientIndex_Object = MibTableColumn
clientIndex = _ClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 5, 1, 2, 1, 1),
    _ClientIndex_Type()
)
clientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIndex.setStatus("mandatory")
_ClientIpAddress_Type = IpAddress
_ClientIpAddress_Object = MibTableColumn
clientIpAddress = _ClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 5, 1, 2, 1, 2),
    _ClientIpAddress_Type()
)
clientIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIpAddress.setStatus("mandatory")
_ClientIpMask_Type = IpAddress
_ClientIpMask_Object = MibTableColumn
clientIpMask = _ClientIpMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 5, 1, 2, 1, 3),
    _ClientIpMask_Type()
)
clientIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIpMask.setStatus("mandatory")


class _ClientCommunity_Type(DisplayString):
    """Custom type clientCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ClientCommunity_Type.__name__ = "DisplayString"
_ClientCommunity_Object = MibTableColumn
clientCommunity = _ClientCommunity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 5, 1, 2, 1, 4),
    _ClientCommunity_Type()
)
clientCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientCommunity.setStatus("mandatory")
_ClientOwner_Type = OwnerString
_ClientOwner_Object = MibTableColumn
clientOwner = _ClientOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 5, 1, 2, 1, 5),
    _ClientOwner_Type()
)
clientOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientOwner.setStatus("mandatory")
_ClientStatus_Type = EntryStatus
_ClientStatus_Object = MibTableColumn
clientStatus = _ClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 5, 1, 2, 1, 6),
    _ClientStatus_Type()
)
clientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientStatus.setStatus("mandatory")
_Slip_ObjectIdentity = ObjectIdentity
slip = _Slip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 15)
)
_SerialConnectionTable_Object = MibTable
serialConnectionTable = _SerialConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 15, 5)
)
if mibBuilder.loadTexts:
    serialConnectionTable.setStatus("mandatory")
_SerialConnectionEntry_Object = MibTableRow
serialConnectionEntry = _SerialConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 15, 5, 1)
)
serialConnectionEntry.setIndexNames(
    (0, "PROBE-MIB", "serialConnectIndex"),
)
if mibBuilder.loadTexts:
    serialConnectionEntry.setStatus("mandatory")


class _SerialConnectIndex_Type(Integer32):
    """Custom type serialConnectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SerialConnectIndex_Type.__name__ = "Integer32"
_SerialConnectIndex_Object = MibTableColumn
serialConnectIndex = _SerialConnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 15, 5, 1, 1),
    _SerialConnectIndex_Type()
)
serialConnectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialConnectIndex.setStatus("mandatory")
_SerialConnectDestIpAddress_Type = IpAddress
_SerialConnectDestIpAddress_Object = MibTableColumn
serialConnectDestIpAddress = _SerialConnectDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 15, 5, 1, 2),
    _SerialConnectDestIpAddress_Type()
)
serialConnectDestIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialConnectDestIpAddress.setStatus("mandatory")


class _SerialConnectType_Type(Integer32):
    """Custom type serialConnectType based on Integer32"""
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
        *(("direct", 1),
          ("modem", 2),
          ("modem-switch", 4),
          ("switch", 3))
    )


_SerialConnectType_Type.__name__ = "Integer32"
_SerialConnectType_Object = MibTableColumn
serialConnectType = _SerialConnectType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 15, 5, 1, 3),
    _SerialConnectType_Type()
)
serialConnectType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialConnectType.setStatus("mandatory")


class _SerialConnectDialString_Type(ControlString):
    """Custom type serialConnectDialString based on ControlString"""
    subtypeSpec = ControlString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SerialConnectDialString_Type.__name__ = "ControlString"
_SerialConnectDialString_Object = MibTableColumn
serialConnectDialString = _SerialConnectDialString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 15, 5, 1, 4),
    _SerialConnectDialString_Type()
)
serialConnectDialString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialConnectDialString.setStatus("mandatory")


class _SerialConnectSwitchConnectSeq_Type(ControlString):
    """Custom type serialConnectSwitchConnectSeq based on ControlString"""
    subtypeSpec = ControlString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SerialConnectSwitchConnectSeq_Type.__name__ = "ControlString"
_SerialConnectSwitchConnectSeq_Object = MibTableColumn
serialConnectSwitchConnectSeq = _SerialConnectSwitchConnectSeq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 15, 5, 1, 5),
    _SerialConnectSwitchConnectSeq_Type()
)
serialConnectSwitchConnectSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialConnectSwitchConnectSeq.setStatus("mandatory")


class _SerialConnectSwitchDisconnectSeq_Type(ControlString):
    """Custom type serialConnectSwitchDisconnectSeq based on ControlString"""
    subtypeSpec = ControlString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SerialConnectSwitchDisconnectSeq_Type.__name__ = "ControlString"
_SerialConnectSwitchDisconnectSeq_Object = MibTableColumn
serialConnectSwitchDisconnectSeq = _SerialConnectSwitchDisconnectSeq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 15, 5, 1, 6),
    _SerialConnectSwitchDisconnectSeq_Type()
)
serialConnectSwitchDisconnectSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialConnectSwitchDisconnectSeq.setStatus("mandatory")


class _SerialConnectSwitchResetSeq_Type(ControlString):
    """Custom type serialConnectSwitchResetSeq based on ControlString"""
    subtypeSpec = ControlString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SerialConnectSwitchResetSeq_Type.__name__ = "ControlString"
_SerialConnectSwitchResetSeq_Object = MibTableColumn
serialConnectSwitchResetSeq = _SerialConnectSwitchResetSeq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 15, 5, 1, 7),
    _SerialConnectSwitchResetSeq_Type()
)
serialConnectSwitchResetSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialConnectSwitchResetSeq.setStatus("mandatory")
_SerialConnectOwner_Type = OwnerString
_SerialConnectOwner_Object = MibTableColumn
serialConnectOwner = _SerialConnectOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 15, 5, 1, 8),
    _SerialConnectOwner_Type()
)
serialConnectOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialConnectOwner.setStatus("mandatory")
_SerialConnectStatus_Type = EntryStatus
_SerialConnectStatus_Object = MibTableColumn
serialConnectStatus = _SerialConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 15, 5, 1, 9),
    _SerialConnectStatus_Type()
)
serialConnectStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialConnectStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

echotestStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 0, 1)
)
echotestStatus.setObjects(
      *(("PROBE-MIB", "echoTestPeriodicMacAddress"),
        ("PROBE-MIB", "echoTestPeriodicNetAddress"),
        ("PROBE-MIB", "echoTestPeriodicProtocol"),
        ("PROBE-MIB", "echoTestPeriodicEchoState"),
        ("PROBE-MIB", "echoTestPeriodicLastEchoStatus"))
)
if mibBuilder.loadTexts:
    echotestStatus.setStatus(
        ""
    )

duplicateIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 0, 2)
)
duplicateIP.setObjects(
      *(("PROBE-MIB", "hostExtDuplicateNetAddresses"),
        ("PROBE-MIB", "hostExtLastDuplicateHost1"),
        ("PROBE-MIB", "hostExtLastDuplicateHost2"),
        ("PROBE-MIB", "hostExtLastDuplicateNetAddress"))
)
if mibBuilder.loadTexts:
    duplicateIP.setStatus(
        ""
    )

changedIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 0, 3)
)
changedIP.setObjects(
      *(("PROBE-MIB", "hostExtChangedNetAddresses"),
        ("PROBE-MIB", "hostExtLastChangedHost"),
        ("PROBE-MIB", "hostExtLastOldNetAddress"),
        ("PROBE-MIB", "hostExtLastNewNetAddress"))
)
if mibBuilder.loadTexts:
    changedIP.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PROBE-MIB",
    **{"AccessLevel": AccessLevel,
       "ControlString": ControlString,
       "hp": hp,
       "nm": nm,
       "hpExperimental": hpExperimental,
       "ntd": ntd,
       "system": system,
       "netElement": netElement,
       "lanprobe": lanprobe,
       "echotestStatus": echotestStatus,
       "duplicateIP": duplicateIP,
       "changedIP": changedIP,
       "general": general,
       "probeAdmin": probeAdmin,
       "probeIdentification": probeIdentification,
       "probeFirmwareRev": probeFirmwareRev,
       "probeHardwareRev": probeHardwareRev,
       "probeDateTime": probeDateTime,
       "probeResetControl": probeResetControl,
       "probeDownloadFile": probeDownloadFile,
       "probeDownloadTFTPServer": probeDownloadTFTPServer,
       "probeDownloadAction": probeDownloadAction,
       "probeDownloadStatus": probeDownloadStatus,
       "probeEchoInterval": probeEchoInterval,
       "probeFeatureDeactivate": probeFeatureDeactivate,
       "cableTest": cableTest,
       "nodeLocation": nodeLocation,
       "probeView": probeView,
       "rmonExtension": rmonExtension,
       "statsExtension": statsExtension,
       "currentUtilizationPeriod": currentUtilizationPeriod,
       "currentUtilization": currentUtilization,
       "currentUtilizationTable": currentUtilizationTable,
       "currentUtilizationEntry": currentUtilizationEntry,
       "curUtilIfIndex": curUtilIfIndex,
       "curUtilPeriod": curUtilPeriod,
       "curUtil": curUtil,
       "curUtilReceive": curUtilReceive,
       "curUtilTransmit": curUtilTransmit,
       "hostsExtension": hostsExtension,
       "hostExtDuplicateNetAddresses": hostExtDuplicateNetAddresses,
       "hostExtDuplicateNetEvent": hostExtDuplicateNetEvent,
       "hostExtLastDuplicateNetAddress": hostExtLastDuplicateNetAddress,
       "hostExtLastDuplicateHost1": hostExtLastDuplicateHost1,
       "hostExtLastDuplicateHost2": hostExtLastDuplicateHost2,
       "hostExtChangedNetAddresses": hostExtChangedNetAddresses,
       "hostExtChangedNetEvent": hostExtChangedNetEvent,
       "hostExtLastChangedHost": hostExtLastChangedHost,
       "hostExtLastOldNetAddress": hostExtLastOldNetAddress,
       "hostExtLastNewNetAddress": hostExtLastNewNetAddress,
       "hostExtTable": hostExtTable,
       "hostExtEntry": hostExtEntry,
       "hostExtIndex": hostExtIndex,
       "hostExtMacAddress": hostExtMacAddress,
       "hostExtNetAddrType": hostExtNetAddrType,
       "hostExtNetAddrStatus": hostExtNetAddrStatus,
       "hostExtNetAddress": hostExtNetAddress,
       "hostExtCreationOrder": hostExtCreationOrder,
       "hostExtLastUpdateTime": hostExtLastUpdateTime,
       "hostTimeExtTable": hostTimeExtTable,
       "hostTimeExtEntry": hostTimeExtEntry,
       "hostTimeExtIndex": hostTimeExtIndex,
       "hostTimeExtMacAddress": hostTimeExtMacAddress,
       "hostTimeExtNetAddrType": hostTimeExtNetAddrType,
       "hostTimeExtNetAddrStatus": hostTimeExtNetAddrStatus,
       "hostTimeExtNetAddress": hostTimeExtNetAddress,
       "hostTimeExtCreationOrder": hostTimeExtCreationOrder,
       "hostTimeExtLastUpdateTime": hostTimeExtLastUpdateTime,
       "filterExtension": filterExtension,
       "channelExtTable": channelExtTable,
       "channelExtEntry": channelExtEntry,
       "channelExtIndex": channelExtIndex,
       "channelExtSelfPktCapture": channelExtSelfPktCapture,
       "channelExtDropEvents": channelExtDropEvents,
       "echoTest": echoTest,
       "echoTestSSTable": echoTestSSTable,
       "echoTestSSEntry": echoTestSSEntry,
       "echoTestSSIndex": echoTestSSIndex,
       "echoTestSSIfIndex": echoTestSSIfIndex,
       "echoTestSSMacAddress": echoTestSSMacAddress,
       "echoTestSSNetAddress": echoTestSSNetAddress,
       "echoTestSSProtocol": echoTestSSProtocol,
       "echoTestSSTimeout": echoTestSSTimeout,
       "echoTestSSRetryAttempts": echoTestSSRetryAttempts,
       "echoTestSSLastEchoStatus": echoTestSSLastEchoStatus,
       "echoTestSSResponseNumber": echoTestSSResponseNumber,
       "echoTestSSResponseTime": echoTestSSResponseTime,
       "echoTestSSOwner": echoTestSSOwner,
       "echoTestSSStatus": echoTestSSStatus,
       "echoTestPeriodicTable": echoTestPeriodicTable,
       "echoTestPeriodicEntry": echoTestPeriodicEntry,
       "echoTestPeriodicIndex": echoTestPeriodicIndex,
       "echoTestPeriodicIfIndex": echoTestPeriodicIfIndex,
       "echoTestPeriodicMacAddress": echoTestPeriodicMacAddress,
       "echoTestPeriodicNetAddress": echoTestPeriodicNetAddress,
       "echoTestPeriodicProtocol": echoTestPeriodicProtocol,
       "echoTestPeriodicTimeout": echoTestPeriodicTimeout,
       "echoTestPeriodicRetryAttempts": echoTestPeriodicRetryAttempts,
       "echoTestPeriodicNoResponseEventIndex": echoTestPeriodicNoResponseEventIndex,
       "echoTestPeriodicRespondedEventIndex": echoTestPeriodicRespondedEventIndex,
       "echoTestPeriodicEchoState": echoTestPeriodicEchoState,
       "echoTestPeriodicLastEchoStatus": echoTestPeriodicLastEchoStatus,
       "echoTestPeriodicTotalOperations": echoTestPeriodicTotalOperations,
       "echoTestPeriodicSuccessfulOperations": echoTestPeriodicSuccessfulOperations,
       "echoTestPeriodicMinRespTime": echoTestPeriodicMinRespTime,
       "echoTestPeriodicMaxRespTime": echoTestPeriodicMaxRespTime,
       "echoTestPeriodicLastRespTime": echoTestPeriodicLastRespTime,
       "echoTestPeriodicTotalRespTime": echoTestPeriodicTotalRespTime,
       "echoTestPeriodicOwner": echoTestPeriodicOwner,
       "echoTestPeriodicStatus": echoTestPeriodicStatus,
       "echoTestPeriodicSumOfSquaresTimeLo": echoTestPeriodicSumOfSquaresTimeLo,
       "echoTestPeriodicSumOfSquaresTimeHi": echoTestPeriodicSumOfSquaresTimeHi,
       "echoTestPeriodicFailedAttemptCount": echoTestPeriodicFailedAttemptCount,
       "echoTestPeriodicMinRespTime30MinInt": echoTestPeriodicMinRespTime30MinInt,
       "echoTestPeriodicMaxRespTime30MinInt": echoTestPeriodicMaxRespTime30MinInt,
       "echoTestPeriodicMinRespTime5MinInt": echoTestPeriodicMinRespTime5MinInt,
       "echoTestPeriodicMaxRespTime5MinInt": echoTestPeriodicMaxRespTime5MinInt,
       "echoTestPeriod": echoTestPeriod,
       "echoTestPeriodicCount": echoTestPeriodicCount,
       "echoTestResetSSTable": echoTestResetSSTable,
       "echoTestResetPeriodicTable": echoTestResetPeriodicTable,
       "echoTestPeriodicTableLastEdit": echoTestPeriodicTableLastEdit,
       "echoTestPeriodicTableStatus": echoTestPeriodicTableStatus,
       "echoTestNovellDefaultGateway": echoTestNovellDefaultGateway,
       "cable": cable,
       "nodeLocatorII": nodeLocatorII,
       "lp1": lp1,
       "lpEther": lpEther,
       "lp2EtherV1": lp2EtherV1,
       "lp2EtherV2": lp2EtherV2,
       "lp3Ether": lp3Ether,
       "pview": pview,
       "lp2TokenRing": lp2TokenRing,
       "lp2TokenRingV2": lp2TokenRingV2,
       "lpFDDI": lpFDDI,
       "lpFDDIV1": lpFDDIV1,
       "lpFDDIV2": lpFDDIV2,
       "lpQ": lpQ,
       "lpQuadEther": lpQuadEther,
       "lpQuadEtherV1": lpQuadEtherV1,
       "lpFE": lpFE,
       "lpFastEther": lpFastEther,
       "lpFastEtherV1": lpFastEtherV1,
       "lpMultiport": lpMultiport,
       "lpMultiportTokenRing": lpMultiportTokenRing,
       "lpMultiportTokenRingV1": lpMultiportTokenRingV1,
       "lpMultiportEther": lpMultiportEther,
       "lpMultiportEtherV1": lpMultiportEtherV1,
       "lpT1": lpT1,
       "lpT1Multiport": lpT1Multiport,
       "lpT1MultiportV1": lpT1MultiportV1,
       "lpE1": lpE1,
       "lpE1Multiport": lpE1Multiport,
       "lpE1MultiportV1": lpE1MultiportV1,
       "lpVSeries": lpVSeries,
       "lpVSeriesMultiport": lpVSeriesMultiport,
       "lpVSeriesMultiportV1": lpVSeriesMultiportV1,
       "lpHSSerial": lpHSSerial,
       "lpHSSI": lpHSSI,
       "lpHSSIV1": lpHSSIV1,
       "lpT3": lpT3,
       "lpT3Multiport": lpT3Multiport,
       "lpT3MultiportV1": lpT3MultiportV1,
       "lpATMUTP": lpATMUTP,
       "lpATMUTPMultiport": lpATMUTPMultiport,
       "lpATMUTPMultiportV1": lpATMUTPMultiportV1,
       "lpATMOC3": lpATMOC3,
       "lpATMOC3Multiport": lpATMOC3Multiport,
       "lpATMOC3MultiportV1": lpATMOC3MultiportV1,
       "lpATMT3": lpATMT3,
       "lpATMT3Multiport": lpATMT3Multiport,
       "lpATMT3MultiportV1": lpATMT3MultiportV1,
       "lpATME3": lpATME3,
       "lpATME3Multiport": lpATME3Multiport,
       "lpATME3MultiportV1": lpATME3MultiportV1,
       "lpATMOC12": lpATMOC12,
       "lpATMOC12Multiport": lpATMOC12Multiport,
       "lpATMOC12MultiportV1": lpATMOC12MultiportV1,
       "lpATMGigabit": lpATMGigabit,
       "lpATMGigabitMultiport": lpATMGigabitMultiport,
       "lpATMGigabitMultiportV1": lpATMGigabitMultiportV1,
       "lpE3": lpE3,
       "lpE3Multiport": lpE3Multiport,
       "lpE3MultiportV1": lpE3MultiportV1,
       "interface": interface,
       "ethernet": ethernet,
       "serial": serial,
       "serialConfigTable": serialConfigTable,
       "serialConfigEntry": serialConfigEntry,
       "serialIfIndex": serialIfIndex,
       "serialIpAddress": serialIpAddress,
       "serialSubnetMask": serialSubnetMask,
       "serialMode": serialMode,
       "serialProtocol": serialProtocol,
       "serialSpeed": serialSpeed,
       "serialTimeout": serialTimeout,
       "serialModemInitString": serialModemInitString,
       "serialModemHangUpString": serialModemHangUpString,
       "serialModemConnectResp": serialModemConnectResp,
       "serialModemNoConnectResp": serialModemNoConnectResp,
       "serialFlowControl": serialFlowControl,
       "serialTrapTimeout": serialTrapTimeout,
       "net": net,
       "netConfigTable": netConfigTable,
       "netConfigEntry": netConfigEntry,
       "netConfigIfIndex": netConfigIfIndex,
       "netConfigIfSpeed": netConfigIfSpeed,
       "netConfigIPAddress": netConfigIPAddress,
       "netConfigSubnetMask": netConfigSubnetMask,
       "netConfigRingNumber": netConfigRingNumber,
       "netConfigPortType": netConfigPortType,
       "netConfigDefaultGateway": netConfigDefaultGateway,
       "netConfigPhysicalConnector": netConfigPhysicalConnector,
       "netConfigLinkSpeed": netConfigLinkSpeed,
       "netConfigDuplex": netConfigDuplex,
       "netConfigLineCode": netConfigLineCode,
       "netConfigFramingType": netConfigFramingType,
       "netConfigChannelRate": netConfigChannelRate,
       "netConfigDataChannel": netConfigDataChannel,
       "netConfigDataSense": netConfigDataSense,
       "netConfigLinkLayerType": netConfigLinkLayerType,
       "netConfigNetworkInterface": netConfigNetworkInterface,
       "netConfigCellSynchronization": netConfigCellSynchronization,
       "netConfigReceiverMode": netConfigReceiverMode,
       "netConfigMaximumFrameSize": netConfigMaximumFrameSize,
       "netDefaultGateway": netDefaultGateway,
       "tokenRing": tokenRing,
       "tokenRingSpeed": tokenRingSpeed,
       "snmp": snmp,
       "trap": trap,
       "delivery": delivery,
       "trapDestTable": trapDestTable,
       "trapDestEntry": trapDestEntry,
       "trapDestIndex": trapDestIndex,
       "trapDestCommunity": trapDestCommunity,
       "trapDestDeliveryType": trapDestDeliveryType,
       "trapDestPrimaryIpAddress": trapDestPrimaryIpAddress,
       "trapDestPrimaryIfIndex": trapDestPrimaryIfIndex,
       "trapDestOwner": trapDestOwner,
       "trapDestStatus": trapDestStatus,
       "community": community,
       "accessControl": accessControl,
       "commAccessTable": commAccessTable,
       "commAccessEntry": commAccessEntry,
       "commAccessIndex": commAccessIndex,
       "commAccessCommunity": commAccessCommunity,
       "commAccessLevel": commAccessLevel,
       "commAccessOwner": commAccessOwner,
       "commAccessStatus": commAccessStatus,
       "clientTable": clientTable,
       "clientEntry": clientEntry,
       "clientIndex": clientIndex,
       "clientIpAddress": clientIpAddress,
       "clientIpMask": clientIpMask,
       "clientCommunity": clientCommunity,
       "clientOwner": clientOwner,
       "clientStatus": clientStatus,
       "slip": slip,
       "serialConnectionTable": serialConnectionTable,
       "serialConnectionEntry": serialConnectionEntry,
       "serialConnectIndex": serialConnectIndex,
       "serialConnectDestIpAddress": serialConnectDestIpAddress,
       "serialConnectType": serialConnectType,
       "serialConnectDialString": serialConnectDialString,
       "serialConnectSwitchConnectSeq": serialConnectSwitchConnectSeq,
       "serialConnectSwitchDisconnectSeq": serialConnectSwitchDisconnectSeq,
       "serialConnectSwitchResetSeq": serialConnectSwitchResetSeq,
       "serialConnectOwner": serialConnectOwner,
       "serialConnectStatus": serialConnectStatus}
)
