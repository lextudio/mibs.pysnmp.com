# SNMP MIB module (CISCO-DIAL-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DIAL-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:06 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(AbsoluteCounter32,) = mibBuilder.importSymbols(
    "DIAL-CONTROL-MIB",
    "AbsoluteCounter32")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoDialControlMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 25)
)
ciscoDialControlMib.setRevisions(
        ("2005-05-26 00:00",
         "2003-07-10 00:01",
         "2002-08-21 00:01",
         "2002-05-24 00:01",
         "2002-02-20 15:46",
         "2001-12-13 15:46",
         "1998-01-16 15:46")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoDialControlMibObjects_ObjectIdentity = ObjectIdentity
ciscoDialControlMibObjects = _CiscoDialControlMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1)
)
_CCallHistory_ObjectIdentity = ObjectIdentity
cCallHistory = _CCallHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4)
)
_CCallHistoryTable_Object = MibTable
cCallHistoryTable = _CCallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cCallHistoryTable.setStatus("current")
_CCallHistoryEntry_Object = MibTableRow
cCallHistoryEntry = _CCallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1)
)
cCallHistoryEntry.setIndexNames(
    (0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    cCallHistoryEntry.setStatus("current")


class _CCallHistoryIndex_Type(Unsigned32):
    """Custom type cCallHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CCallHistoryIndex_Type.__name__ = "Unsigned32"
_CCallHistoryIndex_Object = MibTableColumn
cCallHistoryIndex = _CCallHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 1),
    _CCallHistoryIndex_Type()
)
cCallHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCallHistoryIndex.setStatus("current")
_CCallHistorySetupTime_Type = TimeStamp
_CCallHistorySetupTime_Object = MibTableColumn
cCallHistorySetupTime = _CCallHistorySetupTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 2),
    _CCallHistorySetupTime_Type()
)
cCallHistorySetupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCallHistorySetupTime.setStatus("current")
_CCallHistoryPeerAddress_Type = DisplayString
_CCallHistoryPeerAddress_Object = MibTableColumn
cCallHistoryPeerAddress = _CCallHistoryPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 3),
    _CCallHistoryPeerAddress_Type()
)
cCallHistoryPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCallHistoryPeerAddress.setStatus("current")
_CCallHistoryPeerSubAddress_Type = DisplayString
_CCallHistoryPeerSubAddress_Object = MibTableColumn
cCallHistoryPeerSubAddress = _CCallHistoryPeerSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 4),
    _CCallHistoryPeerSubAddress_Type()
)
cCallHistoryPeerSubAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCallHistoryPeerSubAddress.setStatus("current")


class _CCallHistoryPeerId_Type(Integer32):
    """Custom type cCallHistoryPeerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CCallHistoryPeerId_Type.__name__ = "Integer32"
_CCallHistoryPeerId_Object = MibTableColumn
cCallHistoryPeerId = _CCallHistoryPeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 5),
    _CCallHistoryPeerId_Type()
)
cCallHistoryPeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCallHistoryPeerId.setStatus("current")


class _CCallHistoryPeerIfIndex_Type(Integer32):
    """Custom type cCallHistoryPeerIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CCallHistoryPeerIfIndex_Type.__name__ = "Integer32"
_CCallHistoryPeerIfIndex_Object = MibTableColumn
cCallHistoryPeerIfIndex = _CCallHistoryPeerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 6),
    _CCallHistoryPeerIfIndex_Type()
)
cCallHistoryPeerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCallHistoryPeerIfIndex.setStatus("current")
_CCallHistoryLogicalIfIndex_Type = InterfaceIndexOrZero
_CCallHistoryLogicalIfIndex_Object = MibTableColumn
cCallHistoryLogicalIfIndex = _CCallHistoryLogicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 7),
    _CCallHistoryLogicalIfIndex_Type()
)
cCallHistoryLogicalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCallHistoryLogicalIfIndex.setStatus("current")


class _CCallHistoryDisconnectCause_Type(OctetString):
    """Custom type cCallHistoryDisconnectCause based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CCallHistoryDisconnectCause_Type.__name__ = "OctetString"
