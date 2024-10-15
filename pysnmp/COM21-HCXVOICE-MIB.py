# SNMP MIB module (COM21-HCXVOICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COM21-HCXVOICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:40 2024
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

(com21,
 com21Hcx) = mibBuilder.importSymbols(
    "COM21-HCX-MIB",
    "com21",
    "com21Hcx")

(hcxAlmSeverity,
 hcxEventLogTime) = mibBuilder.importSymbols(
    "COM21-HCXALM-MIB",
    "hcxAlmSeverity",
    "hcxEventLogTime")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

com21HcxVoice = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 100)
)


# Types definitions



class PrimServiceState(Integer32):
    """Custom type PrimServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("is", 1),
          ("oos", 2))
    )





class Com21RowStatus(Integer32):
    """Custom type Com21RowStatus based on Integer32"""
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
        *(("active", 1),
          ("create", 2),
          ("deactive", 4),
          ("destroy", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Com21HcxVoiceGroup_ObjectIdentity = ObjectIdentity
com21HcxVoiceGroup = _Com21HcxVoiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 101)
)
_HcxConfiguredVoiceChannels_Type = Integer32
_HcxConfiguredVoiceChannels_Object = MibScalar
hcxConfiguredVoiceChannels = _HcxConfiguredVoiceChannels_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 101, 1),
    _HcxConfiguredVoiceChannels_Type()
)
hcxConfiguredVoiceChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxConfiguredVoiceChannels.setStatus("current")
_HcxActiveVoiceChannels_Type = Integer32
_HcxActiveVoiceChannels_Object = MibScalar
hcxActiveVoiceChannels = _HcxActiveVoiceChannels_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 101, 2),
    _HcxActiveVoiceChannels_Type()
)
hcxActiveVoiceChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxActiveVoiceChannels.setStatus("current")


class _HcxVoiceChannelMode_Type(Integer32):
    """Custom type hcxVoiceChannelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aLaw", 1),
          ("muLaw", 2))
    )


_HcxVoiceChannelMode_Type.__name__ = "Integer32"
_HcxVoiceChannelMode_Object = MibScalar
hcxVoiceChannelMode = _HcxVoiceChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 101, 3),
    _HcxVoiceChannelMode_Type()
)
hcxVoiceChannelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVoiceChannelMode.setStatus("current")


class _HcxVoiceOAMEnable_Type(Integer32):
    """Custom type hcxVoiceOAMEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HcxVoiceOAMEnable_Type.__name__ = "Integer32"
_HcxVoiceOAMEnable_Object = MibScalar
hcxVoiceOAMEnable = _HcxVoiceOAMEnable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 101, 4),
    _HcxVoiceOAMEnable_Type()
)
hcxVoiceOAMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVoiceOAMEnable.setStatus("current")


class _HcxVoiceFEndEchoCancEnable_Type(Integer32):
    """Custom type hcxVoiceFEndEchoCancEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HcxVoiceFEndEchoCancEnable_Type.__name__ = "Integer32"
_HcxVoiceFEndEchoCancEnable_Object = MibScalar
hcxVoiceFEndEchoCancEnable = _HcxVoiceFEndEchoCancEnable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 101, 5),
    _HcxVoiceFEndEchoCancEnable_Type()
)
hcxVoiceFEndEchoCancEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVoiceFEndEchoCancEnable.setStatus("current")
_HcxVoiceRTTDelay_Type = Integer32
_HcxVoiceRTTDelay_Object = MibScalar
hcxVoiceRTTDelay = _HcxVoiceRTTDelay_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 101, 6),
    _HcxVoiceRTTDelay_Type()
)
hcxVoiceRTTDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVoiceRTTDelay.setStatus("current")
_Com21HcxVpnRxGroup_ObjectIdentity = ObjectIdentity
com21HcxVpnRxGroup = _Com21HcxVpnRxGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 102)
)
_Com21HcxVpnRxTable_Object = MibTable
com21HcxVpnRxTable = _Com21HcxVpnRxTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 102, 1)
)
if mibBuilder.loadTexts:
    com21HcxVpnRxTable.setStatus("current")
_Com21HcxVpnRxEntry_Object = MibTableRow
com21HcxVpnRxEntry = _Com21HcxVpnRxEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 102, 1, 1)
)
com21HcxVpnRxEntry.setIndexNames(
    (0, "COM21-HCXVOICE-MIB", "hcxVpnRxNum"),
    (0, "COM21-HCXVOICE-MIB", "hcxVpnRxEntryId"),
)
if mibBuilder.loadTexts:
    com21HcxVpnRxEntry.setStatus("current")
