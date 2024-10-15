# SNMP MIB module (H320MCU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H320MCU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:39 2024
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

(MmGlobalIdentifier,
 mmH320Root) = mibBuilder.importSymbols(
    "MULTI-MEDIA-MIB-TC",
    "MmGlobalIdentifier",
    "mmH320Root")

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

h320Mcu = ModuleIdentity(
    (0, 0, 8, 341, 1, 2, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H320McuSystem_ObjectIdentity = ObjectIdentity
h320McuSystem = _H320McuSystem_ObjectIdentity(
    (0, 0, 8, 341, 1, 2, 3, 1)
)
_H320McuSysDescr_Type = DisplayString
_H320McuSysDescr_Object = MibScalar
h320McuSysDescr = _H320McuSysDescr_Object(
    (0, 0, 8, 341, 1, 2, 3, 1, 1),
    _H320McuSysDescr_Type()
)
h320McuSysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuSysDescr.setStatus("current")


class _H320McuSysSoftwareVersion_Type(Integer32):
    """Custom type h320McuSysSoftwareVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H320McuSysSoftwareVersion_Type.__name__ = "Integer32"
_H320McuSysSoftwareVersion_Object = MibScalar
h320McuSysSoftwareVersion = _H320McuSysSoftwareVersion_Object(
    (0, 0, 8, 341, 1, 2, 3, 1, 2),
    _H320McuSysSoftwareVersion_Type()
)
h320McuSysSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuSysSoftwareVersion.setStatus("current")
_H320McuSysG728_Type = TruthValue
_H320McuSysG728_Object = MibScalar
h320McuSysG728 = _H320McuSysG728_Object(
    (0, 0, 8, 341, 1, 2, 3, 1, 3),
    _H320McuSysG728_Type()
)
h320McuSysG728.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuSysG728.setStatus("current")
_H320McuSysChairControl_Type = TruthValue
_H320McuSysChairControl_Object = MibScalar
h320McuSysChairControl = _H320McuSysChairControl_Object(
    (0, 0, 8, 341, 1, 2, 3, 1, 4),
    _H320McuSysChairControl_Type()
)
h320McuSysChairControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuSysChairControl.setStatus("current")
_H320McuSysConferencePassword_Type = TruthValue
_H320McuSysConferencePassword_Object = MibScalar
h320McuSysConferencePassword = _H320McuSysConferencePassword_Object(
    (0, 0, 8, 341, 1, 2, 3, 1, 5),
    _H320McuSysConferencePassword_Type()
)
h320McuSysConferencePassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuSysConferencePassword.setStatus("current")
_H320McuSysH243Cascading_Type = TruthValue
_H320McuSysH243Cascading_Object = MibScalar
h320McuSysH243Cascading = _H320McuSysH243Cascading_Object(
    (0, 0, 8, 341, 1, 2, 3, 1, 6),
    _H320McuSysH243Cascading_Type()
)
h320McuSysH243Cascading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuSysH243Cascading.setStatus("current")
_H320McuConference_ObjectIdentity = ObjectIdentity
h320McuConference = _H320McuConference_ObjectIdentity(
    (0, 0, 8, 341, 1, 2, 3, 2)
)
_H320McuConfStatusTable_Object = MibTable
h320McuConfStatusTable = _H320McuConfStatusTable_Object(
    (0, 0, 8, 341, 1, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    h320McuConfStatusTable.setStatus("current")
_H320McuConfStatusTableEntry_Object = MibTableRow
h320McuConfStatusTableEntry = _H320McuConfStatusTableEntry_Object(
    (0, 0, 8, 341, 1, 2, 3, 2, 1, 1)
)
h320McuConfStatusTableEntry.setIndexNames(
    (0, "H320MCU-MIB", "h320McuConfId"),
)
if mibBuilder.loadTexts:
    h320McuConfStatusTableEntry.setStatus("current")
_H320McuConfId_Type = MmGlobalIdentifier
_H320McuConfId_Object = MibTableColumn
h320McuConfId = _H320McuConfId_Object(
    (0, 0, 8, 341, 1, 2, 3, 2, 1, 1, 1),
    _H320McuConfId_Type()
)
h320McuConfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h320McuConfId.setStatus("current")


class _H320McuConfName_Type(OctetString):
    """Custom type h320McuConfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_H320McuConfName_Type.__name__ = "OctetString"
_H320McuConfName_Object = MibTableColumn
h320McuConfName = _H320McuConfName_Object(
    (0, 0, 8, 341, 1, 2, 3, 2, 1, 1, 2),
    _H320McuConfName_Type()
)
h320McuConfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuConfName.setStatus("current")
_H320McuConfVideoSrc_Type = TruthValue
_H320McuConfVideoSrc_Object = MibTableColumn
h320McuConfVideoSrc = _H320McuConfVideoSrc_Object(
    (0, 0, 8, 341, 1, 2, 3, 2, 1, 1, 3),
    _H320McuConfVideoSrc_Type()
)
h320McuConfVideoSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuConfVideoSrc.setStatus("current")
_H320McuConfLsdSrc_Type = TruthValue
_H320McuConfLsdSrc_Object = MibTableColumn
h320McuConfLsdSrc = _H320McuConfLsdSrc_Object(
    (0, 0, 8, 341, 1, 2, 3, 2, 1, 1, 4),
    _H320McuConfLsdSrc_Type()
)
h320McuConfLsdSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuConfLsdSrc.setStatus("current")


class _H320McuConfHsdSrc_Type(TruthValue):
    """Custom type h320McuConfHsdSrc based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H320McuConfHsdSrc_Type.__name__ = "TruthValue"
_H320McuConfHsdSrc_Object = MibTableColumn
h320McuConfHsdSrc = _H320McuConfHsdSrc_Object(
    (0, 0, 8, 341, 1, 2, 3, 2, 1, 1, 5),
    _H320McuConfHsdSrc_Type()
)
h320McuConfHsdSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuConfHsdSrc.setStatus("current")
_H320McuConfConferenceChair_Type = TruthValue
_H320McuConfConferenceChair_Object = MibTableColumn
h320McuConfConferenceChair = _H320McuConfConferenceChair_Object(
    (0, 0, 8, 341, 1, 2, 3, 2, 1, 1, 6),
    _H320McuConfConferenceChair_Type()
)
h320McuConfConferenceChair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuConfConferenceChair.setStatus("current")
_H320McuConfHsdChannelOpen_Type = TruthValue
_H320McuConfHsdChannelOpen_Object = MibTableColumn
h320McuConfHsdChannelOpen = _H320McuConfHsdChannelOpen_Object(
    (0, 0, 8, 341, 1, 2, 3, 2, 1, 1, 7),
    _H320McuConfHsdChannelOpen_Type()
)
h320McuConfHsdChannelOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuConfHsdChannelOpen.setStatus("current")
_H320McuConfLsdChannelOpen_Type = TruthValue
_H320McuConfLsdChannelOpen_Object = MibTableColumn
h320McuConfLsdChannelOpen = _H320McuConfLsdChannelOpen_Object(
    (0, 0, 8, 341, 1, 2, 3, 2, 1, 1, 8),
    _H320McuConfLsdChannelOpen_Type()
)
h320McuConfLsdChannelOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuConfLsdChannelOpen.setStatus("current")
_H320McuConfVideoMode_Type = TruthValue
_H320McuConfVideoMode_Object = MibTableColumn
h320McuConfVideoMode = _H320McuConfVideoMode_Object(
    (0, 0, 8, 341, 1, 2, 3, 2, 1, 1, 9),
    _H320McuConfVideoMode_Type()
)
h320McuConfVideoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuConfVideoMode.setStatus("current")
_H320McuConfSelectedCaps_Type = DisplayString
_H320McuConfSelectedCaps_Object = MibTableColumn
h320McuConfSelectedCaps = _H320McuConfSelectedCaps_Object(
    (0, 0, 8, 341, 1, 2, 3, 2, 1, 1, 10),
    _H320McuConfSelectedCaps_Type()
)
h320McuConfSelectedCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuConfSelectedCaps.setStatus("current")


class _H320McuConfTransferRate_Type(Integer32):
    """Custom type h320McuConfTransferRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H320McuConfTransferRate_Type.__name__ = "Integer32"
_H320McuConfTransferRate_Object = MibTableColumn
h320McuConfTransferRate = _H320McuConfTransferRate_Object(
    (0, 0, 8, 341, 1, 2, 3, 2, 1, 1, 11),
    _H320McuConfTransferRate_Type()
)
h320McuConfTransferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuConfTransferRate.setStatus("current")


class _H320McuConfNetworkSpeed_Type(Integer32):
    """Custom type h320McuConfNetworkSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restricted", 1),
          ("unrestricted", 2))
    )


_H320McuConfNetworkSpeed_Type.__name__ = "Integer32"
_H320McuConfNetworkSpeed_Object = MibTableColumn
h320McuConfNetworkSpeed = _H320McuConfNetworkSpeed_Object(
    (0, 0, 8, 341, 1, 2, 3, 2, 1, 1, 12),
    _H320McuConfNetworkSpeed_Type()
)
h320McuConfNetworkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuConfNetworkSpeed.setStatus("current")
_H320McuTerminal_ObjectIdentity = ObjectIdentity
h320McuTerminal = _H320McuTerminal_ObjectIdentity(
    (0, 0, 8, 341, 1, 2, 3, 3)
)
_H320McuTerminalStatusTable_Object = MibTable
h320McuTerminalStatusTable = _H320McuTerminalStatusTable_Object(
    (0, 0, 8, 341, 1, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    h320McuTerminalStatusTable.setStatus("current")
_H320McuTerminalStatusTableEntry_Object = MibTableRow
h320McuTerminalStatusTableEntry = _H320McuTerminalStatusTableEntry_Object(
    (0, 0, 8, 341, 1, 2, 3, 3, 1, 1)
)
h320McuTerminalStatusTableEntry.setIndexNames(
    (0, "H320MCU-MIB", "h320McuTerminalId"),
)
if mibBuilder.loadTexts:
    h320McuTerminalStatusTableEntry.setStatus("current")
_H320McuTerminalId_Type = Integer32
_H320McuTerminalId_Object = MibTableColumn
h320McuTerminalId = _H320McuTerminalId_Object(
    (0, 0, 8, 341, 1, 2, 3, 3, 1, 1, 1),
    _H320McuTerminalId_Type()
)
h320McuTerminalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h320McuTerminalId.setStatus("current")
_H320McuTerminalConfId_Type = MmGlobalIdentifier
_H320McuTerminalConfId_Object = MibTableColumn
h320McuTerminalConfId = _H320McuTerminalConfId_Object(
    (0, 0, 8, 341, 1, 2, 3, 3, 1, 1, 2),
    _H320McuTerminalConfId_Type()
)
h320McuTerminalConfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuTerminalConfId.setStatus("current")


class _H320McuTerminalConfName_Type(OctetString):
    """Custom type h320McuTerminalConfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_H320McuTerminalConfName_Type.__name__ = "OctetString"
_H320McuTerminalConfName_Object = MibTableColumn
h320McuTerminalConfName = _H320McuTerminalConfName_Object(
    (0, 0, 8, 341, 1, 2, 3, 3, 1, 1, 3),
    _H320McuTerminalConfName_Type()
)
h320McuTerminalConfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuTerminalConfName.setStatus("current")
_H320McuTerminalAudioFrom_Type = TruthValue
_H320McuTerminalAudioFrom_Object = MibTableColumn
h320McuTerminalAudioFrom = _H320McuTerminalAudioFrom_Object(
    (0, 0, 8, 341, 1, 2, 3, 3, 1, 1, 4),
    _H320McuTerminalAudioFrom_Type()
)
h320McuTerminalAudioFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuTerminalAudioFrom.setStatus("current")
_H320McuTerminalVideoFrom_Type = TruthValue
_H320McuTerminalVideoFrom_Object = MibTableColumn
h320McuTerminalVideoFrom = _H320McuTerminalVideoFrom_Object(
    (0, 0, 8, 341, 1, 2, 3, 3, 1, 1, 5),
    _H320McuTerminalVideoFrom_Type()
)
h320McuTerminalVideoFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuTerminalVideoFrom.setStatus("current")


class _H320McuTerminalLsdChannelStatus_Type(Integer32):
    """Custom type h320McuTerminalLsdChannelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("channelClosed", 2),
          ("channelOpen", 1))
    )


_H320McuTerminalLsdChannelStatus_Type.__name__ = "Integer32"
_H320McuTerminalLsdChannelStatus_Object = MibTableColumn
h320McuTerminalLsdChannelStatus = _H320McuTerminalLsdChannelStatus_Object(
    (0, 0, 8, 341, 1, 2, 3, 3, 1, 1, 6),
    _H320McuTerminalLsdChannelStatus_Type()
)
h320McuTerminalLsdChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuTerminalLsdChannelStatus.setStatus("current")


class _H320McuTerminalHsdChannelStatus_Type(Integer32):
    """Custom type h320McuTerminalHsdChannelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("channelClosed", 2),
          ("channelOpen", 1))
    )


