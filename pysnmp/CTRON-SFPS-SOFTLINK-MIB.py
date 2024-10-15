# SNMP MIB module (CTRON-SFPS-SOFTLINK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SFPS-SOFTLINK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:33 2024
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

(sfpsBetaFacility,
 sfpsCallTapFacility,
 sfpsCentersFacility,
 sfpsDiagFacility,
 sfpsFabricFacility,
 sfpsFpcFacility,
 sfpsLiteFacility,
 sfpsMcastFacility,
 sfpsRAFacility,
 sfpsUpLinkFacility,
 sfpsVLANFacility,
 sfpsVNSFacility) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "sfpsBetaFacility",
    "sfpsCallTapFacility",
    "sfpsCentersFacility",
    "sfpsDiagFacility",
    "sfpsFabricFacility",
    "sfpsFpcFacility",
    "sfpsLiteFacility",
    "sfpsMcastFacility",
    "sfpsRAFacility",
    "sfpsUpLinkFacility",
    "sfpsVLANFacility",
    "sfpsVNSFacility")

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


# Types definitions



class HexInteger(Integer32):
    """Custom type HexInteger based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SfpsCentersFacilityTable_Object = MibTable
sfpsCentersFacilityTable = _SfpsCentersFacilityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 1, 1)
)
if mibBuilder.loadTexts:
    sfpsCentersFacilityTable.setStatus("mandatory")
_SfpsCentersFacilityEntry_Object = MibTableRow
sfpsCentersFacilityEntry = _SfpsCentersFacilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 1, 1, 1)
)
sfpsCentersFacilityEntry.setIndexNames(
    (0, "CTRON-SFPS-SOFTLINK-MIB", "sfpsCentersFacilityAddress"),
)
if mibBuilder.loadTexts:
    sfpsCentersFacilityEntry.setStatus("mandatory")
_SfpsCentersFacilityAddress_Type = HexInteger
_SfpsCentersFacilityAddress_Object = MibTableColumn
sfpsCentersFacilityAddress = _SfpsCentersFacilityAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 1, 1, 1, 1),
    _SfpsCentersFacilityAddress_Type()
)
sfpsCentersFacilityAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCentersFacilityAddress.setStatus("mandatory")
_SfpsCentersFacilityMetric_Type = Integer32
_SfpsCentersFacilityMetric_Object = MibTableColumn
sfpsCentersFacilityMetric = _SfpsCentersFacilityMetric_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 1, 1, 1, 2),
    _SfpsCentersFacilityMetric_Type()
)
sfpsCentersFacilityMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCentersFacilityMetric.setStatus("mandatory")
_SfpsCentersFacilityElementName_Type = DisplayString
_SfpsCentersFacilityElementName_Object = MibTableColumn
sfpsCentersFacilityElementName = _SfpsCentersFacilityElementName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 1, 1, 1, 3),
    _SfpsCentersFacilityElementName_Type()
)
sfpsCentersFacilityElementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCentersFacilityElementName.setStatus("mandatory")


class _SfpsCentersFacilityOperStatus_Type(Integer32):
    """Custom type sfpsCentersFacilityOperStatus based on Integer32"""
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
        *(("kStatusFaulted", 4),
          ("kStatusHalted", 2),
          ("kStatusNotStarted", 5),
          ("kStatusPending", 3),
          ("kStatusRunning", 1))
    )


_SfpsCentersFacilityOperStatus_Type.__name__ = "Integer32"
_SfpsCentersFacilityOperStatus_Object = MibTableColumn
sfpsCentersFacilityOperStatus = _SfpsCentersFacilityOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 1, 1, 1, 4),
    _SfpsCentersFacilityOperStatus_Type()
)
sfpsCentersFacilityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCentersFacilityOperStatus.setStatus("mandatory")


class _SfpsCentersFacilityAdminStatus_Type(Integer32):
    """Custom type sfpsCentersFacilityAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("kControlDisable", 2),
          ("kControlEnable", 3),
          ("kControlOther", 1))
    )


_SfpsCentersFacilityAdminStatus_Type.__name__ = "Integer32"
_SfpsCentersFacilityAdminStatus_Object = MibTableColumn
sfpsCentersFacilityAdminStatus = _SfpsCentersFacilityAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 1, 1, 1, 5),
    _SfpsCentersFacilityAdminStatus_Type()
)
sfpsCentersFacilityAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsCentersFacilityAdminStatus.setStatus("mandatory")
_SfpsCentersFacilityStatusTime_Type = TimeTicks
_SfpsCentersFacilityStatusTime_Object = MibTableColumn
sfpsCentersFacilityStatusTime = _SfpsCentersFacilityStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 1, 1, 1, 6),
    _SfpsCentersFacilityStatusTime_Type()
)
sfpsCentersFacilityStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCentersFacilityStatusTime.setStatus("mandatory")
_SfpsCentersFacilityRequests_Type = Integer32
_SfpsCentersFacilityRequests_Object = MibTableColumn
sfpsCentersFacilityRequests = _SfpsCentersFacilityRequests_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 1, 1, 1, 7),
    _SfpsCentersFacilityRequests_Type()
)
sfpsCentersFacilityRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCentersFacilityRequests.setStatus("mandatory")
_SfpsCentersFacilityResponses_Type = Integer32
_SfpsCentersFacilityResponses_Object = MibTableColumn
sfpsCentersFacilityResponses = _SfpsCentersFacilityResponses_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 1, 1, 1, 8),
    _SfpsCentersFacilityResponses_Type()
)
sfpsCentersFacilityResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCentersFacilityResponses.setStatus("mandatory")
_SfpsVNSFacilityTable_Object = MibTable
sfpsVNSFacilityTable = _SfpsVNSFacilityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 2, 1)
)
if mibBuilder.loadTexts:
    sfpsVNSFacilityTable.setStatus("mandatory")
_SfpsVNSFacilityEntry_Object = MibTableRow
sfpsVNSFacilityEntry = _SfpsVNSFacilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 2, 1, 1)
)
sfpsVNSFacilityEntry.setIndexNames(
    (0, "CTRON-SFPS-SOFTLINK-MIB", "sfpsVNSFacilityHashIndex"),
)
if mibBuilder.loadTexts:
    sfpsVNSFacilityEntry.setStatus("mandatory")
