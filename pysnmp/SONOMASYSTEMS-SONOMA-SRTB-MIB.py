# SNMP MIB module (SONOMASYSTEMS-SONOMA-SRTB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONOMASYSTEMS-SONOMA-SRTB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:48 2024
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

(sonomaBridging,) = mibBuilder.importSymbols(
    "SONOMASYSTEMS-SONOMA-MIB",
    "sonomaBridging")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SrtBridging_ObjectIdentity = ObjectIdentity
srtBridging = _SrtBridging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2)
)


class _SrtBridgeNumber_Type(Integer32):
    """Custom type srtBridgeNumber based on Integer32"""
    defaultValue = 65535


_SrtBridgeNumber_Object = MibScalar
srtBridgeNumber = _SrtBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 1),
    _SrtBridgeNumber_Type()
)
srtBridgeNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srtBridgeNumber.setStatus("obsolete")


class _SrtSourceRouteAgingTime_Type(Integer32):
    """Custom type srtSourceRouteAgingTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_SrtSourceRouteAgingTime_Type.__name__ = "Integer32"
_SrtSourceRouteAgingTime_Object = MibScalar
srtSourceRouteAgingTime = _SrtSourceRouteAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 2),
    _SrtSourceRouteAgingTime_Type()
)
srtSourceRouteAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srtSourceRouteAgingTime.setStatus("mandatory")
_SrtPortTable_Object = MibTable
srtPortTable = _SrtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3)
)
if mibBuilder.loadTexts:
    srtPortTable.setStatus("mandatory")
_SrtPortEntry_Object = MibTableRow
srtPortEntry = _SrtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1)
)
srtPortEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-SRTB-MIB", "srtPortIfIndex"),
)
if mibBuilder.loadTexts:
    srtPortEntry.setStatus("mandatory")
_SrtPortIfIndex_Type = Integer32
_SrtPortIfIndex_Object = MibTableColumn
srtPortIfIndex = _SrtPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 1),
    _SrtPortIfIndex_Type()
)
srtPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtPortIfIndex.setStatus("mandatory")
_SrtPortHopCount_Type = Integer32
_SrtPortHopCount_Object = MibTableColumn
srtPortHopCount = _SrtPortHopCount_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 2),
    _SrtPortHopCount_Type()
)
srtPortHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srtPortHopCount.setStatus("mandatory")
_SrtPortLocalSegment_Type = Integer32
_SrtPortLocalSegment_Object = MibTableColumn
srtPortLocalSegment = _SrtPortLocalSegment_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 3),
    _SrtPortLocalSegment_Type()
)
srtPortLocalSegment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srtPortLocalSegment.setStatus("mandatory")


class _SrtPortLargestFrame_Type(Integer32):
    """Custom type srtPortLargestFrame based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("srtMtu11407", 6),
          ("srtMtu1500", 2),
          ("srtMtu17800", 7),
          ("srtMtu2052", 3),
          ("srtMtu4472", 4),
          ("srtMtu516", 1),
          ("srtMtu65535", 8),
          ("srtMtu8144", 5))
    )


_SrtPortLargestFrame_Type.__name__ = "Integer32"
_SrtPortLargestFrame_Object = MibTableColumn
srtPortLargestFrame = _SrtPortLargestFrame_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 4),
    _SrtPortLargestFrame_Type()
)
srtPortLargestFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srtPortLargestFrame.setStatus("mandatory")


