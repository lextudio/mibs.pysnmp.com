# SNMP MIB module (CISCO-VOICE-ATM-DIAL-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VOICE-ATM-DIAL-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:17 2024
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

(cCallHistoryIndex,) = mibBuilder.importSymbols(
    "CISCO-DIAL-CONTROL-MIB",
    "cCallHistoryIndex")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(CvcFaxTransmitRate,
 CvcGUid,
 CvcInBandSignaling,
 CvcSpeechCoderRate) = mibBuilder.importSymbols(
    "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB",
    "CvcFaxTransmitRate",
    "CvcGUid",
    "CvcInBandSignaling",
    "CvcSpeechCoderRate")

(callActiveIndex,
 callActiveSetupTime) = mibBuilder.importSymbols(
    "DIAL-CONTROL-MIB",
    "callActiveIndex",
    "callActiveSetupTime")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

ciscoVoiceAtmDialControlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 35)
)
ciscoVoiceAtmDialControlMIB.setRevisions(
        ("2002-11-17 00:00",
         "1999-03-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CvAtmSessionProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aal2Trunk", 3),
          ("ciscoSwitched", 2),
          ("other", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoVoiceAtmDialControlMIBObjects_ObjectIdentity = ObjectIdentity
ciscoVoiceAtmDialControlMIBObjects = _CiscoVoiceAtmDialControlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1)
)
_CvAtmCallHistory_ObjectIdentity = ObjectIdentity
cvAtmCallHistory = _CvAtmCallHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 1)
)
_CvAtmCallHistoryTable_Object = MibTable
cvAtmCallHistoryTable = _CvAtmCallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cvAtmCallHistoryTable.setStatus("current")
_CvAtmCallHistoryEntry_Object = MibTableRow
cvAtmCallHistoryEntry = _CvAtmCallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 1, 1, 1)
)
cvAtmCallHistoryEntry.setIndexNames(
    (0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    cvAtmCallHistoryEntry.setStatus("current")
_CvAtmCallHistoryConnectionId_Type = CvcGUid
_CvAtmCallHistoryConnectionId_Object = MibTableColumn
cvAtmCallHistoryConnectionId = _CvAtmCallHistoryConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 1, 1, 1, 1),
    _CvAtmCallHistoryConnectionId_Type()
)
cvAtmCallHistoryConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvAtmCallHistoryConnectionId.setStatus("current")


class _CvAtmCallHistoryVpi_Type(Integer32):
    """Custom type cvAtmCallHistoryVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CvAtmCallHistoryVpi_Type.__name__ = "Integer32"
_CvAtmCallHistoryVpi_Object = MibTableColumn
cvAtmCallHistoryVpi = _CvAtmCallHistoryVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 1, 1, 1, 2),
    _CvAtmCallHistoryVpi_Type()
)
cvAtmCallHistoryVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvAtmCallHistoryVpi.setStatus("current")


class _CvAtmCallHistoryVci_Type(Integer32):
    """Custom type cvAtmCallHistoryVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvAtmCallHistoryVci_Type.__name__ = "Integer32"
_CvAtmCallHistoryVci_Object = MibTableColumn
cvAtmCallHistoryVci = _CvAtmCallHistoryVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 1, 1, 1, 3),
    _CvAtmCallHistoryVci_Type()
)
cvAtmCallHistoryVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvAtmCallHistoryVci.setStatus("current")
_CvAtmCallHistoryLowerIfName_Type = DisplayString
_CvAtmCallHistoryLowerIfName_Object = MibTableColumn
cvAtmCallHistoryLowerIfName = _CvAtmCallHistoryLowerIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 1, 1, 1, 4),
    _CvAtmCallHistoryLowerIfName_Type()
)
cvAtmCallHistoryLowerIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvAtmCallHistoryLowerIfName.setStatus("current")
_CvAtmCallHistorySessionTarget_Type = DisplayString
_CvAtmCallHistorySessionTarget_Object = MibTableColumn
cvAtmCallHistorySessionTarget = _CvAtmCallHistorySessionTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 1, 1, 1, 5),
    _CvAtmCallHistorySessionTarget_Type()
)
cvAtmCallHistorySessionTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvAtmCallHistorySessionTarget.setStatus("current")