_SfpsVNSFacilityHashIndex_Type = Integer32
_SfpsVNSFacilityHashIndex_Object = MibTableColumn
sfpsVNSFacilityHashIndex = _SfpsVNSFacilityHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 2, 1, 1, 1),
    _SfpsVNSFacilityHashIndex_Type()
)
sfpsVNSFacilityHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVNSFacilityHashIndex.setStatus("mandatory")
_SfpsVNSFacilityElementName_Type = DisplayString
_SfpsVNSFacilityElementName_Object = MibTableColumn
sfpsVNSFacilityElementName = _SfpsVNSFacilityElementName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 2, 1, 1, 2),
    _SfpsVNSFacilityElementName_Type()
)
sfpsVNSFacilityElementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVNSFacilityElementName.setStatus("mandatory")


class _SfpsVNSFacilityAdminStatus_Type(Integer32):
    """Custom type sfpsVNSFacilityAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("kControlDisable", 2),
          ("kControlEnable", 3),
          ("kControlOther", 1))
    )


_SfpsVNSFacilityAdminStatus_Type.__name__ = "Integer32"
_SfpsVNSFacilityAdminStatus_Object = MibTableColumn
sfpsVNSFacilityAdminStatus = _SfpsVNSFacilityAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 2, 1, 1, 3),
    _SfpsVNSFacilityAdminStatus_Type()
)
sfpsVNSFacilityAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVNSFacilityAdminStatus.setStatus("mandatory")


class _SfpsVNSFacilityOperStatus_Type(Integer32):
    """Custom type sfpsVNSFacilityOperStatus based on Integer32"""
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
        *(("kStatusFaulted", 4),
          ("kStatusHalted", 2),
          ("kStatusNotStarted", 5),
          ("kStatusPending", 3),
          ("kStatusRunning", 1))
    )


_SfpsVNSFacilityOperStatus_Type.__name__ = "Integer32"
_SfpsVNSFacilityOperStatus_Object = MibTableColumn
sfpsVNSFacilityOperStatus = _SfpsVNSFacilityOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 2, 1, 1, 4),
    _SfpsVNSFacilityOperStatus_Type()
)
sfpsVNSFacilityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVNSFacilityOperStatus.setStatus("mandatory")
_SfpsVNSFacilityStatusTime_Type = TimeTicks
_SfpsVNSFacilityStatusTime_Object = MibTableColumn
sfpsVNSFacilityStatusTime = _SfpsVNSFacilityStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 2, 1, 1, 5),
    _SfpsVNSFacilityStatusTime_Type()
)
sfpsVNSFacilityStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVNSFacilityStatusTime.setStatus("mandatory")
_SfpsVLANFacilityTable_Object = MibTable
sfpsVLANFacilityTable = _SfpsVLANFacilityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 3, 1)
)
if mibBuilder.loadTexts:
    sfpsVLANFacilityTable.setStatus("mandatory")
_SfpsVLANFacilityEntry_Object = MibTableRow
sfpsVLANFacilityEntry = _SfpsVLANFacilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 3, 1, 1)
)
sfpsVLANFacilityEntry.setIndexNames(
    (0, "CTRON-SFPS-SOFTLINK-MIB", "sfpsVLANFacilityHashIndex"),
)
if mibBuilder.loadTexts:
    sfpsVLANFacilityEntry.setStatus("mandatory")
_SfpsVLANFacilityHashIndex_Type = Integer32
_SfpsVLANFacilityHashIndex_Object = MibTableColumn
sfpsVLANFacilityHashIndex = _SfpsVLANFacilityHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 3, 1, 1, 1),
    _SfpsVLANFacilityHashIndex_Type()
)
sfpsVLANFacilityHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVLANFacilityHashIndex.setStatus("mandatory")
_SfpsVLANFacilityElementName_Type = DisplayString
_SfpsVLANFacilityElementName_Object = MibTableColumn
sfpsVLANFacilityElementName = _SfpsVLANFacilityElementName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 3, 1, 1, 2),
    _SfpsVLANFacilityElementName_Type()
)
sfpsVLANFacilityElementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVLANFacilityElementName.setStatus("mandatory")


class _SfpsVLANFacilityAdminStatus_Type(Integer32):
    """Custom type sfpsVLANFacilityAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("kControlDisable", 2),
          ("kControlEnable", 3),
          ("kControlOther", 1))
    )


_SfpsVLANFacilityAdminStatus_Type.__name__ = "Integer32"
_SfpsVLANFacilityAdminStatus_Object = MibTableColumn
sfpsVLANFacilityAdminStatus = _SfpsVLANFacilityAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 3, 1, 1, 3),
    _SfpsVLANFacilityAdminStatus_Type()
)
sfpsVLANFacilityAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVLANFacilityAdminStatus.setStatus("mandatory")


class _SfpsVLANFacilityOperStatus_Type(Integer32):
    """Custom type sfpsVLANFacilityOperStatus based on Integer32"""
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
        *(("kStatusFaulted", 4),
          ("kStatusHalted", 2),
          ("kStatusNotStarted", 5),
          ("kStatusPending", 3),
          ("kStatusRunning", 1))
    )


_SfpsVLANFacilityOperStatus_Type.__name__ = "Integer32"
_SfpsVLANFacilityOperStatus_Object = MibTableColumn
sfpsVLANFacilityOperStatus = _SfpsVLANFacilityOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 3, 1, 1, 4),
    _SfpsVLANFacilityOperStatus_Type()
)
sfpsVLANFacilityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVLANFacilityOperStatus.setStatus("mandatory")
_SfpsVLANFacilityStatusTime_Type = TimeTicks
_SfpsVLANFacilityStatusTime_Object = MibTableColumn
sfpsVLANFacilityStatusTime = _SfpsVLANFacilityStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 3, 1, 1, 5),
    _SfpsVLANFacilityStatusTime_Type()
)
sfpsVLANFacilityStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVLANFacilityStatusTime.setStatus("mandatory")
_SfpsDiagFacilityTable_Object = MibTable
sfpsDiagFacilityTable = _SfpsDiagFacilityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 4, 1)
)
if mibBuilder.loadTexts:
    sfpsDiagFacilityTable.setStatus("mandatory")
