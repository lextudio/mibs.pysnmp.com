# SNMP MIB module (CAPWAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CAPWAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:33 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 MacAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

capwapMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 999901)
)
capwapMIB.setRevisions(
        ("2007-07-31 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CapwapWTPId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



class CapwapStationId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



class CapwapRadioId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CapwapWTPTunnelMode(Integer32, TextualConvention):
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
        *(("dot3Tunnel", 2),
          ("localBridging", 1),
          ("nativeTunnel", 3))
    )



class CapwapWTPMACType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localMAC", 1),
          ("splitMAC", 2))
    )



class CapwapWTPRadioTemplateIfIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class CapwapChannelType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("control", 2),
          ("data", 1))
    )



class CapwapWTPAuthenMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              8)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("other", 8),
          ("psk", 3),
          ("x509", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CapwapNotifications_ObjectIdentity = ObjectIdentity
capwapNotifications = _CapwapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999901, 0)
)
_CapwapObjects_ObjectIdentity = ObjectIdentity
capwapObjects = _CapwapObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999901, 1)
)
_CapwapObjectState_ObjectIdentity = ObjectIdentity
capwapObjectState = _CapwapObjectState_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1)
)
_CapwapACState_ObjectIdentity = ObjectIdentity
capwapACState = _CapwapACState_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 1)
)
_CapwapACWTPSessions_Type = Unsigned32
_CapwapACWTPSessions_Object = MibScalar
capwapACWTPSessions = _CapwapACWTPSessions_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 1, 1),
    _CapwapACWTPSessions_Type()
)
capwapACWTPSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapACWTPSessions.setStatus("current")
_CapwapACWTPSessionsLimit_Type = Unsigned32
_CapwapACWTPSessionsLimit_Object = MibScalar
capwapACWTPSessionsLimit = _CapwapACWTPSessionsLimit_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 1, 2),
    _CapwapACWTPSessionsLimit_Type()
)
capwapACWTPSessionsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapACWTPSessionsLimit.setStatus("current")
_CapwapACStationSessions_Type = Unsigned32
_CapwapACStationSessions_Object = MibScalar
capwapACStationSessions = _CapwapACStationSessions_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 1, 3),
    _CapwapACStationSessions_Type()
)
capwapACStationSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapACStationSessions.setStatus("current")
_CapwapACStationSessionsLimit_Type = Unsigned32
_CapwapACStationSessionsLimit_Object = MibScalar
capwapACStationSessionsLimit = _CapwapACStationSessionsLimit_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 1, 4),
    _CapwapACStationSessionsLimit_Type()
)
capwapACStationSessionsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapACStationSessionsLimit.setStatus("current")
_CapwapACDataChannelSecOptions_Type = Integer32
_CapwapACDataChannelSecOptions_Object = MibScalar
capwapACDataChannelSecOptions = _CapwapACDataChannelSecOptions_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 1, 5),
    _CapwapACDataChannelSecOptions_Type()
)
capwapACDataChannelSecOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapACDataChannelSecOptions.setStatus("current")
_CapwapACWTPAuthenOptions_Type = Integer32
_CapwapACWTPAuthenOptions_Object = MibScalar
capwapACWTPAuthenOptions = _CapwapACWTPAuthenOptions_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 1, 6),
    _CapwapACWTPAuthenOptions_Type()
)
capwapACWTPAuthenOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapACWTPAuthenOptions.setStatus("current")


class _CapwapACHwVersion_Type(OctetString):
    """Custom type capwapACHwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_CapwapACHwVersion_Type.__name__ = "OctetString"
_CapwapACHwVersion_Object = MibScalar
capwapACHwVersion = _CapwapACHwVersion_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 1, 7),
    _CapwapACHwVersion_Type()
)
capwapACHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapACHwVersion.setStatus("current")


class _CapwapACSwVersion_Type(OctetString):
    """Custom type capwapACSwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_CapwapACSwVersion_Type.__name__ = "OctetString"
_CapwapACSwVersion_Object = MibScalar
capwapACSwVersion = _CapwapACSwVersion_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 1, 8),
    _CapwapACSwVersion_Type()
)
capwapACSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapACSwVersion.setStatus("current")


class _CapwapWTPFallbackEnable_Type(TruthValue):
    """Custom type capwapWTPFallbackEnable based on TruthValue"""


_CapwapWTPFallbackEnable_Object = MibScalar
capwapWTPFallbackEnable = _CapwapWTPFallbackEnable_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 1, 9),
    _CapwapWTPFallbackEnable_Type()
)
capwapWTPFallbackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapWTPFallbackEnable.setStatus("current")
_CapwapWTPACNameList_Type = Unsigned32
_CapwapWTPACNameList_Object = MibScalar
capwapWTPACNameList = _CapwapWTPACNameList_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 1, 10),
    _CapwapWTPACNameList_Type()
)
capwapWTPACNameList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapWTPACNameList.setStatus("current")


class _CapwapMaxFailedDTLSSessionRetry_Type(Unsigned32):
    """Custom type capwapMaxFailedDTLSSessionRetry based on Unsigned32"""
    defaultValue = 3


_CapwapMaxFailedDTLSSessionRetry_Object = MibScalar
capwapMaxFailedDTLSSessionRetry = _CapwapMaxFailedDTLSSessionRetry_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 1, 11),
    _CapwapMaxFailedDTLSSessionRetry_Type()
)
capwapMaxFailedDTLSSessionRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapMaxFailedDTLSSessionRetry.setStatus("current")


class _CapwapWTPIdleTimeout_Type(Unsigned32):
    """Custom type capwapWTPIdleTimeout based on Unsigned32"""
    defaultValue = 300


_CapwapWTPIdleTimeout_Object = MibScalar
capwapWTPIdleTimeout = _CapwapWTPIdleTimeout_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 1, 12),
    _CapwapWTPIdleTimeout_Type()
)
capwapWTPIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    capwapWTPIdleTimeout.setUnits("kbtyes")


class _CapwapWTPMaxDiscoveries_Type(Unsigned32):
    """Custom type capwapWTPMaxDiscoveries based on Unsigned32"""
    defaultValue = 10


_CapwapWTPMaxDiscoveries_Object = MibScalar
capwapWTPMaxDiscoveries = _CapwapWTPMaxDiscoveries_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 1, 13),
    _CapwapWTPMaxDiscoveries_Type()
)
capwapWTPMaxDiscoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPMaxDiscoveries.setStatus("current")


class _CapwapWTPMaxRetransmit_Type(Unsigned32):
    """Custom type capwapWTPMaxRetransmit based on Unsigned32"""
    defaultValue = 5


_CapwapWTPMaxRetransmit_Object = MibScalar
capwapWTPMaxRetransmit = _CapwapWTPMaxRetransmit_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 1, 14),
    _CapwapWTPMaxRetransmit_Type()
)
capwapWTPMaxRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPMaxRetransmit.setStatus("current")


class _CapwapWTPReportInterval_Type(Unsigned32):
    """Custom type capwapWTPReportInterval based on Unsigned32"""
    defaultValue = 120


_CapwapWTPReportInterval_Object = MibScalar
capwapWTPReportInterval = _CapwapWTPReportInterval_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 1, 15),
    _CapwapWTPReportInterval_Type()
)
capwapWTPReportInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    capwapWTPReportInterval.setUnits("second")
_CapwapWTPStateTable_Object = MibTable
capwapWTPStateTable = _CapwapWTPStateTable_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 2)
)
if mibBuilder.loadTexts:
    capwapWTPStateTable.setStatus("current")