class _CvAtmCallHistorySubchannelID_Type(Integer32):
    """Custom type cvAtmCallHistorySubchannelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CvAtmCallHistorySubchannelID_Type.__name__ = "Integer32"
_CvAtmCallHistorySubchannelID_Object = MibTableColumn
cvAtmCallHistorySubchannelID = _CvAtmCallHistorySubchannelID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 1, 1, 1, 6),
    _CvAtmCallHistorySubchannelID_Type()
)
cvAtmCallHistorySubchannelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvAtmCallHistorySubchannelID.setStatus("current")
_CvAtmCallHistorySessionProtocol_Type = CvAtmSessionProtocol
_CvAtmCallHistorySessionProtocol_Object = MibTableColumn
cvAtmCallHistorySessionProtocol = _CvAtmCallHistorySessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 1, 1, 1, 7),
    _CvAtmCallHistorySessionProtocol_Type()
)
cvAtmCallHistorySessionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvAtmCallHistorySessionProtocol.setStatus("current")
_CvAtmCallHistoryCalledNumber_Type = DisplayString
_CvAtmCallHistoryCalledNumber_Object = MibTableColumn
cvAtmCallHistoryCalledNumber = _CvAtmCallHistoryCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 1, 1, 1, 8),
    _CvAtmCallHistoryCalledNumber_Type()
)
cvAtmCallHistoryCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvAtmCallHistoryCalledNumber.setStatus("current")
_CvAtmCallHistoryDtmfRelay_Type = TruthValue
_CvAtmCallHistoryDtmfRelay_Object = MibTableColumn
cvAtmCallHistoryDtmfRelay = _CvAtmCallHistoryDtmfRelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 1, 1, 1, 9),
    _CvAtmCallHistoryDtmfRelay_Type()
)
cvAtmCallHistoryDtmfRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvAtmCallHistoryDtmfRelay.setStatus("current")
_CvAtmCallHistoryUseSeqNumbers_Type = TruthValue
_CvAtmCallHistoryUseSeqNumbers_Object = MibTableColumn
cvAtmCallHistoryUseSeqNumbers = _CvAtmCallHistoryUseSeqNumbers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 1, 1, 1, 10),
    _CvAtmCallHistoryUseSeqNumbers_Type()
)
cvAtmCallHistoryUseSeqNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvAtmCallHistoryUseSeqNumbers.setStatus("current")
_CvAtmCallActive_ObjectIdentity = ObjectIdentity
cvAtmCallActive = _CvAtmCallActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 2)
)
_CvAtmCallActiveTable_Object = MibTable
cvAtmCallActiveTable = _CvAtmCallActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cvAtmCallActiveTable.setStatus("current")
_CvAtmCallActiveEntry_Object = MibTableRow
cvAtmCallActiveEntry = _CvAtmCallActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 2, 1, 1)
)
cvAtmCallActiveEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    cvAtmCallActiveEntry.setStatus("current")
_CvAtmCallActiveConnectionId_Type = CvcGUid
_CvAtmCallActiveConnectionId_Object = MibTableColumn
cvAtmCallActiveConnectionId = _CvAtmCallActiveConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 2, 1, 1, 1),
    _CvAtmCallActiveConnectionId_Type()
)
cvAtmCallActiveConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvAtmCallActiveConnectionId.setStatus("current")


class _CvAtmCallActiveVpi_Type(Integer32):
    """Custom type cvAtmCallActiveVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CvAtmCallActiveVpi_Type.__name__ = "Integer32"