_SfpsDiagFacilityEntry_Object = MibTableRow
sfpsDiagFacilityEntry = _SfpsDiagFacilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 4, 1, 1)
)
sfpsDiagFacilityEntry.setIndexNames(
    (0, "CTRON-SFPS-SOFTLINK-MIB", "sfpsDiagFacilityHashIndex"),
)
if mibBuilder.loadTexts:
    sfpsDiagFacilityEntry.setStatus("mandatory")
_SfpsDiagFacilityHashIndex_Type = Integer32
_SfpsDiagFacilityHashIndex_Object = MibTableColumn
sfpsDiagFacilityHashIndex = _SfpsDiagFacilityHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 4, 1, 1, 1),
    _SfpsDiagFacilityHashIndex_Type()
)
sfpsDiagFacilityHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDiagFacilityHashIndex.setStatus("mandatory")
_SfpsDiagFacilityElementName_Type = DisplayString
_SfpsDiagFacilityElementName_Object = MibTableColumn
sfpsDiagFacilityElementName = _SfpsDiagFacilityElementName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 4, 1, 1, 2),
    _SfpsDiagFacilityElementName_Type()
)
sfpsDiagFacilityElementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDiagFacilityElementName.setStatus("mandatory")


class _SfpsDiagFacilityAdminStatus_Type(Integer32):
    """Custom type sfpsDiagFacilityAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("kControlDisable", 2),
          ("kControlEnable", 3),
          ("kControlOther", 1))
    )


_SfpsDiagFacilityAdminStatus_Type.__name__ = "Integer32"
_SfpsDiagFacilityAdminStatus_Object = MibTableColumn
sfpsDiagFacilityAdminStatus = _SfpsDiagFacilityAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 4, 1, 1, 3),
    _SfpsDiagFacilityAdminStatus_Type()
)
sfpsDiagFacilityAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDiagFacilityAdminStatus.setStatus("mandatory")


class _SfpsDiagFacilityOperStatus_Type(Integer32):
    """Custom type sfpsDiagFacilityOperStatus based on Integer32"""
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
        *(("kStatusFaulted", 4),
          ("kStatusHalted", 2),
          ("kStatusNotStarted", 5),
          ("kStatusPending", 3),
          ("kStatusRunning", 1))
    )


_SfpsDiagFacilityOperStatus_Type.__name__ = "Integer32"
_SfpsDiagFacilityOperStatus_Object = MibTableColumn
sfpsDiagFacilityOperStatus = _SfpsDiagFacilityOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 4, 1, 1, 4),
    _SfpsDiagFacilityOperStatus_Type()
)
sfpsDiagFacilityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDiagFacilityOperStatus.setStatus("mandatory")
_SfpsDiagFacilityStatusTime_Type = TimeTicks
_SfpsDiagFacilityStatusTime_Object = MibTableColumn
sfpsDiagFacilityStatusTime = _SfpsDiagFacilityStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 4, 1, 1, 5),
    _SfpsDiagFacilityStatusTime_Type()
)
sfpsDiagFacilityStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDiagFacilityStatusTime.setStatus("mandatory")
_SfpsFabricFacilityTable_Object = MibTable
sfpsFabricFacilityTable = _SfpsFabricFacilityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 6, 1)
)
if mibBuilder.loadTexts:
    sfpsFabricFacilityTable.setStatus("mandatory")
_SfpsFabricFacilityEntry_Object = MibTableRow
sfpsFabricFacilityEntry = _SfpsFabricFacilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 6, 1, 1)
)
sfpsFabricFacilityEntry.setIndexNames(
    (0, "CTRON-SFPS-SOFTLINK-MIB", "sfpsFabricFacilityHashIndex"),
)
if mibBuilder.loadTexts:
    sfpsFabricFacilityEntry.setStatus("mandatory")
_SfpsFabricFacilityHashIndex_Type = Integer32
_SfpsFabricFacilityHashIndex_Object = MibTableColumn
sfpsFabricFacilityHashIndex = _SfpsFabricFacilityHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 6, 1, 1, 1),
    _SfpsFabricFacilityHashIndex_Type()
)
sfpsFabricFacilityHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFabricFacilityHashIndex.setStatus("mandatory")
_SfpsFabricFacilityElementName_Type = DisplayString
_SfpsFabricFacilityElementName_Object = MibTableColumn
sfpsFabricFacilityElementName = _SfpsFabricFacilityElementName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 6, 1, 1, 2),
    _SfpsFabricFacilityElementName_Type()
)
sfpsFabricFacilityElementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFabricFacilityElementName.setStatus("mandatory")


class _SfpsFabricFacilityAdminStatus_Type(Integer32):
    """Custom type sfpsFabricFacilityAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("kControlDisable", 2),
          ("kControlEnable", 3),
          ("kControlOther", 1))
    )


_SfpsFabricFacilityAdminStatus_Type.__name__ = "Integer32"
_SfpsFabricFacilityAdminStatus_Object = MibTableColumn
sfpsFabricFacilityAdminStatus = _SfpsFabricFacilityAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 6, 1, 1, 3),
    _SfpsFabricFacilityAdminStatus_Type()
)
sfpsFabricFacilityAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsFabricFacilityAdminStatus.setStatus("mandatory")


class _SfpsFabricFacilityOperStatus_Type(Integer32):
    """Custom type sfpsFabricFacilityOperStatus based on Integer32"""
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
        *(("kStatusFaulted", 4),
          ("kStatusHalted", 2),
          ("kStatusNotStarted", 5),
          ("kStatusPending", 3),
          ("kStatusRunning", 1))
    )


