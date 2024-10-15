# SNMP MIB module (CTRON-SFPS-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SFPS-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:29 2024
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

(sfpsISPPolicy,
 sfpsVMMatrix,
 sfpsVlanMatrix,
 sfpsVlanMatrixApi) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "sfpsISPPolicy",
    "sfpsVMMatrix",
    "sfpsVlanMatrix",
    "sfpsVlanMatrixApi")

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

_SfpsServiceCenterPolicyTable_Object = MibTable
sfpsServiceCenterPolicyTable = _SfpsServiceCenterPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    sfpsServiceCenterPolicyTable.setStatus("mandatory")
_SfpsServiceCenterPolicyEntry_Object = MibTableRow
sfpsServiceCenterPolicyEntry = _SfpsServiceCenterPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 1, 1)
)
sfpsServiceCenterPolicyEntry.setIndexNames(
    (0, "CTRON-SFPS-POLICY-MIB", "sfpsServiceCenterPolicyHashLeaf"),
)
if mibBuilder.loadTexts:
    sfpsServiceCenterPolicyEntry.setStatus("mandatory")
_SfpsServiceCenterPolicyHashLeaf_Type = HexInteger
_SfpsServiceCenterPolicyHashLeaf_Object = MibTableColumn
sfpsServiceCenterPolicyHashLeaf = _SfpsServiceCenterPolicyHashLeaf_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 1, 1, 1),
    _SfpsServiceCenterPolicyHashLeaf_Type()
)
sfpsServiceCenterPolicyHashLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterPolicyHashLeaf.setStatus("mandatory")
_SfpsServiceCenterPolicyMetric_Type = Integer32
_SfpsServiceCenterPolicyMetric_Object = MibTableColumn
sfpsServiceCenterPolicyMetric = _SfpsServiceCenterPolicyMetric_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 1, 1, 2),
    _SfpsServiceCenterPolicyMetric_Type()
)
sfpsServiceCenterPolicyMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterPolicyMetric.setStatus("mandatory")
_SfpsServiceCenterPolicyName_Type = DisplayString
_SfpsServiceCenterPolicyName_Object = MibTableColumn
sfpsServiceCenterPolicyName = _SfpsServiceCenterPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 1, 1, 3),
    _SfpsServiceCenterPolicyName_Type()
)
sfpsServiceCenterPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterPolicyName.setStatus("mandatory")


class _SfpsServiceCenterPolicyOperStatus_Type(Integer32):
    """Custom type sfpsServiceCenterPolicyOperStatus based on Integer32"""
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


_SfpsServiceCenterPolicyOperStatus_Type.__name__ = "Integer32"
_SfpsServiceCenterPolicyOperStatus_Object = MibTableColumn
sfpsServiceCenterPolicyOperStatus = _SfpsServiceCenterPolicyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 1, 1, 4),
    _SfpsServiceCenterPolicyOperStatus_Type()
)
sfpsServiceCenterPolicyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterPolicyOperStatus.setStatus("mandatory")


class _SfpsServiceCenterPolicyAdminStatus_Type(Integer32):
    """Custom type sfpsServiceCenterPolicyAdminStatus based on Integer32"""
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


_SfpsServiceCenterPolicyAdminStatus_Type.__name__ = "Integer32"
_SfpsServiceCenterPolicyAdminStatus_Object = MibTableColumn
sfpsServiceCenterPolicyAdminStatus = _SfpsServiceCenterPolicyAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 1, 1, 5),
    _SfpsServiceCenterPolicyAdminStatus_Type()
)
sfpsServiceCenterPolicyAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsServiceCenterPolicyAdminStatus.setStatus("mandatory")
_SfpsServiceCenterPolicyStatusTime_Type = TimeTicks
_SfpsServiceCenterPolicyStatusTime_Object = MibTableColumn
sfpsServiceCenterPolicyStatusTime = _SfpsServiceCenterPolicyStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 1, 1, 6),
    _SfpsServiceCenterPolicyStatusTime_Type()
)
sfpsServiceCenterPolicyStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterPolicyStatusTime.setStatus("mandatory")
_SfpsServiceCenterPolicyRequests_Type = Integer32
_SfpsServiceCenterPolicyRequests_Object = MibTableColumn
sfpsServiceCenterPolicyRequests = _SfpsServiceCenterPolicyRequests_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 1, 1, 7),
    _SfpsServiceCenterPolicyRequests_Type()
)
sfpsServiceCenterPolicyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterPolicyRequests.setStatus("mandatory")
_SfpsServiceCenterPolicyResponses_Type = Integer32
_SfpsServiceCenterPolicyResponses_Object = MibTableColumn
sfpsServiceCenterPolicyResponses = _SfpsServiceCenterPolicyResponses_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 1, 1, 8),
    _SfpsServiceCenterPolicyResponses_Type()
)
sfpsServiceCenterPolicyResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterPolicyResponses.setStatus("mandatory")
_SfpsMatrixTable_Object = MibTable
sfpsMatrixTable = _SfpsMatrixTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sfpsMatrixTable.setStatus("mandatory")
_SfpsMatrixEntry_Object = MibTableRow
sfpsMatrixEntry = _SfpsMatrixEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 1, 1)
)
sfpsMatrixEntry.setIndexNames(
    (0, "CTRON-SFPS-POLICY-MIB", "sfpsMatrixRowId"),
    (0, "CTRON-SFPS-POLICY-MIB", "sfpsMatrixColId"),
)
if mibBuilder.loadTexts:
    sfpsMatrixEntry.setStatus("mandatory")