class _SrtPortSTESpanMode_Type(Integer32):
    """Custom type srtPortSTESpanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto-span", 1),
          ("disabled", 2),
          ("forced", 3))
    )


_SrtPortSTESpanMode_Type.__name__ = "Integer32"
_SrtPortSTESpanMode_Object = MibTableColumn
srtPortSTESpanMode = _SrtPortSTESpanMode_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 5),
    _SrtPortSTESpanMode_Type()
)
srtPortSTESpanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srtPortSTESpanMode.setStatus("mandatory")
_SrtPortSpecInFrames_Type = Counter32
_SrtPortSpecInFrames_Object = MibTableColumn
srtPortSpecInFrames = _SrtPortSpecInFrames_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 6),
    _SrtPortSpecInFrames_Type()
)
srtPortSpecInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtPortSpecInFrames.setStatus("mandatory")
_SrtPortSpecOutFrames_Type = Counter32
_SrtPortSpecOutFrames_Object = MibTableColumn
srtPortSpecOutFrames = _SrtPortSpecOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 7),
    _SrtPortSpecOutFrames_Type()
)
srtPortSpecOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtPortSpecOutFrames.setStatus("mandatory")
_SrtPortAREInFrames_Type = Counter32
_SrtPortAREInFrames_Object = MibTableColumn
srtPortAREInFrames = _SrtPortAREInFrames_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 8),
    _SrtPortAREInFrames_Type()
)
srtPortAREInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtPortAREInFrames.setStatus("mandatory")
_SrtPortAREOutFrames_Type = Counter32
_SrtPortAREOutFrames_Object = MibTableColumn
srtPortAREOutFrames = _SrtPortAREOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 9),
    _SrtPortAREOutFrames_Type()
)
srtPortAREOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtPortAREOutFrames.setStatus("mandatory")
_SrtPortSteInFrames_Type = Counter32
_SrtPortSteInFrames_Object = MibTableColumn
srtPortSteInFrames = _SrtPortSteInFrames_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 10),
    _SrtPortSteInFrames_Type()
)
srtPortSteInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtPortSteInFrames.setStatus("mandatory")
_SrtPortSteOutFrames_Type = Counter32
_SrtPortSteOutFrames_Object = MibTableColumn
srtPortSteOutFrames = _SrtPortSteOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 11),
    _SrtPortSteOutFrames_Type()
)
srtPortSteOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtPortSteOutFrames.setStatus("mandatory")
_SrtPortSegmentMismatchDiscards_Type = Counter32
_SrtPortSegmentMismatchDiscards_Object = MibTableColumn
srtPortSegmentMismatchDiscards = _SrtPortSegmentMismatchDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 12),
    _SrtPortSegmentMismatchDiscards_Type()
)
srtPortSegmentMismatchDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtPortSegmentMismatchDiscards.setStatus("mandatory")
_SrtPortDuplicateSegmentDiscards_Type = Counter32
_SrtPortDuplicateSegmentDiscards_Object = MibTableColumn
srtPortDuplicateSegmentDiscards = _SrtPortDuplicateSegmentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 13),
    _SrtPortDuplicateSegmentDiscards_Type()
)
srtPortDuplicateSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtPortDuplicateSegmentDiscards.setStatus("mandatory")
_SrtPortHopCountExceededDiscards_Type = Counter32
_SrtPortHopCountExceededDiscards_Object = MibTableColumn
srtPortHopCountExceededDiscards = _SrtPortHopCountExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 14),
    _SrtPortHopCountExceededDiscards_Type()
)
srtPortHopCountExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtPortHopCountExceededDiscards.setStatus("mandatory")
_SrtSourceRouteTable_Object = MibTable
srtSourceRouteTable = _SrtSourceRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 4)
)
if mibBuilder.loadTexts:
    srtSourceRouteTable.setStatus("mandatory")
_SrtSourceRouteEntry_Object = MibTableRow
srtSourceRouteEntry = _SrtSourceRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 4, 1)
)
srtSourceRouteEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-SRTB-MIB", "srtSourceRouteVlanID"),
    (0, "SONOMASYSTEMS-SONOMA-SRTB-MIB", "srtSourceRouteAddress"),
)
if mibBuilder.loadTexts:
    srtSourceRouteEntry.setStatus("mandatory")
_SrtSourceRouteVlanID_Type = Integer32
_SrtSourceRouteVlanID_Object = MibTableColumn
srtSourceRouteVlanID = _SrtSourceRouteVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 4, 1, 1),
    _SrtSourceRouteVlanID_Type()
)
srtSourceRouteVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtSourceRouteVlanID.setStatus("mandatory")


class _SrtSourceRouteAddress_Type(OctetString):
    """Custom type srtSourceRouteAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_SrtSourceRouteAddress_Type.__name__ = "OctetString"
