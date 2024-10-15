# SNMP MIB module (LIGO-RADIO3-DRV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LIGO-RADIO3-DRV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:18:11 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ligoMgmt,) = mibBuilder.importSymbols(
    "LIGOWAVE-MIB",
    "ligoMgmt")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysLocation,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysLocation")

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

ligoRadio3DrvMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8)
)
ligoRadio3DrvMIB.setRevisions(
        ("2010-01-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LigoRadio3DrvMIBObjects_ObjectIdentity = ObjectIdentity
ligoRadio3DrvMIBObjects = _LigoRadio3DrvMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1)
)
_LigoRdo3DrvNotifs_ObjectIdentity = ObjectIdentity
ligoRdo3DrvNotifs = _LigoRdo3DrvNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 0)
)
_LigoRdo3DrvInfo_ObjectIdentity = ObjectIdentity
ligoRdo3DrvInfo = _LigoRdo3DrvInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 1)
)
_LigoRdo3DrvConf_ObjectIdentity = ObjectIdentity
ligoRdo3DrvConf = _LigoRdo3DrvConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 2)
)
_LigoRdo3DrvStats_ObjectIdentity = ObjectIdentity
ligoRdo3DrvStats = _LigoRdo3DrvStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3)
)
_LigoRdo3StatsTable_Object = MibTable
ligoRdo3StatsTable = _LigoRdo3StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ligoRdo3StatsTable.setStatus("current")
_LigoRdo3StatsEntry_Object = MibTableRow
ligoRdo3StatsEntry = _LigoRdo3StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1)
)
ligoRdo3StatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "LIGO-RADIO3-DRV-MIB", "ligoRdo3Endpoint"),
)
if mibBuilder.loadTexts:
    ligoRdo3StatsEntry.setStatus("current")