_SfpsFabricFacilityOperStatus_Type.__name__ = "Integer32"
_SfpsFabricFacilityOperStatus_Object = MibTableColumn
sfpsFabricFacilityOperStatus = _SfpsFabricFacilityOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 6, 1, 1, 4),
    _SfpsFabricFacilityOperStatus_Type()
)
sfpsFabricFacilityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFabricFacilityOperStatus.setStatus("mandatory")
_SfpsFabricFacilityStatusTime_Type = TimeTicks
_SfpsFabricFacilityStatusTime_Object = MibTableColumn
sfpsFabricFacilityStatusTime = _SfpsFabricFacilityStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 6, 1, 1, 5),
    _SfpsFabricFacilityStatusTime_Type()
)
sfpsFabricFacilityStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFabricFacilityStatusTime.setStatus("mandatory")
_SfpsLiteFacilityTable_Object = MibTable
sfpsLiteFacilityTable = _SfpsLiteFacilityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 7, 1)
)
if mibBuilder.loadTexts:
    sfpsLiteFacilityTable.setStatus("mandatory")
_SfpsLiteFacilityEntry_Object = MibTableRow
sfpsLiteFacilityEntry = _SfpsLiteFacilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 7, 1, 1)
)
sfpsLiteFacilityEntry.setIndexNames(
    (0, "CTRON-SFPS-SOFTLINK-MIB", "sfpsLiteFacilityHashIndex"),
)
if mibBuilder.loadTexts:
    sfpsLiteFacilityEntry.setStatus("mandatory")
_SfpsLiteFacilityHashIndex_Type = Integer32
_SfpsLiteFacilityHashIndex_Object = MibTableColumn
sfpsLiteFacilityHashIndex = _SfpsLiteFacilityHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 7, 1, 1, 1),
    _SfpsLiteFacilityHashIndex_Type()
)
sfpsLiteFacilityHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsLiteFacilityHashIndex.setStatus("mandatory")
_SfpsLiteFacilityElementName_Type = DisplayString
_SfpsLiteFacilityElementName_Object = MibTableColumn
sfpsLiteFacilityElementName = _SfpsLiteFacilityElementName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 7, 1, 1, 2),
    _SfpsLiteFacilityElementName_Type()
)
sfpsLiteFacilityElementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsLiteFacilityElementName.setStatus("mandatory")


class _SfpsLiteFacilityAdminStatus_Type(Integer32):
    """Custom type sfpsLiteFacilityAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("kControlDisable", 2),
          ("kControlEnable", 3),
          ("kControlOther", 1))
    )


_SfpsLiteFacilityAdminStatus_Type.__name__ = "Integer32"
_SfpsLiteFacilityAdminStatus_Object = MibTableColumn
sfpsLiteFacilityAdminStatus = _SfpsLiteFacilityAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 7, 1, 1, 3),
    _SfpsLiteFacilityAdminStatus_Type()
)
sfpsLiteFacilityAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsLiteFacilityAdminStatus.setStatus("mandatory")


class _SfpsLiteFacilityOperStatus_Type(Integer32):
    """Custom type sfpsLiteFacilityOperStatus based on Integer32"""
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
        *(("kStatusFaulted", 4),
          ("kStatusHalted", 2),
          ("kStatusNotStarted", 5),
          ("kStatusPending", 3),
          ("kStatusRunning", 1))
    )


_SfpsLiteFacilityOperStatus_Type.__name__ = "Integer32"
_SfpsLiteFacilityOperStatus_Object = MibTableColumn
sfpsLiteFacilityOperStatus = _SfpsLiteFacilityOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 7, 1, 1, 4),
    _SfpsLiteFacilityOperStatus_Type()
)
sfpsLiteFacilityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsLiteFacilityOperStatus.setStatus("mandatory")
_SfpsLiteFacilityStatusTime_Type = TimeTicks
_SfpsLiteFacilityStatusTime_Object = MibTableColumn
sfpsLiteFacilityStatusTime = _SfpsLiteFacilityStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 7, 1, 1, 5),
    _SfpsLiteFacilityStatusTime_Type()
)
sfpsLiteFacilityStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsLiteFacilityStatusTime.setStatus("mandatory")
_SfpsFpcFacilityTable_Object = MibTable
sfpsFpcFacilityTable = _SfpsFpcFacilityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 8, 1)
)
if mibBuilder.loadTexts:
    sfpsFpcFacilityTable.setStatus("mandatory")
_SfpsFpcFacilityEntry_Object = MibTableRow
sfpsFpcFacilityEntry = _SfpsFpcFacilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 8, 1, 1)
)
sfpsFpcFacilityEntry.setIndexNames(
    (0, "CTRON-SFPS-SOFTLINK-MIB", "sfpsFpcFacilityHashIndex"),
)
if mibBuilder.loadTexts:
    sfpsFpcFacilityEntry.setStatus("mandatory")
_SfpsFpcFacilityHashIndex_Type = Integer32
_SfpsFpcFacilityHashIndex_Object = MibTableColumn
sfpsFpcFacilityHashIndex = _SfpsFpcFacilityHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 8, 1, 1, 1),
    _SfpsFpcFacilityHashIndex_Type()
)
sfpsFpcFacilityHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFpcFacilityHashIndex.setStatus("mandatory")
_SfpsFpcFacilityElementName_Type = DisplayString
_SfpsFpcFacilityElementName_Object = MibTableColumn
sfpsFpcFacilityElementName = _SfpsFpcFacilityElementName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 8, 1, 1, 2),
    _SfpsFpcFacilityElementName_Type()
)
sfpsFpcFacilityElementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFpcFacilityElementName.setStatus("mandatory")


class _SfpsFpcFacilityAdminStatus_Type(Integer32):
    """Custom type sfpsFpcFacilityAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("kControlDisable", 2),
          ("kControlEnable", 3),
          ("kControlOther", 1))
    )


_SfpsFpcFacilityAdminStatus_Type.__name__ = "Integer32"
_SfpsFpcFacilityAdminStatus_Object = MibTableColumn
sfpsFpcFacilityAdminStatus = _SfpsFpcFacilityAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 8, 1, 1, 3),
    _SfpsFpcFacilityAdminStatus_Type()
)
sfpsFpcFacilityAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsFpcFacilityAdminStatus.setStatus("mandatory")


class _SfpsFpcFacilityOperStatus_Type(Integer32):
    """Custom type sfpsFpcFacilityOperStatus based on Integer32"""
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
        *(("kStatusFaulted", 4),
          ("kStatusHalted", 2),
          ("kStatusNotStarted", 5),
          ("kStatusPending", 3),
          ("kStatusRunning", 1))
    )


