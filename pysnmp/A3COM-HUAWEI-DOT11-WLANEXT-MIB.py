# SNMP MIB module (A3COM-HUAWEI-DOT11-WLANEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-DOT11-WLANEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:44 2024
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

(H3cDot11ObjectIDType,
 H3cDot11QosAcType,
 H3cDot11RadioScopeType,
 h3cDot11) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-DOT11-REF-MIB",
    "H3cDot11ObjectIDType",
    "H3cDot11QosAcType",
    "H3cDot11RadioScopeType",
    "h3cDot11")

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

h3cDot11WLANEXT = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7)
)
h3cDot11WLANEXT.setRevisions(
        ("2007-06-08 20:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cDot11RFGroup_ObjectIdentity = ObjectIdentity
h3cDot11RFGroup = _H3cDot11RFGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 1)
)
_H3cDot11RFSignalStatisTable_Object = MibTable
h3cDot11RFSignalStatisTable = _H3cDot11RFSignalStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 1, 1)
)
if mibBuilder.loadTexts:
    h3cDot11RFSignalStatisTable.setStatus("current")
_H3cDot11RFSignalStatisEntry_Object = MibTableRow
h3cDot11RFSignalStatisEntry = _H3cDot11RFSignalStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 1, 1, 1)
)
h3cDot11RFSignalStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-WLANEXT-MIB", "h3cDot11RFAPID"),
    (0, "A3COM-HUAWEI-DOT11-WLANEXT-MIB", "h3cDot11RFRadioID"),
)
if mibBuilder.loadTexts:
    h3cDot11RFSignalStatisEntry.setStatus("current")
_H3cDot11RFAPID_Type = H3cDot11ObjectIDType
_H3cDot11RFAPID_Object = MibTableColumn
h3cDot11RFAPID = _H3cDot11RFAPID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 1, 1, 1, 1),
    _H3cDot11RFAPID_Type()
)
h3cDot11RFAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11RFAPID.setStatus("current")
_H3cDot11RFRadioID_Type = H3cDot11RadioScopeType
_H3cDot11RFRadioID_Object = MibTableColumn
h3cDot11RFRadioID = _H3cDot11RFRadioID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 1, 1, 1, 2),
    _H3cDot11RFRadioID_Type()
)
h3cDot11RFRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11RFRadioID.setStatus("current")
_H3cDot11RFSignalStatisInterv_Type = Integer32
_H3cDot11RFSignalStatisInterv_Object = MibTableColumn
h3cDot11RFSignalStatisInterv = _H3cDot11RFSignalStatisInterv_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 1, 1, 1, 3),
    _H3cDot11RFSignalStatisInterv_Type()
)
h3cDot11RFSignalStatisInterv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RFSignalStatisInterv.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RFSignalStatisInterv.setUnits("second")
_H3cDot11RFAverageSignalStrength_Type = Integer32
_H3cDot11RFAverageSignalStrength_Object = MibTableColumn
h3cDot11RFAverageSignalStrength = _H3cDot11RFAverageSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 1, 1, 1, 4),
    _H3cDot11RFAverageSignalStrength_Type()
)
h3cDot11RFAverageSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RFAverageSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RFAverageSignalStrength.setUnits("dBm")
_H3cDot11RFMaxSignalStrength_Type = Integer32
_H3cDot11RFMaxSignalStrength_Object = MibTableColumn
h3cDot11RFMaxSignalStrength = _H3cDot11RFMaxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 1, 1, 1, 5),
    _H3cDot11RFMaxSignalStrength_Type()
)
h3cDot11RFMaxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RFMaxSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RFMaxSignalStrength.setUnits("dBm")
_H3cDot11RFMinSignalStrength_Type = Integer32
_H3cDot11RFMinSignalStrength_Object = MibTableColumn
h3cDot11RFMinSignalStrength = _H3cDot11RFMinSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 1, 1, 1, 6),
    _H3cDot11RFMinSignalStrength_Type()
)
h3cDot11RFMinSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RFMinSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RFMinSignalStrength.setUnits("dBm")
_H3cDot11QosGroup_ObjectIdentity = ObjectIdentity
h3cDot11QosGroup = _H3cDot11QosGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 2)
)
_H3cDot11QosStatisTable_Object = MibTable
h3cDot11QosStatisTable = _H3cDot11QosStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 2, 1)
)
if mibBuilder.loadTexts:
    h3cDot11QosStatisTable.setStatus("current")
_H3cDot11QosStatisEntry_Object = MibTableRow
h3cDot11QosStatisEntry = _H3cDot11QosStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 2, 1, 1)
)
h3cDot11QosStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-WLANEXT-MIB", "h3cDot11QosAPID"),
    (0, "A3COM-HUAWEI-DOT11-WLANEXT-MIB", "h3cDot11QosRadioID"),
)
if mibBuilder.loadTexts:
    h3cDot11QosStatisEntry.setStatus("current")