_CvAtmCallActiveVpi_Object = MibTableColumn
cvAtmCallActiveVpi = _CvAtmCallActiveVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 2, 1, 1, 2),
    _CvAtmCallActiveVpi_Type()
)
cvAtmCallActiveVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvAtmCallActiveVpi.setStatus("current")


class _CvAtmCallActiveVci_Type(Integer32):
    """Custom type cvAtmCallActiveVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvAtmCallActiveVci_Type.__name__ = "Integer32"
_CvAtmCallActiveVci_Object = MibTableColumn
cvAtmCallActiveVci = _CvAtmCallActiveVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 2, 1, 1, 3),
    _CvAtmCallActiveVci_Type()
)
cvAtmCallActiveVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvAtmCallActiveVci.setStatus("current")
_CvAtmCallActiveLowerIfName_Type = DisplayString
_CvAtmCallActiveLowerIfName_Object = MibTableColumn
cvAtmCallActiveLowerIfName = _CvAtmCallActiveLowerIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 2, 1, 1, 4),
    _CvAtmCallActiveLowerIfName_Type()
)
cvAtmCallActiveLowerIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvAtmCallActiveLowerIfName.setStatus("current")
_CvAtmCallActiveSessionTarget_Type = DisplayString
_CvAtmCallActiveSessionTarget_Object = MibTableColumn
cvAtmCallActiveSessionTarget = _CvAtmCallActiveSessionTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 2, 1, 1, 5),
    _CvAtmCallActiveSessionTarget_Type()
)
cvAtmCallActiveSessionTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvAtmCallActiveSessionTarget.setStatus("current")


class _CvAtmCallActiveSubchannelID_Type(Integer32):
    """Custom type cvAtmCallActiveSubchannelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CvAtmCallActiveSubchannelID_Type.__name__ = "Integer32"
_CvAtmCallActiveSubchannelID_Object = MibTableColumn
cvAtmCallActiveSubchannelID = _CvAtmCallActiveSubchannelID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 2, 1, 1, 6),
    _CvAtmCallActiveSubchannelID_Type()
)
cvAtmCallActiveSubchannelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvAtmCallActiveSubchannelID.setStatus("current")
_CvAtmCallActiveSessionProtocol_Type = CvAtmSessionProtocol
_CvAtmCallActiveSessionProtocol_Object = MibTableColumn
cvAtmCallActiveSessionProtocol = _CvAtmCallActiveSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 2, 1, 1, 7),
    _CvAtmCallActiveSessionProtocol_Type()
)
cvAtmCallActiveSessionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvAtmCallActiveSessionProtocol.setStatus("current")
_CvAtmCallActiveCalledNumber_Type = DisplayString
_CvAtmCallActiveCalledNumber_Object = MibTableColumn
cvAtmCallActiveCalledNumber = _CvAtmCallActiveCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 2, 1, 1, 8),
    _CvAtmCallActiveCalledNumber_Type()
)
cvAtmCallActiveCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvAtmCallActiveCalledNumber.setStatus("current")
_CvAtmCallActiveDtmfRelay_Type = TruthValue
_CvAtmCallActiveDtmfRelay_Object = MibTableColumn
cvAtmCallActiveDtmfRelay = _CvAtmCallActiveDtmfRelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 2, 1, 1, 9),
    _CvAtmCallActiveDtmfRelay_Type()
)
cvAtmCallActiveDtmfRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvAtmCallActiveDtmfRelay.setStatus("current")
_CvAtmCallActiveUseSeqNumbers_Type = TruthValue
_CvAtmCallActiveUseSeqNumbers_Object = MibTableColumn
cvAtmCallActiveUseSeqNumbers = _CvAtmCallActiveUseSeqNumbers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 2, 1, 1, 10),
    _CvAtmCallActiveUseSeqNumbers_Type()
)
cvAtmCallActiveUseSeqNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvAtmCallActiveUseSeqNumbers.setStatus("current")
_CvAtmDialPeer_ObjectIdentity = ObjectIdentity
cvAtmDialPeer = _CvAtmDialPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 3)
)
_CvAtmPeerCfgTable_Object = MibTable
cvAtmPeerCfgTable = _CvAtmPeerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cvAtmPeerCfgTable.setStatus("current")
_CvAtmPeerCfgEntry_Object = MibTableRow
cvAtmPeerCfgEntry = _CvAtmPeerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 3, 1, 1)
)
cvAtmPeerCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cvAtmPeerCfgEntry.setStatus("current")