_CapwapWTPStateEntry_Object = MibTableRow
capwapWTPStateEntry = _CapwapWTPStateEntry_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 2, 1)
)
capwapWTPStateEntry.setIndexNames(
    (0, "CAPWAP-MIB", "capwapWTPId"),
)
if mibBuilder.loadTexts:
    capwapWTPStateEntry.setStatus("current")
_CapwapWTPId_Type = CapwapWTPId
_CapwapWTPId_Object = MibTableColumn
capwapWTPId = _CapwapWTPId_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 2, 1, 1),
    _CapwapWTPId_Type()
)
capwapWTPId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapWTPId.setStatus("current")
_CapwapWTPIPAddress_Type = IpAddress
_CapwapWTPIPAddress_Object = MibTableColumn
capwapWTPIPAddress = _CapwapWTPIPAddress_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 2, 1, 2),
    _CapwapWTPIPAddress_Type()
)
capwapWTPIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPIPAddress.setStatus("current")


class _CapwapWTPSerialId_Type(OctetString):
    """Custom type capwapWTPSerialId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_CapwapWTPSerialId_Type.__name__ = "OctetString"
_CapwapWTPSerialId_Object = MibTableColumn
capwapWTPSerialId = _CapwapWTPSerialId_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 2, 1, 3),
    _CapwapWTPSerialId_Type()
)
capwapWTPSerialId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPSerialId.setStatus("current")


class _CapwapWTPState_Type(Integer32):
    """Custom type capwapWTPState based on Integer32"""
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
        *(("clear", 6),
          ("configure", 4),
          ("dtls", 1),
          ("image", 3),
          ("join", 2),
          ("run", 5))
    )


_CapwapWTPState_Type.__name__ = "Integer32"
_CapwapWTPState_Object = MibTableColumn
capwapWTPState = _CapwapWTPState_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 2, 1, 4),
    _CapwapWTPState_Type()
)
capwapWTPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPState.setStatus("current")
_CapwapWTPTable_Object = MibTable
capwapWTPTable = _CapwapWTPTable_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 3)
)
if mibBuilder.loadTexts:
    capwapWTPTable.setStatus("current")
_CapwapWTPEntry_Object = MibTableRow
capwapWTPEntry = _CapwapWTPEntry_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 3, 1)
)
capwapWTPEntry.setIndexNames(
    (0, "CAPWAP-MIB", "capwapWTPCurrId"),
)
if mibBuilder.loadTexts:
    capwapWTPEntry.setStatus("current")
_CapwapWTPCurrId_Type = CapwapWTPId
_CapwapWTPCurrId_Object = MibTableColumn
capwapWTPCurrId = _CapwapWTPCurrId_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 3, 1, 1),
    _CapwapWTPCurrId_Type()
)
capwapWTPCurrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capwapWTPCurrId.setStatus("current")
_CapwapWTPName_Type = DisplayString
_CapwapWTPName_Object = MibTableColumn
capwapWTPName = _CapwapWTPName_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 3, 1, 2),
    _CapwapWTPName_Type()
)
capwapWTPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapWTPName.setStatus("current")
_CapwapWTPLocation_Type = DisplayString
_CapwapWTPLocation_Object = MibTableColumn
capwapWTPLocation = _CapwapWTPLocation_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 3, 1, 3),
    _CapwapWTPLocation_Type()
)
capwapWTPLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapWTPLocation.setStatus("current")
_CapwapWTPManufacturerId_Type = ObjectIdentifier
_CapwapWTPManufacturerId_Object = MibTableColumn
capwapWTPManufacturerId = _CapwapWTPManufacturerId_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 3, 1, 4),
    _CapwapWTPManufacturerId_Type()
)
capwapWTPManufacturerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPManufacturerId.setStatus("current")
_CapwapWTPModelId_Type = Unsigned32
_CapwapWTPModelId_Object = MibTableColumn
capwapWTPModelId = _CapwapWTPModelId_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 3, 1, 5),
    _CapwapWTPModelId_Type()
)
capwapWTPModelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPModelId.setStatus("current")
_CapwapWTPBoardId_Type = Unsigned32
_CapwapWTPBoardId_Object = MibTableColumn
capwapWTPBoardId = _CapwapWTPBoardId_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 3, 1, 6),
    _CapwapWTPBoardId_Type()
)
capwapWTPBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPBoardId.setStatus("current")
_CapwapWTPBoardRevision_Type = Unsigned32
_CapwapWTPBoardRevision_Object = MibTableColumn
capwapWTPBoardRevision = _CapwapWTPBoardRevision_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 3, 1, 7),
    _CapwapWTPBoardRevision_Type()
)
capwapWTPBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPBoardRevision.setStatus("current")
_CapwapWTPBaseMACAddress_Type = MacAddress
_CapwapWTPBaseMACAddress_Object = MibTableColumn
capwapWTPBaseMACAddress = _CapwapWTPBaseMACAddress_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 3, 1, 8),
    _CapwapWTPBaseMACAddress_Type()
)
capwapWTPBaseMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPBaseMACAddress.setStatus("current")
_CapwapWTPTunnelModeOptions_Type = CapwapWTPTunnelMode
_CapwapWTPTunnelModeOptions_Object = MibTableColumn
capwapWTPTunnelModeOptions = _CapwapWTPTunnelModeOptions_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 3, 1, 9),
    _CapwapWTPTunnelModeOptions_Type()
)
capwapWTPTunnelModeOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPTunnelModeOptions.setStatus("current")
_CapwapWTPMACTypeOptions_Type = CapwapWTPMACType
_CapwapWTPMACTypeOptions_Object = MibTableColumn
capwapWTPMACTypeOptions = _CapwapWTPMACTypeOptions_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 3, 1, 10),
    _CapwapWTPMACTypeOptions_Type()
)
capwapWTPMACTypeOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPMACTypeOptions.setStatus("current")


class _CapwapWTPDiscoveryType_Type(Integer32):
    """Custom type capwapWTPDiscoveryType based on Integer32"""
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
        *(("acRef", 5),
          ("dhcp", 3),
          ("dns", 4),
          ("staticConfig", 2),
          ("unknown", 1))
    )


_CapwapWTPDiscoveryType_Type.__name__ = "Integer32"
_CapwapWTPDiscoveryType_Object = MibTableColumn
capwapWTPDiscoveryType = _CapwapWTPDiscoveryType_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 3, 1, 11),
    _CapwapWTPDiscoveryType_Type()
)
capwapWTPDiscoveryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPDiscoveryType.setStatus("current")
_CapwapWTPRadiosInUseNumber_Type = Unsigned32
_CapwapWTPRadiosInUseNumber_Object = MibTableColumn
capwapWTPRadiosInUseNumber = _CapwapWTPRadiosInUseNumber_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 3, 1, 12),
    _CapwapWTPRadiosInUseNumber_Type()
)
capwapWTPRadiosInUseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPRadiosInUseNumber.setStatus("current")
_CapwapWTPRadioNumLimit_Type = Unsigned32
_CapwapWTPRadioNumLimit_Object = MibTableColumn
capwapWTPRadioNumLimit = _CapwapWTPRadioNumLimit_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 3, 1, 13),
    _CapwapWTPRadioNumLimit_Type()
)
capwapWTPRadioNumLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPRadioNumLimit.setStatus("current")


class _CapwapWTPSwVersion_Type(OctetString):
    """Custom type capwapWTPSwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_CapwapWTPSwVersion_Type.__name__ = "OctetString"