_H320McuTerminalHsdChannelStatus_Type.__name__ = "Integer32"
_H320McuTerminalHsdChannelStatus_Object = MibTableColumn
h320McuTerminalHsdChannelStatus = _H320McuTerminalHsdChannelStatus_Object(
    (0, 0, 8, 341, 1, 2, 3, 3, 1, 1, 7),
    _H320McuTerminalHsdChannelStatus_Type()
)
h320McuTerminalHsdChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuTerminalHsdChannelStatus.setStatus("current")
_H320McuTerminalCapabilities_Type = DisplayString
_H320McuTerminalCapabilities_Object = MibTableColumn
h320McuTerminalCapabilities = _H320McuTerminalCapabilities_Object(
    (0, 0, 8, 341, 1, 2, 3, 3, 1, 1, 8),
    _H320McuTerminalCapabilities_Type()
)
h320McuTerminalCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuTerminalCapabilities.setStatus("current")


class _H320McuTerminalStatus_Type(Integer32):
    """Custom type h320McuTerminalStatus based on Integer32"""
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
        *(("connected", 3),
          ("connectionInprogress", 2),
          ("h320Framed", 4),
          ("notConnected", 1))
    )


_H320McuTerminalStatus_Type.__name__ = "Integer32"
_H320McuTerminalStatus_Object = MibTableColumn
h320McuTerminalStatus = _H320McuTerminalStatus_Object(
    (0, 0, 8, 341, 1, 2, 3, 3, 1, 1, 9),
    _H320McuTerminalStatus_Type()
)
h320McuTerminalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuTerminalStatus.setStatus("current")