_SfpsFpcFacilityOperStatus_Type.__name__ = "Integer32"
_SfpsFpcFacilityOperStatus_Object = MibTableColumn
sfpsFpcFacilityOperStatus = _SfpsFpcFacilityOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 8, 1, 1, 4),
    _SfpsFpcFacilityOperStatus_Type()
)
sfpsFpcFacilityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFpcFacilityOperStatus.setStatus("mandatory")
_SfpsFpcFacilityStatusTime_Type = TimeTicks
_SfpsFpcFacilityStatusTime_Object = MibTableColumn
sfpsFpcFacilityStatusTime = _SfpsFpcFacilityStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 8, 1, 1, 5),
    _SfpsFpcFacilityStatusTime_Type()
)
sfpsFpcFacilityStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFpcFacilityStatusTime.setStatus("mandatory")
_SfpsRAFacilityTable_Object = MibTable
sfpsRAFacilityTable = _SfpsRAFacilityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 14, 1)
)
if mibBuilder.loadTexts:
    sfpsRAFacilityTable.setStatus("mandatory")
_SfpsRAFacilityEntry_Object = MibTableRow
sfpsRAFacilityEntry = _SfpsRAFacilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 14, 1, 1)
)
sfpsRAFacilityEntry.setIndexNames(
    (0, "CTRON-SFPS-SOFTLINK-MIB", "sfpsRAFacilityHashIndex"),
)
if mibBuilder.loadTexts:
    sfpsRAFacilityEntry.setStatus("mandatory")
_SfpsRAFacilityHashIndex_Type = Integer32
_SfpsRAFacilityHashIndex_Object = MibTableColumn
sfpsRAFacilityHashIndex = _SfpsRAFacilityHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 14, 1, 1, 1),
    _SfpsRAFacilityHashIndex_Type()
)
sfpsRAFacilityHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRAFacilityHashIndex.setStatus("mandatory")
_SfpsRAFacilityName_Type = DisplayString
_SfpsRAFacilityName_Object = MibTableColumn
sfpsRAFacilityName = _SfpsRAFacilityName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 14, 1, 1, 2),
    _SfpsRAFacilityName_Type()
)
sfpsRAFacilityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRAFacilityName.setStatus("mandatory")


class _SfpsRAFacilityAdminStatus_Type(Integer32):
    """Custom type sfpsRAFacilityAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SfpsRAFacilityAdminStatus_Type.__name__ = "Integer32"
_SfpsRAFacilityAdminStatus_Object = MibTableColumn
sfpsRAFacilityAdminStatus = _SfpsRAFacilityAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 14, 1, 1, 3),
    _SfpsRAFacilityAdminStatus_Type()
)
sfpsRAFacilityAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsRAFacilityAdminStatus.setStatus("mandatory")


class _SfpsRAFacilityOperStatus_Type(Integer32):
    """Custom type sfpsRAFacilityOperStatus based on Integer32"""
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
        *(("faulted", 4),
          ("halted", 2),
          ("notStarted", 5),
          ("pending", 3),
          ("running", 1))
    )


_SfpsRAFacilityOperStatus_Type.__name__ = "Integer32"
_SfpsRAFacilityOperStatus_Object = MibTableColumn
sfpsRAFacilityOperStatus = _SfpsRAFacilityOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 14, 1, 1, 4),
    _SfpsRAFacilityOperStatus_Type()
)
sfpsRAFacilityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRAFacilityOperStatus.setStatus("mandatory")
_SfpsRAFacilityStatusTime_Type = TimeTicks
_SfpsRAFacilityStatusTime_Object = MibTableColumn
sfpsRAFacilityStatusTime = _SfpsRAFacilityStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 14, 1, 1, 5),
    _SfpsRAFacilityStatusTime_Type()
)
sfpsRAFacilityStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRAFacilityStatusTime.setStatus("mandatory")
_SfpsMcastFacilityTable_Object = MibTable
sfpsMcastFacilityTable = _SfpsMcastFacilityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 15, 1)
)
if mibBuilder.loadTexts:
    sfpsMcastFacilityTable.setStatus("mandatory")
_SfpsMcastFacilityEntry_Object = MibTableRow
sfpsMcastFacilityEntry = _SfpsMcastFacilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 15, 1, 1)
)
sfpsMcastFacilityEntry.setIndexNames(
    (0, "CTRON-SFPS-SOFTLINK-MIB", "sfpsMcastFacilityHashIndex"),
)
if mibBuilder.loadTexts:
    sfpsMcastFacilityEntry.setStatus("mandatory")
_SfpsMcastFacilityHashIndex_Type = Integer32
_SfpsMcastFacilityHashIndex_Object = MibTableColumn
sfpsMcastFacilityHashIndex = _SfpsMcastFacilityHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 15, 1, 1, 1),
    _SfpsMcastFacilityHashIndex_Type()
)
sfpsMcastFacilityHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastFacilityHashIndex.setStatus("mandatory")
_SfpsMcastFacilityElementName_Type = DisplayString
_SfpsMcastFacilityElementName_Object = MibTableColumn
sfpsMcastFacilityElementName = _SfpsMcastFacilityElementName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 15, 1, 1, 2),
    _SfpsMcastFacilityElementName_Type()
)
sfpsMcastFacilityElementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastFacilityElementName.setStatus("mandatory")


class _SfpsMcastFacilityAdminStatus_Type(Integer32):
    """Custom type sfpsMcastFacilityAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("kControlDisable", 2),
          ("kControlEnable", 3),
          ("kControlOther", 1))
    )


_SfpsMcastFacilityAdminStatus_Type.__name__ = "Integer32"
_SfpsMcastFacilityAdminStatus_Object = MibTableColumn
sfpsMcastFacilityAdminStatus = _SfpsMcastFacilityAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 15, 1, 1, 3),
    _SfpsMcastFacilityAdminStatus_Type()
)
sfpsMcastFacilityAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMcastFacilityAdminStatus.setStatus("mandatory")


class _SfpsMcastFacilityOperStatus_Type(Integer32):
    """Custom type sfpsMcastFacilityOperStatus based on Integer32"""
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
        *(("kStatusFaulted", 4),
          ("kStatusHalted", 2),
          ("kStatusNotStarted", 5),
          ("kStatusPending", 3),
          ("kStatusRunning", 1))
    )