_HcxVpnRxNum_Type = Integer32
_HcxVpnRxNum_Object = MibTableColumn
hcxVpnRxNum = _HcxVpnRxNum_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 102, 1, 1, 1),
    _HcxVpnRxNum_Type()
)
hcxVpnRxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVpnRxNum.setStatus("current")
_HcxVpnRxEntryId_Type = Integer32
_HcxVpnRxEntryId_Object = MibTableColumn
hcxVpnRxEntryId = _HcxVpnRxEntryId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 102, 1, 1, 2),
    _HcxVpnRxEntryId_Type()
)
hcxVpnRxEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVpnRxEntryId.setStatus("current")
_HcxVpnRxRowStatus_Type = Com21RowStatus
_HcxVpnRxRowStatus_Object = MibTableColumn
hcxVpnRxRowStatus = _HcxVpnRxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 102, 1, 1, 3),
    _HcxVpnRxRowStatus_Type()
)
hcxVpnRxRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcxVpnRxRowStatus.setStatus("current")
_HcxVpnRxMaxActiveCalls_Type = Integer32
_HcxVpnRxMaxActiveCalls_Object = MibTableColumn
hcxVpnRxMaxActiveCalls = _HcxVpnRxMaxActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 102, 1, 1, 4),
    _HcxVpnRxMaxActiveCalls_Type()
)
hcxVpnRxMaxActiveCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVpnRxMaxActiveCalls.setStatus("current")
_Com21HcxVpnRxStatsGroup_ObjectIdentity = ObjectIdentity
com21HcxVpnRxStatsGroup = _Com21HcxVpnRxStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 103)
)
_Com21HcxVpnRxStatsTable_Object = MibTable
com21HcxVpnRxStatsTable = _Com21HcxVpnRxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 103, 1)
)
if mibBuilder.loadTexts:
    com21HcxVpnRxStatsTable.setStatus("current")
_Com21HcxVpnRxStatsEntry_Object = MibTableRow
com21HcxVpnRxStatsEntry = _Com21HcxVpnRxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 103, 1, 1)
)
com21HcxVpnRxStatsEntry.setIndexNames(
    (0, "COM21-HCXVOICE-MIB", "hcxVpnRxStatsNum"),
    (0, "COM21-HCXVOICE-MIB", "hcxVpnRxStatsEntryId"),
)
if mibBuilder.loadTexts:
    com21HcxVpnRxStatsEntry.setStatus("current")
_HcxVpnRxStatsNum_Type = Integer32
_HcxVpnRxStatsNum_Object = MibTableColumn
hcxVpnRxStatsNum = _HcxVpnRxStatsNum_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 103, 1, 1, 1),
    _HcxVpnRxStatsNum_Type()
)
hcxVpnRxStatsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVpnRxStatsNum.setStatus("current")
_HcxVpnRxStatsEntryId_Type = Integer32
_HcxVpnRxStatsEntryId_Object = MibTableColumn
hcxVpnRxStatsEntryId = _HcxVpnRxStatsEntryId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 103, 1, 1, 2),
    _HcxVpnRxStatsEntryId_Type()
)
hcxVpnRxStatsEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVpnRxStatsEntryId.setStatus("current")
_HcxVpnRxStatsCurrCallsAllwd_Type = Integer32
_HcxVpnRxStatsCurrCallsAllwd_Object = MibTableColumn
hcxVpnRxStatsCurrCallsAllwd = _HcxVpnRxStatsCurrCallsAllwd_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 103, 1, 1, 3),
    _HcxVpnRxStatsCurrCallsAllwd_Type()
)
hcxVpnRxStatsCurrCallsAllwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVpnRxStatsCurrCallsAllwd.setStatus("current")
_HcxVpnRxStatsCurrCallsBlkd_Type = Integer32
_HcxVpnRxStatsCurrCallsBlkd_Object = MibTableColumn
hcxVpnRxStatsCurrCallsBlkd = _HcxVpnRxStatsCurrCallsBlkd_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 103, 1, 1, 4),
    _HcxVpnRxStatsCurrCallsBlkd_Type()
)
hcxVpnRxStatsCurrCallsBlkd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVpnRxStatsCurrCallsBlkd.setStatus("current")
_HcxVpnRxStatsPrevCallsAllwd_Type = Integer32
_HcxVpnRxStatsPrevCallsAllwd_Object = MibTableColumn
hcxVpnRxStatsPrevCallsAllwd = _HcxVpnRxStatsPrevCallsAllwd_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 103, 1, 1, 5),
    _HcxVpnRxStatsPrevCallsAllwd_Type()
)
hcxVpnRxStatsPrevCallsAllwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVpnRxStatsPrevCallsAllwd.setStatus("current")
_HcxVpnRxStatsPrevCallsBlkd_Type = Integer32
_HcxVpnRxStatsPrevCallsBlkd_Object = MibTableColumn
hcxVpnRxStatsPrevCallsBlkd = _HcxVpnRxStatsPrevCallsBlkd_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 103, 1, 1, 6),
    _HcxVpnRxStatsPrevCallsBlkd_Type()
)
hcxVpnRxStatsPrevCallsBlkd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVpnRxStatsPrevCallsBlkd.setStatus("current")