_SfpsMatrixRowId_Type = Integer32
_SfpsMatrixRowId_Object = MibTableColumn
sfpsMatrixRowId = _SfpsMatrixRowId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 1, 1, 1),
    _SfpsMatrixRowId_Type()
)
sfpsMatrixRowId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMatrixRowId.setStatus("mandatory")
_SfpsMatrixColId_Type = Integer32
_SfpsMatrixColId_Object = MibTableColumn
sfpsMatrixColId = _SfpsMatrixColId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 1, 1, 2),
    _SfpsMatrixColId_Type()
)
sfpsMatrixColId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMatrixColId.setStatus("mandatory")
_SfpsMatrixUser1Type_Type = OctetString
_SfpsMatrixUser1Type_Object = MibTableColumn
sfpsMatrixUser1Type = _SfpsMatrixUser1Type_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 1, 1, 3),
    _SfpsMatrixUser1Type_Type()
)
sfpsMatrixUser1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMatrixUser1Type.setStatus("mandatory")
_SfpsMatrixUser1Load_Type = OctetString
_SfpsMatrixUser1Load_Object = MibTableColumn
sfpsMatrixUser1Load = _SfpsMatrixUser1Load_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 1, 1, 4),
    _SfpsMatrixUser1Load_Type()
)
sfpsMatrixUser1Load.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMatrixUser1Load.setStatus("mandatory")
_SfpsMatrixUser2Type_Type = OctetString
_SfpsMatrixUser2Type_Object = MibTableColumn
sfpsMatrixUser2Type = _SfpsMatrixUser2Type_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 1, 1, 5),
    _SfpsMatrixUser2Type_Type()
)
sfpsMatrixUser2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMatrixUser2Type.setStatus("mandatory")
_SfpsMatrixUser2Load_Type = OctetString
_SfpsMatrixUser2Load_Object = MibTableColumn
sfpsMatrixUser2Load = _SfpsMatrixUser2Load_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 1, 1, 6),
    _SfpsMatrixUser2Load_Type()
)
sfpsMatrixUser2Load.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMatrixUser2Load.setStatus("mandatory")
_SfpsMatrixConnect_Type = Integer32
_SfpsMatrixConnect_Object = MibTableColumn
sfpsMatrixConnect = _SfpsMatrixConnect_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 1, 1, 7),
    _SfpsMatrixConnect_Type()
)
sfpsMatrixConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMatrixConnect.setStatus("mandatory")
_SfpsMatrixFlood_Type = Integer32
_SfpsMatrixFlood_Object = MibTableColumn
sfpsMatrixFlood = _SfpsMatrixFlood_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 1, 1, 8),
    _SfpsMatrixFlood_Type()
)
sfpsMatrixFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMatrixFlood.setStatus("mandatory")
_SfpsMatrixInfoTable_Object = MibTable
sfpsMatrixInfoTable = _SfpsMatrixInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 2)
)
if mibBuilder.loadTexts:
    sfpsMatrixInfoTable.setStatus("mandatory")
_SfpsMatrixInfoEntry_Object = MibTableRow
sfpsMatrixInfoEntry = _SfpsMatrixInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 2, 1)
)
sfpsMatrixInfoEntry.setIndexNames(
    (0, "CTRON-SFPS-POLICY-MIB", "sfpsMatrixInfoAddrType"),
    (0, "CTRON-SFPS-POLICY-MIB", "sfpsMatrixInfoAddrHash"),
    (0, "CTRON-SFPS-POLICY-MIB", "sfpsMatrixInfoHashIndex"),
)
if mibBuilder.loadTexts:
    sfpsMatrixInfoEntry.setStatus("mandatory")
