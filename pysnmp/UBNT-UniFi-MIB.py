# SNMP MIB module (UBNT-UniFi-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UBNT-UniFi-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:18 2024
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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")

(ubntMIB,
 ubntUniFi,
 ubntUniFiGroups) = mibBuilder.importSymbols(
    "UBNT-MIB",
    "ubntMIB",
    "ubntUniFi",
    "ubntUniFiGroups")


# MODULE-IDENTITY

ubntUniFi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6)
)
ubntUniFi.setRevisions(
        ("2016-06-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TableIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class ObjectIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class Voltage(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )



class Temperature(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_UnifiApWireless_ObjectIdentity = ObjectIdentity
unifiApWireless = _UnifiApWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1)
)
_UnifiRadioTable_Object = MibTable
unifiRadioTable = _UnifiRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    unifiRadioTable.setStatus("current")
_UnifiRadioEntry_Object = MibTableRow
unifiRadioEntry = _UnifiRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 1, 1)
)
unifiRadioEntry.setIndexNames(
    (0, "UBNT-UniFi-MIB", "unifiRadioIndex"),
)
if mibBuilder.loadTexts:
    unifiRadioEntry.setStatus("current")
_UnifiRadioIndex_Type = ObjectIndex
_UnifiRadioIndex_Object = MibTableColumn
unifiRadioIndex = _UnifiRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 1, 1, 1),
    _UnifiRadioIndex_Type()
)
unifiRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unifiRadioIndex.setStatus("current")
_UnifiRadioName_Type = DisplayString
_UnifiRadioName_Object = MibTableColumn
unifiRadioName = _UnifiRadioName_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 1, 1, 2),
    _UnifiRadioName_Type()
)
unifiRadioName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiRadioName.setStatus("current")
_UnifiRadioRadio_Type = DisplayString
_UnifiRadioRadio_Object = MibTableColumn
unifiRadioRadio = _UnifiRadioRadio_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 1, 1, 3),
    _UnifiRadioRadio_Type()
)
unifiRadioRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiRadioRadio.setStatus("current")
_UnifiRadioRxPackets_Type = Counter32
_UnifiRadioRxPackets_Object = MibTableColumn
unifiRadioRxPackets = _UnifiRadioRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 1, 1, 4),
    _UnifiRadioRxPackets_Type()
)
unifiRadioRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiRadioRxPackets.setStatus("current")
_UnifiRadioTxPackets_Type = Counter32
_UnifiRadioTxPackets_Object = MibTableColumn
unifiRadioTxPackets = _UnifiRadioTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 1, 1, 5),
    _UnifiRadioTxPackets_Type()
)
unifiRadioTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiRadioTxPackets.setStatus("current")
_UnifiRadioCuTotal_Type = Integer32
_UnifiRadioCuTotal_Object = MibTableColumn
unifiRadioCuTotal = _UnifiRadioCuTotal_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 1, 1, 6),
    _UnifiRadioCuTotal_Type()
)
unifiRadioCuTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiRadioCuTotal.setStatus("current")
_UnifiRadioCuSelfRx_Type = Integer32
_UnifiRadioCuSelfRx_Object = MibTableColumn
unifiRadioCuSelfRx = _UnifiRadioCuSelfRx_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 1, 1, 7),
    _UnifiRadioCuSelfRx_Type()
)
unifiRadioCuSelfRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiRadioCuSelfRx.setStatus("current")
_UnifiRadioCuSelfTx_Type = Integer32
_UnifiRadioCuSelfTx_Object = MibTableColumn
unifiRadioCuSelfTx = _UnifiRadioCuSelfTx_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 1, 1, 8),
    _UnifiRadioCuSelfTx_Type()
)
unifiRadioCuSelfTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiRadioCuSelfTx.setStatus("current")
_UnifiRadioOtherBss_Type = Integer32
_UnifiRadioOtherBss_Object = MibTableColumn
unifiRadioOtherBss = _UnifiRadioOtherBss_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 1, 1, 9),
    _UnifiRadioOtherBss_Type()
)
unifiRadioOtherBss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiRadioOtherBss.setStatus("current")
_UnifiVapTable_Object = MibTable
unifiVapTable = _UnifiVapTable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    unifiVapTable.setStatus("current")
_UnifiVapEntry_Object = MibTableRow
unifiVapEntry = _UnifiVapEntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1)
)
unifiVapEntry.setIndexNames(
    (0, "UBNT-UniFi-MIB", "unifiVapIndex"),
)
if mibBuilder.loadTexts:
    unifiVapEntry.setStatus("current")