class _HcxVpnRxStatsClear_Type(Integer32):
    """Custom type hcxVpnRxStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("nil", 1))
    )


_HcxVpnRxStatsClear_Type.__name__ = "Integer32"
_HcxVpnRxStatsClear_Object = MibTableColumn
hcxVpnRxStatsClear = _HcxVpnRxStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 103, 1, 1, 7),
    _HcxVpnRxStatsClear_Type()
)
hcxVpnRxStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVpnRxStatsClear.setStatus("current")
_Com21HcxStuVoiceChannelGroup_ObjectIdentity = ObjectIdentity
com21HcxStuVoiceChannelGroup = _Com21HcxStuVoiceChannelGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 104)
)
_Com21HcxStuVoiceChannelTable_Object = MibTable
com21HcxStuVoiceChannelTable = _Com21HcxStuVoiceChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 104, 1)
)
if mibBuilder.loadTexts:
    com21HcxStuVoiceChannelTable.setStatus("current")
_Com21HcxStuVoiceChannelEntry_Object = MibTableRow
com21HcxStuVoiceChannelEntry = _Com21HcxStuVoiceChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 104, 1, 1)
)
com21HcxStuVoiceChannelEntry.setIndexNames(
    (0, "COM21-HCXVOICE-MIB", "hcxStuVoiceChannelMacAddr"),
    (0, "COM21-HCXVOICE-MIB", "hcxStuVoiceChannelNum"),
)
if mibBuilder.loadTexts:
    com21HcxStuVoiceChannelEntry.setStatus("current")
_HcxStuVoiceChannelMacAddr_Type = MacAddress
_HcxStuVoiceChannelMacAddr_Object = MibTableColumn
hcxStuVoiceChannelMacAddr = _HcxStuVoiceChannelMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 104, 1, 1, 1),
    _HcxStuVoiceChannelMacAddr_Type()
)
hcxStuVoiceChannelMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuVoiceChannelMacAddr.setStatus("current")


class _HcxStuVoiceChannelNum_Type(Integer32):
    """Custom type hcxStuVoiceChannelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HcxStuVoiceChannelNum_Type.__name__ = "Integer32"
_HcxStuVoiceChannelNum_Object = MibTableColumn
hcxStuVoiceChannelNum = _HcxStuVoiceChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 104, 1, 1, 2),
    _HcxStuVoiceChannelNum_Type()
)
hcxStuVoiceChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuVoiceChannelNum.setStatus("current")


class _HcxStuVoiceChannelVpi_Type(Integer32):
    """Custom type hcxStuVoiceChannelVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HcxStuVoiceChannelVpi_Type.__name__ = "Integer32"
_HcxStuVoiceChannelVpi_Object = MibTableColumn
hcxStuVoiceChannelVpi = _HcxStuVoiceChannelVpi_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 104, 1, 1, 3),
    _HcxStuVoiceChannelVpi_Type()
)
hcxStuVoiceChannelVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuVoiceChannelVpi.setStatus("current")


class _HcxStuVoiceChannelVci_Type(Integer32):
    """Custom type hcxStuVoiceChannelVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HcxStuVoiceChannelVci_Type.__name__ = "Integer32"