_SfpsMatrixInfoAddrType_Type = Integer32
_SfpsMatrixInfoAddrType_Object = MibTableColumn
sfpsMatrixInfoAddrType = _SfpsMatrixInfoAddrType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 2, 1, 1),
    _SfpsMatrixInfoAddrType_Type()
)
sfpsMatrixInfoAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMatrixInfoAddrType.setStatus("mandatory")
_SfpsMatrixInfoAddrHash_Type = Integer32
_SfpsMatrixInfoAddrHash_Object = MibTableColumn
sfpsMatrixInfoAddrHash = _SfpsMatrixInfoAddrHash_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 2, 1, 2),
    _SfpsMatrixInfoAddrHash_Type()
)
sfpsMatrixInfoAddrHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMatrixInfoAddrHash.setStatus("mandatory")
_SfpsMatrixInfoHashIndex_Type = Integer32
_SfpsMatrixInfoHashIndex_Object = MibTableColumn
sfpsMatrixInfoHashIndex = _SfpsMatrixInfoHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 2, 1, 3),
    _SfpsMatrixInfoHashIndex_Type()
)
sfpsMatrixInfoHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMatrixInfoHashIndex.setStatus("mandatory")
_SfpsMatrixInfoAddrValue_Type = OctetString
_SfpsMatrixInfoAddrValue_Object = MibTableColumn
sfpsMatrixInfoAddrValue = _SfpsMatrixInfoAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 2, 1, 4),
    _SfpsMatrixInfoAddrValue_Type()
)
sfpsMatrixInfoAddrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMatrixInfoAddrValue.setStatus("mandatory")
_SfpsMatrixInfoTableIndex_Type = Integer32
_SfpsMatrixInfoTableIndex_Object = MibTableColumn
sfpsMatrixInfoTableIndex = _SfpsMatrixInfoTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 2, 1, 5),
    _SfpsMatrixInfoTableIndex_Type()
)
sfpsMatrixInfoTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMatrixInfoTableIndex.setStatus("mandatory")
_SfpsMatrixInfoDefConnect_Type = Integer32
_SfpsMatrixInfoDefConnect_Object = MibTableColumn
sfpsMatrixInfoDefConnect = _SfpsMatrixInfoDefConnect_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 2, 1, 6),
    _SfpsMatrixInfoDefConnect_Type()
)
sfpsMatrixInfoDefConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMatrixInfoDefConnect.setStatus("mandatory")
_SfpsMatrixInfoDefFlood_Type = Integer32
_SfpsMatrixInfoDefFlood_Object = MibTableColumn
sfpsMatrixInfoDefFlood = _SfpsMatrixInfoDefFlood_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2, 2, 1, 7),
    _SfpsMatrixInfoDefFlood_Type()
)
sfpsMatrixInfoDefFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMatrixInfoDefFlood.setStatus("mandatory")


class _SfpsMatrixInfoVerb_Type(Integer32):
    """Custom type sfpsMatrixInfoVerb based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("addEntry", 2),
          ("clearFilter1", 12),
          ("clearFitler2", 13),
          ("clearFlagGlobal", 7),
          ("clearFlagValue", 5),
          ("clearTable", 14),
          ("deleteEntry", 3),
          ("other", 1),
          ("resetToDefaults", 9),
          ("setDefaults", 8),
          ("setFilter1", 10),
          ("setFilter2", 11),
          ("setFlagGlobal", 6),
          ("setFlagValue", 4))
    )


_SfpsMatrixInfoVerb_Type.__name__ = "Integer32"
_SfpsMatrixInfoVerb_Object = MibScalar
sfpsMatrixInfoVerb = _SfpsMatrixInfoVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 3, 1),
    _SfpsMatrixInfoVerb_Type()
)
sfpsMatrixInfoVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMatrixInfoVerb.setStatus("mandatory")
_SfpsMatrixInfoIndex1Tag_Type = OctetString
_SfpsMatrixInfoIndex1Tag_Object = MibScalar
sfpsMatrixInfoIndex1Tag = _SfpsMatrixInfoIndex1Tag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 3, 2),
    _SfpsMatrixInfoIndex1Tag_Type()
)
sfpsMatrixInfoIndex1Tag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMatrixInfoIndex1Tag.setStatus("mandatory")
_SfpsMatrixInfoIndex1Load_Type = OctetString
_SfpsMatrixInfoIndex1Load_Object = MibScalar
sfpsMatrixInfoIndex1Load = _SfpsMatrixInfoIndex1Load_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 3, 3),
    _SfpsMatrixInfoIndex1Load_Type()
)
sfpsMatrixInfoIndex1Load.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMatrixInfoIndex1Load.setStatus("mandatory")
_SfpsMatrixInfoIndex2Tag_Type = Integer32
_SfpsMatrixInfoIndex2Tag_Object = MibScalar
sfpsMatrixInfoIndex2Tag = _SfpsMatrixInfoIndex2Tag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 3, 4),
    _SfpsMatrixInfoIndex2Tag_Type()
)
sfpsMatrixInfoIndex2Tag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMatrixInfoIndex2Tag.setStatus("mandatory")
_SfpsMatrixInfoIndex2Load_Type = OctetString
_SfpsMatrixInfoIndex2Load_Object = MibScalar
sfpsMatrixInfoIndex2Load = _SfpsMatrixInfoIndex2Load_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 3, 5),
    _SfpsMatrixInfoIndex2Load_Type()
)
sfpsMatrixInfoIndex2Load.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMatrixInfoIndex2Load.setStatus("mandatory")


class _SfpsMatrixInfoMatrixFlag_Type(Integer32):
    """Custom type sfpsMatrixInfoMatrixFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connect", 1),
          ("flood", 2))
    )