_CapwapWTPSwVersion_Object = MibTableColumn
capwapWTPSwVersion = _CapwapWTPSwVersion_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 3, 1, 14),
    _CapwapWTPSwVersion_Type()
)
capwapWTPSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPSwVersion.setStatus("current")
_CapwapWTPSwSize_Type = Unsigned32
_CapwapWTPSwSize_Object = MibTableColumn
capwapWTPSwSize = _CapwapWTPSwSize_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 3, 1, 15),
    _CapwapWTPSwSize_Type()
)
capwapWTPSwSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPSwSize.setStatus("current")
if mibBuilder.loadTexts:
    capwapWTPSwSize.setUnits("kbtyes")


class _CapwapWTPHwVersion_Type(OctetString):
    """Custom type capwapWTPHwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_CapwapWTPHwVersion_Type.__name__ = "OctetString"
_CapwapWTPHwVersion_Object = MibTableColumn
capwapWTPHwVersion = _CapwapWTPHwVersion_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 3, 1, 16),
    _CapwapWTPHwVersion_Type()
)
capwapWTPHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPHwVersion.setStatus("current")


class _CapwapWTPStaticIPEnable_Type(TruthValue):
    """Custom type capwapWTPStaticIPEnable based on TruthValue"""


_CapwapWTPStaticIPEnable_Object = MibTableColumn
capwapWTPStaticIPEnable = _CapwapWTPStaticIPEnable_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 3, 1, 17),
    _CapwapWTPStaticIPEnable_Type()
)
capwapWTPStaticIPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapWTPStaticIPEnable.setStatus("current")
_CapwapWTPStaticIP_Type = IpAddress
_CapwapWTPStaticIP_Object = MibTableColumn
capwapWTPStaticIP = _CapwapWTPStaticIP_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 3, 1, 18),
    _CapwapWTPStaticIP_Type()
)
capwapWTPStaticIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapWTPStaticIP.setStatus("current")
_CapwapWTPNetmask_Type = IpAddress
_CapwapWTPNetmask_Object = MibTableColumn
capwapWTPNetmask = _CapwapWTPNetmask_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 3, 1, 19),
    _CapwapWTPNetmask_Type()
)
capwapWTPNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapWTPNetmask.setStatus("current")
_CapwapWTPGateway_Type = IpAddress
_CapwapWTPGateway_Object = MibTableColumn
capwapWTPGateway = _CapwapWTPGateway_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 3, 1, 20),
    _CapwapWTPGateway_Type()
)
capwapWTPGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapWTPGateway.setStatus("current")
_CapwapRadioTable_Object = MibTable
capwapRadioTable = _CapwapRadioTable_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 4)
)
if mibBuilder.loadTexts:
    capwapRadioTable.setStatus("current")
_CapwapRadioEntry_Object = MibTableRow
capwapRadioEntry = _CapwapRadioEntry_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 4, 1)
)
capwapRadioEntry.setIndexNames(
    (0, "CAPWAP-MIB", "capwapWTPCurrId"),
    (0, "CAPWAP-MIB", "capwapRadioId"),
)
if mibBuilder.loadTexts:
    capwapRadioEntry.setStatus("current")
_CapwapRadioId_Type = CapwapRadioId
_CapwapRadioId_Object = MibTableColumn
capwapRadioId = _CapwapRadioId_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 4, 1, 1),
    _CapwapRadioId_Type()
)
capwapRadioId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapRadioId.setStatus("current")
_CapwapWTPRadioTemplateIfIndex_Type = CapwapWTPRadioTemplateIfIndex
_CapwapWTPRadioTemplateIfIndex_Object = MibTableColumn
capwapWTPRadioTemplateIfIndex = _CapwapWTPRadioTemplateIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 4, 1, 2),
    _CapwapWTPRadioTemplateIfIndex_Type()
)
capwapWTPRadioTemplateIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapWTPRadioTemplateIfIndex.setStatus("current")


class _CapwapWirelessBinding_Type(Integer32):
    """Custom type capwapWirelessBinding based on Integer32"""
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
        *(("dot11", 2),
          ("dot16", 3),
          ("epc", 4),
          ("none", 1))
    )


_CapwapWirelessBinding_Type.__name__ = "Integer32"
_CapwapWirelessBinding_Object = MibTableColumn
capwapWirelessBinding = _CapwapWirelessBinding_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 4, 1, 3),
    _CapwapWirelessBinding_Type()
)
capwapWirelessBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWirelessBinding.setStatus("current")


class _CapwapAdminStatusEnable_Type(TruthValue):
    """Custom type capwapAdminStatusEnable based on TruthValue"""


_CapwapAdminStatusEnable_Object = MibTableColumn
capwapAdminStatusEnable = _CapwapAdminStatusEnable_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 4, 1, 4),
    _CapwapAdminStatusEnable_Type()
)
capwapAdminStatusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapAdminStatusEnable.setStatus("current")
_CapwapOperStatus_Type = TruthValue
_CapwapOperStatus_Object = MibTableColumn
capwapOperStatus = _CapwapOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 4, 1, 5),
    _CapwapOperStatus_Type()
)
capwapOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapOperStatus.setStatus("current")
_CapwapStationTable_Object = MibTable
capwapStationTable = _CapwapStationTable_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 5)
)
if mibBuilder.loadTexts:
    capwapStationTable.setStatus("current")
_CapwapStationEntry_Object = MibTableRow
capwapStationEntry = _CapwapStationEntry_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 5, 1)
)
capwapStationEntry.setIndexNames(
    (0, "CAPWAP-MIB", "capwapWTPCurrId"),
    (0, "CAPWAP-MIB", "capwapRadioId"),
    (0, "CAPWAP-MIB", "capwapStationId"),
)
if mibBuilder.loadTexts:
    capwapStationEntry.setStatus("current")
_CapwapStationId_Type = CapwapStationId
_CapwapStationId_Object = MibTableColumn
capwapStationId = _CapwapStationId_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 5, 1, 1),
    _CapwapStationId_Type()
)
capwapStationId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capwapStationId.setStatus("current")
_CapwapStationAddedTime_Type = TimeStamp
_CapwapStationAddedTime_Object = MibTableColumn
capwapStationAddedTime = _CapwapStationAddedTime_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 5, 1, 2),
    _CapwapStationAddedTime_Type()
)
capwapStationAddedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapStationAddedTime.setStatus("current")


class _CapwapStationVlanName_Type(OctetString):
    """Custom type capwapStationVlanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_CapwapStationVlanName_Type.__name__ = "OctetString"
_CapwapStationVlanName_Object = MibTableColumn
capwapStationVlanName = _CapwapStationVlanName_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 1, 5, 1, 3),
    _CapwapStationVlanName_Type()
)
capwapStationVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapStationVlanName.setStatus("current")
_CapwapObjectsStats_ObjectIdentity = ObjectIdentity
capwapObjectsStats = _CapwapObjectsStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2)
)
_CapwapWTPRebootStatsTable_Object = MibTable
capwapWTPRebootStatsTable = _CapwapWTPRebootStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2, 1)
)
if mibBuilder.loadTexts:
    capwapWTPRebootStatsTable.setStatus("current")
_CapwapWTPRebootStatsEntry_Object = MibTableRow
capwapWTPRebootStatsEntry = _CapwapWTPRebootStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2, 1, 1)
)
capwapWTPRebootStatsEntry.setIndexNames(
    (0, "CAPWAP-MIB", "capwapWTPCurrId"),
)
if mibBuilder.loadTexts:
    capwapWTPRebootStatsEntry.setStatus("current")