_UnifiVapIndex_Type = ObjectIndex
_UnifiVapIndex_Object = MibTableColumn
unifiVapIndex = _UnifiVapIndex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 1),
    _UnifiVapIndex_Type()
)
unifiVapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unifiVapIndex.setStatus("current")
_UnifiVapBssId_Type = MacAddress
_UnifiVapBssId_Object = MibTableColumn
unifiVapBssId = _UnifiVapBssId_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 2),
    _UnifiVapBssId_Type()
)
unifiVapBssId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiVapBssId.setStatus("current")
_UnifiVapCcq_Type = Integer32
_UnifiVapCcq_Object = MibTableColumn
unifiVapCcq = _UnifiVapCcq_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 3),
    _UnifiVapCcq_Type()
)
unifiVapCcq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiVapCcq.setStatus("current")
_UnifiVapChannel_Type = Integer32
_UnifiVapChannel_Object = MibTableColumn
unifiVapChannel = _UnifiVapChannel_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 4),
    _UnifiVapChannel_Type()
)
unifiVapChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiVapChannel.setStatus("current")
_UnifiVapExtChannel_Type = Integer32
_UnifiVapExtChannel_Object = MibTableColumn
unifiVapExtChannel = _UnifiVapExtChannel_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 5),
    _UnifiVapExtChannel_Type()
)
unifiVapExtChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiVapExtChannel.setStatus("current")
_UnifiVapEssId_Type = DisplayString
_UnifiVapEssId_Object = MibTableColumn
unifiVapEssId = _UnifiVapEssId_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 6),
    _UnifiVapEssId_Type()
)
unifiVapEssId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiVapEssId.setStatus("current")
_UnifiVapName_Type = DisplayString
_UnifiVapName_Object = MibTableColumn
unifiVapName = _UnifiVapName_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 7),
    _UnifiVapName_Type()
)
unifiVapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiVapName.setStatus("current")
_UnifiVapNumStations_Type = Integer32
_UnifiVapNumStations_Object = MibTableColumn
unifiVapNumStations = _UnifiVapNumStations_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 8),
    _UnifiVapNumStations_Type()
)
unifiVapNumStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiVapNumStations.setStatus("current")
_UnifiVapRadio_Type = DisplayString
_UnifiVapRadio_Object = MibTableColumn
unifiVapRadio = _UnifiVapRadio_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 9),
    _UnifiVapRadio_Type()
)
unifiVapRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiVapRadio.setStatus("current")
_UnifiVapRxBytes_Type = Counter32
_UnifiVapRxBytes_Object = MibTableColumn
unifiVapRxBytes = _UnifiVapRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 10),
    _UnifiVapRxBytes_Type()
)
unifiVapRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiVapRxBytes.setStatus("current")
_UnifiVapRxCrypts_Type = Counter32
_UnifiVapRxCrypts_Object = MibTableColumn
unifiVapRxCrypts = _UnifiVapRxCrypts_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 11),
    _UnifiVapRxCrypts_Type()
)
unifiVapRxCrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiVapRxCrypts.setStatus("current")
_UnifiVapRxDropped_Type = Counter32
_UnifiVapRxDropped_Object = MibTableColumn
unifiVapRxDropped = _UnifiVapRxDropped_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 12),
    _UnifiVapRxDropped_Type()
)
unifiVapRxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiVapRxDropped.setStatus("current")
_UnifiVapRxErrors_Type = Counter32
_UnifiVapRxErrors_Object = MibTableColumn
unifiVapRxErrors = _UnifiVapRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 13),
    _UnifiVapRxErrors_Type()
)
unifiVapRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiVapRxErrors.setStatus("current")
_UnifiVapRxFrags_Type = Counter32
_UnifiVapRxFrags_Object = MibTableColumn
unifiVapRxFrags = _UnifiVapRxFrags_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 14),
    _UnifiVapRxFrags_Type()
)
unifiVapRxFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiVapRxFrags.setStatus("current")
_UnifiVapRxPackets_Type = Counter32
_UnifiVapRxPackets_Object = MibTableColumn
unifiVapRxPackets = _UnifiVapRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 15),
    _UnifiVapRxPackets_Type()
)
unifiVapRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiVapRxPackets.setStatus("current")
_UnifiVapTxBytes_Type = Counter32
_UnifiVapTxBytes_Object = MibTableColumn
unifiVapTxBytes = _UnifiVapTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 16),
    _UnifiVapTxBytes_Type()
)
unifiVapTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiVapTxBytes.setStatus("current")
_UnifiVapTxDropped_Type = Counter32
_UnifiVapTxDropped_Object = MibTableColumn
unifiVapTxDropped = _UnifiVapTxDropped_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 17),
    _UnifiVapTxDropped_Type()
)
unifiVapTxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiVapTxDropped.setStatus("current")
_UnifiVapTxErrors_Type = Counter32
_UnifiVapTxErrors_Object = MibTableColumn
unifiVapTxErrors = _UnifiVapTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 18),
    _UnifiVapTxErrors_Type()
)
unifiVapTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiVapTxErrors.setStatus("current")
_UnifiVapTxPackets_Type = Counter32
_UnifiVapTxPackets_Object = MibTableColumn
unifiVapTxPackets = _UnifiVapTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 19),
    _UnifiVapTxPackets_Type()
)
unifiVapTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiVapTxPackets.setStatus("current")
_UnifiVapTxRetries_Type = Counter32
_UnifiVapTxRetries_Object = MibTableColumn
unifiVapTxRetries = _UnifiVapTxRetries_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 20),
    _UnifiVapTxRetries_Type()
)
unifiVapTxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiVapTxRetries.setStatus("current")
_UnifiVapTxPower_Type = Integer32
_UnifiVapTxPower_Object = MibTableColumn
unifiVapTxPower = _UnifiVapTxPower_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 21),
    _UnifiVapTxPower_Type()
)
unifiVapTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiVapTxPower.setStatus("current")
_UnifiVapUp_Type = TruthValue
_UnifiVapUp_Object = MibTableColumn
unifiVapUp = _UnifiVapUp_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 22),
    _UnifiVapUp_Type()
)
unifiVapUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiVapUp.setStatus("current")
_UnifiVapUsage_Type = DisplayString
_UnifiVapUsage_Object = MibTableColumn
unifiVapUsage = _UnifiVapUsage_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 23),
    _UnifiVapUsage_Type()
)
unifiVapUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiVapUsage.setStatus("current")
_UnifiApIf_ObjectIdentity = ObjectIdentity
unifiApIf = _UnifiApIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 2)
)
_UnifiIfTable_Object = MibTable
unifiIfTable = _UnifiIfTable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    unifiIfTable.setStatus("current")
_UnifiIfEntry_Object = MibTableRow
unifiIfEntry = _UnifiIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1)
)
unifiIfEntry.setIndexNames(
    (0, "UBNT-UniFi-MIB", "unifiIfIndex"),
)
if mibBuilder.loadTexts:
    unifiIfEntry.setStatus("current")
