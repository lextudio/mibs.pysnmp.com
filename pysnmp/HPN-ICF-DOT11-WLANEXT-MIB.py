# SNMP MIB module (HPN-ICF-DOT11-WLANEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DOT11-WLANEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:57 2024
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

(HpnicfDot11ObjectIDType,
 HpnicfDot11QosAcType,
 HpnicfDot11RadioScopeType,
 hpnicfDot11) = mibBuilder.importSymbols(
    "HPN-ICF-DOT11-REF-MIB",
    "HpnicfDot11ObjectIDType",
    "HpnicfDot11QosAcType",
    "HpnicfDot11RadioScopeType",
    "hpnicfDot11")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfDot11WLANEXT = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7)
)
hpnicfDot11WLANEXT.setRevisions(
        ("2007-06-08 20:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfDot11RFGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11RFGroup = _HpnicfDot11RFGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 1)
)
_HpnicfDot11RFSignalStatisTable_Object = MibTable
hpnicfDot11RFSignalStatisTable = _HpnicfDot11RFSignalStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot11RFSignalStatisTable.setStatus("current")
_HpnicfDot11RFSignalStatisEntry_Object = MibTableRow
hpnicfDot11RFSignalStatisEntry = _HpnicfDot11RFSignalStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 1, 1, 1)
)
hpnicfDot11RFSignalStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-WLANEXT-MIB", "hpnicfDot11RFAPID"),
    (0, "HPN-ICF-DOT11-WLANEXT-MIB", "hpnicfDot11RFRadioID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RFSignalStatisEntry.setStatus("current")
_HpnicfDot11RFAPID_Type = HpnicfDot11ObjectIDType
_HpnicfDot11RFAPID_Object = MibTableColumn
hpnicfDot11RFAPID = _HpnicfDot11RFAPID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 1, 1, 1, 1),
    _HpnicfDot11RFAPID_Type()
)
hpnicfDot11RFAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RFAPID.setStatus("current")
_HpnicfDot11RFRadioID_Type = HpnicfDot11RadioScopeType
_HpnicfDot11RFRadioID_Object = MibTableColumn
hpnicfDot11RFRadioID = _HpnicfDot11RFRadioID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 1, 1, 1, 2),
    _HpnicfDot11RFRadioID_Type()
)
hpnicfDot11RFRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RFRadioID.setStatus("current")
_HpnicfDot11RFSignalStatisInterv_Type = Integer32
_HpnicfDot11RFSignalStatisInterv_Object = MibTableColumn
hpnicfDot11RFSignalStatisInterv = _HpnicfDot11RFSignalStatisInterv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 1, 1, 1, 3),
    _HpnicfDot11RFSignalStatisInterv_Type()
)
hpnicfDot11RFSignalStatisInterv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RFSignalStatisInterv.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RFSignalStatisInterv.setUnits("second")
_HpnicfDot11RFAverageSignalStrength_Type = Integer32
_HpnicfDot11RFAverageSignalStrength_Object = MibTableColumn
hpnicfDot11RFAverageSignalStrength = _HpnicfDot11RFAverageSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 1, 1, 1, 4),
    _HpnicfDot11RFAverageSignalStrength_Type()
)
hpnicfDot11RFAverageSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RFAverageSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RFAverageSignalStrength.setUnits("dBm")
_HpnicfDot11RFMaxSignalStrength_Type = Integer32
_HpnicfDot11RFMaxSignalStrength_Object = MibTableColumn
hpnicfDot11RFMaxSignalStrength = _HpnicfDot11RFMaxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 1, 1, 1, 5),
    _HpnicfDot11RFMaxSignalStrength_Type()
)
hpnicfDot11RFMaxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RFMaxSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RFMaxSignalStrength.setUnits("dBm")
_HpnicfDot11RFMinSignalStrength_Type = Integer32
_HpnicfDot11RFMinSignalStrength_Object = MibTableColumn
hpnicfDot11RFMinSignalStrength = _HpnicfDot11RFMinSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 1, 1, 1, 6),
    _HpnicfDot11RFMinSignalStrength_Type()
)
hpnicfDot11RFMinSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RFMinSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RFMinSignalStrength.setUnits("dBm")
_HpnicfDot11QosGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11QosGroup = _HpnicfDot11QosGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 2)
)
_HpnicfDot11QosStatisTable_Object = MibTable
hpnicfDot11QosStatisTable = _HpnicfDot11QosStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot11QosStatisTable.setStatus("current")
_HpnicfDot11QosStatisEntry_Object = MibTableRow
hpnicfDot11QosStatisEntry = _HpnicfDot11QosStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 2, 1, 1)
)
hpnicfDot11QosStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-WLANEXT-MIB", "hpnicfDot11QosAPID"),
    (0, "HPN-ICF-DOT11-WLANEXT-MIB", "hpnicfDot11QosRadioID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11QosStatisEntry.setStatus("current")
_HpnicfDot11QosAPID_Type = HpnicfDot11ObjectIDType
_HpnicfDot11QosAPID_Object = MibTableColumn
hpnicfDot11QosAPID = _HpnicfDot11QosAPID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 2, 1, 1, 1),
    _HpnicfDot11QosAPID_Type()
)
hpnicfDot11QosAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11QosAPID.setStatus("current")
_HpnicfDot11QosRadioID_Type = HpnicfDot11RadioScopeType
_HpnicfDot11QosRadioID_Object = MibTableColumn
hpnicfDot11QosRadioID = _HpnicfDot11QosRadioID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 2, 1, 1, 2),
    _HpnicfDot11QosRadioID_Type()
)
hpnicfDot11QosRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11QosRadioID.setStatus("current")
_HpnicfDot11QosAverageQueLen_Type = Integer32
_HpnicfDot11QosAverageQueLen_Object = MibTableColumn
hpnicfDot11QosAverageQueLen = _HpnicfDot11QosAverageQueLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 2, 1, 1, 3),
    _HpnicfDot11QosAverageQueLen_Type()
)
hpnicfDot11QosAverageQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11QosAverageQueLen.setStatus("current")
_HpnicfDot11QosDropFrameRatio_Type = Integer32
_HpnicfDot11QosDropFrameRatio_Object = MibTableColumn
hpnicfDot11QosDropFrameRatio = _HpnicfDot11QosDropFrameRatio_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 2, 1, 1, 4),
    _HpnicfDot11QosDropFrameRatio_Type()
)
hpnicfDot11QosDropFrameRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11QosDropFrameRatio.setStatus("current")
_HpnicfDot11QosAverageDataRate_Type = Integer32
_HpnicfDot11QosAverageDataRate_Object = MibTableColumn
hpnicfDot11QosAverageDataRate = _HpnicfDot11QosAverageDataRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 2, 1, 1, 5),
    _HpnicfDot11QosAverageDataRate_Type()
)
hpnicfDot11QosAverageDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11QosAverageDataRate.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11QosAverageDataRate.setUnits("Kbps")
_HpnicfDot11QosAcStatisTable_Object = MibTable
hpnicfDot11QosAcStatisTable = _HpnicfDot11QosAcStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfDot11QosAcStatisTable.setStatus("current")
_HpnicfDot11QosAcStatisEntry_Object = MibTableRow
hpnicfDot11QosAcStatisEntry = _HpnicfDot11QosAcStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 2, 2, 1)
)
hpnicfDot11QosAcStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-WLANEXT-MIB", "hpnicfDot11QosAPID"),
    (0, "HPN-ICF-DOT11-WLANEXT-MIB", "hpnicfDot11QosRadioID"),
    (0, "HPN-ICF-DOT11-WLANEXT-MIB", "hpnicfDot11QosAcType"),
)
if mibBuilder.loadTexts:
    hpnicfDot11QosAcStatisEntry.setStatus("current")
