# SNMP MIB module (CISCO-WAN-CELL-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-CELL-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:56 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(C3gServiceCapability,) = mibBuilder.importSymbols(
    "CISCO-WAN-3G-MIB",
    "C3gServiceCapability")

(entPhysicalIndex,
 entPhysicalName) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex",
    "entPhysicalName")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

ciscoWanCellExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 817)
)
ciscoWanCellExtMIB.setRevisions(
        ("2014-03-05 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoWanCellExtProtocolType(Integer32, TextualConvention):
    status = "current"
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
        *(("ipv4", 2),
          ("ipv4V6", 5),
          ("ipv6", 4),
          ("ppp", 3),
          ("unknown", 1))
    )



class CiscoWanCellExtRsrp(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"


class CiscoWanCellExtRsrq(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


class CiscoWanCellExtCqiIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class CiscoWanCellExtSNR(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


class CiscoWanCellExtSINR(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


# MIB Managed Objects in the order of their OIDs

_CiscoWanCellExtMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoWanCellExtMIBNotifs = _CiscoWanCellExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 0)
)
_CiscoWanCellExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWanCellExtMIBObjects = _CiscoWanCellExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1)
)
_CiscoWanCellExtLte_ObjectIdentity = ObjectIdentity
ciscoWanCellExtLte = _CiscoWanCellExtLte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1)
)
_CwceLteRadio_ObjectIdentity = ObjectIdentity
cwceLteRadio = _CwceLteRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1)
)
_CwceLteRadioTable_Object = MibTable
cwceLteRadioTable = _CwceLteRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cwceLteRadioTable.setStatus("current")
_CwceLteRadioEntry_Object = MibTableRow
cwceLteRadioEntry = _CwceLteRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 1, 1)
)
cwceLteRadioEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cwceLteRadioEntry.setStatus("current")
_CwceLteCurrRsrp_Type = CiscoWanCellExtRsrp
_CwceLteCurrRsrp_Object = MibTableColumn
cwceLteCurrRsrp = _CwceLteCurrRsrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 1, 1, 1),
    _CwceLteCurrRsrp_Type()
)
cwceLteCurrRsrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteCurrRsrp.setStatus("current")
if mibBuilder.loadTexts:
    cwceLteCurrRsrp.setUnits("dBm")
_CwceLteCurrRsrq_Type = CiscoWanCellExtRsrq
_CwceLteCurrRsrq_Object = MibTableColumn
cwceLteCurrRsrq = _CwceLteCurrRsrq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 1, 1, 2),
    _CwceLteCurrRsrq_Type()
)
cwceLteCurrRsrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteCurrRsrq.setStatus("current")
if mibBuilder.loadTexts:
    cwceLteCurrRsrq.setUnits("dB")
_CwceLteCurrSnr_Type = CiscoWanCellExtSNR
_CwceLteCurrSnr_Object = MibTableColumn
cwceLteCurrSnr = _CwceLteCurrSnr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 1, 1, 3),
    _CwceLteCurrSnr_Type()
)
cwceLteCurrSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteCurrSnr.setStatus("current")
if mibBuilder.loadTexts:
    cwceLteCurrSnr.setUnits("dB")
_CwceLteCurrSinr_Type = CiscoWanCellExtSINR
_CwceLteCurrSinr_Object = MibTableColumn
cwceLteCurrSinr = _CwceLteCurrSinr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 1, 1, 4),
    _CwceLteCurrSinr_Type()
)
cwceLteCurrSinr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteCurrSinr.setStatus("current")
if mibBuilder.loadTexts:
    cwceLteCurrSinr.setUnits("dB")
