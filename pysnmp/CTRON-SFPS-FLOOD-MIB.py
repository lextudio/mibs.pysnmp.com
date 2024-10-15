# SNMP MIB module (CTRON-SFPS-FLOOD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SFPS-FLOOD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:24 2024
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

(sfpsISPFlood,
 sfpsMobileUserReset,
 sfpsMobileUserTable,
 sfpsResolveCounter) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "sfpsISPFlood",
    "sfpsMobileUserReset",
    "sfpsMobileUserTable",
    "sfpsResolveCounter")

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




class SfpsAddress(OctetString):
    """Custom type SfpsAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SfpsServiceCenterFloodTable_Object = MibTable
sfpsServiceCenterFloodTable = _SfpsServiceCenterFloodTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 1)
)
if mibBuilder.loadTexts:
    sfpsServiceCenterFloodTable.setStatus("mandatory")
_SfpsServiceCenterFloodEntry_Object = MibTableRow
sfpsServiceCenterFloodEntry = _SfpsServiceCenterFloodEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 1, 1)
)
sfpsServiceCenterFloodEntry.setIndexNames(
    (0, "CTRON-SFPS-FLOOD-MIB", "sfpsServiceCenterFloodAddress"),
)
if mibBuilder.loadTexts:
    sfpsServiceCenterFloodEntry.setStatus("mandatory")
_SfpsServiceCenterFloodAddress_Type = HexInteger
_SfpsServiceCenterFloodAddress_Object = MibTableColumn
sfpsServiceCenterFloodAddress = _SfpsServiceCenterFloodAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 1, 1, 1),
    _SfpsServiceCenterFloodAddress_Type()
)
sfpsServiceCenterFloodAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterFloodAddress.setStatus("mandatory")
_SfpsServiceCenterFloodMetric_Type = Integer32
_SfpsServiceCenterFloodMetric_Object = MibTableColumn
sfpsServiceCenterFloodMetric = _SfpsServiceCenterFloodMetric_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 1, 1, 2),
    _SfpsServiceCenterFloodMetric_Type()
)
sfpsServiceCenterFloodMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterFloodMetric.setStatus("mandatory")
_SfpsServiceCenterFloodName_Type = DisplayString
_SfpsServiceCenterFloodName_Object = MibTableColumn
sfpsServiceCenterFloodName = _SfpsServiceCenterFloodName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 1, 1, 3),
    _SfpsServiceCenterFloodName_Type()
)
sfpsServiceCenterFloodName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterFloodName.setStatus("mandatory")


class _SfpsServiceCenterFloodOperStatus_Type(Integer32):
    """Custom type sfpsServiceCenterFloodOperStatus based on Integer32"""
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


_SfpsServiceCenterFloodOperStatus_Type.__name__ = "Integer32"
_SfpsServiceCenterFloodOperStatus_Object = MibTableColumn
sfpsServiceCenterFloodOperStatus = _SfpsServiceCenterFloodOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 1, 1, 4),
    _SfpsServiceCenterFloodOperStatus_Type()
)
sfpsServiceCenterFloodOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterFloodOperStatus.setStatus("mandatory")


class _SfpsServiceCenterFloodAdminStatus_Type(Integer32):
    """Custom type sfpsServiceCenterFloodAdminStatus based on Integer32"""
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


_SfpsServiceCenterFloodAdminStatus_Type.__name__ = "Integer32"
_SfpsServiceCenterFloodAdminStatus_Object = MibTableColumn
sfpsServiceCenterFloodAdminStatus = _SfpsServiceCenterFloodAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 1, 1, 5),
    _SfpsServiceCenterFloodAdminStatus_Type()
)
sfpsServiceCenterFloodAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsServiceCenterFloodAdminStatus.setStatus("mandatory")
_SfpsServiceCenterFloodStatusTime_Type = TimeTicks
_SfpsServiceCenterFloodStatusTime_Object = MibTableColumn
sfpsServiceCenterFloodStatusTime = _SfpsServiceCenterFloodStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 1, 1, 6),
    _SfpsServiceCenterFloodStatusTime_Type()
)
sfpsServiceCenterFloodStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterFloodStatusTime.setStatus("mandatory")
_SfpsServiceCenterFloodRequests_Type = Integer32
_SfpsServiceCenterFloodRequests_Object = MibTableColumn
sfpsServiceCenterFloodRequests = _SfpsServiceCenterFloodRequests_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 1, 1, 7),
    _SfpsServiceCenterFloodRequests_Type()
)
sfpsServiceCenterFloodRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterFloodRequests.setStatus("mandatory")
_SfpsServiceCenterFloodResponses_Type = Integer32
_SfpsServiceCenterFloodResponses_Object = MibTableColumn
sfpsServiceCenterFloodResponses = _SfpsServiceCenterFloodResponses_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 1, 1, 8),
    _SfpsServiceCenterFloodResponses_Type()
)
sfpsServiceCenterFloodResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterFloodResponses.setStatus("mandatory")
_SfpsResolveCounterTable_Object = MibTable
sfpsResolveCounterTable = _SfpsResolveCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 8, 1)
)
if mibBuilder.loadTexts:
    sfpsResolveCounterTable.setStatus("mandatory")
_SfpsResolveCounterTableEntry_Object = MibTableRow
sfpsResolveCounterTableEntry = _SfpsResolveCounterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 8, 1, 1)
)
sfpsResolveCounterTableEntry.setIndexNames(
    (0, "CTRON-SFPS-FLOOD-MIB", "sfpsResolveCounterTableSource"),
)
if mibBuilder.loadTexts:
    sfpsResolveCounterTableEntry.setStatus("mandatory")
_SfpsResolveCounterTableSource_Type = SfpsAddress
_SfpsResolveCounterTableSource_Object = MibTableColumn
sfpsResolveCounterTableSource = _SfpsResolveCounterTableSource_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 8, 1, 1, 1),
    _SfpsResolveCounterTableSource_Type()
)
sfpsResolveCounterTableSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveCounterTableSource.setStatus("mandatory")
_SfpsResolveCounterTableNumReq_Type = Integer32
_SfpsResolveCounterTableNumReq_Object = MibTableColumn
sfpsResolveCounterTableNumReq = _SfpsResolveCounterTableNumReq_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 8, 1, 1, 2),
    _SfpsResolveCounterTableNumReq_Type()
)
sfpsResolveCounterTableNumReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveCounterTableNumReq.setStatus("mandatory")
_SfpsResolveCounterTableNumRep_Type = Integer32
_SfpsResolveCounterTableNumRep_Object = MibTableColumn
sfpsResolveCounterTableNumRep = _SfpsResolveCounterTableNumRep_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 8, 1, 1, 3),
    _SfpsResolveCounterTableNumRep_Type()
)
sfpsResolveCounterTableNumRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveCounterTableNumRep.setStatus("mandatory")
_SfpsResolveCounterTableNumUnkRep_Type = Integer32
_SfpsResolveCounterTableNumUnkRep_Object = MibTableColumn
sfpsResolveCounterTableNumUnkRep = _SfpsResolveCounterTableNumUnkRep_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 8, 1, 1, 4),
    _SfpsResolveCounterTableNumUnkRep_Type()
)
sfpsResolveCounterTableNumUnkRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveCounterTableNumUnkRep.setStatus("mandatory")
_SfpsResolveCounterTableTicReq_Type = TimeTicks
_SfpsResolveCounterTableTicReq_Object = MibTableColumn
sfpsResolveCounterTableTicReq = _SfpsResolveCounterTableTicReq_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 8, 1, 1, 5),
    _SfpsResolveCounterTableTicReq_Type()
)
sfpsResolveCounterTableTicReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveCounterTableTicReq.setStatus("mandatory")
_SfpsResolveCounterTableTicRep_Type = TimeTicks
_SfpsResolveCounterTableTicRep_Object = MibTableColumn
sfpsResolveCounterTableTicRep = _SfpsResolveCounterTableTicRep_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 8, 1, 1, 6),
    _SfpsResolveCounterTableTicRep_Type()
)
sfpsResolveCounterTableTicRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveCounterTableTicRep.setStatus("mandatory")
_SfpsResolveCounterTableTicUnkRep_Type = TimeTicks
_SfpsResolveCounterTableTicUnkRep_Object = MibTableColumn
sfpsResolveCounterTableTicUnkRep = _SfpsResolveCounterTableTicUnkRep_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 8, 1, 1, 7),
    _SfpsResolveCounterTableTicUnkRep_Type()
)
sfpsResolveCounterTableTicUnkRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveCounterTableTicUnkRep.setStatus("mandatory")
_SfpsMobileUserTableAOType_Type = DisplayString
_SfpsMobileUserTableAOType_Object = MibScalar
sfpsMobileUserTableAOType = _SfpsMobileUserTableAOType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 9, 1, 1),
    _SfpsMobileUserTableAOType_Type()
)
sfpsMobileUserTableAOType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobileUserTableAOType.setStatus("mandatory")
_SfpsMobileUserTableAOValue_Type = DisplayString
_SfpsMobileUserTableAOValue_Object = MibScalar
sfpsMobileUserTableAOValue = _SfpsMobileUserTableAOValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 9, 1, 2),
    _SfpsMobileUserTableAOValue_Type()
)
sfpsMobileUserTableAOValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobileUserTableAOValue.setStatus("mandatory")
_SfpsMobileUserTableCount_Type = Integer32
_SfpsMobileUserTableCount_Object = MibScalar
sfpsMobileUserTableCount = _SfpsMobileUserTableCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 9, 1, 3),
    _SfpsMobileUserTableCount_Type()
)
sfpsMobileUserTableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobileUserTableCount.setStatus("mandatory")
_SfpsMobileUserTableNewSwitch_Type = SfpsAddress
_SfpsMobileUserTableNewSwitch_Object = MibScalar
sfpsMobileUserTableNewSwitch = _SfpsMobileUserTableNewSwitch_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 9, 1, 4),
    _SfpsMobileUserTableNewSwitch_Type()
)
sfpsMobileUserTableNewSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobileUserTableNewSwitch.setStatus("mandatory")
_SfpsMobileUserTableLastSeen_Type = TimeTicks
_SfpsMobileUserTableLastSeen_Object = MibScalar
sfpsMobileUserTableLastSeen = _SfpsMobileUserTableLastSeen_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 9, 1, 5),
    _SfpsMobileUserTableLastSeen_Type()
)
sfpsMobileUserTableLastSeen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMobileUserTableLastSeen.setStatus("mandatory")
_SfpsMobileUserTableFirstSceen_Type = TimeTicks
_SfpsMobileUserTableFirstSceen_Object = MibScalar
sfpsMobileUserTableFirstSceen = _SfpsMobileUserTableFirstSceen_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 9, 1, 6),
    _SfpsMobileUserTableFirstSceen_Type()
)
sfpsMobileUserTableFirstSceen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMobileUserTableFirstSceen.setStatus("mandatory")
_SfpsMobileUserTablePort_Type = Integer32
_SfpsMobileUserTablePort_Object = MibScalar
sfpsMobileUserTablePort = _SfpsMobileUserTablePort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 9, 1, 7),
    _SfpsMobileUserTablePort_Type()
)
sfpsMobileUserTablePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMobileUserTablePort.setStatus("mandatory")
_SfpsMobileUserResetReset_Type = Integer32
_SfpsMobileUserResetReset_Object = MibScalar
sfpsMobileUserResetReset = _SfpsMobileUserResetReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 9, 2, 1),
    _SfpsMobileUserResetReset_Type()
)
sfpsMobileUserResetReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMobileUserResetReset.setStatus("mandatory")
_SfpsMobileUserResetCount_Type = Integer32
_SfpsMobileUserResetCount_Object = MibScalar
sfpsMobileUserResetCount = _SfpsMobileUserResetCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 9, 2, 2),
    _SfpsMobileUserResetCount_Type()
)
sfpsMobileUserResetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobileUserResetCount.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-FLOOD-MIB",
    **{"HexInteger": HexInteger,
       "SfpsAddress": SfpsAddress,
       "sfpsServiceCenterFloodTable": sfpsServiceCenterFloodTable,
       "sfpsServiceCenterFloodEntry": sfpsServiceCenterFloodEntry,
       "sfpsServiceCenterFloodAddress": sfpsServiceCenterFloodAddress,
       "sfpsServiceCenterFloodMetric": sfpsServiceCenterFloodMetric,
       "sfpsServiceCenterFloodName": sfpsServiceCenterFloodName,
       "sfpsServiceCenterFloodOperStatus": sfpsServiceCenterFloodOperStatus,
       "sfpsServiceCenterFloodAdminStatus": sfpsServiceCenterFloodAdminStatus,
       "sfpsServiceCenterFloodStatusTime": sfpsServiceCenterFloodStatusTime,
       "sfpsServiceCenterFloodRequests": sfpsServiceCenterFloodRequests,
       "sfpsServiceCenterFloodResponses": sfpsServiceCenterFloodResponses,
       "sfpsResolveCounterTable": sfpsResolveCounterTable,
       "sfpsResolveCounterTableEntry": sfpsResolveCounterTableEntry,
       "sfpsResolveCounterTableSource": sfpsResolveCounterTableSource,
       "sfpsResolveCounterTableNumReq": sfpsResolveCounterTableNumReq,
       "sfpsResolveCounterTableNumRep": sfpsResolveCounterTableNumRep,
       "sfpsResolveCounterTableNumUnkRep": sfpsResolveCounterTableNumUnkRep,
       "sfpsResolveCounterTableTicReq": sfpsResolveCounterTableTicReq,
       "sfpsResolveCounterTableTicRep": sfpsResolveCounterTableTicRep,
       "sfpsResolveCounterTableTicUnkRep": sfpsResolveCounterTableTicUnkRep,
       "sfpsMobileUserTableAOType": sfpsMobileUserTableAOType,
       "sfpsMobileUserTableAOValue": sfpsMobileUserTableAOValue,
       "sfpsMobileUserTableCount": sfpsMobileUserTableCount,
       "sfpsMobileUserTableNewSwitch": sfpsMobileUserTableNewSwitch,
       "sfpsMobileUserTableLastSeen": sfpsMobileUserTableLastSeen,
       "sfpsMobileUserTableFirstSceen": sfpsMobileUserTableFirstSceen,
       "sfpsMobileUserTablePort": sfpsMobileUserTablePort,
       "sfpsMobileUserResetReset": sfpsMobileUserResetReset,
       "sfpsMobileUserResetCount": sfpsMobileUserResetCount}
)