_SfpsMcastFacilityOperStatus_Type.__name__ = "Integer32"
_SfpsMcastFacilityOperStatus_Object = MibTableColumn
sfpsMcastFacilityOperStatus = _SfpsMcastFacilityOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 15, 1, 1, 4),
    _SfpsMcastFacilityOperStatus_Type()
)
sfpsMcastFacilityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastFacilityOperStatus.setStatus("mandatory")
_SfpsMcastFacilityStatusTime_Type = TimeTicks
_SfpsMcastFacilityStatusTime_Object = MibTableColumn
sfpsMcastFacilityStatusTime = _SfpsMcastFacilityStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 15, 1, 1, 5),
    _SfpsMcastFacilityStatusTime_Type()
)
sfpsMcastFacilityStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastFacilityStatusTime.setStatus("mandatory")
_SfpsUplinkFacilityTable_Object = MibTable
sfpsUplinkFacilityTable = _SfpsUplinkFacilityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 16, 1)
)
if mibBuilder.loadTexts:
    sfpsUplinkFacilityTable.setStatus("mandatory")
_SfpsUplinkFacilityEntry_Object = MibTableRow
sfpsUplinkFacilityEntry = _SfpsUplinkFacilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 16, 1, 1)
)
sfpsUplinkFacilityEntry.setIndexNames(
    (0, "CTRON-SFPS-SOFTLINK-MIB", "sfpsUplinkFacilityHashIndex"),
)
if mibBuilder.loadTexts:
    sfpsUplinkFacilityEntry.setStatus("mandatory")
_SfpsUplinkFacilityHashIndex_Type = Integer32
_SfpsUplinkFacilityHashIndex_Object = MibTableColumn
sfpsUplinkFacilityHashIndex = _SfpsUplinkFacilityHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 16, 1, 1, 1),
    _SfpsUplinkFacilityHashIndex_Type()
)
sfpsUplinkFacilityHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsUplinkFacilityHashIndex.setStatus("mandatory")
_SfpsUplinkFacilityName_Type = DisplayString
_SfpsUplinkFacilityName_Object = MibTableColumn
sfpsUplinkFacilityName = _SfpsUplinkFacilityName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 16, 1, 1, 2),
    _SfpsUplinkFacilityName_Type()
)
sfpsUplinkFacilityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsUplinkFacilityName.setStatus("mandatory")


class _SfpsUplinkFacilityAdminStatus_Type(Integer32):
    """Custom type sfpsUplinkFacilityAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SfpsUplinkFacilityAdminStatus_Type.__name__ = "Integer32"
_SfpsUplinkFacilityAdminStatus_Object = MibTableColumn
sfpsUplinkFacilityAdminStatus = _SfpsUplinkFacilityAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 16, 1, 1, 3),
    _SfpsUplinkFacilityAdminStatus_Type()
)
sfpsUplinkFacilityAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsUplinkFacilityAdminStatus.setStatus("mandatory")


class _SfpsUplinkFacilityOperStatus_Type(Integer32):
    """Custom type sfpsUplinkFacilityOperStatus based on Integer32"""
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
        *(("faulted", 4),
          ("halted", 2),
          ("notStarted", 5),
          ("pending", 3),
          ("running", 1))
    )


_SfpsUplinkFacilityOperStatus_Type.__name__ = "Integer32"
_SfpsUplinkFacilityOperStatus_Object = MibTableColumn
sfpsUplinkFacilityOperStatus = _SfpsUplinkFacilityOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 16, 1, 1, 4),
    _SfpsUplinkFacilityOperStatus_Type()
)
sfpsUplinkFacilityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsUplinkFacilityOperStatus.setStatus("mandatory")
_SfpsUplinkFacilityStatusTime_Type = TimeTicks
_SfpsUplinkFacilityStatusTime_Object = MibTableColumn
sfpsUplinkFacilityStatusTime = _SfpsUplinkFacilityStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 16, 1, 1, 5),
    _SfpsUplinkFacilityStatusTime_Type()
)
sfpsUplinkFacilityStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsUplinkFacilityStatusTime.setStatus("mandatory")
_SfpsBetaFacilityTable_Object = MibTable
sfpsBetaFacilityTable = _SfpsBetaFacilityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 21, 1)
)
if mibBuilder.loadTexts:
    sfpsBetaFacilityTable.setStatus("mandatory")
_SfpsBetaFacilityEntry_Object = MibTableRow
sfpsBetaFacilityEntry = _SfpsBetaFacilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 21, 1, 1)
)
sfpsBetaFacilityEntry.setIndexNames(
    (0, "CTRON-SFPS-SOFTLINK-MIB", "sfpsBetaFacilityHashIndex"),
)
if mibBuilder.loadTexts:
    sfpsBetaFacilityEntry.setStatus("mandatory")
_SfpsBetaFacilityHashIndex_Type = Integer32
_SfpsBetaFacilityHashIndex_Object = MibTableColumn
sfpsBetaFacilityHashIndex = _SfpsBetaFacilityHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 21, 1, 1, 1),
    _SfpsBetaFacilityHashIndex_Type()
)
sfpsBetaFacilityHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBetaFacilityHashIndex.setStatus("mandatory")
_SfpsBetaFacilityElementName_Type = DisplayString
_SfpsBetaFacilityElementName_Object = MibTableColumn
sfpsBetaFacilityElementName = _SfpsBetaFacilityElementName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 21, 1, 1, 2),
    _SfpsBetaFacilityElementName_Type()
)
sfpsBetaFacilityElementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBetaFacilityElementName.setStatus("mandatory")


class _SfpsBetaFacilityAdminStatus_Type(Integer32):
    """Custom type sfpsBetaFacilityAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("kControlDisable", 2),
          ("kControlEnable", 3),
          ("kControlOther", 1))
    )


_SfpsBetaFacilityAdminStatus_Type.__name__ = "Integer32"
_SfpsBetaFacilityAdminStatus_Object = MibTableColumn
sfpsBetaFacilityAdminStatus = _SfpsBetaFacilityAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 21, 1, 1, 3),
    _SfpsBetaFacilityAdminStatus_Type()
)
sfpsBetaFacilityAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsBetaFacilityAdminStatus.setStatus("mandatory")