_CwceLteCurrCqiIndex_Type = CiscoWanCellExtCqiIndex
_CwceLteCurrCqiIndex_Object = MibTableColumn
cwceLteCurrCqiIndex = _CwceLteCurrCqiIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 1, 1, 5),
    _CwceLteCurrCqiIndex_Type()
)
cwceLteCurrCqiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteCurrCqiIndex.setStatus("current")
_CwceLteCurrOperatingBand_Type = Unsigned32
_CwceLteCurrOperatingBand_Object = MibTableColumn
cwceLteCurrOperatingBand = _CwceLteCurrOperatingBand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 1, 1, 6),
    _CwceLteCurrOperatingBand_Type()
)
cwceLteCurrOperatingBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteCurrOperatingBand.setStatus("current")
_CwceLteNotifRsrp_Type = CiscoWanCellExtRsrp
_CwceLteNotifRsrp_Object = MibTableColumn
cwceLteNotifRsrp = _CwceLteNotifRsrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 1, 1, 7),
    _CwceLteNotifRsrp_Type()
)
cwceLteNotifRsrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteNotifRsrp.setStatus("current")
_CwceLteNotifRsrq_Type = CiscoWanCellExtRsrq
_CwceLteNotifRsrq_Object = MibTableColumn
cwceLteNotifRsrq = _CwceLteNotifRsrq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 1, 1, 8),
    _CwceLteNotifRsrq_Type()
)
cwceLteNotifRsrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteNotifRsrq.setStatus("current")
_CwceLteRsrpOnsetNotifThreshold_Type = CiscoWanCellExtRsrp
_CwceLteRsrpOnsetNotifThreshold_Object = MibTableColumn
cwceLteRsrpOnsetNotifThreshold = _CwceLteRsrpOnsetNotifThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 1, 1, 9),
    _CwceLteRsrpOnsetNotifThreshold_Type()
)
cwceLteRsrpOnsetNotifThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwceLteRsrpOnsetNotifThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cwceLteRsrpOnsetNotifThreshold.setUnits("dBm")
_CwceLteRsrpAbateNotifThreshold_Type = CiscoWanCellExtRsrp
_CwceLteRsrpAbateNotifThreshold_Object = MibTableColumn
cwceLteRsrpAbateNotifThreshold = _CwceLteRsrpAbateNotifThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 1, 1, 10),
    _CwceLteRsrpAbateNotifThreshold_Type()
)
cwceLteRsrpAbateNotifThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwceLteRsrpAbateNotifThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cwceLteRsrpAbateNotifThreshold.setUnits("dBm")
_CwceLteRsrqOnsetNotifThreshold_Type = CiscoWanCellExtRsrq
_CwceLteRsrqOnsetNotifThreshold_Object = MibTableColumn
cwceLteRsrqOnsetNotifThreshold = _CwceLteRsrqOnsetNotifThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 1, 1, 11),
    _CwceLteRsrqOnsetNotifThreshold_Type()
)
cwceLteRsrqOnsetNotifThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwceLteRsrqOnsetNotifThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cwceLteRsrqOnsetNotifThreshold.setUnits("dB")
_CwceLteRsrqAbateNotifThreshold_Type = CiscoWanCellExtRsrq
_CwceLteRsrqAbateNotifThreshold_Object = MibTableColumn
cwceLteRsrqAbateNotifThreshold = _CwceLteRsrqAbateNotifThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 1, 1, 12),
    _CwceLteRsrqAbateNotifThreshold_Type()
)
cwceLteRsrqAbateNotifThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwceLteRsrqAbateNotifThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cwceLteRsrqAbateNotifThreshold.setUnits("dB")
_CwceLteRsrpOnsetNotifFlag_Type = C3gServiceCapability
_CwceLteRsrpOnsetNotifFlag_Object = MibTableColumn
cwceLteRsrpOnsetNotifFlag = _CwceLteRsrpOnsetNotifFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 1, 1, 13),
    _CwceLteRsrpOnsetNotifFlag_Type()
)
cwceLteRsrpOnsetNotifFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwceLteRsrpOnsetNotifFlag.setStatus("current")
_CwceLteRsrpAbateNotifFlag_Type = C3gServiceCapability
_CwceLteRsrpAbateNotifFlag_Object = MibTableColumn
cwceLteRsrpAbateNotifFlag = _CwceLteRsrpAbateNotifFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 1, 1, 14),
    _CwceLteRsrpAbateNotifFlag_Type()
)
cwceLteRsrpAbateNotifFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwceLteRsrpAbateNotifFlag.setStatus("current")
_CwceLteRsrqOnsetNotifFlag_Type = C3gServiceCapability
_CwceLteRsrqOnsetNotifFlag_Object = MibTableColumn
cwceLteRsrqOnsetNotifFlag = _CwceLteRsrqOnsetNotifFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 1, 1, 15),
    _CwceLteRsrqOnsetNotifFlag_Type()
)
cwceLteRsrqOnsetNotifFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwceLteRsrqOnsetNotifFlag.setStatus("current")
_CwceLteRsrqAbateNotifFlag_Type = C3gServiceCapability
_CwceLteRsrqAbateNotifFlag_Object = MibTableColumn
cwceLteRsrqAbateNotifFlag = _CwceLteRsrqAbateNotifFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 1, 1, 16),
    _CwceLteRsrqAbateNotifFlag_Type()
)
cwceLteRsrqAbateNotifFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwceLteRsrqAbateNotifFlag.setStatus("current")
_CwceLteRadioHistory_ObjectIdentity = ObjectIdentity
cwceLteRadioHistory = _CwceLteRadioHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 2)
)
_CwceLteRadioHistoryRsrpTable_Object = MibTable
cwceLteRadioHistoryRsrpTable = _CwceLteRadioHistoryRsrpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cwceLteRadioHistoryRsrpTable.setStatus("current")
_CwceLteRadioHistoryRsrpEntry_Object = MibTableRow
cwceLteRadioHistoryRsrpEntry = _CwceLteRadioHistoryRsrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 2, 1, 1)
)
cwceLteRadioHistoryRsrpEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cwceLteRadioHistoryRsrpEntry.setStatus("current")


class _CwceLteRadioHistoryRsrpPerSecond_Type(OctetString):
    """Custom type cwceLteRadioHistoryRsrpPerSecond based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(60, 60),
    )


_CwceLteRadioHistoryRsrpPerSecond_Type.__name__ = "OctetString"
_CwceLteRadioHistoryRsrpPerSecond_Object = MibTableColumn
cwceLteRadioHistoryRsrpPerSecond = _CwceLteRadioHistoryRsrpPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 2, 1, 1, 1),
    _CwceLteRadioHistoryRsrpPerSecond_Type()
)
cwceLteRadioHistoryRsrpPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteRadioHistoryRsrpPerSecond.setStatus("current")
if mibBuilder.loadTexts:
    cwceLteRadioHistoryRsrpPerSecond.setUnits("-dBm")


class _CwceLteRadioHistoryRsrpPerMinute_Type(OctetString):
    """Custom type cwceLteRadioHistoryRsrpPerMinute based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(60, 60),
    )