class _H320McuTerminalPhoneNumber_Type(OctetString):
    """Custom type h320McuTerminalPhoneNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_H320McuTerminalPhoneNumber_Type.__name__ = "OctetString"
_H320McuTerminalPhoneNumber_Object = MibTableColumn
h320McuTerminalPhoneNumber = _H320McuTerminalPhoneNumber_Object(
    (0, 0, 8, 341, 1, 2, 3, 3, 1, 1, 10),
    _H320McuTerminalPhoneNumber_Type()
)
h320McuTerminalPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuTerminalPhoneNumber.setStatus("current")


class _H320McuTerminalMCUPhoneNumber_Type(OctetString):
    """Custom type h320McuTerminalMCUPhoneNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_H320McuTerminalMCUPhoneNumber_Type.__name__ = "OctetString"
_H320McuTerminalMCUPhoneNumber_Object = MibTableColumn
h320McuTerminalMCUPhoneNumber = _H320McuTerminalMCUPhoneNumber_Object(
    (0, 0, 8, 341, 1, 2, 3, 3, 1, 1, 11),
    _H320McuTerminalMCUPhoneNumber_Type()
)
h320McuTerminalMCUPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuTerminalMCUPhoneNumber.setStatus("current")
_H320McuTerminalStatsTable_Object = MibTable
h320McuTerminalStatsTable = _H320McuTerminalStatsTable_Object(
    (0, 0, 8, 341, 1, 2, 3, 3, 2)
)
if mibBuilder.loadTexts:
    h320McuTerminalStatsTable.setStatus("current")
