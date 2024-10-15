# SNMP MIB module (HH3C-DOT11-WLANEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DOT11-WLANEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:57 2024
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

(Hh3cDot11ObjectIDType,
 Hh3cDot11QosAcType,
 Hh3cDot11RadioScopeType,
 hh3cDot11) = mibBuilder.importSymbols(
    "HH3C-DOT11-REF-MIB",
    "Hh3cDot11ObjectIDType",
    "Hh3cDot11QosAcType",
    "Hh3cDot11RadioScopeType",
    "hh3cDot11")

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

hh3cDot11WLANEXT = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 7)
)
hh3cDot11WLANEXT.setRevisions(
        ("2007-06-08 20:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cDot11RFGroup_ObjectIdentity = ObjectIdentity
hh3cDot11RFGroup = _Hh3cDot11RFGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 7, 1)
)
_Hh3cDot11RFSignalStatisTable_Object = MibTable
hh3cDot11RFSignalStatisTable = _Hh3cDot11RFSignalStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 7, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11RFSignalStatisTable.setStatus("current")
_Hh3cDot11RFSignalStatisEntry_Object = MibTableRow
hh3cDot11RFSignalStatisEntry = _Hh3cDot11RFSignalStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 7, 1, 1, 1)
)
hh3cDot11RFSignalStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-WLANEXT-MIB", "hh3cDot11RFAPID"),
    (0, "HH3C-DOT11-WLANEXT-MIB", "hh3cDot11RFRadioID"),
)
if mibBuilder.loadTexts:
    hh3cDot11RFSignalStatisEntry.setStatus("current")
_Hh3cDot11RFAPID_Type = Hh3cDot11ObjectIDType
_Hh3cDot11RFAPID_Object = MibTableColumn
hh3cDot11RFAPID = _Hh3cDot11RFAPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 7, 1, 1, 1, 1),
    _Hh3cDot11RFAPID_Type()
)
hh3cDot11RFAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RFAPID.setStatus("current")
_Hh3cDot11RFRadioID_Type = Hh3cDot11RadioScopeType
_Hh3cDot11RFRadioID_Object = MibTableColumn
hh3cDot11RFRadioID = _Hh3cDot11RFRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 7, 1, 1, 1, 2),
    _Hh3cDot11RFRadioID_Type()
)
hh3cDot11RFRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RFRadioID.setStatus("current")
_Hh3cDot11RFSignalStatisInterv_Type = Integer32
_Hh3cDot11RFSignalStatisInterv_Object = MibTableColumn
hh3cDot11RFSignalStatisInterv = _Hh3cDot11RFSignalStatisInterv_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 7, 1, 1, 1, 3),
    _Hh3cDot11RFSignalStatisInterv_Type()
)
hh3cDot11RFSignalStatisInterv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RFSignalStatisInterv.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RFSignalStatisInterv.setUnits("second")
_Hh3cDot11RFAverageSignalStrength_Type = Integer32
_Hh3cDot11RFAverageSignalStrength_Object = MibTableColumn
hh3cDot11RFAverageSignalStrength = _Hh3cDot11RFAverageSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 7, 1, 1, 1, 4),
    _Hh3cDot11RFAverageSignalStrength_Type()
)
hh3cDot11RFAverageSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RFAverageSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RFAverageSignalStrength.setUnits("dBm")
_Hh3cDot11RFMaxSignalStrength_Type = Integer32
_Hh3cDot11RFMaxSignalStrength_Object = MibTableColumn
hh3cDot11RFMaxSignalStrength = _Hh3cDot11RFMaxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 7, 1, 1, 1, 5),
    _Hh3cDot11RFMaxSignalStrength_Type()
)
hh3cDot11RFMaxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RFMaxSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RFMaxSignalStrength.setUnits("dBm")
_Hh3cDot11RFMinSignalStrength_Type = Integer32
_Hh3cDot11RFMinSignalStrength_Object = MibTableColumn
hh3cDot11RFMinSignalStrength = _Hh3cDot11RFMinSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 7, 1, 1, 1, 6),
    _Hh3cDot11RFMinSignalStrength_Type()
)
hh3cDot11RFMinSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RFMinSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RFMinSignalStrength.setUnits("dBm")
_Hh3cDot11QosGroup_ObjectIdentity = ObjectIdentity
hh3cDot11QosGroup = _Hh3cDot11QosGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 7, 2)
)
_Hh3cDot11QosStatisTable_Object = MibTable
hh3cDot11QosStatisTable = _Hh3cDot11QosStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 7, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11QosStatisTable.setStatus("current")
_Hh3cDot11QosStatisEntry_Object = MibTableRow
hh3cDot11QosStatisEntry = _Hh3cDot11QosStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 7, 2, 1, 1)
)
hh3cDot11QosStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-WLANEXT-MIB", "hh3cDot11QosAPID"),
    (0, "HH3C-DOT11-WLANEXT-MIB", "hh3cDot11QosRadioID"),
)
if mibBuilder.loadTexts:
    hh3cDot11QosStatisEntry.setStatus("current")