_CwceLteRadioHistoryRsrpPerMinute_Type.__name__ = "OctetString"
_CwceLteRadioHistoryRsrpPerMinute_Object = MibTableColumn
cwceLteRadioHistoryRsrpPerMinute = _CwceLteRadioHistoryRsrpPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 2, 1, 1, 2),
    _CwceLteRadioHistoryRsrpPerMinute_Type()
)
cwceLteRadioHistoryRsrpPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteRadioHistoryRsrpPerMinute.setStatus("current")
if mibBuilder.loadTexts:
    cwceLteRadioHistoryRsrpPerMinute.setUnits("-dBm")


class _CwceLteRadioHistoryRsrpPerHour_Type(OctetString):
    """Custom type cwceLteRadioHistoryRsrpPerHour based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(72, 72),
    )


_CwceLteRadioHistoryRsrpPerHour_Type.__name__ = "OctetString"
_CwceLteRadioHistoryRsrpPerHour_Object = MibTableColumn
cwceLteRadioHistoryRsrpPerHour = _CwceLteRadioHistoryRsrpPerHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 2, 1, 1, 3),
    _CwceLteRadioHistoryRsrpPerHour_Type()
)
cwceLteRadioHistoryRsrpPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteRadioHistoryRsrpPerHour.setStatus("current")
if mibBuilder.loadTexts:
    cwceLteRadioHistoryRsrpPerHour.setUnits("-dBm")
_CwceLteRadioHistoryRsrqTable_Object = MibTable
cwceLteRadioHistoryRsrqTable = _CwceLteRadioHistoryRsrqTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cwceLteRadioHistoryRsrqTable.setStatus("current")
_CwceLteRadioHistoryRsrqEntry_Object = MibTableRow
cwceLteRadioHistoryRsrqEntry = _CwceLteRadioHistoryRsrqEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 2, 2, 1)
)
cwceLteRadioHistoryRsrqEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cwceLteRadioHistoryRsrqEntry.setStatus("current")


class _CwceLteRadioHistoryRsrqPerSecond_Type(OctetString):
    """Custom type cwceLteRadioHistoryRsrqPerSecond based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(60, 60),
    )


_CwceLteRadioHistoryRsrqPerSecond_Type.__name__ = "OctetString"
_CwceLteRadioHistoryRsrqPerSecond_Object = MibTableColumn
cwceLteRadioHistoryRsrqPerSecond = _CwceLteRadioHistoryRsrqPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 2, 2, 1, 1),
    _CwceLteRadioHistoryRsrqPerSecond_Type()
)
cwceLteRadioHistoryRsrqPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteRadioHistoryRsrqPerSecond.setStatus("current")
if mibBuilder.loadTexts:
    cwceLteRadioHistoryRsrqPerSecond.setUnits("-dB")


class _CwceLteRadioHistoryRsrqPerMinute_Type(OctetString):
    """Custom type cwceLteRadioHistoryRsrqPerMinute based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(60, 60),
    )


_CwceLteRadioHistoryRsrqPerMinute_Type.__name__ = "OctetString"
_CwceLteRadioHistoryRsrqPerMinute_Object = MibTableColumn
cwceLteRadioHistoryRsrqPerMinute = _CwceLteRadioHistoryRsrqPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 2, 2, 1, 2),
    _CwceLteRadioHistoryRsrqPerMinute_Type()
)
cwceLteRadioHistoryRsrqPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteRadioHistoryRsrqPerMinute.setStatus("current")
if mibBuilder.loadTexts:
    cwceLteRadioHistoryRsrqPerMinute.setUnits("-dB")


class _CwceLteRadioHistoryRsrqPerHour_Type(OctetString):
    """Custom type cwceLteRadioHistoryRsrqPerHour based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(72, 72),
    )


_CwceLteRadioHistoryRsrqPerHour_Type.__name__ = "OctetString"
_CwceLteRadioHistoryRsrqPerHour_Object = MibTableColumn
cwceLteRadioHistoryRsrqPerHour = _CwceLteRadioHistoryRsrqPerHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 1, 2, 2, 1, 3),
    _CwceLteRadioHistoryRsrqPerHour_Type()
)
cwceLteRadioHistoryRsrqPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteRadioHistoryRsrqPerHour.setStatus("current")
if mibBuilder.loadTexts:
    cwceLteRadioHistoryRsrqPerHour.setUnits("-dB")