_CapwapWTPRebootCount_Type = Counter32
_CapwapWTPRebootCount_Object = MibTableColumn
capwapWTPRebootCount = _CapwapWTPRebootCount_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2, 1, 1, 1),
    _CapwapWTPRebootCount_Type()
)
capwapWTPRebootCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPRebootCount.setStatus("current")
_CapwapWTPInitCount_Type = Counter32
_CapwapWTPInitCount_Object = MibTableColumn
capwapWTPInitCount = _CapwapWTPInitCount_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2, 1, 1, 2),
    _CapwapWTPInitCount_Type()
)
capwapWTPInitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPInitCount.setStatus("current")
_CapwapWTPLinkFailureCount_Type = Counter32
_CapwapWTPLinkFailureCount_Object = MibTableColumn
capwapWTPLinkFailureCount = _CapwapWTPLinkFailureCount_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2, 1, 1, 3),
    _CapwapWTPLinkFailureCount_Type()
)
capwapWTPLinkFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPLinkFailureCount.setStatus("current")
_CapwapWTPSwFailureCount_Type = Counter32
_CapwapWTPSwFailureCount_Object = MibTableColumn
capwapWTPSwFailureCount = _CapwapWTPSwFailureCount_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2, 1, 1, 4),
    _CapwapWTPSwFailureCount_Type()
)
capwapWTPSwFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPSwFailureCount.setStatus("current")
_CapwapWTPHwFailureCount_Type = Counter32
_CapwapWTPHwFailureCount_Object = MibTableColumn
capwapWTPHwFailureCount = _CapwapWTPHwFailureCount_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2, 1, 1, 5),
    _CapwapWTPHwFailureCount_Type()
)
capwapWTPHwFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPHwFailureCount.setStatus("current")
_CapwapWTPOtherFailureCount_Type = Counter32
_CapwapWTPOtherFailureCount_Object = MibTableColumn
capwapWTPOtherFailureCount = _CapwapWTPOtherFailureCount_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2, 1, 1, 6),
    _CapwapWTPOtherFailureCount_Type()
)
capwapWTPOtherFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPOtherFailureCount.setStatus("current")
_CapwapWTPUnknownFailureCount_Type = Counter32
_CapwapWTPUnknownFailureCount_Object = MibTableColumn
capwapWTPUnknownFailureCount = _CapwapWTPUnknownFailureCount_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2, 1, 1, 7),
    _CapwapWTPUnknownFailureCount_Type()
)
capwapWTPUnknownFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPUnknownFailureCount.setStatus("current")


class _CapwapWTPLastFailureType_Type(Integer32):
    """Custom type capwapWTPLastFailureType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("acInit", 2),
          ("hwFailure", 5),
          ("linkfailure", 3),
          ("notSupport", 1),
          ("other", 6),
          ("swFailure", 4),
          ("unknown", 255))
    )


_CapwapWTPLastFailureType_Type.__name__ = "Integer32"
_CapwapWTPLastFailureType_Object = MibTableColumn
capwapWTPLastFailureType = _CapwapWTPLastFailureType_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2, 1, 1, 8),
    _CapwapWTPLastFailureType_Type()
)
capwapWTPLastFailureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWTPLastFailureType.setStatus("current")
_CapwapRadioStatsTable_Object = MibTable
capwapRadioStatsTable = _CapwapRadioStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2, 2)
)
if mibBuilder.loadTexts:
    capwapRadioStatsTable.setStatus("current")
_CapwapRadioStatsEntry_Object = MibTableRow
capwapRadioStatsEntry = _CapwapRadioStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2, 2, 1)
)
capwapRadioStatsEntry.setIndexNames(
    (0, "CAPWAP-MIB", "capwapWTPCurrId"),
    (0, "CAPWAP-MIB", "capwapRadioId"),
)
if mibBuilder.loadTexts:
    capwapRadioStatsEntry.setStatus("current")
_CapwapRadioResetCount_Type = Counter32
_CapwapRadioResetCount_Object = MibTableColumn
capwapRadioResetCount = _CapwapRadioResetCount_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2, 2, 1, 1),
    _CapwapRadioResetCount_Type()
)
capwapRadioResetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapRadioResetCount.setStatus("current")
_CapwapRadioSwFailCount_Type = Counter32
_CapwapRadioSwFailCount_Object = MibTableColumn
capwapRadioSwFailCount = _CapwapRadioSwFailCount_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2, 2, 1, 2),
    _CapwapRadioSwFailCount_Type()
)
capwapRadioSwFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapRadioSwFailCount.setStatus("current")
_CapwapRadioHwFailCount_Type = Counter32
_CapwapRadioHwFailCount_Object = MibTableColumn
capwapRadioHwFailCount = _CapwapRadioHwFailCount_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2, 2, 1, 3),
    _CapwapRadioHwFailCount_Type()
)
capwapRadioHwFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapRadioHwFailCount.setStatus("current")
_CapwapRadioOtherFailCount_Type = Counter32
_CapwapRadioOtherFailCount_Object = MibTableColumn
capwapRadioOtherFailCount = _CapwapRadioOtherFailCount_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2, 2, 1, 4),
    _CapwapRadioOtherFailCount_Type()
)
capwapRadioOtherFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapRadioOtherFailCount.setStatus("current")
_CapwapRadioUnknownFailCount_Type = Counter32
_CapwapRadioUnknownFailCount_Object = MibTableColumn
capwapRadioUnknownFailCount = _CapwapRadioUnknownFailCount_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2, 2, 1, 5),
    _CapwapRadioUnknownFailCount_Type()
)
capwapRadioUnknownFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapRadioUnknownFailCount.setStatus("current")
_CapwapRadioConfigUpdateCount_Type = Counter32
_CapwapRadioConfigUpdateCount_Object = MibTableColumn
capwapRadioConfigUpdateCount = _CapwapRadioConfigUpdateCount_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2, 2, 1, 6),
    _CapwapRadioConfigUpdateCount_Type()
)
capwapRadioConfigUpdateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapRadioConfigUpdateCount.setStatus("current")
_CapwapRadioChannelChangeCount_Type = Counter32
_CapwapRadioChannelChangeCount_Object = MibTableColumn
capwapRadioChannelChangeCount = _CapwapRadioChannelChangeCount_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2, 2, 1, 7),
    _CapwapRadioChannelChangeCount_Type()
)
capwapRadioChannelChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapRadioChannelChangeCount.setStatus("current")
_CapwapRadioBandChangeCount_Type = Counter32
_CapwapRadioBandChangeCount_Object = MibTableColumn
capwapRadioBandChangeCount = _CapwapRadioBandChangeCount_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2, 2, 1, 8),
    _CapwapRadioBandChangeCount_Type()
)
capwapRadioBandChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapRadioBandChangeCount.setStatus("current")
_CapwapRadioCurrentNoiseFloor_Type = Integer32
_CapwapRadioCurrentNoiseFloor_Object = MibTableColumn
capwapRadioCurrentNoiseFloor = _CapwapRadioCurrentNoiseFloor_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2, 2, 1, 9),
    _CapwapRadioCurrentNoiseFloor_Type()
)
capwapRadioCurrentNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapRadioCurrentNoiseFloor.setStatus("current")
if mibBuilder.loadTexts:
    capwapRadioCurrentNoiseFloor.setUnits("dbm")
_CapwapRadioDecryptErrorCount_Type = Counter32
_CapwapRadioDecryptErrorCount_Object = MibTableColumn
capwapRadioDecryptErrorCount = _CapwapRadioDecryptErrorCount_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2, 2, 1, 10),
    _CapwapRadioDecryptErrorCount_Type()
)
capwapRadioDecryptErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapRadioDecryptErrorCount.setStatus("current")


class _CapwapRadioTxQueueLevel_Type(Integer32):
    """Custom type capwapRadioTxQueueLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CapwapRadioTxQueueLevel_Type.__name__ = "Integer32"