_Hh3cDot11QosAPID_Type = Hh3cDot11ObjectIDType
_Hh3cDot11QosAPID_Object = MibTableColumn
hh3cDot11QosAPID = _Hh3cDot11QosAPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 7, 2, 1, 1, 1),
    _Hh3cDot11QosAPID_Type()
)
hh3cDot11QosAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11QosAPID.setStatus("current")
_Hh3cDot11QosRadioID_Type = Hh3cDot11RadioScopeType
_Hh3cDot11QosRadioID_Object = MibTableColumn
hh3cDot11QosRadioID = _Hh3cDot11QosRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 7, 2, 1, 1, 2),
    _Hh3cDot11QosRadioID_Type()
)
hh3cDot11QosRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11QosRadioID.setStatus("current")
_Hh3cDot11QosAverageQueLen_Type = Integer32
_Hh3cDot11QosAverageQueLen_Object = MibTableColumn
hh3cDot11QosAverageQueLen = _Hh3cDot11QosAverageQueLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 7, 2, 1, 1, 3),
    _Hh3cDot11QosAverageQueLen_Type()
)
hh3cDot11QosAverageQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11QosAverageQueLen.setStatus("current")
_Hh3cDot11QosDropFrameRatio_Type = Integer32
_Hh3cDot11QosDropFrameRatio_Object = MibTableColumn
hh3cDot11QosDropFrameRatio = _Hh3cDot11QosDropFrameRatio_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 7, 2, 1, 1, 4),
    _Hh3cDot11QosDropFrameRatio_Type()
)
hh3cDot11QosDropFrameRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11QosDropFrameRatio.setStatus("current")
_Hh3cDot11QosAverageDataRate_Type = Integer32
_Hh3cDot11QosAverageDataRate_Object = MibTableColumn
hh3cDot11QosAverageDataRate = _Hh3cDot11QosAverageDataRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 7, 2, 1, 1, 5),
    _Hh3cDot11QosAverageDataRate_Type()
)
hh3cDot11QosAverageDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11QosAverageDataRate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11QosAverageDataRate.setUnits("Kbps")
_Hh3cDot11QosAcStatisTable_Object = MibTable
hh3cDot11QosAcStatisTable = _Hh3cDot11QosAcStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 7, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11QosAcStatisTable.setStatus("current")
_Hh3cDot11QosAcStatisEntry_Object = MibTableRow
hh3cDot11QosAcStatisEntry = _Hh3cDot11QosAcStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 7, 2, 2, 1)
)
hh3cDot11QosAcStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-WLANEXT-MIB", "hh3cDot11QosAPID"),
    (0, "HH3C-DOT11-WLANEXT-MIB", "hh3cDot11QosRadioID"),
    (0, "HH3C-DOT11-WLANEXT-MIB", "hh3cDot11QosAcType"),
)
if mibBuilder.loadTexts:
    hh3cDot11QosAcStatisEntry.setStatus("current")
_Hh3cDot11QosAcType_Type = Hh3cDot11QosAcType
_Hh3cDot11QosAcType_Object = MibTableColumn
hh3cDot11QosAcType = _Hh3cDot11QosAcType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 7, 2, 2, 1, 1),
    _Hh3cDot11QosAcType_Type()
)
hh3cDot11QosAcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11QosAcType.setStatus("current")
_Hh3cDot11AcDropFrameCnt_Type = Counter32
_Hh3cDot11AcDropFrameCnt_Object = MibTableColumn
hh3cDot11AcDropFrameCnt = _Hh3cDot11AcDropFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 7, 2, 2, 1, 2),
    _Hh3cDot11AcDropFrameCnt_Type()
)
hh3cDot11AcDropFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11AcDropFrameCnt.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DOT11-WLANEXT-MIB",
    **{"hh3cDot11WLANEXT": hh3cDot11WLANEXT,
       "hh3cDot11RFGroup": hh3cDot11RFGroup,
       "hh3cDot11RFSignalStatisTable": hh3cDot11RFSignalStatisTable,
       "hh3cDot11RFSignalStatisEntry": hh3cDot11RFSignalStatisEntry,
       "hh3cDot11RFAPID": hh3cDot11RFAPID,
       "hh3cDot11RFRadioID": hh3cDot11RFRadioID,
       "hh3cDot11RFSignalStatisInterv": hh3cDot11RFSignalStatisInterv,
       "hh3cDot11RFAverageSignalStrength": hh3cDot11RFAverageSignalStrength,
       "hh3cDot11RFMaxSignalStrength": hh3cDot11RFMaxSignalStrength,
       "hh3cDot11RFMinSignalStrength": hh3cDot11RFMinSignalStrength,
       "hh3cDot11QosGroup": hh3cDot11QosGroup,
       "hh3cDot11QosStatisTable": hh3cDot11QosStatisTable,
       "hh3cDot11QosStatisEntry": hh3cDot11QosStatisEntry,
       "hh3cDot11QosAPID": hh3cDot11QosAPID,
       "hh3cDot11QosRadioID": hh3cDot11QosRadioID,
       "hh3cDot11QosAverageQueLen": hh3cDot11QosAverageQueLen,
       "hh3cDot11QosDropFrameRatio": hh3cDot11QosDropFrameRatio,
       "hh3cDot11QosAverageDataRate": hh3cDot11QosAverageDataRate,
       "hh3cDot11QosAcStatisTable": hh3cDot11QosAcStatisTable,
       "hh3cDot11QosAcStatisEntry": hh3cDot11QosAcStatisEntry,
       "hh3cDot11QosAcType": hh3cDot11QosAcType,
       "hh3cDot11AcDropFrameCnt": hh3cDot11AcDropFrameCnt}
)