_CwceLteProfile_ObjectIdentity = ObjectIdentity
cwceLteProfile = _CwceLteProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2)
)
_CwceLteIpv4AddrType_Type = InetAddressType
_CwceLteIpv4AddrType_Object = MibScalar
cwceLteIpv4AddrType = _CwceLteIpv4AddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 1),
    _CwceLteIpv4AddrType_Type()
)
cwceLteIpv4AddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteIpv4AddrType.setStatus("current")
_CwceLteIpv6AddrType_Type = InetAddressType
_CwceLteIpv6AddrType_Object = MibScalar
cwceLteIpv6AddrType = _CwceLteIpv6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 2),
    _CwceLteIpv6AddrType_Type()
)
cwceLteIpv6AddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteIpv6AddrType.setStatus("current")
_CwceLteProfileTable_Object = MibTable
cwceLteProfileTable = _CwceLteProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cwceLteProfileTable.setStatus("current")
_CwceLteProfileEntry_Object = MibTableRow
cwceLteProfileEntry = _CwceLteProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 3, 1)
)
cwceLteProfileEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-WAN-CELL-EXT-MIB", "cwceLteProfileIndex"),
)
if mibBuilder.loadTexts:
    cwceLteProfileEntry.setStatus("current")


class _CwceLteProfileIndex_Type(Unsigned32):
    """Custom type cwceLteProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CwceLteProfileIndex_Type.__name__ = "Unsigned32"
_CwceLteProfileIndex_Object = MibTableColumn
cwceLteProfileIndex = _CwceLteProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 3, 1, 1),
    _CwceLteProfileIndex_Type()
)
cwceLteProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwceLteProfileIndex.setStatus("current")
_CwceLteProfileType_Type = CiscoWanCellExtProtocolType
_CwceLteProfileType_Object = MibTableColumn
cwceLteProfileType = _CwceLteProfileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 3, 1, 2),
    _CwceLteProfileType_Type()
)
cwceLteProfileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwceLteProfileType.setStatus("current")
_CwceLteProfileIPv4Addr_Type = InetAddress
_CwceLteProfileIPv4Addr_Object = MibTableColumn
cwceLteProfileIPv4Addr = _CwceLteProfileIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 3, 1, 3),
    _CwceLteProfileIPv4Addr_Type()
)
cwceLteProfileIPv4Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwceLteProfileIPv4Addr.setStatus("current")
_CwceLteProfileIPv6Addr_Type = InetAddress
_CwceLteProfileIPv6Addr_Object = MibTableColumn
cwceLteProfileIPv6Addr = _CwceLteProfileIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 3, 1, 4),
    _CwceLteProfileIPv6Addr_Type()
)
cwceLteProfileIPv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwceLteProfileIPv6Addr.setStatus("current")


class _CwceLteProfileApn_Type(SnmpAdminString):
    """Custom type cwceLteProfileApn based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CwceLteProfileApn_Type.__name__ = "SnmpAdminString"
_CwceLteProfileApn_Object = MibTableColumn
cwceLteProfileApn = _CwceLteProfileApn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 3, 1, 5),
    _CwceLteProfileApn_Type()
)
cwceLteProfileApn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwceLteProfileApn.setStatus("current")
_CwceLteProfileApnAmbr_Type = Unsigned32
_CwceLteProfileApnAmbr_Object = MibTableColumn
cwceLteProfileApnAmbr = _CwceLteProfileApnAmbr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 3, 1, 6),
    _CwceLteProfileApnAmbr_Type()
)
cwceLteProfileApnAmbr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwceLteProfileApnAmbr.setStatus("current")
_CwceLteProfileStorage_Type = StorageType
_CwceLteProfileStorage_Object = MibTableColumn
cwceLteProfileStorage = _CwceLteProfileStorage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 3, 1, 7),
    _CwceLteProfileStorage_Type()
)
cwceLteProfileStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwceLteProfileStorage.setStatus("current")
_CwceLteProfileRowStatus_Type = RowStatus
_CwceLteProfileRowStatus_Object = MibTableColumn
cwceLteProfileRowStatus = _CwceLteProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 3, 1, 8),
    _CwceLteProfileRowStatus_Type()
)
cwceLteProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwceLteProfileRowStatus.setStatus("current")
_CwceLtePdnTable_Object = MibTable
cwceLtePdnTable = _CwceLtePdnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cwceLtePdnTable.setStatus("current")
_CwceLtePdnEntry_Object = MibTableRow
cwceLtePdnEntry = _CwceLtePdnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 4, 1)
)
cwceLtePdnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwceLtePdnEntry.setStatus("current")
_CwceLtePdnProfileUsed_Type = Unsigned32
_CwceLtePdnProfileUsed_Object = MibTableColumn
cwceLtePdnProfileUsed = _CwceLtePdnProfileUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 4, 1, 2),
    _CwceLtePdnProfileUsed_Type()
)
cwceLtePdnProfileUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLtePdnProfileUsed.setStatus("current")


class _CwceLtePdnConnStatus_Type(Integer32):
    """Custom type cwceLtePdnConnStatus based on Integer32"""
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
        *(("active", 2),
          ("inactive", 3),
          ("unknown", 1))
    )