_LigoRdo3Endpoint_Type = Integer32
_LigoRdo3Endpoint_Object = MibTableColumn
ligoRdo3Endpoint = _LigoRdo3Endpoint_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 1),
    _LigoRdo3Endpoint_Type()
)
ligoRdo3Endpoint.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ligoRdo3Endpoint.setStatus("current")
_LigoRdo3LastUpdate_Type = TimeTicks
_LigoRdo3LastUpdate_Object = MibTableColumn
ligoRdo3LastUpdate = _LigoRdo3LastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 2),
    _LigoRdo3LastUpdate_Type()
)
ligoRdo3LastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3LastUpdate.setStatus("current")
_LigoRdo3MacAddress_Type = MacAddress
_LigoRdo3MacAddress_Object = MibTableColumn
ligoRdo3MacAddress = _LigoRdo3MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 3),
    _LigoRdo3MacAddress_Type()
)
ligoRdo3MacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3MacAddress.setStatus("current")
_LigoRdo3IpAddress_Type = IpAddress
_LigoRdo3IpAddress_Object = MibTableColumn
ligoRdo3IpAddress = _LigoRdo3IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 4),
    _LigoRdo3IpAddress_Type()
)
ligoRdo3IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3IpAddress.setStatus("current")
_LigoRdo3CountryCode_Type = OctetString
_LigoRdo3CountryCode_Object = MibTableColumn
ligoRdo3CountryCode = _LigoRdo3CountryCode_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 5),
    _LigoRdo3CountryCode_Type()
)
ligoRdo3CountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3CountryCode.setStatus("current")
_LigoRdo3Encryption_Type = OctetString
_LigoRdo3Encryption_Object = MibTableColumn
ligoRdo3Encryption = _LigoRdo3Encryption_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 6),
    _LigoRdo3Encryption_Type()
)
ligoRdo3Encryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3Encryption.setStatus("current")
_LigoRdo3Parameters_Type = OctetString
_LigoRdo3Parameters_Object = MibTableColumn
ligoRdo3Parameters = _LigoRdo3Parameters_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 7),
    _LigoRdo3Parameters_Type()
)
ligoRdo3Parameters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3Parameters.setStatus("current")
_LigoRdo3Capabilities_Type = OctetString
_LigoRdo3Capabilities_Object = MibTableColumn
ligoRdo3Capabilities = _LigoRdo3Capabilities_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 8),
    _LigoRdo3Capabilities_Type()
)
ligoRdo3Capabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3Capabilities.setStatus("current")
_LigoRdo3TxPower_Type = Gauge32
_LigoRdo3TxPower_Object = MibTableColumn
ligoRdo3TxPower = _LigoRdo3TxPower_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 9),
    _LigoRdo3TxPower_Type()
)
ligoRdo3TxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxPower.setStatus("current")
_LigoRdo3TxPackets_Type = Counter32
_LigoRdo3TxPackets_Object = MibTableColumn
ligoRdo3TxPackets = _LigoRdo3TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 10),
    _LigoRdo3TxPackets_Type()
)
ligoRdo3TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxPackets.setStatus("current")
_LigoRdo3TxBytes_Type = Counter32
_LigoRdo3TxBytes_Object = MibTableColumn
ligoRdo3TxBytes = _LigoRdo3TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 11),
    _LigoRdo3TxBytes_Type()
)
ligoRdo3TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxBytes.setStatus("current")
_LigoRdo3TxXmitFailed_Type = Counter32
_LigoRdo3TxXmitFailed_Object = MibTableColumn
ligoRdo3TxXmitFailed = _LigoRdo3TxXmitFailed_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 12),
    _LigoRdo3TxXmitFailed_Type()
)
ligoRdo3TxXmitFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxXmitFailed.setStatus("current")
_LigoRdo3TxXmitDropped_Type = Counter32
_LigoRdo3TxXmitDropped_Object = MibTableColumn
ligoRdo3TxXmitDropped = _LigoRdo3TxXmitDropped_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 13),
    _LigoRdo3TxXmitDropped_Type()
)
ligoRdo3TxXmitDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxXmitDropped.setStatus("current")
_LigoRdo3TxOverruns_Type = Counter32
_LigoRdo3TxOverruns_Object = MibTableColumn
ligoRdo3TxOverruns = _LigoRdo3TxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 14),
    _LigoRdo3TxOverruns_Type()
)
ligoRdo3TxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxOverruns.setStatus("current")
_LigoRdo3TxSuccess_Type = Counter32
_LigoRdo3TxSuccess_Object = MibTableColumn
ligoRdo3TxSuccess = _LigoRdo3TxSuccess_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 15),
    _LigoRdo3TxSuccess_Type()
)
ligoRdo3TxSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxSuccess.setStatus("current")
_LigoRdo3TxFailed_Type = Counter32
_LigoRdo3TxFailed_Object = MibTableColumn
ligoRdo3TxFailed = _LigoRdo3TxFailed_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 16),
    _LigoRdo3TxFailed_Type()
)
ligoRdo3TxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxFailed.setStatus("current")
_LigoRdo3TxRetried_Type = Counter32
_LigoRdo3TxRetried_Object = MibTableColumn
ligoRdo3TxRetried = _LigoRdo3TxRetried_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 17),
    _LigoRdo3TxRetried_Type()
)
ligoRdo3TxRetried.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxRetried.setStatus("current")
_LigoRdo3TxNotRetried_Type = Counter32
_LigoRdo3TxNotRetried_Object = MibTableColumn
ligoRdo3TxNotRetried = _LigoRdo3TxNotRetried_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 18),
    _LigoRdo3TxNotRetried_Type()
)
ligoRdo3TxNotRetried.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxNotRetried.setStatus("current")
_LigoRdo3TxPacketsPerMcs_Type = OctetString
_LigoRdo3TxPacketsPerMcs_Object = MibTableColumn
ligoRdo3TxPacketsPerMcs = _LigoRdo3TxPacketsPerMcs_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 19),
    _LigoRdo3TxPacketsPerMcs_Type()
)
ligoRdo3TxPacketsPerMcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxPacketsPerMcs.setStatus("current")
_LigoRdo3TxMsdus_Type = Counter32
_LigoRdo3TxMsdus_Object = MibTableColumn
ligoRdo3TxMsdus = _LigoRdo3TxMsdus_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 20),
    _LigoRdo3TxMsdus_Type()
)
ligoRdo3TxMsdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxMsdus.setStatus("current")
_LigoRdo3TxNotAggregated_Type = Counter32
_LigoRdo3TxNotAggregated_Object = MibTableColumn
ligoRdo3TxNotAggregated = _LigoRdo3TxNotAggregated_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 21),
    _LigoRdo3TxNotAggregated_Type()
)
ligoRdo3TxNotAggregated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxNotAggregated.setStatus("current")
_LigoRdo3TxAckRequired_Type = Counter32
_LigoRdo3TxAckRequired_Object = MibTableColumn
ligoRdo3TxAckRequired = _LigoRdo3TxAckRequired_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 22),
    _LigoRdo3TxAckRequired_Type()
)
ligoRdo3TxAckRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxAckRequired.setStatus("current")
_LigoRdo3TxNoAckRequired_Type = Counter32
_LigoRdo3TxNoAckRequired_Object = MibTableColumn
ligoRdo3TxNoAckRequired = _LigoRdo3TxNoAckRequired_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 23),
    _LigoRdo3TxNoAckRequired_Type()
)
ligoRdo3TxNoAckRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxNoAckRequired.setStatus("current")
_LigoRdo3TxAltRate_Type = Counter32
_LigoRdo3TxAltRate_Object = MibTableColumn
ligoRdo3TxAltRate = _LigoRdo3TxAltRate_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 24),
    _LigoRdo3TxAltRate_Type()
)
ligoRdo3TxAltRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxAltRate.setStatus("current")
_LigoRdo3TxManagement_Type = Counter32
_LigoRdo3TxManagement_Object = MibTableColumn
ligoRdo3TxManagement = _LigoRdo3TxManagement_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 25),
    _LigoRdo3TxManagement_Type()
)
ligoRdo3TxManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxManagement.setStatus("current")
_LigoRdo3TxLegacy_Type = Counter32
_LigoRdo3TxLegacy_Object = MibTableColumn
ligoRdo3TxLegacy = _LigoRdo3TxLegacy_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 26),
    _LigoRdo3TxLegacy_Type()
)
ligoRdo3TxLegacy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxLegacy.setStatus("current")
_LigoRdo3TxLegacyBytes_Type = Counter32
_LigoRdo3TxLegacyBytes_Object = MibTableColumn
ligoRdo3TxLegacyBytes = _LigoRdo3TxLegacyBytes_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 27),
    _LigoRdo3TxLegacyBytes_Type()
)
ligoRdo3TxLegacyBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxLegacyBytes.setStatus("current")
_LigoRdo3TxAmsdus_Type = Counter32
_LigoRdo3TxAmsdus_Object = MibTableColumn
ligoRdo3TxAmsdus = _LigoRdo3TxAmsdus_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 28),
    _LigoRdo3TxAmsdus_Type()
)
ligoRdo3TxAmsdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxAmsdus.setStatus("current")
_LigoRdo3TxPktsInAmsdus_Type = Counter32
_LigoRdo3TxPktsInAmsdus_Object = MibTableColumn
ligoRdo3TxPktsInAmsdus = _LigoRdo3TxPktsInAmsdus_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 29),
    _LigoRdo3TxPktsInAmsdus_Type()
)
ligoRdo3TxPktsInAmsdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxPktsInAmsdus.setStatus("current")
_LigoRdo3TxAmsduBytes_Type = Counter32
_LigoRdo3TxAmsduBytes_Object = MibTableColumn
ligoRdo3TxAmsduBytes = _LigoRdo3TxAmsduBytes_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 30),
    _LigoRdo3TxAmsduBytes_Type()
)
ligoRdo3TxAmsduBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxAmsduBytes.setStatus("current")
_LigoRdo3TxMpdus_Type = Counter32
_LigoRdo3TxMpdus_Object = MibTableColumn
ligoRdo3TxMpdus = _LigoRdo3TxMpdus_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 31),
    _LigoRdo3TxMpdus_Type()
)
ligoRdo3TxMpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxMpdus.setStatus("current")
_LigoRdo3TxMpduBytes_Type = Counter32
_LigoRdo3TxMpduBytes_Object = MibTableColumn
ligoRdo3TxMpduBytes = _LigoRdo3TxMpduBytes_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 32),
    _LigoRdo3TxMpduBytes_Type()
)
ligoRdo3TxMpduBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxMpduBytes.setStatus("current")
_LigoRdo3TxFragmented_Type = Counter32
_LigoRdo3TxFragmented_Object = MibTableColumn
ligoRdo3TxFragmented = _LigoRdo3TxFragmented_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 33),
    _LigoRdo3TxFragmented_Type()
)
ligoRdo3TxFragmented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxFragmented.setStatus("current")
_LigoRdo3TxFragBytes_Type = Counter32
_LigoRdo3TxFragBytes_Object = MibTableColumn
ligoRdo3TxFragBytes = _LigoRdo3TxFragBytes_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 34),
    _LigoRdo3TxFragBytes_Type()
)
ligoRdo3TxFragBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3TxFragBytes.setStatus("current")
_LigoRdo3RxPackets_Type = Counter32
_LigoRdo3RxPackets_Object = MibTableColumn
ligoRdo3RxPackets = _LigoRdo3RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 35),
    _LigoRdo3RxPackets_Type()
)
ligoRdo3RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxPackets.setStatus("current")
_LigoRdo3RxBytes_Type = Counter32
_LigoRdo3RxBytes_Object = MibTableColumn
ligoRdo3RxBytes = _LigoRdo3RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 36),
    _LigoRdo3RxBytes_Type()
)
ligoRdo3RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxBytes.setStatus("current")
_LigoRdo3RxDropped_Type = Counter32
_LigoRdo3RxDropped_Object = MibTableColumn
ligoRdo3RxDropped = _LigoRdo3RxDropped_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 37),
    _LigoRdo3RxDropped_Type()
)
ligoRdo3RxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxDropped.setStatus("current")
_LigoRdo3RxCrcErrors_Type = Counter32
_LigoRdo3RxCrcErrors_Object = MibTableColumn
ligoRdo3RxCrcErrors = _LigoRdo3RxCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 38),
    _LigoRdo3RxCrcErrors_Type()
)
ligoRdo3RxCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxCrcErrors.setStatus("current")
_LigoRdo3RxIcvErrors_Type = Counter32
_LigoRdo3RxIcvErrors_Object = MibTableColumn
ligoRdo3RxIcvErrors = _LigoRdo3RxIcvErrors_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 39),
    _LigoRdo3RxIcvErrors_Type()
)
ligoRdo3RxIcvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxIcvErrors.setStatus("current")
_LigoRdo3RxMicErrors_Type = Counter32
_LigoRdo3RxMicErrors_Object = MibTableColumn
ligoRdo3RxMicErrors = _LigoRdo3RxMicErrors_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 40),
    _LigoRdo3RxMicErrors_Type()
)
ligoRdo3RxMicErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxMicErrors.setStatus("current")
_LigoRdo3RxKeyNotValid_Type = Counter32
_LigoRdo3RxKeyNotValid_Object = MibTableColumn
ligoRdo3RxKeyNotValid = _LigoRdo3RxKeyNotValid_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 41),
    _LigoRdo3RxKeyNotValid_Type()
)
ligoRdo3RxKeyNotValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxKeyNotValid.setStatus("current")
_LigoRdo3RxAclDiscarded_Type = Counter32
_LigoRdo3RxAclDiscarded_Object = MibTableColumn
ligoRdo3RxAclDiscarded = _LigoRdo3RxAclDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 42),
    _LigoRdo3RxAclDiscarded_Type()
)
ligoRdo3RxAclDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxAclDiscarded.setStatus("current")
_LigoRdo3RxManagement_Type = Counter32
_LigoRdo3RxManagement_Object = MibTableColumn
ligoRdo3RxManagement = _LigoRdo3RxManagement_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 43),
    _LigoRdo3RxManagement_Type()
)
ligoRdo3RxManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxManagement.setStatus("current")
_LigoRdo3RxControl_Type = Counter32
_LigoRdo3RxControl_Object = MibTableColumn
ligoRdo3RxControl = _LigoRdo3RxControl_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 44),
    _LigoRdo3RxControl_Type()
)
ligoRdo3RxControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxControl.setStatus("current")
_LigoRdo3RxData_Type = Counter32
_LigoRdo3RxData_Object = MibTableColumn
ligoRdo3RxData = _LigoRdo3RxData_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 45),
    _LigoRdo3RxData_Type()
)
ligoRdo3RxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxData.setStatus("current")
_LigoRdo3RxUnknown_Type = Counter32
_LigoRdo3RxUnknown_Object = MibTableColumn
ligoRdo3RxUnknown = _LigoRdo3RxUnknown_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 46),
    _LigoRdo3RxUnknown_Type()
)
ligoRdo3RxUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxUnknown.setStatus("current")
_LigoRdo3RxNullData_Type = Counter32
_LigoRdo3RxNullData_Object = MibTableColumn
ligoRdo3RxNullData = _LigoRdo3RxNullData_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 47),
    _LigoRdo3RxNullData_Type()
)
ligoRdo3RxNullData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxNullData.setStatus("current")
_LigoRdo3RxBroadcast_Type = Counter32
_LigoRdo3RxBroadcast_Object = MibTableColumn
ligoRdo3RxBroadcast = _LigoRdo3RxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 48),
    _LigoRdo3RxBroadcast_Type()
)
ligoRdo3RxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxBroadcast.setStatus("current")
_LigoRdo3RxMulticast_Type = Counter32
_LigoRdo3RxMulticast_Object = MibTableColumn
ligoRdo3RxMulticast = _LigoRdo3RxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 49),
    _LigoRdo3RxMulticast_Type()
)
ligoRdo3RxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxMulticast.setStatus("current")
_LigoRdo3RxUnicast_Type = Counter32
_LigoRdo3RxUnicast_Object = MibTableColumn
ligoRdo3RxUnicast = _LigoRdo3RxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 50),
    _LigoRdo3RxUnicast_Type()
)
ligoRdo3RxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxUnicast.setStatus("current")
_LigoRdo3RxCck_Type = Counter32
_LigoRdo3RxCck_Object = MibTableColumn
ligoRdo3RxCck = _LigoRdo3RxCck_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 51),
    _LigoRdo3RxCck_Type()
)
ligoRdo3RxCck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxCck.setStatus("current")
_LigoRdo3RxOfdm_Type = Counter32
_LigoRdo3RxOfdm_Object = MibTableColumn
ligoRdo3RxOfdm = _LigoRdo3RxOfdm_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 52),
    _LigoRdo3RxOfdm_Type()
)
ligoRdo3RxOfdm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxOfdm.setStatus("current")
_LigoRdo3RxHtMixedMode_Type = Counter32
_LigoRdo3RxHtMixedMode_Object = MibTableColumn
ligoRdo3RxHtMixedMode = _LigoRdo3RxHtMixedMode_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 53),
    _LigoRdo3RxHtMixedMode_Type()
)
ligoRdo3RxHtMixedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxHtMixedMode.setStatus("current")
_LigoRdo3RxHtGreenfield_Type = Counter32
_LigoRdo3RxHtGreenfield_Object = MibTableColumn
ligoRdo3RxHtGreenfield = _LigoRdo3RxHtGreenfield_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 54),
    _LigoRdo3RxHtGreenfield_Type()
)
ligoRdo3RxHtGreenfield.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxHtGreenfield.setStatus("current")
_LigoRdo3RxAmsdus_Type = Counter32
_LigoRdo3RxAmsdus_Object = MibTableColumn
ligoRdo3RxAmsdus = _LigoRdo3RxAmsdus_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 55),
    _LigoRdo3RxAmsdus_Type()
)
ligoRdo3RxAmsdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxAmsdus.setStatus("current")
_LigoRdo3RxPacketsInAmsdus_Type = Counter32
_LigoRdo3RxPacketsInAmsdus_Object = MibTableColumn
ligoRdo3RxPacketsInAmsdus = _LigoRdo3RxPacketsInAmsdus_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 56),
    _LigoRdo3RxPacketsInAmsdus_Type()
)
ligoRdo3RxPacketsInAmsdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxPacketsInAmsdus.setStatus("current")
_LigoRdo3RxAmpdus_Type = Counter32
_LigoRdo3RxAmpdus_Object = MibTableColumn
ligoRdo3RxAmpdus = _LigoRdo3RxAmpdus_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 57),
    _LigoRdo3RxAmpdus_Type()
)
ligoRdo3RxAmpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxAmpdus.setStatus("current")
_LigoRdo3RxMpduBytes_Type = Counter32
_LigoRdo3RxMpduBytes_Object = MibTableColumn
ligoRdo3RxMpduBytes = _LigoRdo3RxMpduBytes_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 58),
    _LigoRdo3RxMpduBytes_Type()
)
ligoRdo3RxMpduBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxMpduBytes.setStatus("current")
_LigoRdo3RxRoBufTotal_Type = Counter32
_LigoRdo3RxRoBufTotal_Object = MibTableColumn
ligoRdo3RxRoBufTotal = _LigoRdo3RxRoBufTotal_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 59),
    _LigoRdo3RxRoBufTotal_Type()
)
ligoRdo3RxRoBufTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxRoBufTotal.setStatus("current")
_LigoRdo3RxRoBufInSeq_Type = Counter32
_LigoRdo3RxRoBufInSeq_Object = MibTableColumn
ligoRdo3RxRoBufInSeq = _LigoRdo3RxRoBufInSeq_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 60),
    _LigoRdo3RxRoBufInSeq_Type()
)
ligoRdo3RxRoBufInSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxRoBufInSeq.setStatus("current")
_LigoRdo3RxRoBufDup_Type = Counter32
_LigoRdo3RxRoBufDup_Object = MibTableColumn
ligoRdo3RxRoBufDup = _LigoRdo3RxRoBufDup_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 61),
    _LigoRdo3RxRoBufDup_Type()
)
ligoRdo3RxRoBufDup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxRoBufDup.setStatus("current")
_LigoRdo3RxRoBufExpired_Type = Counter32
_LigoRdo3RxRoBufExpired_Object = MibTableColumn
ligoRdo3RxRoBufExpired = _LigoRdo3RxRoBufExpired_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 62),
    _LigoRdo3RxRoBufExpired_Type()
)
ligoRdo3RxRoBufExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxRoBufExpired.setStatus("current")
_LigoRdo3RxRoBufBuffered_Type = Counter32
_LigoRdo3RxRoBufBuffered_Object = MibTableColumn
ligoRdo3RxRoBufBuffered = _LigoRdo3RxRoBufBuffered_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 63),
    _LigoRdo3RxRoBufBuffered_Type()
)
ligoRdo3RxRoBufBuffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxRoBufBuffered.setStatus("current")
_LigoRdo3RxRoBufReordered_Type = Counter32
_LigoRdo3RxRoBufReordered_Object = MibTableColumn
ligoRdo3RxRoBufReordered = _LigoRdo3RxRoBufReordered_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 64),
    _LigoRdo3RxRoBufReordered_Type()
)
ligoRdo3RxRoBufReordered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxRoBufReordered.setStatus("current")
_LigoRdo3RxRoBufFlushed_Type = Counter32
_LigoRdo3RxRoBufFlushed_Object = MibTableColumn
ligoRdo3RxRoBufFlushed = _LigoRdo3RxRoBufFlushed_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 65),
    _LigoRdo3RxRoBufFlushed_Type()
)
ligoRdo3RxRoBufFlushed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxRoBufFlushed.setStatus("current")
_LigoRdo3RxRoBufTooBig_Type = Counter32
_LigoRdo3RxRoBufTooBig_Object = MibTableColumn
ligoRdo3RxRoBufTooBig = _LigoRdo3RxRoBufTooBig_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 66),
    _LigoRdo3RxRoBufTooBig_Type()
)
ligoRdo3RxRoBufTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxRoBufTooBig.setStatus("current")
_LigoRdo3RxL2Pad_Type = Counter32
_LigoRdo3RxL2Pad_Object = MibTableColumn
ligoRdo3RxL2Pad = _LigoRdo3RxL2Pad_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 67),
    _LigoRdo3RxL2Pad_Type()
)
ligoRdo3RxL2Pad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxL2Pad.setStatus("current")
_LigoRdo3RxBlockAcks_Type = Counter32
_LigoRdo3RxBlockAcks_Object = MibTableColumn
ligoRdo3RxBlockAcks = _LigoRdo3RxBlockAcks_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 68),
    _LigoRdo3RxBlockAcks_Type()
)
ligoRdo3RxBlockAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxBlockAcks.setStatus("current")
_LigoRdo3RxFragments_Type = Counter32
_LigoRdo3RxFragments_Object = MibTableColumn
ligoRdo3RxFragments = _LigoRdo3RxFragments_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 69),
    _LigoRdo3RxFragments_Type()
)
ligoRdo3RxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxFragments.setStatus("current")
_LigoRdo3RxStbc_Type = Counter32
_LigoRdo3RxStbc_Object = MibTableColumn
ligoRdo3RxStbc = _LigoRdo3RxStbc_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 70),
    _LigoRdo3RxStbc_Type()
)
ligoRdo3RxStbc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxStbc.setStatus("current")
_LigoRdo3RxShortGuardInt_Type = Counter32
_LigoRdo3RxShortGuardInt_Object = MibTableColumn
ligoRdo3RxShortGuardInt = _LigoRdo3RxShortGuardInt_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 71),
    _LigoRdo3RxShortGuardInt_Type()
)
ligoRdo3RxShortGuardInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxShortGuardInt.setStatus("current")
_LigoRdo3Rx40MhzBandwidth_Type = Counter32
_LigoRdo3Rx40MhzBandwidth_Object = MibTableColumn
ligoRdo3Rx40MhzBandwidth = _LigoRdo3Rx40MhzBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 72),
    _LigoRdo3Rx40MhzBandwidth_Type()
)
ligoRdo3Rx40MhzBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3Rx40MhzBandwidth.setStatus("current")
_LigoRdo3RxHtControl_Type = Counter32
_LigoRdo3RxHtControl_Object = MibTableColumn
ligoRdo3RxHtControl = _LigoRdo3RxHtControl_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 73),
    _LigoRdo3RxHtControl_Type()
)
ligoRdo3RxHtControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxHtControl.setStatus("current")
_LigoRdo3RxPacketsPerMcs_Type = OctetString
_LigoRdo3RxPacketsPerMcs_Object = MibTableColumn
ligoRdo3RxPacketsPerMcs = _LigoRdo3RxPacketsPerMcs_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 74),
    _LigoRdo3RxPacketsPerMcs_Type()
)
ligoRdo3RxPacketsPerMcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxPacketsPerMcs.setStatus("current")
_LigoRdo3RxLastSigLevel0_Type = Integer32
_LigoRdo3RxLastSigLevel0_Object = MibTableColumn
ligoRdo3RxLastSigLevel0 = _LigoRdo3RxLastSigLevel0_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 75),
    _LigoRdo3RxLastSigLevel0_Type()
)
ligoRdo3RxLastSigLevel0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxLastSigLevel0.setStatus("current")
_LigoRdo3RxLastSigLevel1_Type = Integer32
_LigoRdo3RxLastSigLevel1_Object = MibTableColumn
ligoRdo3RxLastSigLevel1 = _LigoRdo3RxLastSigLevel1_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 76),
    _LigoRdo3RxLastSigLevel1_Type()
)
ligoRdo3RxLastSigLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxLastSigLevel1.setStatus("current")
_LigoRdo3RxLastSigLevel2_Type = Integer32
_LigoRdo3RxLastSigLevel2_Object = MibTableColumn
ligoRdo3RxLastSigLevel2 = _LigoRdo3RxLastSigLevel2_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 77),
    _LigoRdo3RxLastSigLevel2_Type()
)
ligoRdo3RxLastSigLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxLastSigLevel2.setStatus("current")
_LigoRdo3RxNoise_Type = Integer32
_LigoRdo3RxNoise_Object = MibTableColumn
ligoRdo3RxNoise = _LigoRdo3RxNoise_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 78),
    _LigoRdo3RxNoise_Type()
)
ligoRdo3RxNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxNoise.setStatus("current")
_LigoRdo3RxLastSnr0_Type = Integer32
_LigoRdo3RxLastSnr0_Object = MibTableColumn
ligoRdo3RxLastSnr0 = _LigoRdo3RxLastSnr0_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 79),
    _LigoRdo3RxLastSnr0_Type()
)
ligoRdo3RxLastSnr0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxLastSnr0.setStatus("current")
_LigoRdo3RxLastSnr1_Type = Integer32
_LigoRdo3RxLastSnr1_Object = MibTableColumn
ligoRdo3RxLastSnr1 = _LigoRdo3RxLastSnr1_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 80),
    _LigoRdo3RxLastSnr1_Type()
)
ligoRdo3RxLastSnr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoRdo3RxLastSnr1.setStatus("current")