class _SfpsBetaFacilityOperStatus_Type(Integer32):
    """Custom type sfpsBetaFacilityOperStatus based on Integer32"""
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
        *(("kStatusFaulted", 4),
          ("kStatusHalted", 2),
          ("kStatusNotStarted", 5),
          ("kStatusPending", 3),
          ("kStatusRunning", 1))
    )


_SfpsBetaFacilityOperStatus_Type.__name__ = "Integer32"
_SfpsBetaFacilityOperStatus_Object = MibTableColumn
sfpsBetaFacilityOperStatus = _SfpsBetaFacilityOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 21, 1, 1, 4),
    _SfpsBetaFacilityOperStatus_Type()
)
sfpsBetaFacilityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBetaFacilityOperStatus.setStatus("mandatory")
_SfpsBetaFacilityStatusTime_Type = TimeTicks
_SfpsBetaFacilityStatusTime_Object = MibTableColumn
sfpsBetaFacilityStatusTime = _SfpsBetaFacilityStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 21, 1, 1, 5),
    _SfpsBetaFacilityStatusTime_Type()
)
sfpsBetaFacilityStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBetaFacilityStatusTime.setStatus("mandatory")
_SfpsCallTapFacilityTable_Object = MibTable
sfpsCallTapFacilityTable = _SfpsCallTapFacilityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 32, 1)
)
if mibBuilder.loadTexts:
    sfpsCallTapFacilityTable.setStatus("mandatory")
_SfpsCallTapFacilityEntry_Object = MibTableRow
sfpsCallTapFacilityEntry = _SfpsCallTapFacilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 32, 1, 1)
)
sfpsCallTapFacilityEntry.setIndexNames(
    (0, "CTRON-SFPS-SOFTLINK-MIB", "sfpsCallTapFacilityHashIndex"),
)
if mibBuilder.loadTexts:
    sfpsCallTapFacilityEntry.setStatus("mandatory")
_SfpsCallTapFacilityHashIndex_Type = Integer32
_SfpsCallTapFacilityHashIndex_Object = MibTableColumn
sfpsCallTapFacilityHashIndex = _SfpsCallTapFacilityHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 32, 1, 1, 1),
    _SfpsCallTapFacilityHashIndex_Type()
)
sfpsCallTapFacilityHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallTapFacilityHashIndex.setStatus("mandatory")
_SfpsCallTapFacilityElementName_Type = DisplayString
_SfpsCallTapFacilityElementName_Object = MibTableColumn
sfpsCallTapFacilityElementName = _SfpsCallTapFacilityElementName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 32, 1, 1, 2),
    _SfpsCallTapFacilityElementName_Type()
)
sfpsCallTapFacilityElementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallTapFacilityElementName.setStatus("mandatory")