_CwceLtePdnConnStatus_Type.__name__ = "Integer32"
_CwceLtePdnConnStatus_Object = MibTableColumn
cwceLtePdnConnStatus = _CwceLtePdnConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 4, 1, 3),
    _CwceLtePdnConnStatus_Type()
)
cwceLtePdnConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLtePdnConnStatus.setStatus("current")
_CwceLtePdnType_Type = CiscoWanCellExtProtocolType
_CwceLtePdnType_Object = MibTableColumn
cwceLtePdnType = _CwceLtePdnType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 4, 1, 4),
    _CwceLtePdnType_Type()
)
cwceLtePdnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLtePdnType.setStatus("current")
_CwceLtePdnIpv4Addr_Type = InetAddress
_CwceLtePdnIpv4Addr_Object = MibTableColumn
cwceLtePdnIpv4Addr = _CwceLtePdnIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 4, 1, 5),
    _CwceLtePdnIpv4Addr_Type()
)
cwceLtePdnIpv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLtePdnIpv4Addr.setStatus("current")
_CwceLtePdnIpv6Addr_Type = InetAddress
_CwceLtePdnIpv6Addr_Object = MibTableColumn
cwceLtePdnIpv6Addr = _CwceLtePdnIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 4, 1, 6),
    _CwceLtePdnIpv6Addr_Type()
)
cwceLtePdnIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLtePdnIpv6Addr.setStatus("current")
_CwceLtePdnPriDnsIpv4Addr_Type = InetAddress
_CwceLtePdnPriDnsIpv4Addr_Object = MibTableColumn
cwceLtePdnPriDnsIpv4Addr = _CwceLtePdnPriDnsIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 4, 1, 7),
    _CwceLtePdnPriDnsIpv4Addr_Type()
)
cwceLtePdnPriDnsIpv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLtePdnPriDnsIpv4Addr.setStatus("current")
_CwceLtePdnSecDnsIpv4Addr_Type = InetAddress
_CwceLtePdnSecDnsIpv4Addr_Object = MibTableColumn
cwceLtePdnSecDnsIpv4Addr = _CwceLtePdnSecDnsIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 4, 1, 8),
    _CwceLtePdnSecDnsIpv4Addr_Type()
)
cwceLtePdnSecDnsIpv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLtePdnSecDnsIpv4Addr.setStatus("current")
_CwceLtePdnPriDnsIpv6Addr_Type = InetAddress
_CwceLtePdnPriDnsIpv6Addr_Object = MibTableColumn
cwceLtePdnPriDnsIpv6Addr = _CwceLtePdnPriDnsIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 4, 1, 9),
    _CwceLtePdnPriDnsIpv6Addr_Type()
)
cwceLtePdnPriDnsIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLtePdnPriDnsIpv6Addr.setStatus("current")
_CwceLtePdnSecDnsIpv6Addr_Type = InetAddress
_CwceLtePdnSecDnsIpv6Addr_Object = MibTableColumn
cwceLtePdnSecDnsIpv6Addr = _CwceLtePdnSecDnsIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 4, 1, 10),
    _CwceLtePdnSecDnsIpv6Addr_Type()
)
cwceLtePdnSecDnsIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLtePdnSecDnsIpv6Addr.setStatus("current")
_CwceLteEpsBearerQosTable_Object = MibTable
cwceLteEpsBearerQosTable = _CwceLteEpsBearerQosTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cwceLteEpsBearerQosTable.setStatus("current")
_CwceLteEpsBearerQosEntry_Object = MibTableRow
cwceLteEpsBearerQosEntry = _CwceLteEpsBearerQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 5, 1)
)
cwceLteEpsBearerQosEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WAN-CELL-EXT-MIB", "cwceLteEpsBearerId"),
)
if mibBuilder.loadTexts:
    cwceLteEpsBearerQosEntry.setStatus("current")


class _CwceLteEpsBearerId_Type(Unsigned32):
    """Custom type cwceLteEpsBearerId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CwceLteEpsBearerId_Type.__name__ = "Unsigned32"
_CwceLteEpsBearerId_Object = MibTableColumn
cwceLteEpsBearerId = _CwceLteEpsBearerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 5, 1, 1),
    _CwceLteEpsBearerId_Type()
)
cwceLteEpsBearerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwceLteEpsBearerId.setStatus("current")


class _CwceLteEpsBearerType_Type(Integer32):
    """Custom type cwceLteEpsBearerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gbr", 1),
          ("nonGbr", 2),
          ("unknown", 3))
    )


_CwceLteEpsBearerType_Type.__name__ = "Integer32"
_CwceLteEpsBearerType_Object = MibTableColumn
cwceLteEpsBearerType = _CwceLteEpsBearerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 5, 1, 2),
    _CwceLteEpsBearerType_Type()
)
cwceLteEpsBearerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteEpsBearerType.setStatus("current")
_CwceLteEpsQCI_Type = Unsigned32
_CwceLteEpsQCI_Object = MibTableColumn
cwceLteEpsQCI = _CwceLteEpsQCI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 5, 1, 3),
    _CwceLteEpsQCI_Type()
)
cwceLteEpsQCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteEpsQCI.setStatus("current")
_CwceLteEpsArp_Type = Unsigned32
_CwceLteEpsArp_Object = MibTableColumn
cwceLteEpsArp = _CwceLteEpsArp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 5, 1, 4),
    _CwceLteEpsArp_Type()
)
cwceLteEpsArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteEpsArp.setStatus("current")


