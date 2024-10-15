# SNMP MIB module (CTRON-SFPS-CALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SFPS-CALL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:17 2024
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

(sfpsCallByTuple,
 sfpsCallTableStats,
 sfpsSap,
 sfpsSapAPI) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "sfpsCallByTuple",
    "sfpsCallTableStats",
    "sfpsSap",
    "sfpsSapAPI")

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

_SfpsSapTable_Object = MibTable
sfpsSapTable = _SfpsSapTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sfpsSapTable.setStatus("mandatory")
_SfpsSapTableEntry_Object = MibTableRow
sfpsSapTableEntry = _SfpsSapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1)
)
sfpsSapTableEntry.setIndexNames(
    (0, "CTRON-SFPS-CALL-MIB", "sfpsSapTableTag"),
    (0, "CTRON-SFPS-CALL-MIB", "sfpsSapTableHash"),
    (0, "CTRON-SFPS-CALL-MIB", "sfpsSapTableHashIndex"),
)
if mibBuilder.loadTexts:
    sfpsSapTableEntry.setStatus("mandatory")
_SfpsSapTableTag_Type = Integer32
_SfpsSapTableTag_Object = MibTableColumn
sfpsSapTableTag = _SfpsSapTableTag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 1),
    _SfpsSapTableTag_Type()
)
sfpsSapTableTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSapTableTag.setStatus("mandatory")
_SfpsSapTableHash_Type = Integer32
_SfpsSapTableHash_Object = MibTableColumn
sfpsSapTableHash = _SfpsSapTableHash_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 2),
    _SfpsSapTableHash_Type()
)
sfpsSapTableHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSapTableHash.setStatus("mandatory")
_SfpsSapTableHashIndex_Type = Integer32
_SfpsSapTableHashIndex_Object = MibTableColumn
sfpsSapTableHashIndex = _SfpsSapTableHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 3),
    _SfpsSapTableHashIndex_Type()
)
sfpsSapTableHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSapTableHashIndex.setStatus("mandatory")
_SfpsSapTableSourceCP_Type = DisplayString
_SfpsSapTableSourceCP_Object = MibTableColumn
sfpsSapTableSourceCP = _SfpsSapTableSourceCP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 4),
    _SfpsSapTableSourceCP_Type()
)
sfpsSapTableSourceCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSapTableSourceCP.setStatus("mandatory")
_SfpsSapTableDestCP_Type = DisplayString
_SfpsSapTableDestCP_Object = MibTableColumn
sfpsSapTableDestCP = _SfpsSapTableDestCP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 5),
    _SfpsSapTableDestCP_Type()
)
sfpsSapTableDestCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSapTableDestCP.setStatus("mandatory")
_SfpsSapTableSAP_Type = DisplayString
_SfpsSapTableSAP_Object = MibTableColumn
sfpsSapTableSAP = _SfpsSapTableSAP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 6),
    _SfpsSapTableSAP_Type()
)
sfpsSapTableSAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSapTableSAP.setStatus("mandatory")


class _SfpsSapTableOperStatus_Type(Integer32):
    """Custom type sfpsSapTableOperStatus based on Integer32"""
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


_SfpsSapTableOperStatus_Type.__name__ = "Integer32"
_SfpsSapTableOperStatus_Object = MibTableColumn
sfpsSapTableOperStatus = _SfpsSapTableOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 7),
    _SfpsSapTableOperStatus_Type()
)
sfpsSapTableOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSapTableOperStatus.setStatus("mandatory")


class _SfpsSapTableAdminStatus_Type(Integer32):
    """Custom type sfpsSapTableAdminStatus based on Integer32"""
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


