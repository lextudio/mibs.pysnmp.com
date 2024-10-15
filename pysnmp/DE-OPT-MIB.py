# SNMP MIB module (DE-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DE-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:30 2024
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Codex_ObjectIdentity = ObjectIdentity
codex = _Codex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449)
)
_CdxProductSpecific_ObjectIdentity = ObjectIdentity
cdxProductSpecific = _CdxProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2)
)
_Cdx6500_ObjectIdentity = ObjectIdentity
cdx6500 = _Cdx6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1)
)
_Cdx6500Configuration_ObjectIdentity = ObjectIdentity
cdx6500Configuration = _Cdx6500Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2)
)
_Cdx6500CfgGeneralGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgGeneralGroup = _Cdx6500CfgGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2)
)
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatOtherStatsGroup_ObjectIdentity = ObjectIdentity
cdx6500StatOtherStatsGroup = _Cdx6500StatOtherStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2)
)
_Cdx6500StatEncryption_ObjectIdentity = ObjectIdentity
cdx6500StatEncryption = _Cdx6500StatEncryption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12)
)
_StatEncryptionGeneral_ObjectIdentity = ObjectIdentity
statEncryptionGeneral = _StatEncryptionGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 1)
)


class _DeDataEncryptionHardwareStatus_Type(Integer32):
    """Custom type deDataEncryptionHardwareStatus based on Integer32"""
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


_DeDataEncryptionHardwareStatus_Type.__name__ = "Integer32"
_DeDataEncryptionHardwareStatus_Object = MibScalar
deDataEncryptionHardwareStatus = _DeDataEncryptionHardwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 1, 1),
    _DeDataEncryptionHardwareStatus_Type()
)
deDataEncryptionHardwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deDataEncryptionHardwareStatus.setStatus("mandatory")


class _DeMaxChannelAvailable_Type(Integer32):
    """Custom type deMaxChannelAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 500),
    )


_DeMaxChannelAvailable_Type.__name__ = "Integer32"
_DeMaxChannelAvailable_Object = MibScalar
deMaxChannelAvailable = _DeMaxChannelAvailable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 1, 2),
    _DeMaxChannelAvailable_Type()
)
deMaxChannelAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deMaxChannelAvailable.setStatus("mandatory")


class _DeMaxChannelConfigured_Type(Integer32):
    """Custom type deMaxChannelConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_DeMaxChannelConfigured_Type.__name__ = "Integer32"
_DeMaxChannelConfigured_Object = MibScalar
deMaxChannelConfigured = _DeMaxChannelConfigured_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 1, 3),
    _DeMaxChannelConfigured_Type()
)
deMaxChannelConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deMaxChannelConfigured.setStatus("mandatory")


class _DeChannelsInUse_Type(Integer32):
    """Custom type deChannelsInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_DeChannelsInUse_Type.__name__ = "Integer32"
_DeChannelsInUse_Object = MibScalar
deChannelsInUse = _DeChannelsInUse_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 1, 4),
    _DeChannelsInUse_Type()
)
deChannelsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deChannelsInUse.setStatus("mandatory")


class _DeMaxSimultaneousChannelsUsed_Type(Integer32):
    """Custom type deMaxSimultaneousChannelsUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_DeMaxSimultaneousChannelsUsed_Type.__name__ = "Integer32"
_DeMaxSimultaneousChannelsUsed_Object = MibScalar
deMaxSimultaneousChannelsUsed = _DeMaxSimultaneousChannelsUsed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 1, 5),
    _DeMaxSimultaneousChannelsUsed_Type()
)
deMaxSimultaneousChannelsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deMaxSimultaneousChannelsUsed.setStatus("mandatory")


class _DeCurrentEncryptionQueueLength_Type(Integer32):
    """Custom type deCurrentEncryptionQueueLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DeCurrentEncryptionQueueLength_Type.__name__ = "Integer32"
_DeCurrentEncryptionQueueLength_Object = MibScalar
deCurrentEncryptionQueueLength = _DeCurrentEncryptionQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 1, 6),
    _DeCurrentEncryptionQueueLength_Type()
)
deCurrentEncryptionQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deCurrentEncryptionQueueLength.setStatus("mandatory")


class _DeMaxEncryptionQueueDepth_Type(Integer32):
    """Custom type deMaxEncryptionQueueDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DeMaxEncryptionQueueDepth_Type.__name__ = "Integer32"