_HcxStuVoiceChannelVci_Object = MibTableColumn
hcxStuVoiceChannelVci = _HcxStuVoiceChannelVci_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 104, 1, 1, 4),
    _HcxStuVoiceChannelVci_Type()
)
hcxStuVoiceChannelVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuVoiceChannelVci.setStatus("current")
_HcxStuVoiceChannelPriStatus_Type = Com21RowStatus
_HcxStuVoiceChannelPriStatus_Object = MibTableColumn
hcxStuVoiceChannelPriStatus = _HcxStuVoiceChannelPriStatus_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 104, 1, 1, 5),
    _HcxStuVoiceChannelPriStatus_Type()
)
hcxStuVoiceChannelPriStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcxStuVoiceChannelPriStatus.setStatus("current")


class _HcxStuVoiceChannelState_Type(Integer32):
    """Custom type hcxStuVoiceChannelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("voiceChanActive", 2),
          ("voiceChanIdle", 1))
    )


_HcxStuVoiceChannelState_Type.__name__ = "Integer32"
_HcxStuVoiceChannelState_Object = MibTableColumn
hcxStuVoiceChannelState = _HcxStuVoiceChannelState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 104, 1, 1, 6),
    _HcxStuVoiceChannelState_Type()
)
hcxStuVoiceChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuVoiceChannelState.setStatus("current")


class _HcxStuVoiceChannelExtLpBk_Type(Integer32):
    """Custom type hcxStuVoiceChannelExtLpBk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HcxStuVoiceChannelExtLpBk_Type.__name__ = "Integer32"
_HcxStuVoiceChannelExtLpBk_Object = MibTableColumn
hcxStuVoiceChannelExtLpBk = _HcxStuVoiceChannelExtLpBk_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 104, 1, 1, 7),
    _HcxStuVoiceChannelExtLpBk_Type()
)
hcxStuVoiceChannelExtLpBk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuVoiceChannelExtLpBk.setStatus("current")
_Com21HcxStuVoiceCallStatsGroup_ObjectIdentity = ObjectIdentity
com21HcxStuVoiceCallStatsGroup = _Com21HcxStuVoiceCallStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 105)
)
_Com21HcxStuVoiceCallStatsTable_Object = MibTable
com21HcxStuVoiceCallStatsTable = _Com21HcxStuVoiceCallStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 105, 1)
)
if mibBuilder.loadTexts:
    com21HcxStuVoiceCallStatsTable.setStatus("current")
_Com21HcxStuVoiceCallStatsEntry_Object = MibTableRow
com21HcxStuVoiceCallStatsEntry = _Com21HcxStuVoiceCallStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 105, 1, 1)
)
com21HcxStuVoiceCallStatsEntry.setIndexNames(
    (0, "COM21-HCXVOICE-MIB", "hcxStuVoiceCallStatsMacAddr"),
    (0, "COM21-HCXVOICE-MIB", "hcxStuVoiceCallStatsNum"),
)
if mibBuilder.loadTexts:
    com21HcxStuVoiceCallStatsEntry.setStatus("current")
_HcxStuVoiceCallStatsMacAddr_Type = MacAddress
_HcxStuVoiceCallStatsMacAddr_Object = MibTableColumn
hcxStuVoiceCallStatsMacAddr = _HcxStuVoiceCallStatsMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 105, 1, 1, 1),
    _HcxStuVoiceCallStatsMacAddr_Type()
)
hcxStuVoiceCallStatsMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuVoiceCallStatsMacAddr.setStatus("current")