class _CvAtmPeerCfgSessionProtocol_Type(CvAtmSessionProtocol):
    """Custom type cvAtmPeerCfgSessionProtocol based on CvAtmSessionProtocol"""


_CvAtmPeerCfgSessionProtocol_Object = MibTableColumn
cvAtmPeerCfgSessionProtocol = _CvAtmPeerCfgSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 3, 1, 1, 1),
    _CvAtmPeerCfgSessionProtocol_Type()
)
cvAtmPeerCfgSessionProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvAtmPeerCfgSessionProtocol.setStatus("current")
_CvAtmPeerCfgInterfaceName_Type = DisplayString
_CvAtmPeerCfgInterfaceName_Object = MibTableColumn
cvAtmPeerCfgInterfaceName = _CvAtmPeerCfgInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 3, 1, 1, 2),
    _CvAtmPeerCfgInterfaceName_Type()
)
cvAtmPeerCfgInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvAtmPeerCfgInterfaceName.setStatus("current")


class _CvAtmPeerCfgVpi_Type(Integer32):
    """Custom type cvAtmPeerCfgVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CvAtmPeerCfgVpi_Type.__name__ = "Integer32"
_CvAtmPeerCfgVpi_Object = MibTableColumn
cvAtmPeerCfgVpi = _CvAtmPeerCfgVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 3, 1, 1, 3),
    _CvAtmPeerCfgVpi_Type()
)
cvAtmPeerCfgVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvAtmPeerCfgVpi.setStatus("current")


class _CvAtmPeerCfgVci_Type(Integer32):
    """Custom type cvAtmPeerCfgVci based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvAtmPeerCfgVci_Type.__name__ = "Integer32"
_CvAtmPeerCfgVci_Object = MibTableColumn
cvAtmPeerCfgVci = _CvAtmPeerCfgVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 3, 1, 1, 4),
    _CvAtmPeerCfgVci_Type()
)
cvAtmPeerCfgVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvAtmPeerCfgVci.setStatus("current")
_CvAtmPeerCfgVcName_Type = DisplayString
_CvAtmPeerCfgVcName_Object = MibTableColumn
cvAtmPeerCfgVcName = _CvAtmPeerCfgVcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 3, 1, 1, 5),
    _CvAtmPeerCfgVcName_Type()
)
cvAtmPeerCfgVcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvAtmPeerCfgVcName.setStatus("current")


class _CvAtmPeerCfgCoderRate_Type(CvcSpeechCoderRate):
    """Custom type cvAtmPeerCfgCoderRate based on CvcSpeechCoderRate"""


_CvAtmPeerCfgCoderRate_Object = MibTableColumn
cvAtmPeerCfgCoderRate = _CvAtmPeerCfgCoderRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 3, 1, 1, 6),
    _CvAtmPeerCfgCoderRate_Type()
)
cvAtmPeerCfgCoderRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvAtmPeerCfgCoderRate.setStatus("current")