_CapwapRadioTxQueueLevel_Object = MibTableColumn
capwapRadioTxQueueLevel = _CapwapRadioTxQueueLevel_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2, 2, 1, 11),
    _CapwapRadioTxQueueLevel_Type()
)
capwapRadioTxQueueLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapRadioTxQueueLevel.setStatus("current")
_CapwapRadioRFLinkFramesPerSec_Type = Counter32
_CapwapRadioRFLinkFramesPerSec_Object = MibTableColumn
capwapRadioRFLinkFramesPerSec = _CapwapRadioRFLinkFramesPerSec_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2, 2, 1, 12),
    _CapwapRadioRFLinkFramesPerSec_Type()
)
capwapRadioRFLinkFramesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapRadioRFLinkFramesPerSec.setStatus("current")


class _CapwapRadioLastFailType_Type(Integer32):
    """Custom type capwapRadioLastFailType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("hwFailure", 3),
          ("notSupport", 1),
          ("otherFailure", 4),
          ("swFailure", 2),
          ("unknown", 255))
    )


_CapwapRadioLastFailType_Type.__name__ = "Integer32"
_CapwapRadioLastFailType_Object = MibTableColumn
capwapRadioLastFailType = _CapwapRadioLastFailType_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 2, 2, 1, 13),
    _CapwapRadioLastFailType_Type()
)
capwapRadioLastFailType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapRadioLastFailType.setStatus("current")
_CapwapNotifyVarObjects_ObjectIdentity = ObjectIdentity
capwapNotifyVarObjects = _CapwapNotifyVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999901, 1, 3)
)
_CapwapChannelType_Type = CapwapChannelType
_CapwapChannelType_Object = MibScalar
capwapChannelType = _CapwapChannelType_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 3, 1),
    _CapwapChannelType_Type()
)
capwapChannelType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapChannelType.setStatus("current")
_CapwapWTPAuthenMethod_Type = CapwapWTPAuthenMethod
_CapwapWTPAuthenMethod_Object = MibScalar
capwapWTPAuthenMethod = _CapwapWTPAuthenMethod_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 3, 2),
    _CapwapWTPAuthenMethod_Type()
)
capwapWTPAuthenMethod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapWTPAuthenMethod.setStatus("current")


class _CapwapChannelDownReason_Type(Integer32):
    """Custom type capwapChannelDownReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("apReboot", 3),
          ("rekeyfailure", 2),
          ("timeout", 1))
    )


_CapwapChannelDownReason_Type.__name__ = "Integer32"
_CapwapChannelDownReason_Object = MibScalar
capwapChannelDownReason = _CapwapChannelDownReason_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 3, 3),
    _CapwapChannelDownReason_Type()
)
capwapChannelDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapChannelDownReason.setStatus("current")
_CapwapIdEntryNum_Type = Unsigned32
_CapwapIdEntryNum_Object = MibScalar
capwapIdEntryNum = _CapwapIdEntryNum_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 3, 4),
    _CapwapIdEntryNum_Type()
)
capwapIdEntryNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapIdEntryNum.setStatus("current")
_CapwapStationIdList_Type = OctetString
_CapwapStationIdList_Object = MibScalar
capwapStationIdList = _CapwapStationIdList_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 3, 5),
    _CapwapStationIdList_Type()
)
capwapStationIdList.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapStationIdList.setStatus("current")


class _CapwapWTPAuthenFailureReason_Type(Integer32):
    """Custom type capwapWTPAuthenFailureReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("invalidCA", 2),
          ("keyMismatch", 1),
          ("micError", 3),
          ("timeout", 4),
          ("unknown", 8))
    )


_CapwapWTPAuthenFailureReason_Type.__name__ = "Integer32"
_CapwapWTPAuthenFailureReason_Object = MibScalar
capwapWTPAuthenFailureReason = _CapwapWTPAuthenFailureReason_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 3, 6),
    _CapwapWTPAuthenFailureReason_Type()
)
capwapWTPAuthenFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapWTPAuthenFailureReason.setStatus("current")


class _CapwapRadioOperStatusFlag_Type(Integer32):
    """Custom type capwapRadioOperStatusFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inoperable", 2),
          ("operable", 1))
    )


_CapwapRadioOperStatusFlag_Type.__name__ = "Integer32"
_CapwapRadioOperStatusFlag_Object = MibScalar
capwapRadioOperStatusFlag = _CapwapRadioOperStatusFlag_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 3, 7),
    _CapwapRadioOperStatusFlag_Type()
)
capwapRadioOperStatusFlag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapRadioOperStatusFlag.setStatus("current")