_SfpsSapTableAdminStatus_Type.__name__ = "Integer32"
_SfpsSapTableAdminStatus_Object = MibTableColumn
sfpsSapTableAdminStatus = _SfpsSapTableAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 8),
    _SfpsSapTableAdminStatus_Type()
)
sfpsSapTableAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSapTableAdminStatus.setStatus("mandatory")
_SfpsSapTableStateTime_Type = TimeTicks
_SfpsSapTableStateTime_Object = MibTableColumn
sfpsSapTableStateTime = _SfpsSapTableStateTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 9),
    _SfpsSapTableStateTime_Type()
)
sfpsSapTableStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSapTableStateTime.setStatus("mandatory")
_SfpsSapTableDescription_Type = DisplayString
_SfpsSapTableDescription_Object = MibTableColumn
sfpsSapTableDescription = _SfpsSapTableDescription_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 10),
    _SfpsSapTableDescription_Type()
)
sfpsSapTableDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSapTableDescription.setStatus("mandatory")
_SfpsSapTableNumAccepted_Type = Integer32
_SfpsSapTableNumAccepted_Object = MibTableColumn
sfpsSapTableNumAccepted = _SfpsSapTableNumAccepted_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 11),
    _SfpsSapTableNumAccepted_Type()
)
sfpsSapTableNumAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSapTableNumAccepted.setStatus("mandatory")
_SfpsSapTableNumDropped_Type = Integer32
_SfpsSapTableNumDropped_Object = MibTableColumn
sfpsSapTableNumDropped = _SfpsSapTableNumDropped_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 12),
    _SfpsSapTableNumDropped_Type()
)
sfpsSapTableNumDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSapTableNumDropped.setStatus("mandatory")
_SfpsSapTableUnicastSap_Type = Integer32
_SfpsSapTableUnicastSap_Object = MibTableColumn
sfpsSapTableUnicastSap = _SfpsSapTableUnicastSap_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 13),
    _SfpsSapTableUnicastSap_Type()
)
sfpsSapTableUnicastSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSapTableUnicastSap.setStatus("mandatory")


class _SfpsSapTableNVStatus_Type(Integer32):
    """Custom type sfpsSapTableNVStatus based on Integer32"""
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
        *(("disable", 2),
          ("enable", 3),
          ("other", 1),
          ("unset", 4))
    )


_SfpsSapTableNVStatus_Type.__name__ = "Integer32"
_SfpsSapTableNVStatus_Object = MibTableColumn
sfpsSapTableNVStatus = _SfpsSapTableNVStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 14),
    _SfpsSapTableNVStatus_Type()
)
sfpsSapTableNVStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSapTableNVStatus.setStatus("mandatory")