class _HcxStuVoiceCallStatsNum_Type(Integer32):
    """Custom type hcxStuVoiceCallStatsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HcxStuVoiceCallStatsNum_Type.__name__ = "Integer32"
_HcxStuVoiceCallStatsNum_Object = MibTableColumn
hcxStuVoiceCallStatsNum = _HcxStuVoiceCallStatsNum_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 105, 1, 1, 2),
    _HcxStuVoiceCallStatsNum_Type()
)
hcxStuVoiceCallStatsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuVoiceCallStatsNum.setStatus("current")
_HcxStuVoiceCallCurrInCallsAllwd_Type = Gauge32
_HcxStuVoiceCallCurrInCallsAllwd_Object = MibTableColumn
hcxStuVoiceCallCurrInCallsAllwd = _HcxStuVoiceCallCurrInCallsAllwd_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 105, 1, 1, 3),
    _HcxStuVoiceCallCurrInCallsAllwd_Type()
)
hcxStuVoiceCallCurrInCallsAllwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuVoiceCallCurrInCallsAllwd.setStatus("current")
_HcxStuVoiceCallCurrOutCallsAllwd_Type = Gauge32
_HcxStuVoiceCallCurrOutCallsAllwd_Object = MibTableColumn
hcxStuVoiceCallCurrOutCallsAllwd = _HcxStuVoiceCallCurrOutCallsAllwd_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 105, 1, 1, 4),
    _HcxStuVoiceCallCurrOutCallsAllwd_Type()
)
hcxStuVoiceCallCurrOutCallsAllwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuVoiceCallCurrOutCallsAllwd.setStatus("current")
_HcxStuVoiceCallCurrInCallsBlkd_Type = Gauge32
_HcxStuVoiceCallCurrInCallsBlkd_Object = MibTableColumn
hcxStuVoiceCallCurrInCallsBlkd = _HcxStuVoiceCallCurrInCallsBlkd_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 105, 1, 1, 5),
    _HcxStuVoiceCallCurrInCallsBlkd_Type()
)
hcxStuVoiceCallCurrInCallsBlkd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuVoiceCallCurrInCallsBlkd.setStatus("current")
_HcxStuVoiceCallCurrOutCallsBlkd_Type = Gauge32
_HcxStuVoiceCallCurrOutCallsBlkd_Object = MibTableColumn
hcxStuVoiceCallCurrOutCallsBlkd = _HcxStuVoiceCallCurrOutCallsBlkd_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 105, 1, 1, 6),
    _HcxStuVoiceCallCurrOutCallsBlkd_Type()
)
hcxStuVoiceCallCurrOutCallsBlkd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuVoiceCallCurrOutCallsBlkd.setStatus("current")
_HcxStuVoiceCallPrevInCallsAllwd_Type = Gauge32
_HcxStuVoiceCallPrevInCallsAllwd_Object = MibTableColumn
hcxStuVoiceCallPrevInCallsAllwd = _HcxStuVoiceCallPrevInCallsAllwd_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 105, 1, 1, 7),
    _HcxStuVoiceCallPrevInCallsAllwd_Type()
)
hcxStuVoiceCallPrevInCallsAllwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuVoiceCallPrevInCallsAllwd.setStatus("current")
_HcxStuVoiceCallPrevOutCallsAllwd_Type = Gauge32
_HcxStuVoiceCallPrevOutCallsAllwd_Object = MibTableColumn
hcxStuVoiceCallPrevOutCallsAllwd = _HcxStuVoiceCallPrevOutCallsAllwd_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 105, 1, 1, 8),
    _HcxStuVoiceCallPrevOutCallsAllwd_Type()
)
hcxStuVoiceCallPrevOutCallsAllwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuVoiceCallPrevOutCallsAllwd.setStatus("current")
_HcxStuVoiceCallPrevInCallsBlkd_Type = Gauge32
_HcxStuVoiceCallPrevInCallsBlkd_Object = MibTableColumn
hcxStuVoiceCallPrevInCallsBlkd = _HcxStuVoiceCallPrevInCallsBlkd_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 105, 1, 1, 9),
    _HcxStuVoiceCallPrevInCallsBlkd_Type()
)
hcxStuVoiceCallPrevInCallsBlkd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuVoiceCallPrevInCallsBlkd.setStatus("current")
_HcxStuVoiceCallPrevOutCallsBlkd_Type = Gauge32
_HcxStuVoiceCallPrevOutCallsBlkd_Object = MibTableColumn
hcxStuVoiceCallPrevOutCallsBlkd = _HcxStuVoiceCallPrevOutCallsBlkd_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 105, 1, 1, 10),
    _HcxStuVoiceCallPrevOutCallsBlkd_Type()
)
hcxStuVoiceCallPrevOutCallsBlkd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuVoiceCallPrevOutCallsBlkd.setStatus("current")


class _HcxStuVoiceCallStatsClear_Type(Integer32):
    """Custom type hcxStuVoiceCallStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("nil", 1))
    )