_SrtSourceRouteAddress_Object = MibTableColumn
srtSourceRouteAddress = _SrtSourceRouteAddress_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 4, 1, 2),
    _SrtSourceRouteAddress_Type()
)
srtSourceRouteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtSourceRouteAddress.setStatus("mandatory")


class _SrtSourceRouteRIF_Type(OctetString):
    """Custom type srtSourceRouteRIF based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_SrtSourceRouteRIF_Type.__name__ = "OctetString"
_SrtSourceRouteRIF_Object = MibTableColumn
srtSourceRouteRIF = _SrtSourceRouteRIF_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 4, 1, 3),
    _SrtSourceRouteRIF_Type()
)
srtSourceRouteRIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtSourceRouteRIF.setStatus("mandatory")


class _SrtSourceRouteType_Type(Integer32):
    """Custom type srtSourceRouteType based on Integer32"""
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
        *(("other", 4),
          ("permanent", 1),
          ("respondWithARE", 3),
          ("temporary", 2))
    )


_SrtSourceRouteType_Type.__name__ = "Integer32"
_SrtSourceRouteType_Object = MibTableColumn
srtSourceRouteType = _SrtSourceRouteType_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 4, 1, 4),
    _SrtSourceRouteType_Type()
)
srtSourceRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtSourceRouteType.setStatus("mandatory")


class _SrtSourceRouteDirection_Type(Integer32):
    """Custom type srtSourceRouteDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inOrder", 1),
          ("reverseOrder", 2))
    )


_SrtSourceRouteDirection_Type.__name__ = "Integer32"
_SrtSourceRouteDirection_Object = MibTableColumn
srtSourceRouteDirection = _SrtSourceRouteDirection_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 4, 1, 5),
    _SrtSourceRouteDirection_Type()
)
srtSourceRouteDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtSourceRouteDirection.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONOMASYSTEMS-SONOMA-SRTB-MIB",
    **{"srtBridging": srtBridging,
       "srtBridgeNumber": srtBridgeNumber,
       "srtSourceRouteAgingTime": srtSourceRouteAgingTime,
       "srtPortTable": srtPortTable,
       "srtPortEntry": srtPortEntry,
       "srtPortIfIndex": srtPortIfIndex,
       "srtPortHopCount": srtPortHopCount,
       "srtPortLocalSegment": srtPortLocalSegment,
       "srtPortLargestFrame": srtPortLargestFrame,
       "srtPortSTESpanMode": srtPortSTESpanMode,
       "srtPortSpecInFrames": srtPortSpecInFrames,
       "srtPortSpecOutFrames": srtPortSpecOutFrames,
       "srtPortAREInFrames": srtPortAREInFrames,
       "srtPortAREOutFrames": srtPortAREOutFrames,
       "srtPortSteInFrames": srtPortSteInFrames,
       "srtPortSteOutFrames": srtPortSteOutFrames,
       "srtPortSegmentMismatchDiscards": srtPortSegmentMismatchDiscards,
       "srtPortDuplicateSegmentDiscards": srtPortDuplicateSegmentDiscards,
       "srtPortHopCountExceededDiscards": srtPortHopCountExceededDiscards,
       "srtSourceRouteTable": srtSourceRouteTable,
       "srtSourceRouteEntry": srtSourceRouteEntry,
       "srtSourceRouteVlanID": srtSourceRouteVlanID,
       "srtSourceRouteAddress": srtSourceRouteAddress,
       "srtSourceRouteRIF": srtSourceRouteRIF,
       "srtSourceRouteType": srtSourceRouteType,
       "srtSourceRouteDirection": srtSourceRouteDirection}
)