class _CvAtmPeerCfgCodecBytes_Type(Integer32):
    """Custom type cvAtmPeerCfgCodecBytes based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_CvAtmPeerCfgCodecBytes_Type.__name__ = "Integer32"
_CvAtmPeerCfgCodecBytes_Object = MibTableColumn
cvAtmPeerCfgCodecBytes = _CvAtmPeerCfgCodecBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 3, 1, 1, 7),
    _CvAtmPeerCfgCodecBytes_Type()
)
cvAtmPeerCfgCodecBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvAtmPeerCfgCodecBytes.setStatus("current")


class _CvAtmPeerCfgFaxRate_Type(CvcFaxTransmitRate):
    """Custom type cvAtmPeerCfgFaxRate based on CvcFaxTransmitRate"""


_CvAtmPeerCfgFaxRate_Object = MibTableColumn
cvAtmPeerCfgFaxRate = _CvAtmPeerCfgFaxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 3, 1, 1, 8),
    _CvAtmPeerCfgFaxRate_Type()
)
cvAtmPeerCfgFaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvAtmPeerCfgFaxRate.setStatus("current")


class _CvAtmPeerCfgFaxBytes_Type(Integer32):
    """Custom type cvAtmPeerCfgFaxBytes based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_CvAtmPeerCfgFaxBytes_Type.__name__ = "Integer32"
_CvAtmPeerCfgFaxBytes_Object = MibTableColumn
cvAtmPeerCfgFaxBytes = _CvAtmPeerCfgFaxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 3, 1, 1, 9),
    _CvAtmPeerCfgFaxBytes_Type()
)
cvAtmPeerCfgFaxBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvAtmPeerCfgFaxBytes.setStatus("current")


class _CvAtmPeerCfgInBandSignaling_Type(CvcInBandSignaling):
    """Custom type cvAtmPeerCfgInBandSignaling based on CvcInBandSignaling"""


_CvAtmPeerCfgInBandSignaling_Object = MibTableColumn
cvAtmPeerCfgInBandSignaling = _CvAtmPeerCfgInBandSignaling_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 3, 1, 1, 10),
    _CvAtmPeerCfgInBandSignaling_Type()
)
cvAtmPeerCfgInBandSignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvAtmPeerCfgInBandSignaling.setStatus("current")


class _CvAtmPeerCfgVADEnable_Type(TruthValue):
    """Custom type cvAtmPeerCfgVADEnable based on TruthValue"""


_CvAtmPeerCfgVADEnable_Object = MibTableColumn
cvAtmPeerCfgVADEnable = _CvAtmPeerCfgVADEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 3, 1, 1, 11),
    _CvAtmPeerCfgVADEnable_Type()
)
cvAtmPeerCfgVADEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvAtmPeerCfgVADEnable.setStatus("current")


class _CvAtmPeerCfgUseSeqNumbers_Type(TruthValue):
    """Custom type cvAtmPeerCfgUseSeqNumbers based on TruthValue"""


_CvAtmPeerCfgUseSeqNumbers_Object = MibTableColumn
cvAtmPeerCfgUseSeqNumbers = _CvAtmPeerCfgUseSeqNumbers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 3, 1, 1, 12),
    _CvAtmPeerCfgUseSeqNumbers_Type()
)
cvAtmPeerCfgUseSeqNumbers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvAtmPeerCfgUseSeqNumbers.setStatus("current")


class _CvAtmPeerCfgDtmfRelay_Type(TruthValue):
    """Custom type cvAtmPeerCfgDtmfRelay based on TruthValue"""


_CvAtmPeerCfgDtmfRelay_Object = MibTableColumn
cvAtmPeerCfgDtmfRelay = _CvAtmPeerCfgDtmfRelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 1, 3, 1, 1, 13),
    _CvAtmPeerCfgDtmfRelay_Type()
)
cvAtmPeerCfgDtmfRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvAtmPeerCfgDtmfRelay.setStatus("current")
_CiscoVoiceAtmDialControlMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoVoiceAtmDialControlMIBNotificationPrefix = _CiscoVoiceAtmDialControlMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 2)
)
_CiscoVoiceAtmDialControlMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoVoiceAtmDialControlMIBNotifications = _CiscoVoiceAtmDialControlMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 2, 0)
)
_CiscoVoiceAtmDialControlMIBConformance_ObjectIdentity = ObjectIdentity
ciscoVoiceAtmDialControlMIBConformance = _CiscoVoiceAtmDialControlMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 3)
)
_CiscoVoiceAtmDialControlMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVoiceAtmDialControlMIBCompliances = _CiscoVoiceAtmDialControlMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 3, 1)
)
_CiscoVoiceAtmDialControlMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVoiceAtmDialControlMIBGroups = _CiscoVoiceAtmDialControlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 3, 2)
)