_UnifiIfIndex_Type = ObjectIndex
_UnifiIfIndex_Object = MibTableColumn
unifiIfIndex = _UnifiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 1),
    _UnifiIfIndex_Type()
)
unifiIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unifiIfIndex.setStatus("current")
_UnifiIfFullDuplex_Type = TruthValue
_UnifiIfFullDuplex_Object = MibTableColumn
unifiIfFullDuplex = _UnifiIfFullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 2),
    _UnifiIfFullDuplex_Type()
)
unifiIfFullDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiIfFullDuplex.setStatus("current")
_UnifiIfIp_Type = IpAddress
_UnifiIfIp_Object = MibTableColumn
unifiIfIp = _UnifiIfIp_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 3),
    _UnifiIfIp_Type()
)
unifiIfIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiIfIp.setStatus("current")
_UnifiIfMac_Type = MacAddress
_UnifiIfMac_Object = MibTableColumn
unifiIfMac = _UnifiIfMac_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 4),
    _UnifiIfMac_Type()
)
unifiIfMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiIfMac.setStatus("current")
_UnifiIfName_Type = DisplayString
_UnifiIfName_Object = MibTableColumn
unifiIfName = _UnifiIfName_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 5),
    _UnifiIfName_Type()
)
unifiIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiIfName.setStatus("current")
_UnifiIfRxBytes_Type = Counter32
_UnifiIfRxBytes_Object = MibTableColumn
unifiIfRxBytes = _UnifiIfRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 6),
    _UnifiIfRxBytes_Type()
)
unifiIfRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiIfRxBytes.setStatus("current")
_UnifiIfRxDropped_Type = Counter32
_UnifiIfRxDropped_Object = MibTableColumn
unifiIfRxDropped = _UnifiIfRxDropped_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 7),
    _UnifiIfRxDropped_Type()
)
unifiIfRxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiIfRxDropped.setStatus("current")
_UnifiIfRxError_Type = Counter32
_UnifiIfRxError_Object = MibTableColumn
unifiIfRxError = _UnifiIfRxError_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 8),
    _UnifiIfRxError_Type()
)
unifiIfRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiIfRxError.setStatus("current")
_UnifiIfRxMulticast_Type = Counter32
_UnifiIfRxMulticast_Object = MibTableColumn
unifiIfRxMulticast = _UnifiIfRxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 9),
    _UnifiIfRxMulticast_Type()
)
unifiIfRxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiIfRxMulticast.setStatus("current")
_UnifiIfRxPackets_Type = Counter32
_UnifiIfRxPackets_Object = MibTableColumn
unifiIfRxPackets = _UnifiIfRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 10),
    _UnifiIfRxPackets_Type()
)
unifiIfRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiIfRxPackets.setStatus("current")
_UnifiIfSpeed_Type = Integer32
_UnifiIfSpeed_Object = MibTableColumn
unifiIfSpeed = _UnifiIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 11),
    _UnifiIfSpeed_Type()
)
unifiIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiIfSpeed.setStatus("current")
_UnifiIfTxBytes_Type = Counter32
_UnifiIfTxBytes_Object = MibTableColumn
unifiIfTxBytes = _UnifiIfTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 12),
    _UnifiIfTxBytes_Type()
)
unifiIfTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiIfTxBytes.setStatus("current")
_UnifiIfTxDropped_Type = Counter32
_UnifiIfTxDropped_Object = MibTableColumn
unifiIfTxDropped = _UnifiIfTxDropped_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 13),
    _UnifiIfTxDropped_Type()
)
unifiIfTxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiIfTxDropped.setStatus("current")
_UnifiIfTxError_Type = Counter32
_UnifiIfTxError_Object = MibTableColumn
unifiIfTxError = _UnifiIfTxError_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 14),
    _UnifiIfTxError_Type()
)
unifiIfTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiIfTxError.setStatus("current")
_UnifiIfTxPackets_Type = Counter32
_UnifiIfTxPackets_Object = MibTableColumn
unifiIfTxPackets = _UnifiIfTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 15),
    _UnifiIfTxPackets_Type()
)
unifiIfTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiIfTxPackets.setStatus("current")
_UnifiIfUp_Type = TruthValue
_UnifiIfUp_Object = MibTableColumn
unifiIfUp = _UnifiIfUp_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 16),
    _UnifiIfUp_Type()
)
unifiIfUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiIfUp.setStatus("current")
_UnifiApSystem_ObjectIdentity = ObjectIdentity
unifiApSystem = _UnifiApSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 3)
)
_UnifiApSystemIp_Type = IpAddress
_UnifiApSystemIp_Object = MibScalar
unifiApSystemIp = _UnifiApSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 3, 1),
    _UnifiApSystemIp_Type()
)
unifiApSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiApSystemIp.setStatus("current")
_UnifiApSystemIsolated_Type = TruthValue
_UnifiApSystemIsolated_Object = MibScalar
unifiApSystemIsolated = _UnifiApSystemIsolated_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 3, 2),
    _UnifiApSystemIsolated_Type()
)
unifiApSystemIsolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiApSystemIsolated.setStatus("current")
_UnifiApSystemModel_Type = DisplayString
_UnifiApSystemModel_Object = MibScalar
unifiApSystemModel = _UnifiApSystemModel_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 3, 3),
    _UnifiApSystemModel_Type()
)
unifiApSystemModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiApSystemModel.setStatus("current")
_UnifiApSystemUplink_Type = DisplayString
_UnifiApSystemUplink_Object = MibScalar
unifiApSystemUplink = _UnifiApSystemUplink_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 3, 4),
    _UnifiApSystemUplink_Type()
)
unifiApSystemUplink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiApSystemUplink.setStatus("current")
_UnifiApSystemUptime_Type = Counter32
_UnifiApSystemUptime_Object = MibScalar
unifiApSystemUptime = _UnifiApSystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 3, 5),
    _UnifiApSystemUptime_Type()
)
unifiApSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiApSystemUptime.setStatus("current")
_UnifiApSystemVersion_Type = DisplayString
_UnifiApSystemVersion_Object = MibScalar
unifiApSystemVersion = _UnifiApSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6, 3, 6),
    _UnifiApSystemVersion_Type()
)
unifiApSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unifiApSystemVersion.setStatus("current")