_HpnicfDot11QosAcType_Type = HpnicfDot11QosAcType
_HpnicfDot11QosAcType_Object = MibTableColumn
hpnicfDot11QosAcType = _HpnicfDot11QosAcType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 2, 2, 1, 1),
    _HpnicfDot11QosAcType_Type()
)
hpnicfDot11QosAcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11QosAcType.setStatus("current")
_HpnicfDot11AcDropFrameCnt_Type = Counter32
_HpnicfDot11AcDropFrameCnt_Object = MibTableColumn
hpnicfDot11AcDropFrameCnt = _HpnicfDot11AcDropFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 2, 2, 1, 2),
    _HpnicfDot11AcDropFrameCnt_Type()
)
hpnicfDot11AcDropFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11AcDropFrameCnt.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DOT11-WLANEXT-MIB",
    **{"hpnicfDot11WLANEXT": hpnicfDot11WLANEXT,
       "hpnicfDot11RFGroup": hpnicfDot11RFGroup,
       "hpnicfDot11RFSignalStatisTable": hpnicfDot11RFSignalStatisTable,
       "hpnicfDot11RFSignalStatisEntry": hpnicfDot11RFSignalStatisEntry,
       "hpnicfDot11RFAPID": hpnicfDot11RFAPID,
       "hpnicfDot11RFRadioID": hpnicfDot11RFRadioID,
       "hpnicfDot11RFSignalStatisInterv": hpnicfDot11RFSignalStatisInterv,
       "hpnicfDot11RFAverageSignalStrength": hpnicfDot11RFAverageSignalStrength,
       "hpnicfDot11RFMaxSignalStrength": hpnicfDot11RFMaxSignalStrength,
       "hpnicfDot11RFMinSignalStrength": hpnicfDot11RFMinSignalStrength,
       "hpnicfDot11QosGroup": hpnicfDot11QosGroup,
       "hpnicfDot11QosStatisTable": hpnicfDot11QosStatisTable,
       "hpnicfDot11QosStatisEntry": hpnicfDot11QosStatisEntry,
       "hpnicfDot11QosAPID": hpnicfDot11QosAPID,
       "hpnicfDot11QosRadioID": hpnicfDot11QosRadioID,
       "hpnicfDot11QosAverageQueLen": hpnicfDot11QosAverageQueLen,
       "hpnicfDot11QosDropFrameRatio": hpnicfDot11QosDropFrameRatio,
       "hpnicfDot11QosAverageDataRate": hpnicfDot11QosAverageDataRate,
       "hpnicfDot11QosAcStatisTable": hpnicfDot11QosAcStatisTable,
       "hpnicfDot11QosAcStatisEntry": hpnicfDot11QosAcStatisEntry,
       "hpnicfDot11QosAcType": hpnicfDot11QosAcType,
       "hpnicfDot11AcDropFrameCnt": hpnicfDot11AcDropFrameCnt}
)