_CCallHistoryDisconnectCause_Object = MibTableColumn
cCallHistoryDisconnectCause = _CCallHistoryDisconnectCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 8),
    _CCallHistoryDisconnectCause_Type()
)
cCallHistoryDisconnectCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCallHistoryDisconnectCause.setStatus("current")
_CCallHistoryDisconnectText_Type = DisplayString
_CCallHistoryDisconnectText_Object = MibTableColumn
cCallHistoryDisconnectText = _CCallHistoryDisconnectText_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 9),
    _CCallHistoryDisconnectText_Type()
)
cCallHistoryDisconnectText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCallHistoryDisconnectText.setStatus("current")
_CCallHistoryConnectTime_Type = TimeStamp
_CCallHistoryConnectTime_Object = MibTableColumn
cCallHistoryConnectTime = _CCallHistoryConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 10),
    _CCallHistoryConnectTime_Type()
)
cCallHistoryConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCallHistoryConnectTime.setStatus("current")
_CCallHistoryDisconnectTime_Type = TimeStamp
_CCallHistoryDisconnectTime_Object = MibTableColumn
cCallHistoryDisconnectTime = _CCallHistoryDisconnectTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 11),
    _CCallHistoryDisconnectTime_Type()
)
cCallHistoryDisconnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCallHistoryDisconnectTime.setStatus("current")


class _CCallHistoryCallOrigin_Type(Integer32):
    """Custom type cCallHistoryCallOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("answer", 2),
          ("callback", 3),
          ("originate", 1))
    )


_CCallHistoryCallOrigin_Type.__name__ = "Integer32"
_CCallHistoryCallOrigin_Object = MibTableColumn
cCallHistoryCallOrigin = _CCallHistoryCallOrigin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 12),
    _CCallHistoryCallOrigin_Type()
)
cCallHistoryCallOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCallHistoryCallOrigin.setStatus("current")
_CCallHistoryChargedUnits_Type = AbsoluteCounter32
_CCallHistoryChargedUnits_Object = MibTableColumn
cCallHistoryChargedUnits = _CCallHistoryChargedUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 13),
    _CCallHistoryChargedUnits_Type()
)
cCallHistoryChargedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCallHistoryChargedUnits.setStatus("current")


class _CCallHistoryInfoType_Type(Integer32):
    """Custom type cCallHistoryInfoType based on Integer32"""
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
        *(("audio31", 6),
          ("audio7", 7),
          ("fax", 10),
          ("other", 1),
          ("packetSwitched", 9),
          ("restrictedDigital", 5),
          ("speech", 2),
          ("unrestrictedDigital", 3),
          ("unrestrictedDigital56", 4),
          ("video", 8))
    )


_CCallHistoryInfoType_Type.__name__ = "Integer32"
_CCallHistoryInfoType_Object = MibTableColumn
cCallHistoryInfoType = _CCallHistoryInfoType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 14),
    _CCallHistoryInfoType_Type()
)
cCallHistoryInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCallHistoryInfoType.setStatus("current")
_CCallHistoryTransmitPackets_Type = AbsoluteCounter32
_CCallHistoryTransmitPackets_Object = MibTableColumn
cCallHistoryTransmitPackets = _CCallHistoryTransmitPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 15),
    _CCallHistoryTransmitPackets_Type()
)
cCallHistoryTransmitPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCallHistoryTransmitPackets.setStatus("current")
_CCallHistoryTransmitBytes_Type = AbsoluteCounter32
_CCallHistoryTransmitBytes_Object = MibTableColumn
cCallHistoryTransmitBytes = _CCallHistoryTransmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 16),
    _CCallHistoryTransmitBytes_Type()
)
cCallHistoryTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCallHistoryTransmitBytes.setStatus("current")
_CCallHistoryReceivePackets_Type = AbsoluteCounter32
_CCallHistoryReceivePackets_Object = MibTableColumn
cCallHistoryReceivePackets = _CCallHistoryReceivePackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 17),
    _CCallHistoryReceivePackets_Type()
)
cCallHistoryReceivePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCallHistoryReceivePackets.setStatus("current")
_CCallHistoryReceiveBytes_Type = AbsoluteCounter32
_CCallHistoryReceiveBytes_Object = MibTableColumn
cCallHistoryReceiveBytes = _CCallHistoryReceiveBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 18),
    _CCallHistoryReceiveBytes_Type()
)
cCallHistoryReceiveBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCallHistoryReceiveBytes.setStatus("current")


class _CCallHistoryReleaseSource_Type(Integer32):
    """Custom type cCallHistoryReleaseSource based on Integer32"""
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
        *(("calledPartyInPstn", 3),
          ("calledPartyInVoip", 4),
          ("callingPartyInPstn", 1),
          ("callingPartyInVoip", 2),
          ("consoleCommand", 7),
          ("externalCallControlAgent", 10),
          ("externalNmsApp", 9),
          ("externalRadiusServer", 8),
          ("internalCallControlApp", 6),
          ("internalRelease", 5))
    )


_CCallHistoryReleaseSource_Type.__name__ = "Integer32"
_CCallHistoryReleaseSource_Object = MibTableColumn
cCallHistoryReleaseSource = _CCallHistoryReleaseSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 19),
    _CCallHistoryReleaseSource_Type()
)
cCallHistoryReleaseSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCallHistoryReleaseSource.setStatus("deprecated")


class _CCallHistoryReleaseSrc_Type(Integer32):
    """Custom type cCallHistoryReleaseSrc based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("calledPartyInPstn", 3),
          ("calledPartyInVoip", 4),
          ("callingPartyInPstn", 1),
          ("callingPartyInVoip", 2),
          ("consoleCommand", 9),
          ("externalCallControlAgent", 12),
          ("externalGKTMPServer", 14),
          ("externalNmsApp", 11),
          ("externalRadiusServer", 10),
          ("gatekeeper", 13),
          ("internalCallControlApp", 7),
          ("internalReleaseInPotsLeg", 5),
          ("internalReleaseInVoipAAA", 8),
          ("internalReleaseInVoipLeg", 6))
    )