class _CwceLteEpsBearerResType_Type(Integer32):
    """Custom type cwceLteEpsBearerResType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dedicatedBearer", 2),
          ("defaultBearer", 1),
          ("unknown", 3))
    )


_CwceLteEpsBearerResType_Type.__name__ = "Integer32"
_CwceLteEpsBearerResType_Object = MibTableColumn
cwceLteEpsBearerResType = _CwceLteEpsBearerResType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 5, 1, 5),
    _CwceLteEpsBearerResType_Type()
)
cwceLteEpsBearerResType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteEpsBearerResType.setStatus("current")
_CwceLteEpsGbr_Type = Unsigned32
_CwceLteEpsGbr_Object = MibTableColumn
cwceLteEpsGbr = _CwceLteEpsGbr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 5, 1, 6),
    _CwceLteEpsGbr_Type()
)
cwceLteEpsGbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteEpsGbr.setStatus("current")
_CwceLteEpsMbr_Type = Unsigned32
_CwceLteEpsMbr_Object = MibTableColumn
cwceLteEpsMbr = _CwceLteEpsMbr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 5, 1, 7),
    _CwceLteEpsMbr_Type()
)
cwceLteEpsMbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteEpsMbr.setStatus("current")
_CwceLteEpsAmbr_Type = Unsigned32
_CwceLteEpsAmbr_Object = MibTableColumn
cwceLteEpsAmbr = _CwceLteEpsAmbr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 5, 1, 8),
    _CwceLteEpsAmbr_Type()
)
cwceLteEpsAmbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteEpsAmbr.setStatus("current")
_CwceLteEpsTotalBytesTx_Type = Counter64
_CwceLteEpsTotalBytesTx_Object = MibTableColumn
cwceLteEpsTotalBytesTx = _CwceLteEpsTotalBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 5, 1, 9),
    _CwceLteEpsTotalBytesTx_Type()
)
cwceLteEpsTotalBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteEpsTotalBytesTx.setStatus("current")
if mibBuilder.loadTexts:
    cwceLteEpsTotalBytesTx.setUnits("bytes")
_CwceLteEpsTotalBytesRx_Type = Counter64
_CwceLteEpsTotalBytesRx_Object = MibTableColumn
cwceLteEpsTotalBytesRx = _CwceLteEpsTotalBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 5, 1, 10),
    _CwceLteEpsTotalBytesRx_Type()
)
cwceLteEpsTotalBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteEpsTotalBytesRx.setStatus("current")
if mibBuilder.loadTexts:
    cwceLteEpsTotalBytesRx.setUnits("bytes")
_CwceLteEpsPacketsTx_Type = Counter64
_CwceLteEpsPacketsTx_Object = MibTableColumn
cwceLteEpsPacketsTx = _CwceLteEpsPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 5, 1, 11),
    _CwceLteEpsPacketsTx_Type()
)
cwceLteEpsPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteEpsPacketsTx.setStatus("current")
if mibBuilder.loadTexts:
    cwceLteEpsPacketsTx.setUnits("packets")
_CwceLteEpsPacketsRx_Type = Counter64
_CwceLteEpsPacketsRx_Object = MibTableColumn
cwceLteEpsPacketsRx = _CwceLteEpsPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 1, 1, 2, 5, 1, 12),
    _CwceLteEpsPacketsRx_Type()
)
cwceLteEpsPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwceLteEpsPacketsRx.setStatus("current")
if mibBuilder.loadTexts:
    cwceLteEpsPacketsRx.setUnits("packets")
_CiscoWanCellExtMIBConform_ObjectIdentity = ObjectIdentity
ciscoWanCellExtMIBConform = _CiscoWanCellExtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 2)
)
_CiscoWanCellExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWanCellExtMIBCompliances = _CiscoWanCellExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 2, 1)
)
_CiscoWanCellExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWanCellExtMIBGroups = _CiscoWanCellExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 2, 2)
)

# Managed Objects groups

ciscoWanCellExtMIBLteObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 2, 2, 1)
)
ciscoWanCellExtMIBLteObjectGroup.setObjects(
      *(("CISCO-WAN-CELL-EXT-MIB", "cwceLteCurrRsrp"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteCurrRsrq"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteCurrSnr"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteCurrSinr"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteCurrCqiIndex"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteNotifRsrp"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteNotifRsrq"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteRsrpOnsetNotifThreshold"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteRsrpAbateNotifThreshold"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteRsrqOnsetNotifThreshold"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteRsrqAbateNotifThreshold"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteRsrpOnsetNotifFlag"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteRsrpAbateNotifFlag"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteRsrqOnsetNotifFlag"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteRsrqAbateNotifFlag"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteCurrOperatingBand"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteRadioHistoryRsrpPerSecond"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteRadioHistoryRsrpPerMinute"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteRadioHistoryRsrpPerHour"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteRadioHistoryRsrqPerSecond"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteRadioHistoryRsrqPerMinute"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteRadioHistoryRsrqPerHour"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteIpv4AddrType"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteIpv6AddrType"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteProfileType"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteProfileIPv4Addr"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteProfileIPv6Addr"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteProfileApn"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteProfileApnAmbr"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteProfileStorage"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteProfileRowStatus"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLtePdnProfileUsed"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLtePdnConnStatus"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLtePdnType"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLtePdnIpv4Addr"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLtePdnIpv6Addr"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLtePdnPriDnsIpv4Addr"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLtePdnSecDnsIpv4Addr"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLtePdnPriDnsIpv6Addr"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLtePdnSecDnsIpv6Addr"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteEpsBearerType"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteEpsArp"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteEpsQCI"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteEpsBearerResType"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteEpsGbr"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteEpsMbr"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteEpsAmbr"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteEpsTotalBytesTx"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteEpsTotalBytesRx"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteEpsPacketsTx"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteEpsPacketsRx"))
)
if mibBuilder.loadTexts:
    ciscoWanCellExtMIBLteObjectGroup.setStatus("current")


# Notification objects

cwceLteRsrqOnsetNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 0, 1)
)
cwceLteRsrqOnsetNotif.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteRsrqOnsetNotifFlag"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteNotifRsrq"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteRsrqOnsetNotifThreshold"))
)
if mibBuilder.loadTexts:
    cwceLteRsrqOnsetNotif.setStatus(
        "current"
    )

cwceLteRsrqAbateNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 0, 2)
)
cwceLteRsrqAbateNotif.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteRsrqAbateNotifFlag"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteNotifRsrq"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteRsrqAbateNotifThreshold"))
)
if mibBuilder.loadTexts:
    cwceLteRsrqAbateNotif.setStatus(
        "current"
    )

cwceLteRsrpOnsetNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 0, 3)
)
cwceLteRsrpOnsetNotif.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteRsrpOnsetNotifFlag"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteNotifRsrp"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteRsrpOnsetNotifThreshold"))
)
if mibBuilder.loadTexts:
    cwceLteRsrpOnsetNotif.setStatus(
        "current"
    )

cwceLteRsrpAbateNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 0, 4)
)
cwceLteRsrpAbateNotif.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteRsrpAbateNotifFlag"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteNotifRsrp"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteRsrpAbateNotifThreshold"))
)
if mibBuilder.loadTexts:
    cwceLteRsrpAbateNotif.setStatus(
        "current"
    )


# Notifications groups

ciscoWanCellExtMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 2, 2, 2)
)
ciscoWanCellExtMIBNotificationGroup.setObjects(
      *(("CISCO-WAN-CELL-EXT-MIB", "cwceLteRsrqOnsetNotif"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteRsrqAbateNotif"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteRsrpOnsetNotif"),
        ("CISCO-WAN-CELL-EXT-MIB", "cwceLteRsrpAbateNotif"))
)
if mibBuilder.loadTexts:
    ciscoWanCellExtMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoWanCellExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 817, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoWanCellExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-CELL-EXT-MIB",
    **{"CiscoWanCellExtProtocolType": CiscoWanCellExtProtocolType,
       "CiscoWanCellExtRsrp": CiscoWanCellExtRsrp,
       "CiscoWanCellExtRsrq": CiscoWanCellExtRsrq,
       "CiscoWanCellExtCqiIndex": CiscoWanCellExtCqiIndex,
       "CiscoWanCellExtSNR": CiscoWanCellExtSNR,
       "CiscoWanCellExtSINR": CiscoWanCellExtSINR,
       "ciscoWanCellExtMIB": ciscoWanCellExtMIB,
       "ciscoWanCellExtMIBNotifs": ciscoWanCellExtMIBNotifs,
       "cwceLteRsrqOnsetNotif": cwceLteRsrqOnsetNotif,
       "cwceLteRsrqAbateNotif": cwceLteRsrqAbateNotif,
       "cwceLteRsrpOnsetNotif": cwceLteRsrpOnsetNotif,
       "cwceLteRsrpAbateNotif": cwceLteRsrpAbateNotif,
       "ciscoWanCellExtMIBObjects": ciscoWanCellExtMIBObjects,
       "ciscoWanCellExtLte": ciscoWanCellExtLte,
       "cwceLteRadio": cwceLteRadio,
       "cwceLteRadioTable": cwceLteRadioTable,
       "cwceLteRadioEntry": cwceLteRadioEntry,
       "cwceLteCurrRsrp": cwceLteCurrRsrp,
       "cwceLteCurrRsrq": cwceLteCurrRsrq,
       "cwceLteCurrSnr": cwceLteCurrSnr,
       "cwceLteCurrSinr": cwceLteCurrSinr,
       "cwceLteCurrCqiIndex": cwceLteCurrCqiIndex,
       "cwceLteCurrOperatingBand": cwceLteCurrOperatingBand,
       "cwceLteNotifRsrp": cwceLteNotifRsrp,
       "cwceLteNotifRsrq": cwceLteNotifRsrq,
       "cwceLteRsrpOnsetNotifThreshold": cwceLteRsrpOnsetNotifThreshold,
       "cwceLteRsrpAbateNotifThreshold": cwceLteRsrpAbateNotifThreshold,
       "cwceLteRsrqOnsetNotifThreshold": cwceLteRsrqOnsetNotifThreshold,
       "cwceLteRsrqAbateNotifThreshold": cwceLteRsrqAbateNotifThreshold,
       "cwceLteRsrpOnsetNotifFlag": cwceLteRsrpOnsetNotifFlag,
       "cwceLteRsrpAbateNotifFlag": cwceLteRsrpAbateNotifFlag,
       "cwceLteRsrqOnsetNotifFlag": cwceLteRsrqOnsetNotifFlag,
       "cwceLteRsrqAbateNotifFlag": cwceLteRsrqAbateNotifFlag,
       "cwceLteRadioHistory": cwceLteRadioHistory,
       "cwceLteRadioHistoryRsrpTable": cwceLteRadioHistoryRsrpTable,
       "cwceLteRadioHistoryRsrpEntry": cwceLteRadioHistoryRsrpEntry,
       "cwceLteRadioHistoryRsrpPerSecond": cwceLteRadioHistoryRsrpPerSecond,
       "cwceLteRadioHistoryRsrpPerMinute": cwceLteRadioHistoryRsrpPerMinute,
       "cwceLteRadioHistoryRsrpPerHour": cwceLteRadioHistoryRsrpPerHour,
       "cwceLteRadioHistoryRsrqTable": cwceLteRadioHistoryRsrqTable,
       "cwceLteRadioHistoryRsrqEntry": cwceLteRadioHistoryRsrqEntry,
       "cwceLteRadioHistoryRsrqPerSecond": cwceLteRadioHistoryRsrqPerSecond,
       "cwceLteRadioHistoryRsrqPerMinute": cwceLteRadioHistoryRsrqPerMinute,
       "cwceLteRadioHistoryRsrqPerHour": cwceLteRadioHistoryRsrqPerHour,
       "cwceLteProfile": cwceLteProfile,
       "cwceLteIpv4AddrType": cwceLteIpv4AddrType,
       "cwceLteIpv6AddrType": cwceLteIpv6AddrType,
       "cwceLteProfileTable": cwceLteProfileTable,
       "cwceLteProfileEntry": cwceLteProfileEntry,
       "cwceLteProfileIndex": cwceLteProfileIndex,
       "cwceLteProfileType": cwceLteProfileType,
       "cwceLteProfileIPv4Addr": cwceLteProfileIPv4Addr,
       "cwceLteProfileIPv6Addr": cwceLteProfileIPv6Addr,
       "cwceLteProfileApn": cwceLteProfileApn,
       "cwceLteProfileApnAmbr": cwceLteProfileApnAmbr,
       "cwceLteProfileStorage": cwceLteProfileStorage,
       "cwceLteProfileRowStatus": cwceLteProfileRowStatus,
       "cwceLtePdnTable": cwceLtePdnTable,
       "cwceLtePdnEntry": cwceLtePdnEntry,
       "cwceLtePdnProfileUsed": cwceLtePdnProfileUsed,
       "cwceLtePdnConnStatus": cwceLtePdnConnStatus,
       "cwceLtePdnType": cwceLtePdnType,
       "cwceLtePdnIpv4Addr": cwceLtePdnIpv4Addr,
       "cwceLtePdnIpv6Addr": cwceLtePdnIpv6Addr,
       "cwceLtePdnPriDnsIpv4Addr": cwceLtePdnPriDnsIpv4Addr,
       "cwceLtePdnSecDnsIpv4Addr": cwceLtePdnSecDnsIpv4Addr,
       "cwceLtePdnPriDnsIpv6Addr": cwceLtePdnPriDnsIpv6Addr,
       "cwceLtePdnSecDnsIpv6Addr": cwceLtePdnSecDnsIpv6Addr,
       "cwceLteEpsBearerQosTable": cwceLteEpsBearerQosTable,
       "cwceLteEpsBearerQosEntry": cwceLteEpsBearerQosEntry,
       "cwceLteEpsBearerId": cwceLteEpsBearerId,
       "cwceLteEpsBearerType": cwceLteEpsBearerType,
       "cwceLteEpsQCI": cwceLteEpsQCI,
       "cwceLteEpsArp": cwceLteEpsArp,
       "cwceLteEpsBearerResType": cwceLteEpsBearerResType,
       "cwceLteEpsGbr": cwceLteEpsGbr,
       "cwceLteEpsMbr": cwceLteEpsMbr,
       "cwceLteEpsAmbr": cwceLteEpsAmbr,
       "cwceLteEpsTotalBytesTx": cwceLteEpsTotalBytesTx,
       "cwceLteEpsTotalBytesRx": cwceLteEpsTotalBytesRx,
       "cwceLteEpsPacketsTx": cwceLteEpsPacketsTx,
       "cwceLteEpsPacketsRx": cwceLteEpsPacketsRx,
       "ciscoWanCellExtMIBConform": ciscoWanCellExtMIBConform,
       "ciscoWanCellExtMIBCompliances": ciscoWanCellExtMIBCompliances,
       "ciscoWanCellExtMIBCompliance": ciscoWanCellExtMIBCompliance,
       "ciscoWanCellExtMIBGroups": ciscoWanCellExtMIBGroups,
       "ciscoWanCellExtMIBLteObjectGroup": ciscoWanCellExtMIBLteObjectGroup,
       "ciscoWanCellExtMIBNotificationGroup": ciscoWanCellExtMIBNotificationGroup}
)