class _SfpsCallTapFacilityAdminStatus_Type(Integer32):
    """Custom type sfpsCallTapFacilityAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("kControlDisable", 2),
          ("kControlEnable", 3),
          ("kControlOther", 1))
    )


_SfpsCallTapFacilityAdminStatus_Type.__name__ = "Integer32"
_SfpsCallTapFacilityAdminStatus_Object = MibTableColumn
sfpsCallTapFacilityAdminStatus = _SfpsCallTapFacilityAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 32, 1, 1, 3),
    _SfpsCallTapFacilityAdminStatus_Type()
)
sfpsCallTapFacilityAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsCallTapFacilityAdminStatus.setStatus("mandatory")


class _SfpsCallTapFacilityOperStatus_Type(Integer32):
    """Custom type sfpsCallTapFacilityOperStatus based on Integer32"""
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
        *(("kStatusFaulted", 4),
          ("kStatusHalted", 2),
          ("kStatusNotStarted", 5),
          ("kStatusPending", 3),
          ("kStatusRunning", 1))
    )


_SfpsCallTapFacilityOperStatus_Type.__name__ = "Integer32"
_SfpsCallTapFacilityOperStatus_Object = MibTableColumn
sfpsCallTapFacilityOperStatus = _SfpsCallTapFacilityOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 32, 1, 1, 4),
    _SfpsCallTapFacilityOperStatus_Type()
)
sfpsCallTapFacilityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallTapFacilityOperStatus.setStatus("mandatory")
_SfpsCallTapFacilityStatusTime_Type = TimeTicks
_SfpsCallTapFacilityStatusTime_Object = MibTableColumn
sfpsCallTapFacilityStatusTime = _SfpsCallTapFacilityStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 32, 1, 1, 5),
    _SfpsCallTapFacilityStatusTime_Type()
)
sfpsCallTapFacilityStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallTapFacilityStatusTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-SOFTLINK-MIB",
    **{"HexInteger": HexInteger,
       "sfpsCentersFacilityTable": sfpsCentersFacilityTable,
       "sfpsCentersFacilityEntry": sfpsCentersFacilityEntry,
       "sfpsCentersFacilityAddress": sfpsCentersFacilityAddress,
       "sfpsCentersFacilityMetric": sfpsCentersFacilityMetric,
       "sfpsCentersFacilityElementName": sfpsCentersFacilityElementName,
       "sfpsCentersFacilityOperStatus": sfpsCentersFacilityOperStatus,
       "sfpsCentersFacilityAdminStatus": sfpsCentersFacilityAdminStatus,
       "sfpsCentersFacilityStatusTime": sfpsCentersFacilityStatusTime,
       "sfpsCentersFacilityRequests": sfpsCentersFacilityRequests,
       "sfpsCentersFacilityResponses": sfpsCentersFacilityResponses,
       "sfpsVNSFacilityTable": sfpsVNSFacilityTable,
       "sfpsVNSFacilityEntry": sfpsVNSFacilityEntry,
       "sfpsVNSFacilityHashIndex": sfpsVNSFacilityHashIndex,
       "sfpsVNSFacilityElementName": sfpsVNSFacilityElementName,
       "sfpsVNSFacilityAdminStatus": sfpsVNSFacilityAdminStatus,
       "sfpsVNSFacilityOperStatus": sfpsVNSFacilityOperStatus,
       "sfpsVNSFacilityStatusTime": sfpsVNSFacilityStatusTime,
       "sfpsVLANFacilityTable": sfpsVLANFacilityTable,
       "sfpsVLANFacilityEntry": sfpsVLANFacilityEntry,
       "sfpsVLANFacilityHashIndex": sfpsVLANFacilityHashIndex,
       "sfpsVLANFacilityElementName": sfpsVLANFacilityElementName,
       "sfpsVLANFacilityAdminStatus": sfpsVLANFacilityAdminStatus,
       "sfpsVLANFacilityOperStatus": sfpsVLANFacilityOperStatus,
       "sfpsVLANFacilityStatusTime": sfpsVLANFacilityStatusTime,
       "sfpsDiagFacilityTable": sfpsDiagFacilityTable,
       "sfpsDiagFacilityEntry": sfpsDiagFacilityEntry,
       "sfpsDiagFacilityHashIndex": sfpsDiagFacilityHashIndex,
       "sfpsDiagFacilityElementName": sfpsDiagFacilityElementName,
       "sfpsDiagFacilityAdminStatus": sfpsDiagFacilityAdminStatus,
       "sfpsDiagFacilityOperStatus": sfpsDiagFacilityOperStatus,
       "sfpsDiagFacilityStatusTime": sfpsDiagFacilityStatusTime,
       "sfpsFabricFacilityTable": sfpsFabricFacilityTable,
       "sfpsFabricFacilityEntry": sfpsFabricFacilityEntry,
       "sfpsFabricFacilityHashIndex": sfpsFabricFacilityHashIndex,
       "sfpsFabricFacilityElementName": sfpsFabricFacilityElementName,
       "sfpsFabricFacilityAdminStatus": sfpsFabricFacilityAdminStatus,
       "sfpsFabricFacilityOperStatus": sfpsFabricFacilityOperStatus,
       "sfpsFabricFacilityStatusTime": sfpsFabricFacilityStatusTime,
       "sfpsLiteFacilityTable": sfpsLiteFacilityTable,
       "sfpsLiteFacilityEntry": sfpsLiteFacilityEntry,
       "sfpsLiteFacilityHashIndex": sfpsLiteFacilityHashIndex,
       "sfpsLiteFacilityElementName": sfpsLiteFacilityElementName,
       "sfpsLiteFacilityAdminStatus": sfpsLiteFacilityAdminStatus,
       "sfpsLiteFacilityOperStatus": sfpsLiteFacilityOperStatus,
       "sfpsLiteFacilityStatusTime": sfpsLiteFacilityStatusTime,
       "sfpsFpcFacilityTable": sfpsFpcFacilityTable,
       "sfpsFpcFacilityEntry": sfpsFpcFacilityEntry,
       "sfpsFpcFacilityHashIndex": sfpsFpcFacilityHashIndex,
       "sfpsFpcFacilityElementName": sfpsFpcFacilityElementName,
       "sfpsFpcFacilityAdminStatus": sfpsFpcFacilityAdminStatus,
       "sfpsFpcFacilityOperStatus": sfpsFpcFacilityOperStatus,
       "sfpsFpcFacilityStatusTime": sfpsFpcFacilityStatusTime,
       "sfpsRAFacilityTable": sfpsRAFacilityTable,
       "sfpsRAFacilityEntry": sfpsRAFacilityEntry,
       "sfpsRAFacilityHashIndex": sfpsRAFacilityHashIndex,
       "sfpsRAFacilityName": sfpsRAFacilityName,
       "sfpsRAFacilityAdminStatus": sfpsRAFacilityAdminStatus,
       "sfpsRAFacilityOperStatus": sfpsRAFacilityOperStatus,
       "sfpsRAFacilityStatusTime": sfpsRAFacilityStatusTime,
       "sfpsMcastFacilityTable": sfpsMcastFacilityTable,
       "sfpsMcastFacilityEntry": sfpsMcastFacilityEntry,
       "sfpsMcastFacilityHashIndex": sfpsMcastFacilityHashIndex,
       "sfpsMcastFacilityElementName": sfpsMcastFacilityElementName,
       "sfpsMcastFacilityAdminStatus": sfpsMcastFacilityAdminStatus,
       "sfpsMcastFacilityOperStatus": sfpsMcastFacilityOperStatus,
       "sfpsMcastFacilityStatusTime": sfpsMcastFacilityStatusTime,
       "sfpsUplinkFacilityTable": sfpsUplinkFacilityTable,
       "sfpsUplinkFacilityEntry": sfpsUplinkFacilityEntry,
       "sfpsUplinkFacilityHashIndex": sfpsUplinkFacilityHashIndex,
       "sfpsUplinkFacilityName": sfpsUplinkFacilityName,
       "sfpsUplinkFacilityAdminStatus": sfpsUplinkFacilityAdminStatus,
       "sfpsUplinkFacilityOperStatus": sfpsUplinkFacilityOperStatus,
       "sfpsUplinkFacilityStatusTime": sfpsUplinkFacilityStatusTime,
       "sfpsBetaFacilityTable": sfpsBetaFacilityTable,
       "sfpsBetaFacilityEntry": sfpsBetaFacilityEntry,
       "sfpsBetaFacilityHashIndex": sfpsBetaFacilityHashIndex,
       "sfpsBetaFacilityElementName": sfpsBetaFacilityElementName,
       "sfpsBetaFacilityAdminStatus": sfpsBetaFacilityAdminStatus,
       "sfpsBetaFacilityOperStatus": sfpsBetaFacilityOperStatus,
       "sfpsBetaFacilityStatusTime": sfpsBetaFacilityStatusTime,
       "sfpsCallTapFacilityTable": sfpsCallTapFacilityTable,
       "sfpsCallTapFacilityEntry": sfpsCallTapFacilityEntry,
       "sfpsCallTapFacilityHashIndex": sfpsCallTapFacilityHashIndex,
       "sfpsCallTapFacilityElementName": sfpsCallTapFacilityElementName,
       "sfpsCallTapFacilityAdminStatus": sfpsCallTapFacilityAdminStatus,
       "sfpsCallTapFacilityOperStatus": sfpsCallTapFacilityOperStatus,
       "sfpsCallTapFacilityStatusTime": sfpsCallTapFacilityStatusTime}
)