class _SfpsSapAPIVerb_Type(Integer32):
    """Custom type sfpsSapAPIVerb based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("clearAllNvram", 9),
          ("clearFromNvram", 8),
          ("disable", 4),
          ("disableInNvram", 5),
          ("enable", 6),
          ("enableInNvram", 7),
          ("first", 3),
          ("getStatus", 1),
          ("next", 2),
          ("resetAllStats", 11),
          ("resetStats", 10))
    )


_SfpsSapAPIVerb_Type.__name__ = "Integer32"
_SfpsSapAPIVerb_Object = MibScalar
sfpsSapAPIVerb = _SfpsSapAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 1),
    _SfpsSapAPIVerb_Type()
)
sfpsSapAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSapAPIVerb.setStatus("mandatory")
_SfpsSapAPISourceCP_Type = DisplayString
_SfpsSapAPISourceCP_Object = MibScalar
sfpsSapAPISourceCP = _SfpsSapAPISourceCP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 2),
    _SfpsSapAPISourceCP_Type()
)
sfpsSapAPISourceCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSapAPISourceCP.setStatus("mandatory")
_SfpsSapAPIDestCP_Type = DisplayString
_SfpsSapAPIDestCP_Object = MibScalar
sfpsSapAPIDestCP = _SfpsSapAPIDestCP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 3),
    _SfpsSapAPIDestCP_Type()
)
sfpsSapAPIDestCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSapAPIDestCP.setStatus("mandatory")
_SfpsSapAPISAP_Type = DisplayString
_SfpsSapAPISAP_Object = MibScalar
sfpsSapAPISAP = _SfpsSapAPISAP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 4),
    _SfpsSapAPISAP_Type()
)
sfpsSapAPISAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSapAPISAP.setStatus("mandatory")


class _SfpsSapAPINVStatus_Type(Integer32):
    """Custom type sfpsSapAPINVStatus based on Integer32"""
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
        *(("disable", 2),
          ("enable", 3),
          ("other", 1),
          ("unset", 4))
    )


_SfpsSapAPINVStatus_Type.__name__ = "Integer32"
_SfpsSapAPINVStatus_Object = MibScalar
sfpsSapAPINVStatus = _SfpsSapAPINVStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 5),
    _SfpsSapAPINVStatus_Type()
)
sfpsSapAPINVStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSapAPINVStatus.setStatus("mandatory")


class _SfpsSapAPIAdminStatus_Type(Integer32):
    """Custom type sfpsSapAPIAdminStatus based on Integer32"""
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


_SfpsSapAPIAdminStatus_Type.__name__ = "Integer32"
_SfpsSapAPIAdminStatus_Object = MibScalar
sfpsSapAPIAdminStatus = _SfpsSapAPIAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 6),
    _SfpsSapAPIAdminStatus_Type()
)
sfpsSapAPIAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSapAPIAdminStatus.setStatus("mandatory")


class _SfpsSapAPIOperStatus_Type(Integer32):
    """Custom type sfpsSapAPIOperStatus based on Integer32"""
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


_SfpsSapAPIOperStatus_Type.__name__ = "Integer32"
_SfpsSapAPIOperStatus_Object = MibScalar
sfpsSapAPIOperStatus = _SfpsSapAPIOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 7),
    _SfpsSapAPIOperStatus_Type()
)
sfpsSapAPIOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSapAPIOperStatus.setStatus("mandatory")
_SfpsSapAPINvSet_Type = Integer32
_SfpsSapAPINvSet_Object = MibScalar
sfpsSapAPINvSet = _SfpsSapAPINvSet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 8),
    _SfpsSapAPINvSet_Type()
)
sfpsSapAPINvSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSapAPINvSet.setStatus("mandatory")
_SfpsSapAPINVTotal_Type = Integer32
_SfpsSapAPINVTotal_Object = MibScalar
sfpsSapAPINVTotal = _SfpsSapAPINVTotal_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 9),
    _SfpsSapAPINVTotal_Type()
)
sfpsSapAPINVTotal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSapAPINVTotal.setStatus("mandatory")
_SfpsSapAPINumAccept_Type = Integer32
_SfpsSapAPINumAccept_Object = MibScalar
sfpsSapAPINumAccept = _SfpsSapAPINumAccept_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 10),
    _SfpsSapAPINumAccept_Type()
)
sfpsSapAPINumAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSapAPINumAccept.setStatus("mandatory")
_SfpsSapAPINvDiscard_Type = Integer32
_SfpsSapAPINvDiscard_Object = MibScalar
sfpsSapAPINvDiscard = _SfpsSapAPINvDiscard_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 11),
    _SfpsSapAPINvDiscard_Type()
)
sfpsSapAPINvDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSapAPINvDiscard.setStatus("mandatory")


class _SfpsSapAPIDefaultStatus_Type(Integer32):
    """Custom type sfpsSapAPIDefaultStatus based on Integer32"""
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


_SfpsSapAPIDefaultStatus_Type.__name__ = "Integer32"
_SfpsSapAPIDefaultStatus_Object = MibScalar
sfpsSapAPIDefaultStatus = _SfpsSapAPIDefaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 12),
    _SfpsSapAPIDefaultStatus_Type()
)
sfpsSapAPIDefaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSapAPIDefaultStatus.setStatus("mandatory")
_SfpsCallByTupleTable_Object = MibTable
sfpsCallByTupleTable = _SfpsCallByTupleTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1)
)
if mibBuilder.loadTexts:
    sfpsCallByTupleTable.setStatus("mandatory")
_SfpsCallByTupleEntry_Object = MibTableRow
sfpsCallByTupleEntry = _SfpsCallByTupleEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1)
)
sfpsCallByTupleEntry.setIndexNames(
    (0, "CTRON-SFPS-CALL-MIB", "sfpsCallByTupleInPort"),
    (0, "CTRON-SFPS-CALL-MIB", "sfpsCallByTupleSrcHash"),
    (0, "CTRON-SFPS-CALL-MIB", "sfpsCallByTupleDstHash"),
    (0, "CTRON-SFPS-CALL-MIB", "sfpsCallByTupleHashIndex"),
)
if mibBuilder.loadTexts:
    sfpsCallByTupleEntry.setStatus("mandatory")
_SfpsCallByTupleInPort_Type = Integer32
_SfpsCallByTupleInPort_Object = MibTableColumn
sfpsCallByTupleInPort = _SfpsCallByTupleInPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 1),
    _SfpsCallByTupleInPort_Type()
)
sfpsCallByTupleInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallByTupleInPort.setStatus("mandatory")
_SfpsCallByTupleSrcHash_Type = Integer32
_SfpsCallByTupleSrcHash_Object = MibTableColumn
sfpsCallByTupleSrcHash = _SfpsCallByTupleSrcHash_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 2),
    _SfpsCallByTupleSrcHash_Type()
)
sfpsCallByTupleSrcHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallByTupleSrcHash.setStatus("mandatory")
_SfpsCallByTupleDstHash_Type = Integer32
_SfpsCallByTupleDstHash_Object = MibTableColumn
sfpsCallByTupleDstHash = _SfpsCallByTupleDstHash_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 3),
    _SfpsCallByTupleDstHash_Type()
)
sfpsCallByTupleDstHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallByTupleDstHash.setStatus("mandatory")
_SfpsCallByTupleHashIndex_Type = Integer32
_SfpsCallByTupleHashIndex_Object = MibTableColumn
sfpsCallByTupleHashIndex = _SfpsCallByTupleHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 4),
    _SfpsCallByTupleHashIndex_Type()
)
sfpsCallByTupleHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallByTupleHashIndex.setStatus("mandatory")
_SfpsCallByTupleBotSrcType_Type = DisplayString
_SfpsCallByTupleBotSrcType_Object = MibTableColumn
sfpsCallByTupleBotSrcType = _SfpsCallByTupleBotSrcType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 5),
    _SfpsCallByTupleBotSrcType_Type()
)
sfpsCallByTupleBotSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallByTupleBotSrcType.setStatus("mandatory")
_SfpsCallByTupleBotSrcAddress_Type = DisplayString
_SfpsCallByTupleBotSrcAddress_Object = MibTableColumn
sfpsCallByTupleBotSrcAddress = _SfpsCallByTupleBotSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 6),
    _SfpsCallByTupleBotSrcAddress_Type()
)
sfpsCallByTupleBotSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallByTupleBotSrcAddress.setStatus("mandatory")
_SfpsCallByTupleBotDstType_Type = DisplayString
_SfpsCallByTupleBotDstType_Object = MibTableColumn
sfpsCallByTupleBotDstType = _SfpsCallByTupleBotDstType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 7),
    _SfpsCallByTupleBotDstType_Type()
)
sfpsCallByTupleBotDstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallByTupleBotDstType.setStatus("mandatory")
_SfpsCallByTupleBotDstAddress_Type = DisplayString
_SfpsCallByTupleBotDstAddress_Object = MibTableColumn
sfpsCallByTupleBotDstAddress = _SfpsCallByTupleBotDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 8),
    _SfpsCallByTupleBotDstAddress_Type()
)
sfpsCallByTupleBotDstAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallByTupleBotDstAddress.setStatus("mandatory")
_SfpsCallByTupleTopSrcType_Type = DisplayString
_SfpsCallByTupleTopSrcType_Object = MibTableColumn
sfpsCallByTupleTopSrcType = _SfpsCallByTupleTopSrcType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 9),
    _SfpsCallByTupleTopSrcType_Type()
)
sfpsCallByTupleTopSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallByTupleTopSrcType.setStatus("mandatory")
_SfpsCallByTupleTopSrcAddress_Type = DisplayString
_SfpsCallByTupleTopSrcAddress_Object = MibTableColumn
sfpsCallByTupleTopSrcAddress = _SfpsCallByTupleTopSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 10),
    _SfpsCallByTupleTopSrcAddress_Type()
)
sfpsCallByTupleTopSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallByTupleTopSrcAddress.setStatus("mandatory")
_SfpsCallByTupleTopDstType_Type = DisplayString
_SfpsCallByTupleTopDstType_Object = MibTableColumn
sfpsCallByTupleTopDstType = _SfpsCallByTupleTopDstType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 11),
    _SfpsCallByTupleTopDstType_Type()
)
sfpsCallByTupleTopDstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallByTupleTopDstType.setStatus("mandatory")
_SfpsCallByTupleTopDstAddress_Type = DisplayString
_SfpsCallByTupleTopDstAddress_Object = MibTableColumn
sfpsCallByTupleTopDstAddress = _SfpsCallByTupleTopDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 12),
    _SfpsCallByTupleTopDstAddress_Type()
)
sfpsCallByTupleTopDstAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallByTupleTopDstAddress.setStatus("mandatory")
_SfpsCallByTupleCallProcName_Type = DisplayString
_SfpsCallByTupleCallProcName_Object = MibTableColumn
sfpsCallByTupleCallProcName = _SfpsCallByTupleCallProcName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 13),
    _SfpsCallByTupleCallProcName_Type()
)
sfpsCallByTupleCallProcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallByTupleCallProcName.setStatus("mandatory")
_SfpsCallByTupleCallTag_Type = HexInteger
_SfpsCallByTupleCallTag_Object = MibTableColumn
sfpsCallByTupleCallTag = _SfpsCallByTupleCallTag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 14),
    _SfpsCallByTupleCallTag_Type()
)
sfpsCallByTupleCallTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallByTupleCallTag.setStatus("mandatory")
_SfpsCallByTupleCallState_Type = DisplayString
_SfpsCallByTupleCallState_Object = MibTableColumn
sfpsCallByTupleCallState = _SfpsCallByTupleCallState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 15),
    _SfpsCallByTupleCallState_Type()
)
sfpsCallByTupleCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallByTupleCallState.setStatus("mandatory")
_SfpsCallByTupleTimeRemaining_Type = TimeTicks
_SfpsCallByTupleTimeRemaining_Object = MibTableColumn
sfpsCallByTupleTimeRemaining = _SfpsCallByTupleTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 16),
    _SfpsCallByTupleTimeRemaining_Type()
)
sfpsCallByTupleTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallByTupleTimeRemaining.setStatus("mandatory")
_SfpsCallTableStatsRam_Type = Integer32
_SfpsCallTableStatsRam_Object = MibScalar
sfpsCallTableStatsRam = _SfpsCallTableStatsRam_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 6, 1),
    _SfpsCallTableStatsRam_Type()
)
sfpsCallTableStatsRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallTableStatsRam.setStatus("mandatory")
_SfpsCallTableStatsSize_Type = Integer32
_SfpsCallTableStatsSize_Object = MibScalar
sfpsCallTableStatsSize = _SfpsCallTableStatsSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 6, 2),
    _SfpsCallTableStatsSize_Type()
)
sfpsCallTableStatsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallTableStatsSize.setStatus("mandatory")
_SfpsCallTableStatsInUse_Type = Integer32
_SfpsCallTableStatsInUse_Object = MibScalar
sfpsCallTableStatsInUse = _SfpsCallTableStatsInUse_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 6, 3),
    _SfpsCallTableStatsInUse_Type()
)
sfpsCallTableStatsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallTableStatsInUse.setStatus("mandatory")
_SfpsCallTableStatsMax_Type = Integer32
_SfpsCallTableStatsMax_Object = MibScalar
sfpsCallTableStatsMax = _SfpsCallTableStatsMax_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 6, 4),
    _SfpsCallTableStatsMax_Type()
)
sfpsCallTableStatsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallTableStatsMax.setStatus("mandatory")
_SfpsCallTableStatsTotMisses_Type = Integer32
_SfpsCallTableStatsTotMisses_Object = MibScalar
sfpsCallTableStatsTotMisses = _SfpsCallTableStatsTotMisses_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 6, 5),
    _SfpsCallTableStatsTotMisses_Type()
)
sfpsCallTableStatsTotMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallTableStatsTotMisses.setStatus("mandatory")
_SfpsCallTableStatsMissStart_Type = TimeTicks
_SfpsCallTableStatsMissStart_Object = MibScalar
sfpsCallTableStatsMissStart = _SfpsCallTableStatsMissStart_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 6, 7),
    _SfpsCallTableStatsMissStart_Type()
)
sfpsCallTableStatsMissStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallTableStatsMissStart.setStatus("mandatory")
_SfpsCallTableStatsMissStop_Type = TimeTicks
_SfpsCallTableStatsMissStop_Object = MibScalar
sfpsCallTableStatsMissStop = _SfpsCallTableStatsMissStop_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 6, 8),
    _SfpsCallTableStatsMissStop_Type()
)
sfpsCallTableStatsMissStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCallTableStatsMissStop.setStatus("mandatory")
_SfpsCallTableStatsLastMiss_Type = Integer32
_SfpsCallTableStatsLastMiss_Object = MibScalar
sfpsCallTableStatsLastMiss = _SfpsCallTableStatsLastMiss_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 6, 9),
    _SfpsCallTableStatsLastMiss_Type()
)
sfpsCallTableStatsLastMiss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsCallTableStatsLastMiss.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-CALL-MIB",
    **{"HexInteger": HexInteger,
       "sfpsSapTable": sfpsSapTable,
       "sfpsSapTableEntry": sfpsSapTableEntry,
       "sfpsSapTableTag": sfpsSapTableTag,
       "sfpsSapTableHash": sfpsSapTableHash,
       "sfpsSapTableHashIndex": sfpsSapTableHashIndex,
       "sfpsSapTableSourceCP": sfpsSapTableSourceCP,
       "sfpsSapTableDestCP": sfpsSapTableDestCP,
       "sfpsSapTableSAP": sfpsSapTableSAP,
       "sfpsSapTableOperStatus": sfpsSapTableOperStatus,
       "sfpsSapTableAdminStatus": sfpsSapTableAdminStatus,
       "sfpsSapTableStateTime": sfpsSapTableStateTime,
       "sfpsSapTableDescription": sfpsSapTableDescription,
       "sfpsSapTableNumAccepted": sfpsSapTableNumAccepted,
       "sfpsSapTableNumDropped": sfpsSapTableNumDropped,
       "sfpsSapTableUnicastSap": sfpsSapTableUnicastSap,
       "sfpsSapTableNVStatus": sfpsSapTableNVStatus,
       "sfpsSapAPIVerb": sfpsSapAPIVerb,
       "sfpsSapAPISourceCP": sfpsSapAPISourceCP,
       "sfpsSapAPIDestCP": sfpsSapAPIDestCP,
       "sfpsSapAPISAP": sfpsSapAPISAP,
       "sfpsSapAPINVStatus": sfpsSapAPINVStatus,
       "sfpsSapAPIAdminStatus": sfpsSapAPIAdminStatus,
       "sfpsSapAPIOperStatus": sfpsSapAPIOperStatus,
       "sfpsSapAPINvSet": sfpsSapAPINvSet,
       "sfpsSapAPINVTotal": sfpsSapAPINVTotal,
       "sfpsSapAPINumAccept": sfpsSapAPINumAccept,
       "sfpsSapAPINvDiscard": sfpsSapAPINvDiscard,
       "sfpsSapAPIDefaultStatus": sfpsSapAPIDefaultStatus,
       "sfpsCallByTupleTable": sfpsCallByTupleTable,
       "sfpsCallByTupleEntry": sfpsCallByTupleEntry,
       "sfpsCallByTupleInPort": sfpsCallByTupleInPort,
       "sfpsCallByTupleSrcHash": sfpsCallByTupleSrcHash,
       "sfpsCallByTupleDstHash": sfpsCallByTupleDstHash,
       "sfpsCallByTupleHashIndex": sfpsCallByTupleHashIndex,
       "sfpsCallByTupleBotSrcType": sfpsCallByTupleBotSrcType,
       "sfpsCallByTupleBotSrcAddress": sfpsCallByTupleBotSrcAddress,
       "sfpsCallByTupleBotDstType": sfpsCallByTupleBotDstType,
       "sfpsCallByTupleBotDstAddress": sfpsCallByTupleBotDstAddress,
       "sfpsCallByTupleTopSrcType": sfpsCallByTupleTopSrcType,
       "sfpsCallByTupleTopSrcAddress": sfpsCallByTupleTopSrcAddress,
       "sfpsCallByTupleTopDstType": sfpsCallByTupleTopDstType,
       "sfpsCallByTupleTopDstAddress": sfpsCallByTupleTopDstAddress,
       "sfpsCallByTupleCallProcName": sfpsCallByTupleCallProcName,
       "sfpsCallByTupleCallTag": sfpsCallByTupleCallTag,
       "sfpsCallByTupleCallState": sfpsCallByTupleCallState,
       "sfpsCallByTupleTimeRemaining": sfpsCallByTupleTimeRemaining,
       "sfpsCallTableStatsRam": sfpsCallTableStatsRam,
       "sfpsCallTableStatsSize": sfpsCallTableStatsSize,
       "sfpsCallTableStatsInUse": sfpsCallTableStatsInUse,
       "sfpsCallTableStatsMax": sfpsCallTableStatsMax,
       "sfpsCallTableStatsTotMisses": sfpsCallTableStatsTotMisses,
       "sfpsCallTableStatsMissStart": sfpsCallTableStatsMissStart,
       "sfpsCallTableStatsMissStop": sfpsCallTableStatsMissStop,
       "sfpsCallTableStatsLastMiss": sfpsCallTableStatsLastMiss}
)