_SfpsMatrixInfoMatrixFlag_Type.__name__ = "Integer32"
_SfpsMatrixInfoMatrixFlag_Object = MibScalar
sfpsMatrixInfoMatrixFlag = _SfpsMatrixInfoMatrixFlag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 3, 6),
    _SfpsMatrixInfoMatrixFlag_Type()
)
sfpsMatrixInfoMatrixFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMatrixInfoMatrixFlag.setStatus("mandatory")
_SfpsMatrixInfoFlagMask_Type = HexInteger
_SfpsMatrixInfoFlagMask_Object = MibScalar
sfpsMatrixInfoFlagMask = _SfpsMatrixInfoFlagMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 3, 7),
    _SfpsMatrixInfoFlagMask_Type()
)
sfpsMatrixInfoFlagMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMatrixInfoFlagMask.setStatus("mandatory")
_SfpsMatrixInfoFilter1Tag_Type = OctetString
_SfpsMatrixInfoFilter1Tag_Object = MibScalar
sfpsMatrixInfoFilter1Tag = _SfpsMatrixInfoFilter1Tag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 3, 8),
    _SfpsMatrixInfoFilter1Tag_Type()
)
sfpsMatrixInfoFilter1Tag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMatrixInfoFilter1Tag.setStatus("mandatory")
_SfpsMatrixInfoFilter1Load_Type = OctetString
_SfpsMatrixInfoFilter1Load_Object = MibScalar
sfpsMatrixInfoFilter1Load = _SfpsMatrixInfoFilter1Load_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 3, 9),
    _SfpsMatrixInfoFilter1Load_Type()
)
sfpsMatrixInfoFilter1Load.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMatrixInfoFilter1Load.setStatus("mandatory")
_SfpsMatrixInfoFilter2Tag_Type = OctetString
_SfpsMatrixInfoFilter2Tag_Object = MibScalar
sfpsMatrixInfoFilter2Tag = _SfpsMatrixInfoFilter2Tag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 3, 10),
    _SfpsMatrixInfoFilter2Tag_Type()
)
sfpsMatrixInfoFilter2Tag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMatrixInfoFilter2Tag.setStatus("mandatory")
_SfpsMatrixInfoFilter2Load_Type = OctetString
_SfpsMatrixInfoFilter2Load_Object = MibScalar
sfpsMatrixInfoFilter2Load = _SfpsMatrixInfoFilter2Load_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 3, 11),
    _SfpsMatrixInfoFilter2Load_Type()
)
sfpsMatrixInfoFilter2Load.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMatrixInfoFilter2Load.setStatus("mandatory")
_SfpsVMMatrixRowIndex_Type = Integer32
_SfpsVMMatrixRowIndex_Object = MibScalar
sfpsVMMatrixRowIndex = _SfpsVMMatrixRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 4, 1),
    _SfpsVMMatrixRowIndex_Type()
)
sfpsVMMatrixRowIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVMMatrixRowIndex.setStatus("mandatory")
_SfpsVMMatrixCellIndexMask_Type = OctetString
_SfpsVMMatrixCellIndexMask_Object = MibScalar
sfpsVMMatrixCellIndexMask = _SfpsVMMatrixCellIndexMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 4, 2),
    _SfpsVMMatrixCellIndexMask_Type()
)
sfpsVMMatrixCellIndexMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVMMatrixCellIndexMask.setStatus("mandatory")
_SfpsVMMatrixAction_Type = Integer32
_SfpsVMMatrixAction_Object = MibScalar
sfpsVMMatrixAction = _SfpsVMMatrixAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 4, 3),
    _SfpsVMMatrixAction_Type()
)
sfpsVMMatrixAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVMMatrixAction.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-POLICY-MIB",
    **{"HexInteger": HexInteger,
       "sfpsServiceCenterPolicyTable": sfpsServiceCenterPolicyTable,
       "sfpsServiceCenterPolicyEntry": sfpsServiceCenterPolicyEntry,
       "sfpsServiceCenterPolicyHashLeaf": sfpsServiceCenterPolicyHashLeaf,
       "sfpsServiceCenterPolicyMetric": sfpsServiceCenterPolicyMetric,
       "sfpsServiceCenterPolicyName": sfpsServiceCenterPolicyName,
       "sfpsServiceCenterPolicyOperStatus": sfpsServiceCenterPolicyOperStatus,
       "sfpsServiceCenterPolicyAdminStatus": sfpsServiceCenterPolicyAdminStatus,
       "sfpsServiceCenterPolicyStatusTime": sfpsServiceCenterPolicyStatusTime,
       "sfpsServiceCenterPolicyRequests": sfpsServiceCenterPolicyRequests,
       "sfpsServiceCenterPolicyResponses": sfpsServiceCenterPolicyResponses,
       "sfpsMatrixTable": sfpsMatrixTable,
       "sfpsMatrixEntry": sfpsMatrixEntry,
       "sfpsMatrixRowId": sfpsMatrixRowId,
       "sfpsMatrixColId": sfpsMatrixColId,
       "sfpsMatrixUser1Type": sfpsMatrixUser1Type,
       "sfpsMatrixUser1Load": sfpsMatrixUser1Load,
       "sfpsMatrixUser2Type": sfpsMatrixUser2Type,
       "sfpsMatrixUser2Load": sfpsMatrixUser2Load,
       "sfpsMatrixConnect": sfpsMatrixConnect,
       "sfpsMatrixFlood": sfpsMatrixFlood,
       "sfpsMatrixInfoTable": sfpsMatrixInfoTable,
       "sfpsMatrixInfoEntry": sfpsMatrixInfoEntry,
       "sfpsMatrixInfoAddrType": sfpsMatrixInfoAddrType,
       "sfpsMatrixInfoAddrHash": sfpsMatrixInfoAddrHash,
       "sfpsMatrixInfoHashIndex": sfpsMatrixInfoHashIndex,
       "sfpsMatrixInfoAddrValue": sfpsMatrixInfoAddrValue,
       "sfpsMatrixInfoTableIndex": sfpsMatrixInfoTableIndex,
       "sfpsMatrixInfoDefConnect": sfpsMatrixInfoDefConnect,
       "sfpsMatrixInfoDefFlood": sfpsMatrixInfoDefFlood,
       "sfpsMatrixInfoVerb": sfpsMatrixInfoVerb,
       "sfpsMatrixInfoIndex1Tag": sfpsMatrixInfoIndex1Tag,
       "sfpsMatrixInfoIndex1Load": sfpsMatrixInfoIndex1Load,
       "sfpsMatrixInfoIndex2Tag": sfpsMatrixInfoIndex2Tag,
       "sfpsMatrixInfoIndex2Load": sfpsMatrixInfoIndex2Load,
       "sfpsMatrixInfoMatrixFlag": sfpsMatrixInfoMatrixFlag,
       "sfpsMatrixInfoFlagMask": sfpsMatrixInfoFlagMask,
       "sfpsMatrixInfoFilter1Tag": sfpsMatrixInfoFilter1Tag,
       "sfpsMatrixInfoFilter1Load": sfpsMatrixInfoFilter1Load,
       "sfpsMatrixInfoFilter2Tag": sfpsMatrixInfoFilter2Tag,
       "sfpsMatrixInfoFilter2Load": sfpsMatrixInfoFilter2Load,
       "sfpsVMMatrixRowIndex": sfpsVMMatrixRowIndex,
       "sfpsVMMatrixCellIndexMask": sfpsVMMatrixCellIndexMask,
       "sfpsVMMatrixAction": sfpsVMMatrixAction}
)