_DeMaxEncryptionQueueDepth_Object = MibScalar
deMaxEncryptionQueueDepth = _DeMaxEncryptionQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 1, 7),
    _DeMaxEncryptionQueueDepth_Type()
)
deMaxEncryptionQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deMaxEncryptionQueueDepth.setStatus("mandatory")
_DeTimeLastStatisticsReset_Type = DisplayString
_DeTimeLastStatisticsReset_Object = MibScalar
deTimeLastStatisticsReset = _DeTimeLastStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 1, 8),
    _DeTimeLastStatisticsReset_Type()
)
deTimeLastStatisticsReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deTimeLastStatisticsReset.setStatus("mandatory")


class _DeAlgorithmSupportedByHardwareStatus_Type(Integer32):
    """Custom type deAlgorithmSupportedByHardwareStatus based on Integer32"""
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
        *(("des-128", 4),
          ("des-40", 2),
          ("des-64", 3),
          ("no-simm", 1))
    )


_DeAlgorithmSupportedByHardwareStatus_Type.__name__ = "Integer32"
_DeAlgorithmSupportedByHardwareStatus_Object = MibScalar
deAlgorithmSupportedByHardwareStatus = _DeAlgorithmSupportedByHardwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 1, 9),
    _DeAlgorithmSupportedByHardwareStatus_Type()
)
deAlgorithmSupportedByHardwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deAlgorithmSupportedByHardwareStatus.setStatus("mandatory")
_StatEncryptionChannelTable_Object = MibTable
statEncryptionChannelTable = _StatEncryptionChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 2)
)
if mibBuilder.loadTexts:
    statEncryptionChannelTable.setStatus("mandatory")
_StatEncryptionChannelEntry_Object = MibTableRow
statEncryptionChannelEntry = _StatEncryptionChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 2, 1)
)
statEncryptionChannelEntry.setIndexNames(
    (0, "DE-OPT-MIB", "deStatChannelNumber"),
)
if mibBuilder.loadTexts:
    statEncryptionChannelEntry.setStatus("mandatory")
_DeStatChannelNumber_Type = Integer32
_DeStatChannelNumber_Object = MibTableColumn
deStatChannelNumber = _DeStatChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 2, 1, 1),
    _DeStatChannelNumber_Type()
)
deStatChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deStatChannelNumber.setStatus("mandatory")
_DeLastStatisticsReset_Type = DisplayString
_DeLastStatisticsReset_Object = MibTableColumn
deLastStatisticsReset = _DeLastStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 2, 1, 2),
    _DeLastStatisticsReset_Type()
)
deLastStatisticsReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deLastStatisticsReset.setStatus("mandatory")


class _DeChannelState_Type(Integer32):
    """Custom type deChannelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 2),
          ("nonData", 1))
    )


_DeChannelState_Type.__name__ = "Integer32"
_DeChannelState_Object = MibTableColumn
deChannelState = _DeChannelState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 2, 1, 3),
    _DeChannelState_Type()
)
deChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deChannelState.setStatus("mandatory")
_DeSourceChannel_Type = DisplayString
_DeSourceChannel_Object = MibTableColumn
deSourceChannel = _DeSourceChannel_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 2, 1, 4),
    _DeSourceChannel_Type()
)
deSourceChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deSourceChannel.setStatus("mandatory")
_DeDestinationChannel_Type = DisplayString
_DeDestinationChannel_Object = MibTableColumn
deDestinationChannel = _DeDestinationChannel_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 2, 1, 5),
    _DeDestinationChannel_Type()
)
deDestinationChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deDestinationChannel.setStatus("mandatory")
_DeCorruptedPackets_Type = Integer32
_DeCorruptedPackets_Object = MibTableColumn
deCorruptedPackets = _DeCorruptedPackets_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 2, 1, 6),
    _DeCorruptedPackets_Type()
)
deCorruptedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deCorruptedPackets.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)
_Cdx6500ControlsEncryption_ObjectIdentity = ObjectIdentity
cdx6500ControlsEncryption = _Cdx6500ControlsEncryption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 18)
)
_CtrlEncryptionGeneral_ObjectIdentity = ObjectIdentity
ctrlEncryptionGeneral = _CtrlEncryptionGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 18, 1)
)


class _DeCtrlEncryptionGeneral_Type(Integer32):
    """Custom type deCtrlEncryptionGeneral based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetStatistics", 1)
    )