_H320McuTerminalStatsTableEntry_Object = MibTableRow
h320McuTerminalStatsTableEntry = _H320McuTerminalStatsTableEntry_Object(
    (0, 0, 8, 341, 1, 2, 3, 3, 2, 1)
)
h320McuTerminalStatsTableEntry.setIndexNames(
    (0, "H320MCU-MIB", "h320McuTerminalId"),
)
if mibBuilder.loadTexts:
    h320McuTerminalStatsTableEntry.setStatus("current")
_H320McuTerminalStatsTerminalId_Type = Integer32
_H320McuTerminalStatsTerminalId_Object = MibTableColumn
h320McuTerminalStatsTerminalId = _H320McuTerminalStatsTerminalId_Object(
    (0, 0, 8, 341, 1, 2, 3, 3, 2, 1, 1),
    _H320McuTerminalStatsTerminalId_Type()
)
h320McuTerminalStatsTerminalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuTerminalStatsTerminalId.setStatus("current")
_H320McuTerminalStatsConfId_Type = MmGlobalIdentifier
_H320McuTerminalStatsConfId_Object = MibTableColumn
h320McuTerminalStatsConfId = _H320McuTerminalStatsConfId_Object(
    (0, 0, 8, 341, 1, 2, 3, 3, 2, 1, 2),
    _H320McuTerminalStatsConfId_Type()
)
h320McuTerminalStatsConfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuTerminalStatsConfId.setStatus("current")