class _CapwapRadioFailureReason_Type(Integer32):
    """Custom type capwapRadioFailureReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              8)
        )
    )
    namedValues = NamedValues(
        *(("adminSet", 3),
          ("hwError", 1),
          ("swError", 2),
          ("unknown", 8))
    )


_CapwapRadioFailureReason_Type.__name__ = "Integer32"
_CapwapRadioFailureReason_Object = MibScalar
capwapRadioFailureReason = _CapwapRadioFailureReason_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 3, 8),
    _CapwapRadioFailureReason_Type()
)
capwapRadioFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapRadioFailureReason.setStatus("current")


class _CapwapJoinFailureReason_Type(Integer32):
    """Custom type capwapJoinFailureReason based on Integer32"""
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
        *(("incorrectData", 4),
          ("notSupportBinding", 7),
          ("notSupportHw", 6),
          ("resDepletion", 2),
          ("sessionInUse", 5),
          ("unknownSource", 3),
          ("unspecified", 1))
    )


_CapwapJoinFailureReason_Type.__name__ = "Integer32"
_CapwapJoinFailureReason_Object = MibScalar
capwapJoinFailureReason = _CapwapJoinFailureReason_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 3, 9),
    _CapwapJoinFailureReason_Type()
)
capwapJoinFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapJoinFailureReason.setStatus("current")


class _CapwapImageFailureReason_Type(Integer32):
    """Custom type capwapImageFailureReason based on Integer32"""
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
        *(("inUse", 4),
          ("invalidChecksum", 1),
          ("invalidLength", 2),
          ("other", 3))
    )


_CapwapImageFailureReason_Type.__name__ = "Integer32"
_CapwapImageFailureReason_Object = MibScalar
capwapImageFailureReason = _CapwapImageFailureReason_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 3, 10),
    _CapwapImageFailureReason_Type()
)
capwapImageFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapImageFailureReason.setStatus("current")


class _CapwapConfigMsgErrorType_Type(Integer32):
    """Custom type capwapConfigMsgErrorType based on Integer32"""
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
        *(("unknownElement", 1),
          ("unknownValue", 3),
          ("unsupportedElement", 2),
          ("unsupportedValue", 4))
    )


_CapwapConfigMsgErrorType_Type.__name__ = "Integer32"
_CapwapConfigMsgErrorType_Object = MibScalar
capwapConfigMsgErrorType = _CapwapConfigMsgErrorType_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 3, 11),
    _CapwapConfigMsgErrorType_Type()
)
capwapConfigMsgErrorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapConfigMsgErrorType.setStatus("current")
_CapwapMsgErrorElements_Type = DisplayString
_CapwapMsgErrorElements_Object = MibScalar
capwapMsgErrorElements = _CapwapMsgErrorElements_Object(
    (1, 3, 6, 1, 2, 1, 999901, 1, 3, 12),
    _CapwapMsgErrorElements_Type()
)
capwapMsgErrorElements.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapMsgErrorElements.setStatus("current")
_CapwapConformance_ObjectIdentity = ObjectIdentity
capwapConformance = _CapwapConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999901, 2)
)
_CapwapGroups_ObjectIdentity = ObjectIdentity
capwapGroups = _CapwapGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999901, 2, 1)
)
_CapwapCompliances_ObjectIdentity = ObjectIdentity
capwapCompliances = _CapwapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999901, 2, 2)
)

# Managed Objects groups

capwapACNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999901, 2, 1, 1)
)
capwapACNodeGroup.setObjects(
      *(("CAPWAP-MIB", "capwapACWTPSessions"),
        ("CAPWAP-MIB", "capwapACWTPSessionsLimit"),
        ("CAPWAP-MIB", "capwapACStationSessions"),
        ("CAPWAP-MIB", "capwapACStationSessionsLimit"),
        ("CAPWAP-MIB", "capwapACDataChannelSecOptions"),
        ("CAPWAP-MIB", "capwapACWTPAuthenOptions"),
        ("CAPWAP-MIB", "capwapACHwVersion"),
        ("CAPWAP-MIB", "capwapACSwVersion"))
)
if mibBuilder.loadTexts:
    capwapACNodeGroup.setStatus("current")

capwapWTPStateGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999901, 2, 1, 2)
)
capwapWTPStateGroup.setObjects(
      *(("CAPWAP-MIB", "capwapWTPIPAddress"),
        ("CAPWAP-MIB", "capwapWTPSerialId"),
        ("CAPWAP-MIB", "capwapWTPState"))
)
if mibBuilder.loadTexts:
    capwapWTPStateGroup.setStatus("current")

capwapWTPsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999901, 2, 1, 3)
)
capwapWTPsGroup.setObjects(
      *(("CAPWAP-MIB", "capwapWTPFallbackEnable"),
        ("CAPWAP-MIB", "capwapWTPACNameList"),
        ("CAPWAP-MIB", "capwapMaxFailedDTLSSessionRetry"),
        ("CAPWAP-MIB", "capwapWTPIdleTimeout"),
        ("CAPWAP-MIB", "capwapWTPMaxDiscoveries"),
        ("CAPWAP-MIB", "capwapWTPMaxRetransmit"),
        ("CAPWAP-MIB", "capwapWTPReportInterval"),
        ("CAPWAP-MIB", "capwapWTPName"),
        ("CAPWAP-MIB", "capwapWTPLocation"),
        ("CAPWAP-MIB", "capwapWTPManufacturerId"),
        ("CAPWAP-MIB", "capwapWTPModelId"),
        ("CAPWAP-MIB", "capwapWTPTunnelModeOptions"),
        ("CAPWAP-MIB", "capwapWTPMACTypeOptions"),
        ("CAPWAP-MIB", "capwapWTPDiscoveryType"),
        ("CAPWAP-MIB", "capwapWTPRadiosInUseNumber"),
        ("CAPWAP-MIB", "capwapWTPRadioNumLimit"),
        ("CAPWAP-MIB", "capwapWTPSwVersion"),
        ("CAPWAP-MIB", "capwapWTPSwSize"),
        ("CAPWAP-MIB", "capwapWTPHwVersion"))
)
if mibBuilder.loadTexts:
    capwapWTPsGroup.setStatus("current")

capwapRadiosGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999901, 2, 1, 4)
)
capwapRadiosGroup.setObjects(
      *(("CAPWAP-MIB", "capwapWTPRadioTemplateIfIndex"),
        ("CAPWAP-MIB", "capwapWirelessBinding"),
        ("CAPWAP-MIB", "capwapAdminStatusEnable"),
        ("CAPWAP-MIB", "capwapOperStatus"))
)
if mibBuilder.loadTexts:
    capwapRadiosGroup.setStatus("current")

capwapStationsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999901, 2, 1, 5)
)
capwapStationsGroup.setObjects(
      *(("CAPWAP-MIB", "capwapStationAddedTime"),
        ("CAPWAP-MIB", "capwapStationVlanName"))
)
if mibBuilder.loadTexts:
    capwapStationsGroup.setStatus("current")

capwapWTPsPhysicalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999901, 2, 1, 6)
)
capwapWTPsPhysicalGroup.setObjects(
      *(("CAPWAP-MIB", "capwapWTPBoardId"),
        ("CAPWAP-MIB", "capwapWTPBoardRevision"),
        ("CAPWAP-MIB", "capwapWTPBaseMACAddress"))
)
if mibBuilder.loadTexts:
    capwapWTPsPhysicalGroup.setStatus("current")

capwapWTPsLayer3Group = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999901, 2, 1, 7)
)
capwapWTPsLayer3Group.setObjects(
      *(("CAPWAP-MIB", "capwapWTPStaticIPEnable"),
        ("CAPWAP-MIB", "capwapWTPStaticIP"),
        ("CAPWAP-MIB", "capwapWTPNetmask"),
        ("CAPWAP-MIB", "capwapWTPGateway"))
)
if mibBuilder.loadTexts:
    capwapWTPsLayer3Group.setStatus("current")

capwapWTPRebootStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999901, 2, 1, 8)
)
capwapWTPRebootStatsGroup.setObjects(
      *(("CAPWAP-MIB", "capwapWTPRebootCount"),
        ("CAPWAP-MIB", "capwapWTPInitCount"),
        ("CAPWAP-MIB", "capwapWTPLinkFailureCount"),
        ("CAPWAP-MIB", "capwapWTPSwFailureCount"),
        ("CAPWAP-MIB", "capwapWTPHwFailureCount"),
        ("CAPWAP-MIB", "capwapWTPOtherFailureCount"),
        ("CAPWAP-MIB", "capwapWTPUnknownFailureCount"),
        ("CAPWAP-MIB", "capwapWTPLastFailureType"))
)
if mibBuilder.loadTexts:
    capwapWTPRebootStatsGroup.setStatus("current")

capwapRadioStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999901, 2, 1, 9)
)
capwapRadioStatsGroup.setObjects(
      *(("CAPWAP-MIB", "capwapRadioResetCount"),
        ("CAPWAP-MIB", "capwapRadioSwFailCount"),
        ("CAPWAP-MIB", "capwapRadioHwFailCount"),
        ("CAPWAP-MIB", "capwapRadioOtherFailCount"),
        ("CAPWAP-MIB", "capwapRadioUnknownFailCount"),
        ("CAPWAP-MIB", "capwapRadioConfigUpdateCount"),
        ("CAPWAP-MIB", "capwapRadioChannelChangeCount"),
        ("CAPWAP-MIB", "capwapRadioBandChangeCount"),
        ("CAPWAP-MIB", "capwapRadioCurrentNoiseFloor"),
        ("CAPWAP-MIB", "capwapRadioDecryptErrorCount"),
        ("CAPWAP-MIB", "capwapRadioTxQueueLevel"),
        ("CAPWAP-MIB", "capwapRadioRFLinkFramesPerSec"),
        ("CAPWAP-MIB", "capwapRadioLastFailType"))
)
if mibBuilder.loadTexts:
    capwapRadioStatsGroup.setStatus("current")

capwapNotifyVarGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999901, 2, 1, 11)
)
capwapNotifyVarGroup.setObjects(
      *(("CAPWAP-MIB", "capwapWTPId"),
        ("CAPWAP-MIB", "capwapRadioId"),
        ("CAPWAP-MIB", "capwapChannelType"),
        ("CAPWAP-MIB", "capwapWTPAuthenMethod"),
        ("CAPWAP-MIB", "capwapChannelDownReason"),
        ("CAPWAP-MIB", "capwapIdEntryNum"),
        ("CAPWAP-MIB", "capwapStationIdList"),
        ("CAPWAP-MIB", "capwapWTPAuthenFailureReason"),
        ("CAPWAP-MIB", "capwapRadioOperStatusFlag"),
        ("CAPWAP-MIB", "capwapRadioFailureReason"),
        ("CAPWAP-MIB", "capwapJoinFailureReason"),
        ("CAPWAP-MIB", "capwapImageFailureReason"),
        ("CAPWAP-MIB", "capwapConfigMsgErrorType"),
        ("CAPWAP-MIB", "capwapMsgErrorElements"))
)
if mibBuilder.loadTexts:
    capwapNotifyVarGroup.setStatus("current")


# Notification objects

capwapChannelUp = NotificationType(
    (1, 3, 6, 1, 2, 1, 999901, 0, 1)
)
capwapChannelUp.setObjects(
      *(("CAPWAP-MIB", "capwapWTPId"),
        ("CAPWAP-MIB", "capwapChannelType"),
        ("CAPWAP-MIB", "capwapWTPAuthenMethod"))
)
if mibBuilder.loadTexts:
    capwapChannelUp.setStatus(
        "current"
    )

capwapChannelDown = NotificationType(
    (1, 3, 6, 1, 2, 1, 999901, 0, 2)
)
capwapChannelDown.setObjects(
      *(("CAPWAP-MIB", "capwapWTPId"),
        ("CAPWAP-MIB", "capwapChannelDownReason"))
)
if mibBuilder.loadTexts:
    capwapChannelDown.setStatus(
        "current"
    )

capwapDecryptErrorReport = NotificationType(
    (1, 3, 6, 1, 2, 1, 999901, 0, 3)
)
capwapDecryptErrorReport.setObjects(
      *(("CAPWAP-MIB", "capwapWTPId"),
        ("CAPWAP-MIB", "capwapRadioId"),
        ("CAPWAP-MIB", "capwapIdEntryNum"),
        ("CAPWAP-MIB", "capwapStationIdList"))
)
if mibBuilder.loadTexts:
    capwapDecryptErrorReport.setStatus(
        "current"
    )

capwapJoinFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 999901, 0, 4)
)
capwapJoinFailure.setObjects(
      *(("CAPWAP-MIB", "capwapWTPId"),
        ("CAPWAP-MIB", "capwapJoinFailureReason"))
)
if mibBuilder.loadTexts:
    capwapJoinFailure.setStatus(
        "current"
    )

capwapImageUpgradeFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 999901, 0, 5)
)
capwapImageUpgradeFailure.setObjects(
      *(("CAPWAP-MIB", "capwapWTPId"),
        ("CAPWAP-MIB", "capwapImageFailureReason"))
)
if mibBuilder.loadTexts:
    capwapImageUpgradeFailure.setStatus(
        "current"
    )

capwapConfigMsgError = NotificationType(
    (1, 3, 6, 1, 2, 1, 999901, 0, 6)
)
capwapConfigMsgError.setObjects(
      *(("CAPWAP-MIB", "capwapWTPId"),
        ("CAPWAP-MIB", "capwapConfigMsgErrorType"),
        ("CAPWAP-MIB", "capwapMsgErrorElements"))
)
if mibBuilder.loadTexts:
    capwapConfigMsgError.setStatus(
        "current"
    )

capwapRadioOperableStatus = NotificationType(
    (1, 3, 6, 1, 2, 1, 999901, 0, 7)
)
capwapRadioOperableStatus.setObjects(
      *(("CAPWAP-MIB", "capwapWTPId"),
        ("CAPWAP-MIB", "capwapRadioId"),
        ("CAPWAP-MIB", "capwapRadioOperStatusFlag"),
        ("CAPWAP-MIB", "capwapRadioFailureReason"))
)
if mibBuilder.loadTexts:
    capwapRadioOperableStatus.setStatus(
        "current"
    )

capwapWTPAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 999901, 0, 8)
)
capwapWTPAuthenticationFailure.setObjects(
      *(("CAPWAP-MIB", "capwapWTPId"),
        ("CAPWAP-MIB", "capwapChannelType"),
        ("CAPWAP-MIB", "capwapWTPAuthenMethod"),
        ("CAPWAP-MIB", "capwapWTPAuthenFailureReason"))
)
if mibBuilder.loadTexts:
    capwapWTPAuthenticationFailure.setStatus(
        "current"
    )


# Notifications groups

capwapNofificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 999901, 2, 1, 10)
)
capwapNofificationGroup.setObjects(
      *(("CAPWAP-MIB", "capwapChannelUp"),
        ("CAPWAP-MIB", "capwapChannelDown"),
        ("CAPWAP-MIB", "capwapDecryptErrorReport"),
        ("CAPWAP-MIB", "capwapJoinFailure"),
        ("CAPWAP-MIB", "capwapImageUpgradeFailure"),
        ("CAPWAP-MIB", "capwapConfigMsgError"),
        ("CAPWAP-MIB", "capwapRadioOperableStatus"),
        ("CAPWAP-MIB", "capwapWTPAuthenticationFailure"))
)
if mibBuilder.loadTexts:
    capwapNofificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

capwapFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 999901, 2, 2, 1)
)
if mibBuilder.loadTexts:
    capwapFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAPWAP-MIB",
    **{"CapwapWTPId": CapwapWTPId,
       "CapwapStationId": CapwapStationId,
       "CapwapRadioId": CapwapRadioId,
       "CapwapWTPTunnelMode": CapwapWTPTunnelMode,
       "CapwapWTPMACType": CapwapWTPMACType,
       "CapwapWTPRadioTemplateIfIndex": CapwapWTPRadioTemplateIfIndex,
       "CapwapChannelType": CapwapChannelType,
       "CapwapWTPAuthenMethod": CapwapWTPAuthenMethod,
       "capwapMIB": capwapMIB,
       "capwapNotifications": capwapNotifications,
       "capwapChannelUp": capwapChannelUp,
       "capwapChannelDown": capwapChannelDown,
       "capwapDecryptErrorReport": capwapDecryptErrorReport,
       "capwapJoinFailure": capwapJoinFailure,
       "capwapImageUpgradeFailure": capwapImageUpgradeFailure,
       "capwapConfigMsgError": capwapConfigMsgError,
       "capwapRadioOperableStatus": capwapRadioOperableStatus,
       "capwapWTPAuthenticationFailure": capwapWTPAuthenticationFailure,
       "capwapObjects": capwapObjects,
       "capwapObjectState": capwapObjectState,
       "capwapACState": capwapACState,
       "capwapACWTPSessions": capwapACWTPSessions,
       "capwapACWTPSessionsLimit": capwapACWTPSessionsLimit,
       "capwapACStationSessions": capwapACStationSessions,
       "capwapACStationSessionsLimit": capwapACStationSessionsLimit,
       "capwapACDataChannelSecOptions": capwapACDataChannelSecOptions,
       "capwapACWTPAuthenOptions": capwapACWTPAuthenOptions,
       "capwapACHwVersion": capwapACHwVersion,
       "capwapACSwVersion": capwapACSwVersion,
       "capwapWTPFallbackEnable": capwapWTPFallbackEnable,
       "capwapWTPACNameList": capwapWTPACNameList,
       "capwapMaxFailedDTLSSessionRetry": capwapMaxFailedDTLSSessionRetry,
       "capwapWTPIdleTimeout": capwapWTPIdleTimeout,
       "capwapWTPMaxDiscoveries": capwapWTPMaxDiscoveries,
       "capwapWTPMaxRetransmit": capwapWTPMaxRetransmit,
       "capwapWTPReportInterval": capwapWTPReportInterval,
       "capwapWTPStateTable": capwapWTPStateTable,
       "capwapWTPStateEntry": capwapWTPStateEntry,
       "capwapWTPId": capwapWTPId,
       "capwapWTPIPAddress": capwapWTPIPAddress,
       "capwapWTPSerialId": capwapWTPSerialId,
       "capwapWTPState": capwapWTPState,
       "capwapWTPTable": capwapWTPTable,
       "capwapWTPEntry": capwapWTPEntry,
       "capwapWTPCurrId": capwapWTPCurrId,
       "capwapWTPName": capwapWTPName,
       "capwapWTPLocation": capwapWTPLocation,
       "capwapWTPManufacturerId": capwapWTPManufacturerId,
       "capwapWTPModelId": capwapWTPModelId,
       "capwapWTPBoardId": capwapWTPBoardId,
       "capwapWTPBoardRevision": capwapWTPBoardRevision,
       "capwapWTPBaseMACAddress": capwapWTPBaseMACAddress,
       "capwapWTPTunnelModeOptions": capwapWTPTunnelModeOptions,
       "capwapWTPMACTypeOptions": capwapWTPMACTypeOptions,
       "capwapWTPDiscoveryType": capwapWTPDiscoveryType,
       "capwapWTPRadiosInUseNumber": capwapWTPRadiosInUseNumber,
       "capwapWTPRadioNumLimit": capwapWTPRadioNumLimit,
       "capwapWTPSwVersion": capwapWTPSwVersion,
       "capwapWTPSwSize": capwapWTPSwSize,
       "capwapWTPHwVersion": capwapWTPHwVersion,
       "capwapWTPStaticIPEnable": capwapWTPStaticIPEnable,
       "capwapWTPStaticIP": capwapWTPStaticIP,
       "capwapWTPNetmask": capwapWTPNetmask,
       "capwapWTPGateway": capwapWTPGateway,
       "capwapRadioTable": capwapRadioTable,
       "capwapRadioEntry": capwapRadioEntry,
       "capwapRadioId": capwapRadioId,
       "capwapWTPRadioTemplateIfIndex": capwapWTPRadioTemplateIfIndex,
       "capwapWirelessBinding": capwapWirelessBinding,
       "capwapAdminStatusEnable": capwapAdminStatusEnable,
       "capwapOperStatus": capwapOperStatus,
       "capwapStationTable": capwapStationTable,
       "capwapStationEntry": capwapStationEntry,
       "capwapStationId": capwapStationId,
       "capwapStationAddedTime": capwapStationAddedTime,
       "capwapStationVlanName": capwapStationVlanName,
       "capwapObjectsStats": capwapObjectsStats,
       "capwapWTPRebootStatsTable": capwapWTPRebootStatsTable,
       "capwapWTPRebootStatsEntry": capwapWTPRebootStatsEntry,
       "capwapWTPRebootCount": capwapWTPRebootCount,
       "capwapWTPInitCount": capwapWTPInitCount,
       "capwapWTPLinkFailureCount": capwapWTPLinkFailureCount,
       "capwapWTPSwFailureCount": capwapWTPSwFailureCount,
       "capwapWTPHwFailureCount": capwapWTPHwFailureCount,
       "capwapWTPOtherFailureCount": capwapWTPOtherFailureCount,
       "capwapWTPUnknownFailureCount": capwapWTPUnknownFailureCount,
       "capwapWTPLastFailureType": capwapWTPLastFailureType,
       "capwapRadioStatsTable": capwapRadioStatsTable,
       "capwapRadioStatsEntry": capwapRadioStatsEntry,
       "capwapRadioResetCount": capwapRadioResetCount,
       "capwapRadioSwFailCount": capwapRadioSwFailCount,
       "capwapRadioHwFailCount": capwapRadioHwFailCount,
       "capwapRadioOtherFailCount": capwapRadioOtherFailCount,
       "capwapRadioUnknownFailCount": capwapRadioUnknownFailCount,
       "capwapRadioConfigUpdateCount": capwapRadioConfigUpdateCount,
       "capwapRadioChannelChangeCount": capwapRadioChannelChangeCount,
       "capwapRadioBandChangeCount": capwapRadioBandChangeCount,
       "capwapRadioCurrentNoiseFloor": capwapRadioCurrentNoiseFloor,
       "capwapRadioDecryptErrorCount": capwapRadioDecryptErrorCount,
       "capwapRadioTxQueueLevel": capwapRadioTxQueueLevel,
       "capwapRadioRFLinkFramesPerSec": capwapRadioRFLinkFramesPerSec,
       "capwapRadioLastFailType": capwapRadioLastFailType,
       "capwapNotifyVarObjects": capwapNotifyVarObjects,
       "capwapChannelType": capwapChannelType,
       "capwapWTPAuthenMethod": capwapWTPAuthenMethod,
       "capwapChannelDownReason": capwapChannelDownReason,
       "capwapIdEntryNum": capwapIdEntryNum,
       "capwapStationIdList": capwapStationIdList,
       "capwapWTPAuthenFailureReason": capwapWTPAuthenFailureReason,
       "capwapRadioOperStatusFlag": capwapRadioOperStatusFlag,
       "capwapRadioFailureReason": capwapRadioFailureReason,
       "capwapJoinFailureReason": capwapJoinFailureReason,
       "capwapImageFailureReason": capwapImageFailureReason,
       "capwapConfigMsgErrorType": capwapConfigMsgErrorType,
       "capwapMsgErrorElements": capwapMsgErrorElements,
       "capwapConformance": capwapConformance,
       "capwapGroups": capwapGroups,
       "capwapACNodeGroup": capwapACNodeGroup,
       "capwapWTPStateGroup": capwapWTPStateGroup,
       "capwapWTPsGroup": capwapWTPsGroup,
       "capwapRadiosGroup": capwapRadiosGroup,
       "capwapStationsGroup": capwapStationsGroup,
       "capwapWTPsPhysicalGroup": capwapWTPsPhysicalGroup,
       "capwapWTPsLayer3Group": capwapWTPsLayer3Group,
       "capwapWTPRebootStatsGroup": capwapWTPRebootStatsGroup,
       "capwapRadioStatsGroup": capwapRadioStatsGroup,
       "capwapNofificationGroup": capwapNofificationGroup,
       "capwapNotifyVarGroup": capwapNotifyVarGroup,
       "capwapCompliances": capwapCompliances,
       "capwapFullCompliance": capwapFullCompliance}
)