_H3cDot11QosAPID_Type = H3cDot11ObjectIDType
_H3cDot11QosAPID_Object = MibTableColumn
h3cDot11QosAPID = _H3cDot11QosAPID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 2, 1, 1, 1),
    _H3cDot11QosAPID_Type()
)
h3cDot11QosAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11QosAPID.setStatus("current")
_H3cDot11QosRadioID_Type = H3cDot11RadioScopeType
_H3cDot11QosRadioID_Object = MibTableColumn
h3cDot11QosRadioID = _H3cDot11QosRadioID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 2, 1, 1, 2),
    _H3cDot11QosRadioID_Type()
)
h3cDot11QosRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11QosRadioID.setStatus("current")
_H3cDot11QosAverageQueLen_Type = Integer32
_H3cDot11QosAverageQueLen_Object = MibTableColumn
h3cDot11QosAverageQueLen = _H3cDot11QosAverageQueLen_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 2, 1, 1, 3),
    _H3cDot11QosAverageQueLen_Type()
)
h3cDot11QosAverageQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11QosAverageQueLen.setStatus("current")
_H3cDot11QosDropFrameRatio_Type = Integer32
_H3cDot11QosDropFrameRatio_Object = MibTableColumn
h3cDot11QosDropFrameRatio = _H3cDot11QosDropFrameRatio_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 2, 1, 1, 4),
    _H3cDot11QosDropFrameRatio_Type()
)
h3cDot11QosDropFrameRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11QosDropFrameRatio.setStatus("current")
_H3cDot11QosAverageDataRate_Type = Integer32
_H3cDot11QosAverageDataRate_Object = MibTableColumn
h3cDot11QosAverageDataRate = _H3cDot11QosAverageDataRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 2, 1, 1, 5),
    _H3cDot11QosAverageDataRate_Type()
)
h3cDot11QosAverageDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11QosAverageDataRate.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11QosAverageDataRate.setUnits("Kbps")
_H3cDot11QosAcStatisTable_Object = MibTable
h3cDot11QosAcStatisTable = _H3cDot11QosAcStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 2, 2)
)
if mibBuilder.loadTexts:
    h3cDot11QosAcStatisTable.setStatus("current")
_H3cDot11QosAcStatisEntry_Object = MibTableRow
h3cDot11QosAcStatisEntry = _H3cDot11QosAcStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 2, 2, 1)
)
h3cDot11QosAcStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-WLANEXT-MIB", "h3cDot11QosAPID"),
    (0, "A3COM-HUAWEI-DOT11-WLANEXT-MIB", "h3cDot11QosRadioID"),
    (0, "A3COM-HUAWEI-DOT11-WLANEXT-MIB", "h3cDot11QosAcType"),
)
if mibBuilder.loadTexts:
    h3cDot11QosAcStatisEntry.setStatus("current")
_H3cDot11QosAcType_Type = H3cDot11QosAcType
_H3cDot11QosAcType_Object = MibTableColumn
h3cDot11QosAcType = _H3cDot11QosAcType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 2, 2, 1, 1),
    _H3cDot11QosAcType_Type()
)
h3cDot11QosAcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11QosAcType.setStatus("current")
_H3cDot11AcDropFrameCnt_Type = Counter32
_H3cDot11AcDropFrameCnt_Object = MibTableColumn
h3cDot11AcDropFrameCnt = _H3cDot11AcDropFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 2, 2, 1, 2),
    _H3cDot11AcDropFrameCnt_Type()
)
h3cDot11AcDropFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11AcDropFrameCnt.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-DOT11-WLANEXT-MIB",
    **{"h3cDot11WLANEXT": h3cDot11WLANEXT,
       "h3cDot11RFGroup": h3cDot11RFGroup,
       "h3cDot11RFSignalStatisTable": h3cDot11RFSignalStatisTable,
       "h3cDot11RFSignalStatisEntry": h3cDot11RFSignalStatisEntry,
       "h3cDot11RFAPID": h3cDot11RFAPID,
       "h3cDot11RFRadioID": h3cDot11RFRadioID,
       "h3cDot11RFSignalStatisInterv": h3cDot11RFSignalStatisInterv,
       "h3cDot11RFAverageSignalStrength": h3cDot11RFAverageSignalStrength,
       "h3cDot11RFMaxSignalStrength": h3cDot11RFMaxSignalStrength,
       "h3cDot11RFMinSignalStrength": h3cDot11RFMinSignalStrength,
       "h3cDot11QosGroup": h3cDot11QosGroup,
       "h3cDot11QosStatisTable": h3cDot11QosStatisTable,
       "h3cDot11QosStatisEntry": h3cDot11QosStatisEntry,
       "h3cDot11QosAPID": h3cDot11QosAPID,
       "h3cDot11QosRadioID": h3cDot11QosRadioID,
       "h3cDot11QosAverageQueLen": h3cDot11QosAverageQueLen,
       "h3cDot11QosDropFrameRatio": h3cDot11QosDropFrameRatio,
       "h3cDot11QosAverageDataRate": h3cDot11QosAverageDataRate,
       "h3cDot11QosAcStatisTable": h3cDot11QosAcStatisTable,
       "h3cDot11QosAcStatisEntry": h3cDot11QosAcStatisEntry,
       "h3cDot11QosAcType": h3cDot11QosAcType,
       "h3cDot11AcDropFrameCnt": h3cDot11AcDropFrameCnt}
)