_HcxStuVoiceCallStatsClear_Type.__name__ = "Integer32"
_HcxStuVoiceCallStatsClear_Object = MibTableColumn
hcxStuVoiceCallStatsClear = _HcxStuVoiceCallStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 105, 1, 1, 11),
    _HcxStuVoiceCallStatsClear_Type()
)
hcxStuVoiceCallStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuVoiceCallStatsClear.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COM21-HCXVOICE-MIB",
    **{"PrimServiceState": PrimServiceState,
       "Com21RowStatus": Com21RowStatus,
       "com21HcxVoice": com21HcxVoice,
       "com21HcxVoiceGroup": com21HcxVoiceGroup,
       "hcxConfiguredVoiceChannels": hcxConfiguredVoiceChannels,
       "hcxActiveVoiceChannels": hcxActiveVoiceChannels,
       "hcxVoiceChannelMode": hcxVoiceChannelMode,
       "hcxVoiceOAMEnable": hcxVoiceOAMEnable,
       "hcxVoiceFEndEchoCancEnable": hcxVoiceFEndEchoCancEnable,
       "hcxVoiceRTTDelay": hcxVoiceRTTDelay,
       "com21HcxVpnRxGroup": com21HcxVpnRxGroup,
       "com21HcxVpnRxTable": com21HcxVpnRxTable,
       "com21HcxVpnRxEntry": com21HcxVpnRxEntry,
       "hcxVpnRxNum": hcxVpnRxNum,
       "hcxVpnRxEntryId": hcxVpnRxEntryId,
       "hcxVpnRxRowStatus": hcxVpnRxRowStatus,
       "hcxVpnRxMaxActiveCalls": hcxVpnRxMaxActiveCalls,
       "com21HcxVpnRxStatsGroup": com21HcxVpnRxStatsGroup,
       "com21HcxVpnRxStatsTable": com21HcxVpnRxStatsTable,
       "com21HcxVpnRxStatsEntry": com21HcxVpnRxStatsEntry,
       "hcxVpnRxStatsNum": hcxVpnRxStatsNum,
       "hcxVpnRxStatsEntryId": hcxVpnRxStatsEntryId,
       "hcxVpnRxStatsCurrCallsAllwd": hcxVpnRxStatsCurrCallsAllwd,
       "hcxVpnRxStatsCurrCallsBlkd": hcxVpnRxStatsCurrCallsBlkd,
       "hcxVpnRxStatsPrevCallsAllwd": hcxVpnRxStatsPrevCallsAllwd,
       "hcxVpnRxStatsPrevCallsBlkd": hcxVpnRxStatsPrevCallsBlkd,
       "hcxVpnRxStatsClear": hcxVpnRxStatsClear,
       "com21HcxStuVoiceChannelGroup": com21HcxStuVoiceChannelGroup,
       "com21HcxStuVoiceChannelTable": com21HcxStuVoiceChannelTable,
       "com21HcxStuVoiceChannelEntry": com21HcxStuVoiceChannelEntry,
       "hcxStuVoiceChannelMacAddr": hcxStuVoiceChannelMacAddr,
       "hcxStuVoiceChannelNum": hcxStuVoiceChannelNum,
       "hcxStuVoiceChannelVpi": hcxStuVoiceChannelVpi,
       "hcxStuVoiceChannelVci": hcxStuVoiceChannelVci,
       "hcxStuVoiceChannelPriStatus": hcxStuVoiceChannelPriStatus,
       "hcxStuVoiceChannelState": hcxStuVoiceChannelState,
       "hcxStuVoiceChannelExtLpBk": hcxStuVoiceChannelExtLpBk,
       "com21HcxStuVoiceCallStatsGroup": com21HcxStuVoiceCallStatsGroup,
       "com21HcxStuVoiceCallStatsTable": com21HcxStuVoiceCallStatsTable,
       "com21HcxStuVoiceCallStatsEntry": com21HcxStuVoiceCallStatsEntry,
       "hcxStuVoiceCallStatsMacAddr": hcxStuVoiceCallStatsMacAddr,
       "hcxStuVoiceCallStatsNum": hcxStuVoiceCallStatsNum,
       "hcxStuVoiceCallCurrInCallsAllwd": hcxStuVoiceCallCurrInCallsAllwd,
       "hcxStuVoiceCallCurrOutCallsAllwd": hcxStuVoiceCallCurrOutCallsAllwd,
       "hcxStuVoiceCallCurrInCallsBlkd": hcxStuVoiceCallCurrInCallsBlkd,
       "hcxStuVoiceCallCurrOutCallsBlkd": hcxStuVoiceCallCurrOutCallsBlkd,
       "hcxStuVoiceCallPrevInCallsAllwd": hcxStuVoiceCallPrevInCallsAllwd,
       "hcxStuVoiceCallPrevOutCallsAllwd": hcxStuVoiceCallPrevOutCallsAllwd,
       "hcxStuVoiceCallPrevInCallsBlkd": hcxStuVoiceCallPrevInCallsBlkd,
       "hcxStuVoiceCallPrevOutCallsBlkd": hcxStuVoiceCallPrevOutCallsBlkd,
       "hcxStuVoiceCallStatsClear": hcxStuVoiceCallStatsClear}
)