# Managed Objects groups


# Notification objects

ligoRdo3RxDropsThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 0, 1)
)
ligoRdo3RxDropsThreshold.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("IF-MIB", "ifIndex"),
        ("LIGO-RADIO3-DRV-MIB", "ligoRdo3MacAddress"),
        ("LIGO-RADIO3-DRV-MIB", "ligoRdo3RxDropped"))
)
if mibBuilder.loadTexts:
    ligoRdo3RxDropsThreshold.setStatus(
        "current"
    )

ligoRdo3TxRetriesThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 0, 2)
)
ligoRdo3TxRetriesThreshold.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("IF-MIB", "ifIndex"),
        ("LIGO-RADIO3-DRV-MIB", "ligoRdo3MacAddress"),
        ("LIGO-RADIO3-DRV-MIB", "ligoRdo3TxRetried"))
)
if mibBuilder.loadTexts:
    ligoRdo3TxRetriesThreshold.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIGO-RADIO3-DRV-MIB",
    **{"ligoRadio3DrvMIB": ligoRadio3DrvMIB,
       "ligoRadio3DrvMIBObjects": ligoRadio3DrvMIBObjects,
       "ligoRdo3DrvNotifs": ligoRdo3DrvNotifs,
       "ligoRdo3RxDropsThreshold": ligoRdo3RxDropsThreshold,
       "ligoRdo3TxRetriesThreshold": ligoRdo3TxRetriesThreshold,
       "ligoRdo3DrvInfo": ligoRdo3DrvInfo,
       "ligoRdo3DrvConf": ligoRdo3DrvConf,
       "ligoRdo3DrvStats": ligoRdo3DrvStats,
       "ligoRdo3StatsTable": ligoRdo3StatsTable,
       "ligoRdo3StatsEntry": ligoRdo3StatsEntry,
       "ligoRdo3Endpoint": ligoRdo3Endpoint,
       "ligoRdo3LastUpdate": ligoRdo3LastUpdate,
       "ligoRdo3MacAddress": ligoRdo3MacAddress,
       "ligoRdo3IpAddress": ligoRdo3IpAddress,
       "ligoRdo3CountryCode": ligoRdo3CountryCode,
       "ligoRdo3Encryption": ligoRdo3Encryption,
       "ligoRdo3Parameters": ligoRdo3Parameters,
       "ligoRdo3Capabilities": ligoRdo3Capabilities,
       "ligoRdo3TxPower": ligoRdo3TxPower,
       "ligoRdo3TxPackets": ligoRdo3TxPackets,
       "ligoRdo3TxBytes": ligoRdo3TxBytes,
       "ligoRdo3TxXmitFailed": ligoRdo3TxXmitFailed,
       "ligoRdo3TxXmitDropped": ligoRdo3TxXmitDropped,
       "ligoRdo3TxOverruns": ligoRdo3TxOverruns,
       "ligoRdo3TxSuccess": ligoRdo3TxSuccess,
       "ligoRdo3TxFailed": ligoRdo3TxFailed,
       "ligoRdo3TxRetried": ligoRdo3TxRetried,
       "ligoRdo3TxNotRetried": ligoRdo3TxNotRetried,
       "ligoRdo3TxPacketsPerMcs": ligoRdo3TxPacketsPerMcs,
       "ligoRdo3TxMsdus": ligoRdo3TxMsdus,
       "ligoRdo3TxNotAggregated": ligoRdo3TxNotAggregated,
       "ligoRdo3TxAckRequired": ligoRdo3TxAckRequired,
       "ligoRdo3TxNoAckRequired": ligoRdo3TxNoAckRequired,
       "ligoRdo3TxAltRate": ligoRdo3TxAltRate,
       "ligoRdo3TxManagement": ligoRdo3TxManagement,
       "ligoRdo3TxLegacy": ligoRdo3TxLegacy,
       "ligoRdo3TxLegacyBytes": ligoRdo3TxLegacyBytes,
       "ligoRdo3TxAmsdus": ligoRdo3TxAmsdus,
       "ligoRdo3TxPktsInAmsdus": ligoRdo3TxPktsInAmsdus,
       "ligoRdo3TxAmsduBytes": ligoRdo3TxAmsduBytes,
       "ligoRdo3TxMpdus": ligoRdo3TxMpdus,
       "ligoRdo3TxMpduBytes": ligoRdo3TxMpduBytes,
       "ligoRdo3TxFragmented": ligoRdo3TxFragmented,
       "ligoRdo3TxFragBytes": ligoRdo3TxFragBytes,
       "ligoRdo3RxPackets": ligoRdo3RxPackets,
       "ligoRdo3RxBytes": ligoRdo3RxBytes,
       "ligoRdo3RxDropped": ligoRdo3RxDropped,
       "ligoRdo3RxCrcErrors": ligoRdo3RxCrcErrors,
       "ligoRdo3RxIcvErrors": ligoRdo3RxIcvErrors,
       "ligoRdo3RxMicErrors": ligoRdo3RxMicErrors,
       "ligoRdo3RxKeyNotValid": ligoRdo3RxKeyNotValid,
       "ligoRdo3RxAclDiscarded": ligoRdo3RxAclDiscarded,
       "ligoRdo3RxManagement": ligoRdo3RxManagement,
       "ligoRdo3RxControl": ligoRdo3RxControl,
       "ligoRdo3RxData": ligoRdo3RxData,
       "ligoRdo3RxUnknown": ligoRdo3RxUnknown,
       "ligoRdo3RxNullData": ligoRdo3RxNullData,
       "ligoRdo3RxBroadcast": ligoRdo3RxBroadcast,
       "ligoRdo3RxMulticast": ligoRdo3RxMulticast,
       "ligoRdo3RxUnicast": ligoRdo3RxUnicast,
       "ligoRdo3RxCck": ligoRdo3RxCck,
       "ligoRdo3RxOfdm": ligoRdo3RxOfdm,
       "ligoRdo3RxHtMixedMode": ligoRdo3RxHtMixedMode,
       "ligoRdo3RxHtGreenfield": ligoRdo3RxHtGreenfield,
       "ligoRdo3RxAmsdus": ligoRdo3RxAmsdus,
       "ligoRdo3RxPacketsInAmsdus": ligoRdo3RxPacketsInAmsdus,
       "ligoRdo3RxAmpdus": ligoRdo3RxAmpdus,
       "ligoRdo3RxMpduBytes": ligoRdo3RxMpduBytes,
       "ligoRdo3RxRoBufTotal": ligoRdo3RxRoBufTotal,
       "ligoRdo3RxRoBufInSeq": ligoRdo3RxRoBufInSeq,
       "ligoRdo3RxRoBufDup": ligoRdo3RxRoBufDup,
       "ligoRdo3RxRoBufExpired": ligoRdo3RxRoBufExpired,
       "ligoRdo3RxRoBufBuffered": ligoRdo3RxRoBufBuffered,
       "ligoRdo3RxRoBufReordered": ligoRdo3RxRoBufReordered,
       "ligoRdo3RxRoBufFlushed": ligoRdo3RxRoBufFlushed,
       "ligoRdo3RxRoBufTooBig": ligoRdo3RxRoBufTooBig,
       "ligoRdo3RxL2Pad": ligoRdo3RxL2Pad,
       "ligoRdo3RxBlockAcks": ligoRdo3RxBlockAcks,
       "ligoRdo3RxFragments": ligoRdo3RxFragments,
       "ligoRdo3RxStbc": ligoRdo3RxStbc,
       "ligoRdo3RxShortGuardInt": ligoRdo3RxShortGuardInt,
       "ligoRdo3Rx40MhzBandwidth": ligoRdo3Rx40MhzBandwidth,
       "ligoRdo3RxHtControl": ligoRdo3RxHtControl,
       "ligoRdo3RxPacketsPerMcs": ligoRdo3RxPacketsPerMcs,
       "ligoRdo3RxLastSigLevel0": ligoRdo3RxLastSigLevel0,
       "ligoRdo3RxLastSigLevel1": ligoRdo3RxLastSigLevel1,
       "ligoRdo3RxLastSigLevel2": ligoRdo3RxLastSigLevel2,
       "ligoRdo3RxNoise": ligoRdo3RxNoise,
       "ligoRdo3RxLastSnr0": ligoRdo3RxLastSnr0,
       "ligoRdo3RxLastSnr1": ligoRdo3RxLastSnr1}
)