# Managed Objects groups

unifiIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 5, 1)
)
unifiIfGroup.setObjects(
      *(("UBNT-UniFi-MIB", "unifiIfFullDuplex"),
        ("UBNT-UniFi-MIB", "unifiIfIp"),
        ("UBNT-UniFi-MIB", "unifiIfMac"),
        ("UBNT-UniFi-MIB", "unifiIfName"),
        ("UBNT-UniFi-MIB", "unifiIfRxBytes"),
        ("UBNT-UniFi-MIB", "unifiIfRxDropped"),
        ("UBNT-UniFi-MIB", "unifiIfRxError"),
        ("UBNT-UniFi-MIB", "unifiIfRxMulticast"),
        ("UBNT-UniFi-MIB", "unifiIfRxPackets"),
        ("UBNT-UniFi-MIB", "unifiIfSpeed"),
        ("UBNT-UniFi-MIB", "unifiIfTxBytes"),
        ("UBNT-UniFi-MIB", "unifiIfTxDropped"),
        ("UBNT-UniFi-MIB", "unifiIfTxError"),
        ("UBNT-UniFi-MIB", "unifiIfTxPackets"),
        ("UBNT-UniFi-MIB", "unifiIfUp"))
)
if mibBuilder.loadTexts:
    unifiIfGroup.setStatus("current")

unifiRadioGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 5, 2)
)
unifiRadioGroups.setObjects(
      *(("UBNT-UniFi-MIB", "unifiRadioName"),
        ("UBNT-UniFi-MIB", "unifiRadioRadio"),
        ("UBNT-UniFi-MIB", "unifiRadioRxPackets"),
        ("UBNT-UniFi-MIB", "unifiRadioTxPackets"),
        ("UBNT-UniFi-MIB", "unifiRadioCuTotal"),
        ("UBNT-UniFi-MIB", "unifiRadioCuSelfRx"),
        ("UBNT-UniFi-MIB", "unifiRadioCuSelfTx"),
        ("UBNT-UniFi-MIB", "unifiRadioOtherBss"))
)
if mibBuilder.loadTexts:
    unifiRadioGroups.setStatus("current")

unifiVapGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 5, 3)
)
unifiVapGroups.setObjects(
      *(("UBNT-UniFi-MIB", "unifiVapBssId"),
        ("UBNT-UniFi-MIB", "unifiVapCcq"),
        ("UBNT-UniFi-MIB", "unifiVapChannel"),
        ("UBNT-UniFi-MIB", "unifiVapExtChannel"),
        ("UBNT-UniFi-MIB", "unifiVapEssId"),
        ("UBNT-UniFi-MIB", "unifiVapName"),
        ("UBNT-UniFi-MIB", "unifiVapNumStations"),
        ("UBNT-UniFi-MIB", "unifiVapRadio"),
        ("UBNT-UniFi-MIB", "unifiVapRxBytes"),
        ("UBNT-UniFi-MIB", "unifiVapRxCrypts"),
        ("UBNT-UniFi-MIB", "unifiVapRxDropped"),
        ("UBNT-UniFi-MIB", "unifiVapRxErrors"),
        ("UBNT-UniFi-MIB", "unifiVapRxFrags"),
        ("UBNT-UniFi-MIB", "unifiVapRxPackets"),
        ("UBNT-UniFi-MIB", "unifiVapTxBytes"),
        ("UBNT-UniFi-MIB", "unifiVapTxDropped"),
        ("UBNT-UniFi-MIB", "unifiVapTxErrors"),
        ("UBNT-UniFi-MIB", "unifiVapTxPackets"),
        ("UBNT-UniFi-MIB", "unifiVapTxRetries"),
        ("UBNT-UniFi-MIB", "unifiVapTxPower"),
        ("UBNT-UniFi-MIB", "unifiVapUp"),
        ("UBNT-UniFi-MIB", "unifiVapUsage"))
)
if mibBuilder.loadTexts:
    unifiVapGroups.setStatus("current")

unifiApSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 5, 4)
)
unifiApSystemGroup.setObjects(
      *(("UBNT-UniFi-MIB", "unifiApSystemIp"),
        ("UBNT-UniFi-MIB", "unifiApSystemIsolated"),
        ("UBNT-UniFi-MIB", "unifiApSystemModel"),
        ("UBNT-UniFi-MIB", "unifiApSystemUplink"),
        ("UBNT-UniFi-MIB", "unifiApSystemUptime"),
        ("UBNT-UniFi-MIB", "unifiApSystemVersion"))
)
if mibBuilder.loadTexts:
    unifiApSystemGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBNT-UniFi-MIB",
    **{"TableIndex": TableIndex,
       "ObjectIndex": ObjectIndex,
       "Voltage": Voltage,
       "Temperature": Temperature,
       "unifiIfGroup": unifiIfGroup,
       "unifiRadioGroups": unifiRadioGroups,
       "unifiVapGroups": unifiVapGroups,
       "unifiApSystemGroup": unifiApSystemGroup,
       "ubntUniFi": ubntUniFi,
       "unifiApWireless": unifiApWireless,
       "unifiRadioTable": unifiRadioTable,
       "unifiRadioEntry": unifiRadioEntry,
       "unifiRadioIndex": unifiRadioIndex,
       "unifiRadioName": unifiRadioName,
       "unifiRadioRadio": unifiRadioRadio,
       "unifiRadioRxPackets": unifiRadioRxPackets,
       "unifiRadioTxPackets": unifiRadioTxPackets,
       "unifiRadioCuTotal": unifiRadioCuTotal,
       "unifiRadioCuSelfRx": unifiRadioCuSelfRx,
       "unifiRadioCuSelfTx": unifiRadioCuSelfTx,
       "unifiRadioOtherBss": unifiRadioOtherBss,
       "unifiVapTable": unifiVapTable,
       "unifiVapEntry": unifiVapEntry,
       "unifiVapIndex": unifiVapIndex,
       "unifiVapBssId": unifiVapBssId,
       "unifiVapCcq": unifiVapCcq,
       "unifiVapChannel": unifiVapChannel,
       "unifiVapExtChannel": unifiVapExtChannel,
       "unifiVapEssId": unifiVapEssId,
       "unifiVapName": unifiVapName,
       "unifiVapNumStations": unifiVapNumStations,
       "unifiVapRadio": unifiVapRadio,
       "unifiVapRxBytes": unifiVapRxBytes,
       "unifiVapRxCrypts": unifiVapRxCrypts,
       "unifiVapRxDropped": unifiVapRxDropped,
       "unifiVapRxErrors": unifiVapRxErrors,
       "unifiVapRxFrags": unifiVapRxFrags,
       "unifiVapRxPackets": unifiVapRxPackets,
       "unifiVapTxBytes": unifiVapTxBytes,
       "unifiVapTxDropped": unifiVapTxDropped,
       "unifiVapTxErrors": unifiVapTxErrors,
       "unifiVapTxPackets": unifiVapTxPackets,
       "unifiVapTxRetries": unifiVapTxRetries,
       "unifiVapTxPower": unifiVapTxPower,
       "unifiVapUp": unifiVapUp,
       "unifiVapUsage": unifiVapUsage,
       "unifiApIf": unifiApIf,
       "unifiIfTable": unifiIfTable,
       "unifiIfEntry": unifiIfEntry,
       "unifiIfIndex": unifiIfIndex,
       "unifiIfFullDuplex": unifiIfFullDuplex,
       "unifiIfIp": unifiIfIp,
       "unifiIfMac": unifiIfMac,
       "unifiIfName": unifiIfName,
       "unifiIfRxBytes": unifiIfRxBytes,
       "unifiIfRxDropped": unifiIfRxDropped,
       "unifiIfRxError": unifiIfRxError,
       "unifiIfRxMulticast": unifiIfRxMulticast,
       "unifiIfRxPackets": unifiIfRxPackets,
       "unifiIfSpeed": unifiIfSpeed,
       "unifiIfTxBytes": unifiIfTxBytes,
       "unifiIfTxDropped": unifiIfTxDropped,
       "unifiIfTxError": unifiIfTxError,
       "unifiIfTxPackets": unifiIfTxPackets,
       "unifiIfUp": unifiIfUp,
       "unifiApSystem": unifiApSystem,
       "unifiApSystemIp": unifiApSystemIp,
       "unifiApSystemIsolated": unifiApSystemIsolated,
       "unifiApSystemModel": unifiApSystemModel,
       "unifiApSystemUplink": unifiApSystemUplink,
       "unifiApSystemUptime": unifiApSystemUptime,
       "unifiApSystemVersion": unifiApSystemVersion}
)