class _H320McuTerminalStatsConfName_Type(OctetString):
    """Custom type h320McuTerminalStatsConfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_H320McuTerminalStatsConfName_Type.__name__ = "OctetString"
_H320McuTerminalStatsConfName_Object = MibTableColumn
h320McuTerminalStatsConfName = _H320McuTerminalStatsConfName_Object(
    (0, 0, 8, 341, 1, 2, 3, 3, 2, 1, 3),
    _H320McuTerminalStatsConfName_Type()
)
h320McuTerminalStatsConfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuTerminalStatsConfName.setStatus("current")
_H320McuTerminalStatsRxMultiframes_Type = Integer32
_H320McuTerminalStatsRxMultiframes_Object = MibTableColumn
h320McuTerminalStatsRxMultiframes = _H320McuTerminalStatsRxMultiframes_Object(
    (0, 0, 8, 341, 1, 2, 3, 3, 2, 1, 4),
    _H320McuTerminalStatsRxMultiframes_Type()
)
h320McuTerminalStatsRxMultiframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuTerminalStatsRxMultiframes.setStatus("current")
_H320McuTerminalStatsFALossAtTerminal_Type = Integer32
_H320McuTerminalStatsFALossAtTerminal_Object = MibTableColumn
h320McuTerminalStatsFALossAtTerminal = _H320McuTerminalStatsFALossAtTerminal_Object(
    (0, 0, 8, 341, 1, 2, 3, 3, 2, 1, 5),
    _H320McuTerminalStatsFALossAtTerminal_Type()
)
h320McuTerminalStatsFALossAtTerminal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuTerminalStatsFALossAtTerminal.setStatus("current")
_H320McuTerminalStatsMCUCrcErrors_Type = Counter32
_H320McuTerminalStatsMCUCrcErrors_Object = MibTableColumn
h320McuTerminalStatsMCUCrcErrors = _H320McuTerminalStatsMCUCrcErrors_Object(
    (0, 0, 8, 341, 1, 2, 3, 3, 2, 1, 6),
    _H320McuTerminalStatsMCUCrcErrors_Type()
)
h320McuTerminalStatsMCUCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuTerminalStatsMCUCrcErrors.setStatus("current")
_H320McuTerminalStatsTerminalCrcErrors_Type = Counter32
_H320McuTerminalStatsTerminalCrcErrors_Object = MibTableColumn
h320McuTerminalStatsTerminalCrcErrors = _H320McuTerminalStatsTerminalCrcErrors_Object(
    (0, 0, 8, 341, 1, 2, 3, 3, 2, 1, 7),
    _H320McuTerminalStatsTerminalCrcErrors_Type()
)
h320McuTerminalStatsTerminalCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuTerminalStatsTerminalCrcErrors.setStatus("current")
_H320McuTerminalStatsStatsRequests_Type = Counter32
_H320McuTerminalStatsStatsRequests_Object = MibTableColumn
h320McuTerminalStatsStatsRequests = _H320McuTerminalStatsStatsRequests_Object(
    (0, 0, 8, 341, 1, 2, 3, 3, 2, 1, 8),
    _H320McuTerminalStatsStatsRequests_Type()
)
h320McuTerminalStatsStatsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320McuTerminalStatsStatsRequests.setStatus("current")
_H320McuControls_ObjectIdentity = ObjectIdentity
h320McuControls = _H320McuControls_ObjectIdentity(
    (0, 0, 8, 341, 1, 2, 3, 4)
)


class _H320McuControlsCommands_Type(Integer32):
    """Custom type h320McuControlsCommands based on Integer32"""
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
        *(("abruptRestart", 2),
          ("abruptShutdown", 4),
          ("enterQuiescence", 6),
          ("exitQuiescence", 7),
          ("gracefulRestart", 3),
          ("gracefulShutdown", 5),
          ("other", 1),
          ("resetStatistics", 10),
          ("runDiagnostic", 11),
          ("startLog", 8),
          ("stopLog", 9))
    )


_H320McuControlsCommands_Type.__name__ = "Integer32"
_H320McuControlsCommands_Object = MibScalar
h320McuControlsCommands = _H320McuControlsCommands_Object(
    (0, 0, 8, 341, 1, 2, 3, 4, 1),
    _H320McuControlsCommands_Type()
)
h320McuControlsCommands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h320McuControlsCommands.setStatus("current")
_H320McuMIBConformance_ObjectIdentity = ObjectIdentity
h320McuMIBConformance = _H320McuMIBConformance_ObjectIdentity(
    (0, 0, 8, 341, 1, 2, 3, 5)
)
_H320McuMIBGroups_ObjectIdentity = ObjectIdentity
h320McuMIBGroups = _H320McuMIBGroups_ObjectIdentity(
    (0, 0, 8, 341, 1, 2, 3, 5, 1)
)

# Managed Objects groups

h320McuSystemGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 2, 3, 5, 1, 1)
)
h320McuSystemGroup.setObjects(
      *(("H320MCU-MIB", "h320McuSysDescr"),
        ("H320MCU-MIB", "h320McuSysSoftwareVersion"),
        ("H320MCU-MIB", "h320McuSysG728"),
        ("H320MCU-MIB", "h320McuSysChairControl"),
        ("H320MCU-MIB", "h320McuSysConferencePassword"),
        ("H320MCU-MIB", "h320McuSysH243Cascading"))
)
if mibBuilder.loadTexts:
    h320McuSystemGroup.setStatus("current")

h320McuConferenceGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 2, 3, 5, 1, 2)
)
h320McuConferenceGroup.setObjects(
      *(("H320MCU-MIB", "h320McuConfName"),
        ("H320MCU-MIB", "h320McuConfVideoSrc"),
        ("H320MCU-MIB", "h320McuConfLsdSrc"),
        ("H320MCU-MIB", "h320McuConfHsdSrc"),
        ("H320MCU-MIB", "h320McuConfConferenceChair"),
        ("H320MCU-MIB", "h320McuConfLsdChannelOpen"),
        ("H320MCU-MIB", "h320McuConfHsdChannelOpen"),
        ("H320MCU-MIB", "h320McuConfVideoMode"),
        ("H320MCU-MIB", "h320McuConfSelectedCaps"),
        ("H320MCU-MIB", "h320McuConfTransferRate"),
        ("H320MCU-MIB", "h320McuConfNetworkSpeed"))
)
if mibBuilder.loadTexts:
    h320McuConferenceGroup.setStatus("current")

h320McuTerminalGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 2, 3, 5, 1, 3)
)
h320McuTerminalGroup.setObjects(
      *(("H320MCU-MIB", "h320McuTerminalConfId"),
        ("H320MCU-MIB", "h320McuTerminalConfName"),
        ("H320MCU-MIB", "h320McuTerminalAudioFrom"),
        ("H320MCU-MIB", "h320McuTerminalVideoFrom"),
        ("H320MCU-MIB", "h320McuTerminalLsdChannelStatus"),
        ("H320MCU-MIB", "h320McuTerminalHsdChannelStatus"),
        ("H320MCU-MIB", "h320McuTerminalCapabilities"),
        ("H320MCU-MIB", "h320McuTerminalStatus"),
        ("H320MCU-MIB", "h320McuTerminalPhoneNumber"),
        ("H320MCU-MIB", "h320McuTerminalMCUPhoneNumber"),
        ("H320MCU-MIB", "h320McuTerminalStatsTerminalId"),
        ("H320MCU-MIB", "h320McuTerminalStatsConfId"),
        ("H320MCU-MIB", "h320McuTerminalStatsConfName"),
        ("H320MCU-MIB", "h320McuTerminalStatsRxMultiframes"),
        ("H320MCU-MIB", "h320McuTerminalStatsFALossAtTerminal"),
        ("H320MCU-MIB", "h320McuTerminalStatsMCUCrcErrors"),
        ("H320MCU-MIB", "h320McuTerminalStatsTerminalCrcErrors"),
        ("H320MCU-MIB", "h320McuTerminalStatsStatsRequests"))
)
if mibBuilder.loadTexts:
    h320McuTerminalGroup.setStatus("current")

h320McuControlsGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 2, 3, 5, 1, 4)
)
h320McuControlsGroup.setObjects(
    ("H320MCU-MIB", "h320McuControlsCommands")
)
if mibBuilder.loadTexts:
    h320McuControlsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

h320McuMIBCompliance = ModuleCompliance(
    (0, 0, 8, 341, 1, 2, 3, 5, 2)
)
if mibBuilder.loadTexts:
    h320McuMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H320MCU-MIB",
    **{"h320Mcu": h320Mcu,
       "h320McuSystem": h320McuSystem,
       "h320McuSysDescr": h320McuSysDescr,
       "h320McuSysSoftwareVersion": h320McuSysSoftwareVersion,
       "h320McuSysG728": h320McuSysG728,
       "h320McuSysChairControl": h320McuSysChairControl,
       "h320McuSysConferencePassword": h320McuSysConferencePassword,
       "h320McuSysH243Cascading": h320McuSysH243Cascading,
       "h320McuConference": h320McuConference,
       "h320McuConfStatusTable": h320McuConfStatusTable,
       "h320McuConfStatusTableEntry": h320McuConfStatusTableEntry,
       "h320McuConfId": h320McuConfId,
       "h320McuConfName": h320McuConfName,
       "h320McuConfVideoSrc": h320McuConfVideoSrc,
       "h320McuConfLsdSrc": h320McuConfLsdSrc,
       "h320McuConfHsdSrc": h320McuConfHsdSrc,
       "h320McuConfConferenceChair": h320McuConfConferenceChair,
       "h320McuConfHsdChannelOpen": h320McuConfHsdChannelOpen,
       "h320McuConfLsdChannelOpen": h320McuConfLsdChannelOpen,
       "h320McuConfVideoMode": h320McuConfVideoMode,
       "h320McuConfSelectedCaps": h320McuConfSelectedCaps,
       "h320McuConfTransferRate": h320McuConfTransferRate,
       "h320McuConfNetworkSpeed": h320McuConfNetworkSpeed,
       "h320McuTerminal": h320McuTerminal,
       "h320McuTerminalStatusTable": h320McuTerminalStatusTable,
       "h320McuTerminalStatusTableEntry": h320McuTerminalStatusTableEntry,
       "h320McuTerminalId": h320McuTerminalId,
       "h320McuTerminalConfId": h320McuTerminalConfId,
       "h320McuTerminalConfName": h320McuTerminalConfName,
       "h320McuTerminalAudioFrom": h320McuTerminalAudioFrom,
       "h320McuTerminalVideoFrom": h320McuTerminalVideoFrom,
       "h320McuTerminalLsdChannelStatus": h320McuTerminalLsdChannelStatus,
       "h320McuTerminalHsdChannelStatus": h320McuTerminalHsdChannelStatus,
       "h320McuTerminalCapabilities": h320McuTerminalCapabilities,
       "h320McuTerminalStatus": h320McuTerminalStatus,
       "h320McuTerminalPhoneNumber": h320McuTerminalPhoneNumber,
       "h320McuTerminalMCUPhoneNumber": h320McuTerminalMCUPhoneNumber,
       "h320McuTerminalStatsTable": h320McuTerminalStatsTable,
       "h320McuTerminalStatsTableEntry": h320McuTerminalStatsTableEntry,
       "h320McuTerminalStatsTerminalId": h320McuTerminalStatsTerminalId,
       "h320McuTerminalStatsConfId": h320McuTerminalStatsConfId,
       "h320McuTerminalStatsConfName": h320McuTerminalStatsConfName,
       "h320McuTerminalStatsRxMultiframes": h320McuTerminalStatsRxMultiframes,
       "h320McuTerminalStatsFALossAtTerminal": h320McuTerminalStatsFALossAtTerminal,
       "h320McuTerminalStatsMCUCrcErrors": h320McuTerminalStatsMCUCrcErrors,
       "h320McuTerminalStatsTerminalCrcErrors": h320McuTerminalStatsTerminalCrcErrors,
       "h320McuTerminalStatsStatsRequests": h320McuTerminalStatsStatsRequests,
       "h320McuControls": h320McuControls,
       "h320McuControlsCommands": h320McuControlsCommands,
       "h320McuMIBConformance": h320McuMIBConformance,
       "h320McuMIBGroups": h320McuMIBGroups,
       "h320McuSystemGroup": h320McuSystemGroup,
       "h320McuConferenceGroup": h320McuConferenceGroup,
       "h320McuTerminalGroup": h320McuTerminalGroup,
       "h320McuControlsGroup": h320McuControlsGroup,
       "h320McuMIBCompliance": h320McuMIBCompliance}
)