_CCallHistoryReleaseSrc_Type.__name__ = "Integer32"
_CCallHistoryReleaseSrc_Object = MibTableColumn
cCallHistoryReleaseSrc = _CCallHistoryReleaseSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 20),
    _CCallHistoryReleaseSrc_Type()
)
cCallHistoryReleaseSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCallHistoryReleaseSrc.setStatus("current")
_CCallHistoryIecTable_Object = MibTable
cCallHistoryIecTable = _CCallHistoryIecTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 4)
)
if mibBuilder.loadTexts:
    cCallHistoryIecTable.setStatus("current")
_CCallHistoryIecEntry_Object = MibTableRow
cCallHistoryIecEntry = _CCallHistoryIecEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 4, 1)
)
cCallHistoryIecEntry.setIndexNames(
    (0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"),
    (0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIecIndex"),
)
if mibBuilder.loadTexts:
    cCallHistoryIecEntry.setStatus("current")


class _CCallHistoryIecIndex_Type(Unsigned32):
    """Custom type cCallHistoryIecIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CCallHistoryIecIndex_Type.__name__ = "Unsigned32"
_CCallHistoryIecIndex_Object = MibTableColumn
cCallHistoryIecIndex = _CCallHistoryIecIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 4, 1, 1),
    _CCallHistoryIecIndex_Type()
)
cCallHistoryIecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCallHistoryIecIndex.setStatus("current")
_CCallHistoryIec_Type = SnmpAdminString
_CCallHistoryIec_Object = MibTableColumn
cCallHistoryIec = _CCallHistoryIec_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 4, 1, 2),
    _CCallHistoryIec_Type()
)
cCallHistoryIec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCallHistoryIec.setStatus("current")
_CPeerGlobalConfiguration_ObjectIdentity = ObjectIdentity
cPeerGlobalConfiguration = _CPeerGlobalConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 5)
)


class _CPeerSearchType_Type(Integer32):
    """Custom type cPeerSearchType based on Integer32"""
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
        *(("datavoice", 2),
          ("none", 1),
          ("voicedata", 3))
    )


_CPeerSearchType_Type.__name__ = "Integer32"
_CPeerSearchType_Object = MibScalar
cPeerSearchType = _CPeerSearchType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 5, 1),
    _CPeerSearchType_Type()
)
cPeerSearchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cPeerSearchType.setStatus("current")
_CiscoDialControlMibConformance_ObjectIdentity = ObjectIdentity
ciscoDialControlMibConformance = _CiscoDialControlMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 3)
)
_CiscoDialControlMibCompliances_ObjectIdentity = ObjectIdentity
ciscoDialControlMibCompliances = _CiscoDialControlMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 3, 1)
)
_CiscoDialControlMibGroups_ObjectIdentity = ObjectIdentity
ciscoDialControlMibGroups = _CiscoDialControlMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 3, 2)
)

# Managed Objects groups

cCallHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 3, 2, 1)
)
cCallHistoryGroup.setObjects(
      *(("CISCO-DIAL-CONTROL-MIB", "cCallHistorySetupTime"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryPeerAddress"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryPeerSubAddress"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryPeerId"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryPeerIfIndex"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryLogicalIfIndex"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryDisconnectCause"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryDisconnectText"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryConnectTime"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryDisconnectTime"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryCallOrigin"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryChargedUnits"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryInfoType"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryTransmitPackets"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryTransmitBytes"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryReceivePackets"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryReceiveBytes"))
)
if mibBuilder.loadTexts:
    cCallHistoryGroup.setStatus("deprecated")

cCallHistoryGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 3, 2, 2)
)
cCallHistoryGroupRev1.setObjects(
      *(("CISCO-DIAL-CONTROL-MIB", "cCallHistorySetupTime"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryPeerAddress"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryPeerSubAddress"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryPeerId"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryPeerIfIndex"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryLogicalIfIndex"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryDisconnectCause"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryDisconnectText"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryConnectTime"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryDisconnectTime"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryCallOrigin"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryChargedUnits"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryInfoType"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryTransmitPackets"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryTransmitBytes"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryReceivePackets"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryReceiveBytes"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryReleaseSource"))
)
if mibBuilder.loadTexts:
    cCallHistoryGroupRev1.setStatus("deprecated")

cCallHistoryGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 3, 2, 3)
)
cCallHistoryGroupRev2.setObjects(
      *(("CISCO-DIAL-CONTROL-MIB", "cCallHistorySetupTime"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryPeerAddress"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryPeerSubAddress"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryPeerId"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryPeerIfIndex"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryLogicalIfIndex"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryDisconnectCause"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryDisconnectText"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryConnectTime"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryDisconnectTime"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryCallOrigin"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryChargedUnits"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryInfoType"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryTransmitPackets"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryTransmitBytes"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryReceivePackets"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryReceiveBytes"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryReleaseSrc"))
)
if mibBuilder.loadTexts:
    cCallHistoryGroupRev2.setStatus("current")

cPeerGlobalConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 3, 2, 4)
)
cPeerGlobalConfigurationGroup.setObjects(
    ("CISCO-DIAL-CONTROL-MIB", "cPeerSearchType")
)
if mibBuilder.loadTexts:
    cPeerGlobalConfigurationGroup.setStatus("current")

cCallHistoryIecGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 3, 2, 5)
)
cCallHistoryIecGroup.setObjects(
    ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryIec")
)
if mibBuilder.loadTexts:
    cCallHistoryIecGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoDialControlMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDialControlMibCompliance.setStatus(
        "deprecated"
    )

ciscoDialControlMibComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoDialControlMibComplianceRev1.setStatus(
        "deprecated"
    )

ciscoDialControlMibComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoDialControlMibComplianceRev2.setStatus(
        "deprecated"
    )

ciscoDialControlMibComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoDialControlMibComplianceRev3.setStatus(
        "deprecated"
    )

ciscoDialControlMibComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 25, 3, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoDialControlMibComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DIAL-CONTROL-MIB",
    **{"ciscoDialControlMib": ciscoDialControlMib,
       "ciscoDialControlMibObjects": ciscoDialControlMibObjects,
       "cCallHistory": cCallHistory,
       "cCallHistoryTable": cCallHistoryTable,
       "cCallHistoryEntry": cCallHistoryEntry,
       "cCallHistoryIndex": cCallHistoryIndex,
       "cCallHistorySetupTime": cCallHistorySetupTime,
       "cCallHistoryPeerAddress": cCallHistoryPeerAddress,
       "cCallHistoryPeerSubAddress": cCallHistoryPeerSubAddress,
       "cCallHistoryPeerId": cCallHistoryPeerId,
       "cCallHistoryPeerIfIndex": cCallHistoryPeerIfIndex,
       "cCallHistoryLogicalIfIndex": cCallHistoryLogicalIfIndex,
       "cCallHistoryDisconnectCause": cCallHistoryDisconnectCause,
       "cCallHistoryDisconnectText": cCallHistoryDisconnectText,
       "cCallHistoryConnectTime": cCallHistoryConnectTime,
       "cCallHistoryDisconnectTime": cCallHistoryDisconnectTime,
       "cCallHistoryCallOrigin": cCallHistoryCallOrigin,
       "cCallHistoryChargedUnits": cCallHistoryChargedUnits,
       "cCallHistoryInfoType": cCallHistoryInfoType,
       "cCallHistoryTransmitPackets": cCallHistoryTransmitPackets,
       "cCallHistoryTransmitBytes": cCallHistoryTransmitBytes,
       "cCallHistoryReceivePackets": cCallHistoryReceivePackets,
       "cCallHistoryReceiveBytes": cCallHistoryReceiveBytes,
       "cCallHistoryReleaseSource": cCallHistoryReleaseSource,
       "cCallHistoryReleaseSrc": cCallHistoryReleaseSrc,
       "cCallHistoryIecTable": cCallHistoryIecTable,
       "cCallHistoryIecEntry": cCallHistoryIecEntry,
       "cCallHistoryIecIndex": cCallHistoryIecIndex,
       "cCallHistoryIec": cCallHistoryIec,
       "cPeerGlobalConfiguration": cPeerGlobalConfiguration,
       "cPeerSearchType": cPeerSearchType,
       "ciscoDialControlMibConformance": ciscoDialControlMibConformance,
       "ciscoDialControlMibCompliances": ciscoDialControlMibCompliances,
       "ciscoDialControlMibCompliance": ciscoDialControlMibCompliance,
       "ciscoDialControlMibComplianceRev1": ciscoDialControlMibComplianceRev1,
       "ciscoDialControlMibComplianceRev2": ciscoDialControlMibComplianceRev2,
       "ciscoDialControlMibComplianceRev3": ciscoDialControlMibComplianceRev3,
       "ciscoDialControlMibComplianceRev4": ciscoDialControlMibComplianceRev4,
       "ciscoDialControlMibGroups": ciscoDialControlMibGroups,
       "cCallHistoryGroup": cCallHistoryGroup,
       "cCallHistoryGroupRev1": cCallHistoryGroupRev1,
       "cCallHistoryGroupRev2": cCallHistoryGroupRev2,
       "cPeerGlobalConfigurationGroup": cPeerGlobalConfigurationGroup,
       "cCallHistoryIecGroup": cCallHistoryIecGroup}
)