_DeCtrlEncryptionGeneral_Type.__name__ = "Integer32"
_DeCtrlEncryptionGeneral_Object = MibScalar
deCtrlEncryptionGeneral = _DeCtrlEncryptionGeneral_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 18, 1, 1),
    _DeCtrlEncryptionGeneral_Type()
)
deCtrlEncryptionGeneral.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    deCtrlEncryptionGeneral.setStatus("mandatory")
_CtrlEncryptionChannelTable_Object = MibTable
ctrlEncryptionChannelTable = _CtrlEncryptionChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 18, 2)
)
if mibBuilder.loadTexts:
    ctrlEncryptionChannelTable.setStatus("mandatory")
_CtrlEncryptionChannelEntry_Object = MibTableRow
ctrlEncryptionChannelEntry = _CtrlEncryptionChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 18, 2, 1)
)
ctrlEncryptionChannelEntry.setIndexNames(
    (0, "DE-OPT-MIB", "deCtrlChannelNumber"),
)
if mibBuilder.loadTexts:
    ctrlEncryptionChannelEntry.setStatus("mandatory")
_DeCtrlChannelNumber_Type = Integer32
_DeCtrlChannelNumber_Object = MibTableColumn
deCtrlChannelNumber = _DeCtrlChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 18, 2, 1, 1),
    _DeCtrlChannelNumber_Type()
)
deCtrlChannelNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    deCtrlChannelNumber.setStatus("mandatory")


class _DeCtrlEncryptionChannel_Type(Integer32):
    """Custom type deCtrlEncryptionChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetStatistics", 1)
    )


_DeCtrlEncryptionChannel_Type.__name__ = "Integer32"
_DeCtrlEncryptionChannel_Object = MibTableColumn
deCtrlEncryptionChannel = _DeCtrlEncryptionChannel_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 18, 2, 1, 2),
    _DeCtrlEncryptionChannel_Type()
)
deCtrlEncryptionChannel.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    deCtrlEncryptionChannel.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DE-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgGeneralGroup": cdx6500CfgGeneralGroup,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatOtherStatsGroup": cdx6500StatOtherStatsGroup,
       "cdx6500StatEncryption": cdx6500StatEncryption,
       "statEncryptionGeneral": statEncryptionGeneral,
       "deDataEncryptionHardwareStatus": deDataEncryptionHardwareStatus,
       "deMaxChannelAvailable": deMaxChannelAvailable,
       "deMaxChannelConfigured": deMaxChannelConfigured,
       "deChannelsInUse": deChannelsInUse,
       "deMaxSimultaneousChannelsUsed": deMaxSimultaneousChannelsUsed,
       "deCurrentEncryptionQueueLength": deCurrentEncryptionQueueLength,
       "deMaxEncryptionQueueDepth": deMaxEncryptionQueueDepth,
       "deTimeLastStatisticsReset": deTimeLastStatisticsReset,
       "deAlgorithmSupportedByHardwareStatus": deAlgorithmSupportedByHardwareStatus,
       "statEncryptionChannelTable": statEncryptionChannelTable,
       "statEncryptionChannelEntry": statEncryptionChannelEntry,
       "deStatChannelNumber": deStatChannelNumber,
       "deLastStatisticsReset": deLastStatisticsReset,
       "deChannelState": deChannelState,
       "deSourceChannel": deSourceChannel,
       "deDestinationChannel": deDestinationChannel,
       "deCorruptedPackets": deCorruptedPackets,
       "cdx6500Controls": cdx6500Controls,
       "cdx6500ControlsEncryption": cdx6500ControlsEncryption,
       "ctrlEncryptionGeneral": ctrlEncryptionGeneral,
       "deCtrlEncryptionGeneral": deCtrlEncryptionGeneral,
       "ctrlEncryptionChannelTable": ctrlEncryptionChannelTable,
       "ctrlEncryptionChannelEntry": ctrlEncryptionChannelEntry,
       "deCtrlChannelNumber": deCtrlChannelNumber,
       "deCtrlEncryptionChannel": deCtrlEncryptionChannel}
)