# Managed Objects groups

cvAtmCallHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 3, 2, 1)
)
cvAtmCallHistoryGroup.setObjects(
      *(("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmCallHistoryConnectionId"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmCallHistoryVpi"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmCallHistoryVci"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmCallHistoryLowerIfName"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmCallHistorySessionTarget"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmCallHistorySubchannelID"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmCallHistorySessionProtocol"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmCallHistoryCalledNumber"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmCallHistoryDtmfRelay"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmCallHistoryUseSeqNumbers"))
)
if mibBuilder.loadTexts:
    cvAtmCallHistoryGroup.setStatus("current")

cvAtmCallActiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 3, 2, 2)
)
cvAtmCallActiveGroup.setObjects(
      *(("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmCallActiveConnectionId"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmCallActiveVpi"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmCallActiveVci"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmCallActiveLowerIfName"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmCallActiveSessionTarget"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmCallActiveSubchannelID"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmCallActiveSessionProtocol"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmCallActiveCalledNumber"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmCallActiveDtmfRelay"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmCallActiveUseSeqNumbers"))
)
if mibBuilder.loadTexts:
    cvAtmCallActiveGroup.setStatus("current")

cvAtmPeerCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 3, 2, 3)
)
cvAtmPeerCfgGroup.setObjects(
      *(("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmPeerCfgSessionProtocol"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmPeerCfgInterfaceName"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmPeerCfgVpi"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmPeerCfgVci"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmPeerCfgVcName"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmPeerCfgCoderRate"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmPeerCfgCodecBytes"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmPeerCfgFaxRate"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmPeerCfgFaxBytes"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmPeerCfgInBandSignaling"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmPeerCfgVADEnable"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmPeerCfgUseSeqNumbers"),
        ("CISCO-VOICE-ATM-DIAL-CONTROL-MIB", "cvAtmPeerCfgDtmfRelay"))
)
if mibBuilder.loadTexts:
    cvAtmPeerCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoVoiceAtmDialControlMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 35, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoVoiceAtmDialControlMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VOICE-ATM-DIAL-CONTROL-MIB",
    **{"CvAtmSessionProtocol": CvAtmSessionProtocol,
       "ciscoVoiceAtmDialControlMIB": ciscoVoiceAtmDialControlMIB,
       "ciscoVoiceAtmDialControlMIBObjects": ciscoVoiceAtmDialControlMIBObjects,
       "cvAtmCallHistory": cvAtmCallHistory,
       "cvAtmCallHistoryTable": cvAtmCallHistoryTable,
       "cvAtmCallHistoryEntry": cvAtmCallHistoryEntry,
       "cvAtmCallHistoryConnectionId": cvAtmCallHistoryConnectionId,
       "cvAtmCallHistoryVpi": cvAtmCallHistoryVpi,
       "cvAtmCallHistoryVci": cvAtmCallHistoryVci,
       "cvAtmCallHistoryLowerIfName": cvAtmCallHistoryLowerIfName,
       "cvAtmCallHistorySessionTarget": cvAtmCallHistorySessionTarget,
       "cvAtmCallHistorySubchannelID": cvAtmCallHistorySubchannelID,
       "cvAtmCallHistorySessionProtocol": cvAtmCallHistorySessionProtocol,
       "cvAtmCallHistoryCalledNumber": cvAtmCallHistoryCalledNumber,
       "cvAtmCallHistoryDtmfRelay": cvAtmCallHistoryDtmfRelay,
       "cvAtmCallHistoryUseSeqNumbers": cvAtmCallHistoryUseSeqNumbers,
       "cvAtmCallActive": cvAtmCallActive,
       "cvAtmCallActiveTable": cvAtmCallActiveTable,
       "cvAtmCallActiveEntry": cvAtmCallActiveEntry,
       "cvAtmCallActiveConnectionId": cvAtmCallActiveConnectionId,
       "cvAtmCallActiveVpi": cvAtmCallActiveVpi,
       "cvAtmCallActiveVci": cvAtmCallActiveVci,
       "cvAtmCallActiveLowerIfName": cvAtmCallActiveLowerIfName,
       "cvAtmCallActiveSessionTarget": cvAtmCallActiveSessionTarget,
       "cvAtmCallActiveSubchannelID": cvAtmCallActiveSubchannelID,
       "cvAtmCallActiveSessionProtocol": cvAtmCallActiveSessionProtocol,
       "cvAtmCallActiveCalledNumber": cvAtmCallActiveCalledNumber,
       "cvAtmCallActiveDtmfRelay": cvAtmCallActiveDtmfRelay,
       "cvAtmCallActiveUseSeqNumbers": cvAtmCallActiveUseSeqNumbers,
       "cvAtmDialPeer": cvAtmDialPeer,
       "cvAtmPeerCfgTable": cvAtmPeerCfgTable,
       "cvAtmPeerCfgEntry": cvAtmPeerCfgEntry,
       "cvAtmPeerCfgSessionProtocol": cvAtmPeerCfgSessionProtocol,
       "cvAtmPeerCfgInterfaceName": cvAtmPeerCfgInterfaceName,
       "cvAtmPeerCfgVpi": cvAtmPeerCfgVpi,
       "cvAtmPeerCfgVci": cvAtmPeerCfgVci,
       "cvAtmPeerCfgVcName": cvAtmPeerCfgVcName,
       "cvAtmPeerCfgCoderRate": cvAtmPeerCfgCoderRate,
       "cvAtmPeerCfgCodecBytes": cvAtmPeerCfgCodecBytes,
       "cvAtmPeerCfgFaxRate": cvAtmPeerCfgFaxRate,
       "cvAtmPeerCfgFaxBytes": cvAtmPeerCfgFaxBytes,
       "cvAtmPeerCfgInBandSignaling": cvAtmPeerCfgInBandSignaling,
       "cvAtmPeerCfgVADEnable": cvAtmPeerCfgVADEnable,
       "cvAtmPeerCfgUseSeqNumbers": cvAtmPeerCfgUseSeqNumbers,
       "cvAtmPeerCfgDtmfRelay": cvAtmPeerCfgDtmfRelay,
       "ciscoVoiceAtmDialControlMIBNotificationPrefix": ciscoVoiceAtmDialControlMIBNotificationPrefix,
       "ciscoVoiceAtmDialControlMIBNotifications": ciscoVoiceAtmDialControlMIBNotifications,
       "ciscoVoiceAtmDialControlMIBConformance": ciscoVoiceAtmDialControlMIBConformance,
       "ciscoVoiceAtmDialControlMIBCompliances": ciscoVoiceAtmDialControlMIBCompliances,
       "ciscoVoiceAtmDialControlMIBCompliance": ciscoVoiceAtmDialControlMIBCompliance,
       "ciscoVoiceAtmDialControlMIBGroups": ciscoVoiceAtmDialControlMIBGroups,
       "cvAtmCallHistoryGroup": cvAtmCallHistoryGroup,
       "cvAtmCallActiveGroup": cvAtmCallActiveGroup,
       "cvAtmPeerCfgGroup": cvAtmPeerCfgGroup}
)
