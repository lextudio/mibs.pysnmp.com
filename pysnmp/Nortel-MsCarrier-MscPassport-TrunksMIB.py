# SNMP MIB module (Nortel-MsCarrier-MscPassport-TrunksMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-TrunksMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:56 2024
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

(Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 InterfaceIndex,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "InterfaceIndex",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 AsciiStringIndex,
 FixedPoint1,
 NonReplicated,
 PassportCounter64) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "FixedPoint1",
    "NonReplicated",
    "PassportCounter64")

(mscComponents,
 mscPassportMIBs) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscComponents",
    "mscPassportMIBs")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MscTrk_ObjectIdentity = ObjectIdentity
mscTrk = _MscTrk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60)
)
_MscTrkRowStatusTable_Object = MibTable
mscTrkRowStatusTable = _MscTrkRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 1)
)
if mibBuilder.loadTexts:
    mscTrkRowStatusTable.setStatus("mandatory")
_MscTrkRowStatusEntry_Object = MibTableRow
mscTrkRowStatusEntry = _MscTrkRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 1, 1)
)
mscTrkRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
)
if mibBuilder.loadTexts:
    mscTrkRowStatusEntry.setStatus("mandatory")
_MscTrkRowStatus_Type = RowStatus
_MscTrkRowStatus_Object = MibTableColumn
mscTrkRowStatus = _MscTrkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 1, 1, 1),
    _MscTrkRowStatus_Type()
)
mscTrkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkRowStatus.setStatus("mandatory")
_MscTrkComponentName_Type = DisplayString
_MscTrkComponentName_Object = MibTableColumn
mscTrkComponentName = _MscTrkComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 1, 1, 2),
    _MscTrkComponentName_Type()
)
mscTrkComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkComponentName.setStatus("mandatory")
_MscTrkStorageType_Type = StorageType
_MscTrkStorageType_Object = MibTableColumn
mscTrkStorageType = _MscTrkStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 1, 1, 4),
    _MscTrkStorageType_Type()
)
mscTrkStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkStorageType.setStatus("mandatory")


class _MscTrkIndex_Type(Integer32):
    """Custom type mscTrkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscTrkIndex_Type.__name__ = "Integer32"
_MscTrkIndex_Object = MibTableColumn
mscTrkIndex = _MscTrkIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 1, 1, 10),
    _MscTrkIndex_Type()
)
mscTrkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkIndex.setStatus("mandatory")
_MscTrkPorsStats_ObjectIdentity = ObjectIdentity
mscTrkPorsStats = _MscTrkPorsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6)
)
_MscTrkPorsStatsRowStatusTable_Object = MibTable
mscTrkPorsStatsRowStatusTable = _MscTrkPorsStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 1)
)
if mibBuilder.loadTexts:
    mscTrkPorsStatsRowStatusTable.setStatus("mandatory")
_MscTrkPorsStatsRowStatusEntry_Object = MibTableRow
mscTrkPorsStatsRowStatusEntry = _MscTrkPorsStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 1, 1)
)
mscTrkPorsStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkPorsStatsIndex"),
)
if mibBuilder.loadTexts:
    mscTrkPorsStatsRowStatusEntry.setStatus("mandatory")
_MscTrkPorsStatsRowStatus_Type = RowStatus
_MscTrkPorsStatsRowStatus_Object = MibTableColumn
mscTrkPorsStatsRowStatus = _MscTrkPorsStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 1, 1, 1),
    _MscTrkPorsStatsRowStatus_Type()
)
mscTrkPorsStatsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPorsStatsRowStatus.setStatus("mandatory")
_MscTrkPorsStatsComponentName_Type = DisplayString
_MscTrkPorsStatsComponentName_Object = MibTableColumn
mscTrkPorsStatsComponentName = _MscTrkPorsStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 1, 1, 2),
    _MscTrkPorsStatsComponentName_Type()
)
mscTrkPorsStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPorsStatsComponentName.setStatus("mandatory")
_MscTrkPorsStatsStorageType_Type = StorageType
_MscTrkPorsStatsStorageType_Object = MibTableColumn
mscTrkPorsStatsStorageType = _MscTrkPorsStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 1, 1, 4),
    _MscTrkPorsStatsStorageType_Type()
)
mscTrkPorsStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPorsStatsStorageType.setStatus("mandatory")
_MscTrkPorsStatsIndex_Type = NonReplicated
_MscTrkPorsStatsIndex_Object = MibTableColumn
mscTrkPorsStatsIndex = _MscTrkPorsStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 1, 1, 10),
    _MscTrkPorsStatsIndex_Type()
)
mscTrkPorsStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkPorsStatsIndex.setStatus("mandatory")
_MscTrkPorsStatsOperTable_Object = MibTable
mscTrkPorsStatsOperTable = _MscTrkPorsStatsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 10)
)
if mibBuilder.loadTexts:
    mscTrkPorsStatsOperTable.setStatus("mandatory")
_MscTrkPorsStatsOperEntry_Object = MibTableRow
mscTrkPorsStatsOperEntry = _MscTrkPorsStatsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 10, 1)
)
mscTrkPorsStatsOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkPorsStatsIndex"),
)
if mibBuilder.loadTexts:
    mscTrkPorsStatsOperEntry.setStatus("mandatory")
_MscTrkPorsStatsPorsNormPktFromIf_Type = PassportCounter64
_MscTrkPorsStatsPorsNormPktFromIf_Object = MibTableColumn
mscTrkPorsStatsPorsNormPktFromIf = _MscTrkPorsStatsPorsNormPktFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 10, 1, 1),
    _MscTrkPorsStatsPorsNormPktFromIf_Type()
)
mscTrkPorsStatsPorsNormPktFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPorsStatsPorsNormPktFromIf.setStatus("mandatory")
_MscTrkPorsStatsPorsNormDiscUnforwardFromIf_Type = PassportCounter64
_MscTrkPorsStatsPorsNormDiscUnforwardFromIf_Object = MibTableColumn
mscTrkPorsStatsPorsNormDiscUnforwardFromIf = _MscTrkPorsStatsPorsNormDiscUnforwardFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 10, 1, 2),
    _MscTrkPorsStatsPorsNormDiscUnforwardFromIf_Type()
)
mscTrkPorsStatsPorsNormDiscUnforwardFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPorsStatsPorsNormDiscUnforwardFromIf.setStatus("mandatory")
_MscTrkPorsStatsPorsNormOctetFromIf_Type = PassportCounter64
_MscTrkPorsStatsPorsNormOctetFromIf_Object = MibTableColumn
mscTrkPorsStatsPorsNormOctetFromIf = _MscTrkPorsStatsPorsNormOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 10, 1, 3),
    _MscTrkPorsStatsPorsNormOctetFromIf_Type()
)
mscTrkPorsStatsPorsNormOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPorsStatsPorsNormOctetFromIf.setStatus("mandatory")
_MscTrkPorsStatsPorsIntPktFromIf_Type = PassportCounter64
_MscTrkPorsStatsPorsIntPktFromIf_Object = MibTableColumn
mscTrkPorsStatsPorsIntPktFromIf = _MscTrkPorsStatsPorsIntPktFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 10, 1, 4),
    _MscTrkPorsStatsPorsIntPktFromIf_Type()
)
mscTrkPorsStatsPorsIntPktFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPorsStatsPorsIntPktFromIf.setStatus("mandatory")
_MscTrkPorsStatsPorsIntDiscUnforwardFromIf_Type = PassportCounter64
_MscTrkPorsStatsPorsIntDiscUnforwardFromIf_Object = MibTableColumn
mscTrkPorsStatsPorsIntDiscUnforwardFromIf = _MscTrkPorsStatsPorsIntDiscUnforwardFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 10, 1, 5),
    _MscTrkPorsStatsPorsIntDiscUnforwardFromIf_Type()
)
mscTrkPorsStatsPorsIntDiscUnforwardFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPorsStatsPorsIntDiscUnforwardFromIf.setStatus("mandatory")
_MscTrkPorsStatsPorsIntOctetFromIf_Type = PassportCounter64
_MscTrkPorsStatsPorsIntOctetFromIf_Object = MibTableColumn
mscTrkPorsStatsPorsIntOctetFromIf = _MscTrkPorsStatsPorsIntOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 10, 1, 6),
    _MscTrkPorsStatsPorsIntOctetFromIf_Type()
)
mscTrkPorsStatsPorsIntOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPorsStatsPorsIntOctetFromIf.setStatus("mandatory")
_MscTrkPorsStatsPktBpTable_Object = MibTable
mscTrkPorsStatsPktBpTable = _MscTrkPorsStatsPktBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 371)
)
if mibBuilder.loadTexts:
    mscTrkPorsStatsPktBpTable.setStatus("mandatory")
_MscTrkPorsStatsPktBpEntry_Object = MibTableRow
mscTrkPorsStatsPktBpEntry = _MscTrkPorsStatsPktBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 371, 1)
)
mscTrkPorsStatsPktBpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkPorsStatsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkPorsStatsPktBpEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkPorsStatsPktBpDpIndex"),
)
if mibBuilder.loadTexts:
    mscTrkPorsStatsPktBpEntry.setStatus("mandatory")


class _MscTrkPorsStatsPktBpEpIndex_Type(Integer32):
    """Custom type mscTrkPorsStatsPktBpEpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ep0", 0),
          ("ep1", 1),
          ("ep2", 2))
    )


_MscTrkPorsStatsPktBpEpIndex_Type.__name__ = "Integer32"
_MscTrkPorsStatsPktBpEpIndex_Object = MibTableColumn
mscTrkPorsStatsPktBpEpIndex = _MscTrkPorsStatsPktBpEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 371, 1, 1),
    _MscTrkPorsStatsPktBpEpIndex_Type()
)
mscTrkPorsStatsPktBpEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkPorsStatsPktBpEpIndex.setStatus("mandatory")


class _MscTrkPorsStatsPktBpDpIndex_Type(Integer32):
    """Custom type mscTrkPorsStatsPktBpDpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dp0", 0),
          ("dp1", 1),
          ("dp2", 2),
          ("dp3", 3))
    )


_MscTrkPorsStatsPktBpDpIndex_Type.__name__ = "Integer32"
_MscTrkPorsStatsPktBpDpIndex_Object = MibTableColumn
mscTrkPorsStatsPktBpDpIndex = _MscTrkPorsStatsPktBpDpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 371, 1, 2),
    _MscTrkPorsStatsPktBpDpIndex_Type()
)
mscTrkPorsStatsPktBpDpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkPorsStatsPktBpDpIndex.setStatus("mandatory")
_MscTrkPorsStatsPktBpValue_Type = PassportCounter64
_MscTrkPorsStatsPktBpValue_Object = MibTableColumn
mscTrkPorsStatsPktBpValue = _MscTrkPorsStatsPktBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 371, 1, 3),
    _MscTrkPorsStatsPktBpValue_Type()
)
mscTrkPorsStatsPktBpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPorsStatsPktBpValue.setStatus("mandatory")
_MscTrkPorsStatsDiscBpTable_Object = MibTable
mscTrkPorsStatsDiscBpTable = _MscTrkPorsStatsDiscBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 372)
)
if mibBuilder.loadTexts:
    mscTrkPorsStatsDiscBpTable.setStatus("mandatory")
_MscTrkPorsStatsDiscBpEntry_Object = MibTableRow
mscTrkPorsStatsDiscBpEntry = _MscTrkPorsStatsDiscBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 372, 1)
)
mscTrkPorsStatsDiscBpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkPorsStatsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkPorsStatsDiscBpEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkPorsStatsDiscBpDpIndex"),
)
if mibBuilder.loadTexts:
    mscTrkPorsStatsDiscBpEntry.setStatus("mandatory")


class _MscTrkPorsStatsDiscBpEpIndex_Type(Integer32):
    """Custom type mscTrkPorsStatsDiscBpEpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ep0", 0),
          ("ep1", 1),
          ("ep2", 2))
    )


_MscTrkPorsStatsDiscBpEpIndex_Type.__name__ = "Integer32"
_MscTrkPorsStatsDiscBpEpIndex_Object = MibTableColumn
mscTrkPorsStatsDiscBpEpIndex = _MscTrkPorsStatsDiscBpEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 372, 1, 1),
    _MscTrkPorsStatsDiscBpEpIndex_Type()
)
mscTrkPorsStatsDiscBpEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkPorsStatsDiscBpEpIndex.setStatus("mandatory")


class _MscTrkPorsStatsDiscBpDpIndex_Type(Integer32):
    """Custom type mscTrkPorsStatsDiscBpDpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dp0", 0),
          ("dp1", 1),
          ("dp2", 2),
          ("dp3", 3))
    )


_MscTrkPorsStatsDiscBpDpIndex_Type.__name__ = "Integer32"
_MscTrkPorsStatsDiscBpDpIndex_Object = MibTableColumn
mscTrkPorsStatsDiscBpDpIndex = _MscTrkPorsStatsDiscBpDpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 372, 1, 2),
    _MscTrkPorsStatsDiscBpDpIndex_Type()
)
mscTrkPorsStatsDiscBpDpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkPorsStatsDiscBpDpIndex.setStatus("mandatory")
_MscTrkPorsStatsDiscBpValue_Type = PassportCounter64
_MscTrkPorsStatsDiscBpValue_Object = MibTableColumn
mscTrkPorsStatsDiscBpValue = _MscTrkPorsStatsDiscBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 372, 1, 3),
    _MscTrkPorsStatsDiscBpValue_Type()
)
mscTrkPorsStatsDiscBpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPorsStatsDiscBpValue.setStatus("mandatory")
_MscTrkPorsStatsOctBpTable_Object = MibTable
mscTrkPorsStatsOctBpTable = _MscTrkPorsStatsOctBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 373)
)
if mibBuilder.loadTexts:
    mscTrkPorsStatsOctBpTable.setStatus("mandatory")
_MscTrkPorsStatsOctBpEntry_Object = MibTableRow
mscTrkPorsStatsOctBpEntry = _MscTrkPorsStatsOctBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 373, 1)
)
mscTrkPorsStatsOctBpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkPorsStatsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkPorsStatsOctBpEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkPorsStatsOctBpDpIndex"),
)
if mibBuilder.loadTexts:
    mscTrkPorsStatsOctBpEntry.setStatus("mandatory")


class _MscTrkPorsStatsOctBpEpIndex_Type(Integer32):
    """Custom type mscTrkPorsStatsOctBpEpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ep0", 0),
          ("ep1", 1),
          ("ep2", 2))
    )


_MscTrkPorsStatsOctBpEpIndex_Type.__name__ = "Integer32"
_MscTrkPorsStatsOctBpEpIndex_Object = MibTableColumn
mscTrkPorsStatsOctBpEpIndex = _MscTrkPorsStatsOctBpEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 373, 1, 1),
    _MscTrkPorsStatsOctBpEpIndex_Type()
)
mscTrkPorsStatsOctBpEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkPorsStatsOctBpEpIndex.setStatus("mandatory")


class _MscTrkPorsStatsOctBpDpIndex_Type(Integer32):
    """Custom type mscTrkPorsStatsOctBpDpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dp0", 0),
          ("dp1", 1),
          ("dp2", 2),
          ("dp3", 3))
    )


_MscTrkPorsStatsOctBpDpIndex_Type.__name__ = "Integer32"
_MscTrkPorsStatsOctBpDpIndex_Object = MibTableColumn
mscTrkPorsStatsOctBpDpIndex = _MscTrkPorsStatsOctBpDpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 373, 1, 2),
    _MscTrkPorsStatsOctBpDpIndex_Type()
)
mscTrkPorsStatsOctBpDpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkPorsStatsOctBpDpIndex.setStatus("mandatory")
_MscTrkPorsStatsOctBpValue_Type = PassportCounter64
_MscTrkPorsStatsOctBpValue_Object = MibTableColumn
mscTrkPorsStatsOctBpValue = _MscTrkPorsStatsOctBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 6, 373, 1, 3),
    _MscTrkPorsStatsOctBpValue_Type()
)
mscTrkPorsStatsOctBpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPorsStatsOctBpValue.setStatus("mandatory")
_MscTrkFwdStats_ObjectIdentity = ObjectIdentity
mscTrkFwdStats = _MscTrkFwdStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 7)
)
_MscTrkFwdStatsRowStatusTable_Object = MibTable
mscTrkFwdStatsRowStatusTable = _MscTrkFwdStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 7, 1)
)
if mibBuilder.loadTexts:
    mscTrkFwdStatsRowStatusTable.setStatus("mandatory")
_MscTrkFwdStatsRowStatusEntry_Object = MibTableRow
mscTrkFwdStatsRowStatusEntry = _MscTrkFwdStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 7, 1, 1)
)
mscTrkFwdStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkFwdStatsIndex"),
)
if mibBuilder.loadTexts:
    mscTrkFwdStatsRowStatusEntry.setStatus("mandatory")
_MscTrkFwdStatsRowStatus_Type = RowStatus
_MscTrkFwdStatsRowStatus_Object = MibTableColumn
mscTrkFwdStatsRowStatus = _MscTrkFwdStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 7, 1, 1, 1),
    _MscTrkFwdStatsRowStatus_Type()
)
mscTrkFwdStatsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkFwdStatsRowStatus.setStatus("mandatory")
_MscTrkFwdStatsComponentName_Type = DisplayString
_MscTrkFwdStatsComponentName_Object = MibTableColumn
mscTrkFwdStatsComponentName = _MscTrkFwdStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 7, 1, 1, 2),
    _MscTrkFwdStatsComponentName_Type()
)
mscTrkFwdStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkFwdStatsComponentName.setStatus("mandatory")
_MscTrkFwdStatsStorageType_Type = StorageType
_MscTrkFwdStatsStorageType_Object = MibTableColumn
mscTrkFwdStatsStorageType = _MscTrkFwdStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 7, 1, 1, 4),
    _MscTrkFwdStatsStorageType_Type()
)
mscTrkFwdStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkFwdStatsStorageType.setStatus("mandatory")
_MscTrkFwdStatsIndex_Type = NonReplicated
_MscTrkFwdStatsIndex_Object = MibTableColumn
mscTrkFwdStatsIndex = _MscTrkFwdStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 7, 1, 1, 10),
    _MscTrkFwdStatsIndex_Type()
)
mscTrkFwdStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkFwdStatsIndex.setStatus("mandatory")
_MscTrkFwdStatsOperTable_Object = MibTable
mscTrkFwdStatsOperTable = _MscTrkFwdStatsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 7, 10)
)
if mibBuilder.loadTexts:
    mscTrkFwdStatsOperTable.setStatus("mandatory")
_MscTrkFwdStatsOperEntry_Object = MibTableRow
mscTrkFwdStatsOperEntry = _MscTrkFwdStatsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 7, 10, 1)
)
mscTrkFwdStatsOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkFwdStatsIndex"),
)
if mibBuilder.loadTexts:
    mscTrkFwdStatsOperEntry.setStatus("mandatory")
_MscTrkFwdStatsFwdPktFromIf_Type = PassportCounter64
_MscTrkFwdStatsFwdPktFromIf_Object = MibTableColumn
mscTrkFwdStatsFwdPktFromIf = _MscTrkFwdStatsFwdPktFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 7, 10, 1, 1),
    _MscTrkFwdStatsFwdPktFromIf_Type()
)
mscTrkFwdStatsFwdPktFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkFwdStatsFwdPktFromIf.setStatus("mandatory")
_MscTrkFwdStatsFwdDiscUnforwardFromIf_Type = PassportCounter64
_MscTrkFwdStatsFwdDiscUnforwardFromIf_Object = MibTableColumn
mscTrkFwdStatsFwdDiscUnforwardFromIf = _MscTrkFwdStatsFwdDiscUnforwardFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 7, 10, 1, 2),
    _MscTrkFwdStatsFwdDiscUnforwardFromIf_Type()
)
mscTrkFwdStatsFwdDiscUnforwardFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkFwdStatsFwdDiscUnforwardFromIf.setStatus("mandatory")
_MscTrkFwdStatsFwdOctetFromIf_Type = PassportCounter64
_MscTrkFwdStatsFwdOctetFromIf_Object = MibTableColumn
mscTrkFwdStatsFwdOctetFromIf = _MscTrkFwdStatsFwdOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 7, 10, 1, 3),
    _MscTrkFwdStatsFwdOctetFromIf_Type()
)
mscTrkFwdStatsFwdOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkFwdStatsFwdOctetFromIf.setStatus("mandatory")
_MscTrkVnsStats_ObjectIdentity = ObjectIdentity
mscTrkVnsStats = _MscTrkVnsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8)
)
_MscTrkVnsStatsRowStatusTable_Object = MibTable
mscTrkVnsStatsRowStatusTable = _MscTrkVnsStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 1)
)
if mibBuilder.loadTexts:
    mscTrkVnsStatsRowStatusTable.setStatus("mandatory")
_MscTrkVnsStatsRowStatusEntry_Object = MibTableRow
mscTrkVnsStatsRowStatusEntry = _MscTrkVnsStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 1, 1)
)
mscTrkVnsStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkVnsStatsIndex"),
)
if mibBuilder.loadTexts:
    mscTrkVnsStatsRowStatusEntry.setStatus("mandatory")
_MscTrkVnsStatsRowStatus_Type = RowStatus
_MscTrkVnsStatsRowStatus_Object = MibTableColumn
mscTrkVnsStatsRowStatus = _MscTrkVnsStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 1, 1, 1),
    _MscTrkVnsStatsRowStatus_Type()
)
mscTrkVnsStatsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkVnsStatsRowStatus.setStatus("mandatory")
_MscTrkVnsStatsComponentName_Type = DisplayString
_MscTrkVnsStatsComponentName_Object = MibTableColumn
mscTrkVnsStatsComponentName = _MscTrkVnsStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 1, 1, 2),
    _MscTrkVnsStatsComponentName_Type()
)
mscTrkVnsStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkVnsStatsComponentName.setStatus("mandatory")
_MscTrkVnsStatsStorageType_Type = StorageType
_MscTrkVnsStatsStorageType_Object = MibTableColumn
mscTrkVnsStatsStorageType = _MscTrkVnsStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 1, 1, 4),
    _MscTrkVnsStatsStorageType_Type()
)
mscTrkVnsStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkVnsStatsStorageType.setStatus("mandatory")
_MscTrkVnsStatsIndex_Type = NonReplicated
_MscTrkVnsStatsIndex_Object = MibTableColumn
mscTrkVnsStatsIndex = _MscTrkVnsStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 1, 1, 10),
    _MscTrkVnsStatsIndex_Type()
)
mscTrkVnsStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkVnsStatsIndex.setStatus("mandatory")
_MscTrkVnsStatsOperTable_Object = MibTable
mscTrkVnsStatsOperTable = _MscTrkVnsStatsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 10)
)
if mibBuilder.loadTexts:
    mscTrkVnsStatsOperTable.setStatus("mandatory")
_MscTrkVnsStatsOperEntry_Object = MibTableRow
mscTrkVnsStatsOperEntry = _MscTrkVnsStatsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 10, 1)
)
mscTrkVnsStatsOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkVnsStatsIndex"),
)
if mibBuilder.loadTexts:
    mscTrkVnsStatsOperEntry.setStatus("mandatory")
_MscTrkVnsStatsVnsPktFromIf_Type = PassportCounter64
_MscTrkVnsStatsVnsPktFromIf_Object = MibTableColumn
mscTrkVnsStatsVnsPktFromIf = _MscTrkVnsStatsVnsPktFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 10, 1, 1),
    _MscTrkVnsStatsVnsPktFromIf_Type()
)
mscTrkVnsStatsVnsPktFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkVnsStatsVnsPktFromIf.setStatus("mandatory")
_MscTrkVnsStatsVnsDiscUnforwardFromIf_Type = PassportCounter64
_MscTrkVnsStatsVnsDiscUnforwardFromIf_Object = MibTableColumn
mscTrkVnsStatsVnsDiscUnforwardFromIf = _MscTrkVnsStatsVnsDiscUnforwardFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 10, 1, 2),
    _MscTrkVnsStatsVnsDiscUnforwardFromIf_Type()
)
mscTrkVnsStatsVnsDiscUnforwardFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkVnsStatsVnsDiscUnforwardFromIf.setStatus("mandatory")
_MscTrkVnsStatsVnsOctetFromIf_Type = PassportCounter64
_MscTrkVnsStatsVnsOctetFromIf_Object = MibTableColumn
mscTrkVnsStatsVnsOctetFromIf = _MscTrkVnsStatsVnsOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 10, 1, 3),
    _MscTrkVnsStatsVnsOctetFromIf_Type()
)
mscTrkVnsStatsVnsOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkVnsStatsVnsOctetFromIf.setStatus("mandatory")
_MscTrkVnsStatsPktBpTable_Object = MibTable
mscTrkVnsStatsPktBpTable = _MscTrkVnsStatsPktBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 377)
)
if mibBuilder.loadTexts:
    mscTrkVnsStatsPktBpTable.setStatus("mandatory")
_MscTrkVnsStatsPktBpEntry_Object = MibTableRow
mscTrkVnsStatsPktBpEntry = _MscTrkVnsStatsPktBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 377, 1)
)
mscTrkVnsStatsPktBpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkVnsStatsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkVnsStatsPktBpEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkVnsStatsPktBpDpIndex"),
)
if mibBuilder.loadTexts:
    mscTrkVnsStatsPktBpEntry.setStatus("mandatory")


class _MscTrkVnsStatsPktBpEpIndex_Type(Integer32):
    """Custom type mscTrkVnsStatsPktBpEpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ep0", 0),
          ("ep1", 1),
          ("ep2", 2))
    )


_MscTrkVnsStatsPktBpEpIndex_Type.__name__ = "Integer32"
_MscTrkVnsStatsPktBpEpIndex_Object = MibTableColumn
mscTrkVnsStatsPktBpEpIndex = _MscTrkVnsStatsPktBpEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 377, 1, 1),
    _MscTrkVnsStatsPktBpEpIndex_Type()
)
mscTrkVnsStatsPktBpEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkVnsStatsPktBpEpIndex.setStatus("mandatory")


class _MscTrkVnsStatsPktBpDpIndex_Type(Integer32):
    """Custom type mscTrkVnsStatsPktBpDpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dp0", 0),
          ("dp1", 1),
          ("dp2", 2),
          ("dp3", 3))
    )


_MscTrkVnsStatsPktBpDpIndex_Type.__name__ = "Integer32"
_MscTrkVnsStatsPktBpDpIndex_Object = MibTableColumn
mscTrkVnsStatsPktBpDpIndex = _MscTrkVnsStatsPktBpDpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 377, 1, 2),
    _MscTrkVnsStatsPktBpDpIndex_Type()
)
mscTrkVnsStatsPktBpDpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkVnsStatsPktBpDpIndex.setStatus("mandatory")
_MscTrkVnsStatsPktBpValue_Type = PassportCounter64
_MscTrkVnsStatsPktBpValue_Object = MibTableColumn
mscTrkVnsStatsPktBpValue = _MscTrkVnsStatsPktBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 377, 1, 3),
    _MscTrkVnsStatsPktBpValue_Type()
)
mscTrkVnsStatsPktBpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkVnsStatsPktBpValue.setStatus("mandatory")
_MscTrkVnsStatsDiscBpTable_Object = MibTable
mscTrkVnsStatsDiscBpTable = _MscTrkVnsStatsDiscBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 378)
)
if mibBuilder.loadTexts:
    mscTrkVnsStatsDiscBpTable.setStatus("mandatory")
_MscTrkVnsStatsDiscBpEntry_Object = MibTableRow
mscTrkVnsStatsDiscBpEntry = _MscTrkVnsStatsDiscBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 378, 1)
)
mscTrkVnsStatsDiscBpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkVnsStatsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkVnsStatsDiscBpEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkVnsStatsDiscBpDpIndex"),
)
if mibBuilder.loadTexts:
    mscTrkVnsStatsDiscBpEntry.setStatus("mandatory")


class _MscTrkVnsStatsDiscBpEpIndex_Type(Integer32):
    """Custom type mscTrkVnsStatsDiscBpEpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ep0", 0),
          ("ep1", 1),
          ("ep2", 2))
    )


_MscTrkVnsStatsDiscBpEpIndex_Type.__name__ = "Integer32"
_MscTrkVnsStatsDiscBpEpIndex_Object = MibTableColumn
mscTrkVnsStatsDiscBpEpIndex = _MscTrkVnsStatsDiscBpEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 378, 1, 1),
    _MscTrkVnsStatsDiscBpEpIndex_Type()
)
mscTrkVnsStatsDiscBpEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkVnsStatsDiscBpEpIndex.setStatus("mandatory")


class _MscTrkVnsStatsDiscBpDpIndex_Type(Integer32):
    """Custom type mscTrkVnsStatsDiscBpDpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dp0", 0),
          ("dp1", 1),
          ("dp2", 2),
          ("dp3", 3))
    )


_MscTrkVnsStatsDiscBpDpIndex_Type.__name__ = "Integer32"
_MscTrkVnsStatsDiscBpDpIndex_Object = MibTableColumn
mscTrkVnsStatsDiscBpDpIndex = _MscTrkVnsStatsDiscBpDpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 378, 1, 2),
    _MscTrkVnsStatsDiscBpDpIndex_Type()
)
mscTrkVnsStatsDiscBpDpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkVnsStatsDiscBpDpIndex.setStatus("mandatory")
_MscTrkVnsStatsDiscBpValue_Type = PassportCounter64
_MscTrkVnsStatsDiscBpValue_Object = MibTableColumn
mscTrkVnsStatsDiscBpValue = _MscTrkVnsStatsDiscBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 378, 1, 3),
    _MscTrkVnsStatsDiscBpValue_Type()
)
mscTrkVnsStatsDiscBpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkVnsStatsDiscBpValue.setStatus("mandatory")
_MscTrkVnsStatsOctBpTable_Object = MibTable
mscTrkVnsStatsOctBpTable = _MscTrkVnsStatsOctBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 379)
)
if mibBuilder.loadTexts:
    mscTrkVnsStatsOctBpTable.setStatus("mandatory")
_MscTrkVnsStatsOctBpEntry_Object = MibTableRow
mscTrkVnsStatsOctBpEntry = _MscTrkVnsStatsOctBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 379, 1)
)
mscTrkVnsStatsOctBpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkVnsStatsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkVnsStatsOctBpEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkVnsStatsOctBpDpIndex"),
)
if mibBuilder.loadTexts:
    mscTrkVnsStatsOctBpEntry.setStatus("mandatory")


class _MscTrkVnsStatsOctBpEpIndex_Type(Integer32):
    """Custom type mscTrkVnsStatsOctBpEpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ep0", 0),
          ("ep1", 1),
          ("ep2", 2))
    )


_MscTrkVnsStatsOctBpEpIndex_Type.__name__ = "Integer32"
_MscTrkVnsStatsOctBpEpIndex_Object = MibTableColumn
mscTrkVnsStatsOctBpEpIndex = _MscTrkVnsStatsOctBpEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 379, 1, 1),
    _MscTrkVnsStatsOctBpEpIndex_Type()
)
mscTrkVnsStatsOctBpEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkVnsStatsOctBpEpIndex.setStatus("mandatory")


class _MscTrkVnsStatsOctBpDpIndex_Type(Integer32):
    """Custom type mscTrkVnsStatsOctBpDpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dp0", 0),
          ("dp1", 1),
          ("dp2", 2),
          ("dp3", 3))
    )


_MscTrkVnsStatsOctBpDpIndex_Type.__name__ = "Integer32"
_MscTrkVnsStatsOctBpDpIndex_Object = MibTableColumn
mscTrkVnsStatsOctBpDpIndex = _MscTrkVnsStatsOctBpDpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 379, 1, 2),
    _MscTrkVnsStatsOctBpDpIndex_Type()
)
mscTrkVnsStatsOctBpDpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkVnsStatsOctBpDpIndex.setStatus("mandatory")
_MscTrkVnsStatsOctBpValue_Type = PassportCounter64
_MscTrkVnsStatsOctBpValue_Object = MibTableColumn
mscTrkVnsStatsOctBpValue = _MscTrkVnsStatsOctBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 8, 379, 1, 3),
    _MscTrkVnsStatsOctBpValue_Type()
)
mscTrkVnsStatsOctBpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkVnsStatsOctBpValue.setStatus("mandatory")
_MscTrkDprsStats_ObjectIdentity = ObjectIdentity
mscTrkDprsStats = _MscTrkDprsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 10)
)
_MscTrkDprsStatsRowStatusTable_Object = MibTable
mscTrkDprsStatsRowStatusTable = _MscTrkDprsStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 10, 1)
)
if mibBuilder.loadTexts:
    mscTrkDprsStatsRowStatusTable.setStatus("mandatory")
_MscTrkDprsStatsRowStatusEntry_Object = MibTableRow
mscTrkDprsStatsRowStatusEntry = _MscTrkDprsStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 10, 1, 1)
)
mscTrkDprsStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkDprsStatsIndex"),
)
if mibBuilder.loadTexts:
    mscTrkDprsStatsRowStatusEntry.setStatus("mandatory")
_MscTrkDprsStatsRowStatus_Type = RowStatus
_MscTrkDprsStatsRowStatus_Object = MibTableColumn
mscTrkDprsStatsRowStatus = _MscTrkDprsStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 10, 1, 1, 1),
    _MscTrkDprsStatsRowStatus_Type()
)
mscTrkDprsStatsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkDprsStatsRowStatus.setStatus("mandatory")
_MscTrkDprsStatsComponentName_Type = DisplayString
_MscTrkDprsStatsComponentName_Object = MibTableColumn
mscTrkDprsStatsComponentName = _MscTrkDprsStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 10, 1, 1, 2),
    _MscTrkDprsStatsComponentName_Type()
)
mscTrkDprsStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkDprsStatsComponentName.setStatus("mandatory")
_MscTrkDprsStatsStorageType_Type = StorageType
_MscTrkDprsStatsStorageType_Object = MibTableColumn
mscTrkDprsStatsStorageType = _MscTrkDprsStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 10, 1, 1, 4),
    _MscTrkDprsStatsStorageType_Type()
)
mscTrkDprsStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkDprsStatsStorageType.setStatus("mandatory")
_MscTrkDprsStatsIndex_Type = NonReplicated
_MscTrkDprsStatsIndex_Object = MibTableColumn
mscTrkDprsStatsIndex = _MscTrkDprsStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 10, 1, 1, 10),
    _MscTrkDprsStatsIndex_Type()
)
mscTrkDprsStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkDprsStatsIndex.setStatus("mandatory")
_MscTrkDprsStatsPktBpTable_Object = MibTable
mscTrkDprsStatsPktBpTable = _MscTrkDprsStatsPktBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 10, 374)
)
if mibBuilder.loadTexts:
    mscTrkDprsStatsPktBpTable.setStatus("mandatory")
_MscTrkDprsStatsPktBpEntry_Object = MibTableRow
mscTrkDprsStatsPktBpEntry = _MscTrkDprsStatsPktBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 10, 374, 1)
)
mscTrkDprsStatsPktBpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkDprsStatsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkDprsStatsPktBpEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkDprsStatsPktBpDpIndex"),
)
if mibBuilder.loadTexts:
    mscTrkDprsStatsPktBpEntry.setStatus("mandatory")


class _MscTrkDprsStatsPktBpEpIndex_Type(Integer32):
    """Custom type mscTrkDprsStatsPktBpEpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ep0", 0),
          ("ep1", 1),
          ("ep2", 2))
    )


_MscTrkDprsStatsPktBpEpIndex_Type.__name__ = "Integer32"
_MscTrkDprsStatsPktBpEpIndex_Object = MibTableColumn
mscTrkDprsStatsPktBpEpIndex = _MscTrkDprsStatsPktBpEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 10, 374, 1, 1),
    _MscTrkDprsStatsPktBpEpIndex_Type()
)
mscTrkDprsStatsPktBpEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkDprsStatsPktBpEpIndex.setStatus("mandatory")


class _MscTrkDprsStatsPktBpDpIndex_Type(Integer32):
    """Custom type mscTrkDprsStatsPktBpDpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dp0", 0),
          ("dp1", 1),
          ("dp2", 2),
          ("dp3", 3))
    )


_MscTrkDprsStatsPktBpDpIndex_Type.__name__ = "Integer32"
_MscTrkDprsStatsPktBpDpIndex_Object = MibTableColumn
mscTrkDprsStatsPktBpDpIndex = _MscTrkDprsStatsPktBpDpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 10, 374, 1, 2),
    _MscTrkDprsStatsPktBpDpIndex_Type()
)
mscTrkDprsStatsPktBpDpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkDprsStatsPktBpDpIndex.setStatus("mandatory")
_MscTrkDprsStatsPktBpValue_Type = PassportCounter64
_MscTrkDprsStatsPktBpValue_Object = MibTableColumn
mscTrkDprsStatsPktBpValue = _MscTrkDprsStatsPktBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 10, 374, 1, 3),
    _MscTrkDprsStatsPktBpValue_Type()
)
mscTrkDprsStatsPktBpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkDprsStatsPktBpValue.setStatus("mandatory")
_MscTrkDprsStatsDiscBpTable_Object = MibTable
mscTrkDprsStatsDiscBpTable = _MscTrkDprsStatsDiscBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 10, 375)
)
if mibBuilder.loadTexts:
    mscTrkDprsStatsDiscBpTable.setStatus("mandatory")
_MscTrkDprsStatsDiscBpEntry_Object = MibTableRow
mscTrkDprsStatsDiscBpEntry = _MscTrkDprsStatsDiscBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 10, 375, 1)
)
mscTrkDprsStatsDiscBpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkDprsStatsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkDprsStatsDiscBpEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkDprsStatsDiscBpDpIndex"),
)
if mibBuilder.loadTexts:
    mscTrkDprsStatsDiscBpEntry.setStatus("mandatory")


class _MscTrkDprsStatsDiscBpEpIndex_Type(Integer32):
    """Custom type mscTrkDprsStatsDiscBpEpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ep0", 0),
          ("ep1", 1),
          ("ep2", 2))
    )


_MscTrkDprsStatsDiscBpEpIndex_Type.__name__ = "Integer32"
_MscTrkDprsStatsDiscBpEpIndex_Object = MibTableColumn
mscTrkDprsStatsDiscBpEpIndex = _MscTrkDprsStatsDiscBpEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 10, 375, 1, 1),
    _MscTrkDprsStatsDiscBpEpIndex_Type()
)
mscTrkDprsStatsDiscBpEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkDprsStatsDiscBpEpIndex.setStatus("mandatory")


class _MscTrkDprsStatsDiscBpDpIndex_Type(Integer32):
    """Custom type mscTrkDprsStatsDiscBpDpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dp0", 0),
          ("dp1", 1),
          ("dp2", 2),
          ("dp3", 3))
    )


_MscTrkDprsStatsDiscBpDpIndex_Type.__name__ = "Integer32"
_MscTrkDprsStatsDiscBpDpIndex_Object = MibTableColumn
mscTrkDprsStatsDiscBpDpIndex = _MscTrkDprsStatsDiscBpDpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 10, 375, 1, 2),
    _MscTrkDprsStatsDiscBpDpIndex_Type()
)
mscTrkDprsStatsDiscBpDpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkDprsStatsDiscBpDpIndex.setStatus("mandatory")
_MscTrkDprsStatsDiscBpValue_Type = PassportCounter64
_MscTrkDprsStatsDiscBpValue_Object = MibTableColumn
mscTrkDprsStatsDiscBpValue = _MscTrkDprsStatsDiscBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 10, 375, 1, 3),
    _MscTrkDprsStatsDiscBpValue_Type()
)
mscTrkDprsStatsDiscBpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkDprsStatsDiscBpValue.setStatus("mandatory")
_MscTrkDprsStatsOctBpTable_Object = MibTable
mscTrkDprsStatsOctBpTable = _MscTrkDprsStatsOctBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 10, 376)
)
if mibBuilder.loadTexts:
    mscTrkDprsStatsOctBpTable.setStatus("mandatory")
_MscTrkDprsStatsOctBpEntry_Object = MibTableRow
mscTrkDprsStatsOctBpEntry = _MscTrkDprsStatsOctBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 10, 376, 1)
)
mscTrkDprsStatsOctBpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkDprsStatsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkDprsStatsOctBpEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkDprsStatsOctBpDpIndex"),
)
if mibBuilder.loadTexts:
    mscTrkDprsStatsOctBpEntry.setStatus("mandatory")


class _MscTrkDprsStatsOctBpEpIndex_Type(Integer32):
    """Custom type mscTrkDprsStatsOctBpEpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ep0", 0),
          ("ep1", 1),
          ("ep2", 2))
    )


_MscTrkDprsStatsOctBpEpIndex_Type.__name__ = "Integer32"
_MscTrkDprsStatsOctBpEpIndex_Object = MibTableColumn
mscTrkDprsStatsOctBpEpIndex = _MscTrkDprsStatsOctBpEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 10, 376, 1, 1),
    _MscTrkDprsStatsOctBpEpIndex_Type()
)
mscTrkDprsStatsOctBpEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkDprsStatsOctBpEpIndex.setStatus("mandatory")


class _MscTrkDprsStatsOctBpDpIndex_Type(Integer32):
    """Custom type mscTrkDprsStatsOctBpDpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dp0", 0),
          ("dp1", 1),
          ("dp2", 2),
          ("dp3", 3))
    )


_MscTrkDprsStatsOctBpDpIndex_Type.__name__ = "Integer32"
_MscTrkDprsStatsOctBpDpIndex_Object = MibTableColumn
mscTrkDprsStatsOctBpDpIndex = _MscTrkDprsStatsOctBpDpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 10, 376, 1, 2),
    _MscTrkDprsStatsOctBpDpIndex_Type()
)
mscTrkDprsStatsOctBpDpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkDprsStatsOctBpDpIndex.setStatus("mandatory")
_MscTrkDprsStatsOctBpValue_Type = PassportCounter64
_MscTrkDprsStatsOctBpValue_Object = MibTableColumn
mscTrkDprsStatsOctBpValue = _MscTrkDprsStatsOctBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 10, 376, 1, 3),
    _MscTrkDprsStatsOctBpValue_Type()
)
mscTrkDprsStatsOctBpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkDprsStatsOctBpValue.setStatus("mandatory")
_MscTrkAddr_ObjectIdentity = ObjectIdentity
mscTrkAddr = _MscTrkAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 11)
)
_MscTrkAddrRowStatusTable_Object = MibTable
mscTrkAddrRowStatusTable = _MscTrkAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 11, 1)
)
if mibBuilder.loadTexts:
    mscTrkAddrRowStatusTable.setStatus("mandatory")
_MscTrkAddrRowStatusEntry_Object = MibTableRow
mscTrkAddrRowStatusEntry = _MscTrkAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 11, 1, 1)
)
mscTrkAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkAddrAddressIndex"),
)
if mibBuilder.loadTexts:
    mscTrkAddrRowStatusEntry.setStatus("mandatory")
_MscTrkAddrRowStatus_Type = RowStatus
_MscTrkAddrRowStatus_Object = MibTableColumn
mscTrkAddrRowStatus = _MscTrkAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 11, 1, 1, 1),
    _MscTrkAddrRowStatus_Type()
)
mscTrkAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkAddrRowStatus.setStatus("mandatory")
_MscTrkAddrComponentName_Type = DisplayString
_MscTrkAddrComponentName_Object = MibTableColumn
mscTrkAddrComponentName = _MscTrkAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 11, 1, 1, 2),
    _MscTrkAddrComponentName_Type()
)
mscTrkAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkAddrComponentName.setStatus("mandatory")
_MscTrkAddrStorageType_Type = StorageType
_MscTrkAddrStorageType_Object = MibTableColumn
mscTrkAddrStorageType = _MscTrkAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 11, 1, 1, 4),
    _MscTrkAddrStorageType_Type()
)
mscTrkAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkAddrStorageType.setStatus("mandatory")


class _MscTrkAddrAddressIndex_Type(AsciiStringIndex):
    """Custom type mscTrkAddrAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MscTrkAddrAddressIndex_Type.__name__ = "AsciiStringIndex"
_MscTrkAddrAddressIndex_Object = MibTableColumn
mscTrkAddrAddressIndex = _MscTrkAddrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 11, 1, 1, 10),
    _MscTrkAddrAddressIndex_Type()
)
mscTrkAddrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkAddrAddressIndex.setStatus("mandatory")
_MscTrkAddrProvTable_Object = MibTable
mscTrkAddrProvTable = _MscTrkAddrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 11, 10)
)
if mibBuilder.loadTexts:
    mscTrkAddrProvTable.setStatus("mandatory")
_MscTrkAddrProvEntry_Object = MibTableRow
mscTrkAddrProvEntry = _MscTrkAddrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 11, 10, 1)
)
mscTrkAddrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkAddrAddressIndex"),
)
if mibBuilder.loadTexts:
    mscTrkAddrProvEntry.setStatus("mandatory")


class _MscTrkAddrCost_Type(Unsigned32):
    """Custom type mscTrkAddrCost based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65435),
    )


_MscTrkAddrCost_Type.__name__ = "Unsigned32"
_MscTrkAddrCost_Object = MibTableColumn
mscTrkAddrCost = _MscTrkAddrCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 11, 10, 1, 2),
    _MscTrkAddrCost_Type()
)
mscTrkAddrCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkAddrCost.setStatus("mandatory")
_MscTrkIfEntryTable_Object = MibTable
mscTrkIfEntryTable = _MscTrkIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 100)
)
if mibBuilder.loadTexts:
    mscTrkIfEntryTable.setStatus("mandatory")
_MscTrkIfEntryEntry_Object = MibTableRow
mscTrkIfEntryEntry = _MscTrkIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 100, 1)
)
mscTrkIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
)
if mibBuilder.loadTexts:
    mscTrkIfEntryEntry.setStatus("mandatory")


class _MscTrkIfAdminStatus_Type(Integer32):
    """Custom type mscTrkIfAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscTrkIfAdminStatus_Type.__name__ = "Integer32"
_MscTrkIfAdminStatus_Object = MibTableColumn
mscTrkIfAdminStatus = _MscTrkIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 100, 1, 1),
    _MscTrkIfAdminStatus_Type()
)
mscTrkIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkIfAdminStatus.setStatus("mandatory")


class _MscTrkIfIndex_Type(InterfaceIndex):
    """Custom type mscTrkIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscTrkIfIndex_Type.__name__ = "InterfaceIndex"
_MscTrkIfIndex_Object = MibTableColumn
mscTrkIfIndex = _MscTrkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 100, 1, 2),
    _MscTrkIfIndex_Type()
)
mscTrkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkIfIndex.setStatus("mandatory")
_MscTrkProvTable_Object = MibTable
mscTrkProvTable = _MscTrkProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 101)
)
if mibBuilder.loadTexts:
    mscTrkProvTable.setStatus("mandatory")
_MscTrkProvEntry_Object = MibTableRow
mscTrkProvEntry = _MscTrkProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 101, 1)
)
mscTrkProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
)
if mibBuilder.loadTexts:
    mscTrkProvEntry.setStatus("mandatory")


class _MscTrkExpectedRemoteNodeName_Type(AsciiString):
    """Custom type mscTrkExpectedRemoteNodeName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_MscTrkExpectedRemoteNodeName_Type.__name__ = "AsciiString"
_MscTrkExpectedRemoteNodeName_Object = MibTableColumn
mscTrkExpectedRemoteNodeName = _MscTrkExpectedRemoteNodeName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 101, 1, 1),
    _MscTrkExpectedRemoteNodeName_Type()
)
mscTrkExpectedRemoteNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkExpectedRemoteNodeName.setStatus("mandatory")


class _MscTrkRemoteValidationAction_Type(Integer32):
    """Custom type mscTrkRemoteValidationAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("continue", 0),
          ("disable", 1))
    )


_MscTrkRemoteValidationAction_Type.__name__ = "Integer32"
_MscTrkRemoteValidationAction_Object = MibTableColumn
mscTrkRemoteValidationAction = _MscTrkRemoteValidationAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 101, 1, 2),
    _MscTrkRemoteValidationAction_Type()
)
mscTrkRemoteValidationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkRemoteValidationAction.setStatus("mandatory")


class _MscTrkMaximumExpectedRoundTripDelay_Type(Unsigned32):
    """Custom type mscTrkMaximumExpectedRoundTripDelay based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1500),
    )


_MscTrkMaximumExpectedRoundTripDelay_Type.__name__ = "Unsigned32"
_MscTrkMaximumExpectedRoundTripDelay_Object = MibTableColumn
mscTrkMaximumExpectedRoundTripDelay = _MscTrkMaximumExpectedRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 101, 1, 3),
    _MscTrkMaximumExpectedRoundTripDelay_Type()
)
mscTrkMaximumExpectedRoundTripDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkMaximumExpectedRoundTripDelay.setStatus("mandatory")


class _MscTrkIdleTimeOut_Type(Unsigned32):
    """Custom type mscTrkIdleTimeOut based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_MscTrkIdleTimeOut_Type.__name__ = "Unsigned32"
_MscTrkIdleTimeOut_Object = MibTableColumn
mscTrkIdleTimeOut = _MscTrkIdleTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 101, 1, 4),
    _MscTrkIdleTimeOut_Type()
)
mscTrkIdleTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkIdleTimeOut.setStatus("mandatory")
_MscTrkOverridesTable_Object = MibTable
mscTrkOverridesTable = _MscTrkOverridesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 102)
)
if mibBuilder.loadTexts:
    mscTrkOverridesTable.setStatus("mandatory")
_MscTrkOverridesEntry_Object = MibTableRow
mscTrkOverridesEntry = _MscTrkOverridesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 102, 1)
)
mscTrkOverridesEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
)
if mibBuilder.loadTexts:
    mscTrkOverridesEntry.setStatus("mandatory")


class _MscTrkOverrideTransmitSpeed_Type(Gauge32):
    """Custom type mscTrkOverrideTransmitSpeed based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1000, 4294967295),
    )


_MscTrkOverrideTransmitSpeed_Type.__name__ = "Gauge32"
_MscTrkOverrideTransmitSpeed_Object = MibTableColumn
mscTrkOverrideTransmitSpeed = _MscTrkOverrideTransmitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 102, 1, 1),
    _MscTrkOverrideTransmitSpeed_Type()
)
mscTrkOverrideTransmitSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkOverrideTransmitSpeed.setStatus("mandatory")


class _MscTrkOldOverrideRoundTripDelay_Type(Gauge32):
    """Custom type mscTrkOldOverrideRoundTripDelay based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_MscTrkOldOverrideRoundTripDelay_Type.__name__ = "Gauge32"
_MscTrkOldOverrideRoundTripDelay_Object = MibTableColumn
mscTrkOldOverrideRoundTripDelay = _MscTrkOldOverrideRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 102, 1, 2),
    _MscTrkOldOverrideRoundTripDelay_Type()
)
mscTrkOldOverrideRoundTripDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkOldOverrideRoundTripDelay.setStatus("obsolete")


class _MscTrkOverrideRoundTripUsec_Type(FixedPoint1):
    """Custom type mscTrkOverrideRoundTripUsec based on FixedPoint1"""
    defaultValue = 0

    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_MscTrkOverrideRoundTripUsec_Type.__name__ = "FixedPoint1"
_MscTrkOverrideRoundTripUsec_Object = MibTableColumn
mscTrkOverrideRoundTripUsec = _MscTrkOverrideRoundTripUsec_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 102, 1, 3),
    _MscTrkOverrideRoundTripUsec_Type()
)
mscTrkOverrideRoundTripUsec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkOverrideRoundTripUsec.setStatus("mandatory")
_MscTrkStateTable_Object = MibTable
mscTrkStateTable = _MscTrkStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 103)
)
if mibBuilder.loadTexts:
    mscTrkStateTable.setStatus("mandatory")
_MscTrkStateEntry_Object = MibTableRow
mscTrkStateEntry = _MscTrkStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 103, 1)
)
mscTrkStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
)
if mibBuilder.loadTexts:
    mscTrkStateEntry.setStatus("mandatory")


class _MscTrkAdminState_Type(Integer32):
    """Custom type mscTrkAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_MscTrkAdminState_Type.__name__ = "Integer32"
_MscTrkAdminState_Object = MibTableColumn
mscTrkAdminState = _MscTrkAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 103, 1, 1),
    _MscTrkAdminState_Type()
)
mscTrkAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkAdminState.setStatus("mandatory")


class _MscTrkOperationalState_Type(Integer32):
    """Custom type mscTrkOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MscTrkOperationalState_Type.__name__ = "Integer32"
_MscTrkOperationalState_Object = MibTableColumn
mscTrkOperationalState = _MscTrkOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 103, 1, 2),
    _MscTrkOperationalState_Type()
)
mscTrkOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkOperationalState.setStatus("mandatory")


class _MscTrkUsageState_Type(Integer32):
    """Custom type mscTrkUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_MscTrkUsageState_Type.__name__ = "Integer32"
_MscTrkUsageState_Object = MibTableColumn
mscTrkUsageState = _MscTrkUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 103, 1, 3),
    _MscTrkUsageState_Type()
)
mscTrkUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUsageState.setStatus("mandatory")


class _MscTrkAvailabilityStatus_Type(OctetString):
    """Custom type mscTrkAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscTrkAvailabilityStatus_Type.__name__ = "OctetString"
_MscTrkAvailabilityStatus_Object = MibTableColumn
mscTrkAvailabilityStatus = _MscTrkAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 103, 1, 4),
    _MscTrkAvailabilityStatus_Type()
)
mscTrkAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkAvailabilityStatus.setStatus("mandatory")


class _MscTrkProceduralStatus_Type(OctetString):
    """Custom type mscTrkProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscTrkProceduralStatus_Type.__name__ = "OctetString"
_MscTrkProceduralStatus_Object = MibTableColumn
mscTrkProceduralStatus = _MscTrkProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 103, 1, 5),
    _MscTrkProceduralStatus_Type()
)
mscTrkProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkProceduralStatus.setStatus("mandatory")


class _MscTrkControlStatus_Type(OctetString):
    """Custom type mscTrkControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscTrkControlStatus_Type.__name__ = "OctetString"
_MscTrkControlStatus_Object = MibTableColumn
mscTrkControlStatus = _MscTrkControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 103, 1, 6),
    _MscTrkControlStatus_Type()
)
mscTrkControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkControlStatus.setStatus("mandatory")


class _MscTrkAlarmStatus_Type(OctetString):
    """Custom type mscTrkAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscTrkAlarmStatus_Type.__name__ = "OctetString"
_MscTrkAlarmStatus_Object = MibTableColumn
mscTrkAlarmStatus = _MscTrkAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 103, 1, 7),
    _MscTrkAlarmStatus_Type()
)
mscTrkAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkAlarmStatus.setStatus("mandatory")


class _MscTrkStandbyStatus_Type(Integer32):
    """Custom type mscTrkStandbyStatus based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              15)
        )
    )
    namedValues = NamedValues(
        *(("coldStandby", 1),
          ("hotStandby", 0),
          ("notSet", 15),
          ("providingService", 2))
    )


_MscTrkStandbyStatus_Type.__name__ = "Integer32"
_MscTrkStandbyStatus_Object = MibTableColumn
mscTrkStandbyStatus = _MscTrkStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 103, 1, 8),
    _MscTrkStandbyStatus_Type()
)
mscTrkStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkStandbyStatus.setStatus("mandatory")


class _MscTrkUnknownStatus_Type(Integer32):
    """Custom type mscTrkUnknownStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_MscTrkUnknownStatus_Type.__name__ = "Integer32"
_MscTrkUnknownStatus_Object = MibTableColumn
mscTrkUnknownStatus = _MscTrkUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 103, 1, 9),
    _MscTrkUnknownStatus_Type()
)
mscTrkUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnknownStatus.setStatus("mandatory")
_MscTrkOperStatusTable_Object = MibTable
mscTrkOperStatusTable = _MscTrkOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 104)
)
if mibBuilder.loadTexts:
    mscTrkOperStatusTable.setStatus("mandatory")
_MscTrkOperStatusEntry_Object = MibTableRow
mscTrkOperStatusEntry = _MscTrkOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 104, 1)
)
mscTrkOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
)
if mibBuilder.loadTexts:
    mscTrkOperStatusEntry.setStatus("mandatory")


class _MscTrkSnmpOperStatus_Type(Integer32):
    """Custom type mscTrkSnmpOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscTrkSnmpOperStatus_Type.__name__ = "Integer32"
_MscTrkSnmpOperStatus_Object = MibTableColumn
mscTrkSnmpOperStatus = _MscTrkSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 104, 1, 1),
    _MscTrkSnmpOperStatus_Type()
)
mscTrkSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkSnmpOperStatus.setStatus("mandatory")
_MscTrkOperTable_Object = MibTable
mscTrkOperTable = _MscTrkOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 105)
)
if mibBuilder.loadTexts:
    mscTrkOperTable.setStatus("mandatory")
_MscTrkOperEntry_Object = MibTableRow
mscTrkOperEntry = _MscTrkOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 105, 1)
)
mscTrkOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
)
if mibBuilder.loadTexts:
    mscTrkOperEntry.setStatus("mandatory")


class _MscTrkRemoteComponentName_Type(AsciiString):
    """Custom type mscTrkRemoteComponentName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 27),
    )


_MscTrkRemoteComponentName_Type.__name__ = "AsciiString"
_MscTrkRemoteComponentName_Object = MibTableColumn
mscTrkRemoteComponentName = _MscTrkRemoteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 105, 1, 1),
    _MscTrkRemoteComponentName_Type()
)
mscTrkRemoteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkRemoteComponentName.setStatus("mandatory")
_MscTrkTransportTable_Object = MibTable
mscTrkTransportTable = _MscTrkTransportTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 106)
)
if mibBuilder.loadTexts:
    mscTrkTransportTable.setStatus("mandatory")
_MscTrkTransportEntry_Object = MibTableRow
mscTrkTransportEntry = _MscTrkTransportEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 106, 1)
)
mscTrkTransportEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
)
if mibBuilder.loadTexts:
    mscTrkTransportEntry.setStatus("mandatory")


class _MscTrkMeasuredSpeedToIf_Type(Gauge32):
    """Custom type mscTrkMeasuredSpeedToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscTrkMeasuredSpeedToIf_Type.__name__ = "Gauge32"
_MscTrkMeasuredSpeedToIf_Object = MibTableColumn
mscTrkMeasuredSpeedToIf = _MscTrkMeasuredSpeedToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 106, 1, 1),
    _MscTrkMeasuredSpeedToIf_Type()
)
mscTrkMeasuredSpeedToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkMeasuredSpeedToIf.setStatus("mandatory")


class _MscTrkMeasuredRoundTripDelay_Type(Gauge32):
    """Custom type mscTrkMeasuredRoundTripDelay based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_MscTrkMeasuredRoundTripDelay_Type.__name__ = "Gauge32"
_MscTrkMeasuredRoundTripDelay_Object = MibTableColumn
mscTrkMeasuredRoundTripDelay = _MscTrkMeasuredRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 106, 1, 2),
    _MscTrkMeasuredRoundTripDelay_Type()
)
mscTrkMeasuredRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkMeasuredRoundTripDelay.setStatus("obsolete")


class _MscTrkMaxTxUnit_Type(Gauge32):
    """Custom type mscTrkMaxTxUnit based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscTrkMaxTxUnit_Type.__name__ = "Gauge32"
_MscTrkMaxTxUnit_Object = MibTableColumn
mscTrkMaxTxUnit = _MscTrkMaxTxUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 106, 1, 3),
    _MscTrkMaxTxUnit_Type()
)
mscTrkMaxTxUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkMaxTxUnit.setStatus("mandatory")


class _MscTrkMeasuredRoundTripDelayUsec_Type(FixedPoint1):
    """Custom type mscTrkMeasuredRoundTripDelayUsec based on FixedPoint1"""
    defaultValue = 0

    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_MscTrkMeasuredRoundTripDelayUsec_Type.__name__ = "FixedPoint1"
_MscTrkMeasuredRoundTripDelayUsec_Object = MibTableColumn
mscTrkMeasuredRoundTripDelayUsec = _MscTrkMeasuredRoundTripDelayUsec_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 106, 1, 4),
    _MscTrkMeasuredRoundTripDelayUsec_Type()
)
mscTrkMeasuredRoundTripDelayUsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkMeasuredRoundTripDelayUsec.setStatus("mandatory")
_MscTrkStatsTable_Object = MibTable
mscTrkStatsTable = _MscTrkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 107)
)
if mibBuilder.loadTexts:
    mscTrkStatsTable.setStatus("mandatory")
_MscTrkStatsEntry_Object = MibTableRow
mscTrkStatsEntry = _MscTrkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 107, 1)
)
mscTrkStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
)
if mibBuilder.loadTexts:
    mscTrkStatsEntry.setStatus("mandatory")
_MscTrkAreYouThereModeEntries_Type = Counter32
_MscTrkAreYouThereModeEntries_Object = MibTableColumn
mscTrkAreYouThereModeEntries = _MscTrkAreYouThereModeEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 107, 1, 1),
    _MscTrkAreYouThereModeEntries_Type()
)
mscTrkAreYouThereModeEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkAreYouThereModeEntries.setStatus("mandatory")
_MscTrkPktFromIf_Type = PassportCounter64
_MscTrkPktFromIf_Object = MibTableColumn
mscTrkPktFromIf = _MscTrkPktFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 107, 1, 2),
    _MscTrkPktFromIf_Type()
)
mscTrkPktFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPktFromIf.setStatus("mandatory")
_MscTrkTrunkPktFromIf_Type = Counter32
_MscTrkTrunkPktFromIf_Object = MibTableColumn
mscTrkTrunkPktFromIf = _MscTrkTrunkPktFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 107, 1, 3),
    _MscTrkTrunkPktFromIf_Type()
)
mscTrkTrunkPktFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkTrunkPktFromIf.setStatus("mandatory")
_MscTrkTrunkPktToIf_Type = Counter32
_MscTrkTrunkPktToIf_Object = MibTableColumn
mscTrkTrunkPktToIf = _MscTrkTrunkPktToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 107, 1, 4),
    _MscTrkTrunkPktToIf_Type()
)
mscTrkTrunkPktToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkTrunkPktToIf.setStatus("mandatory")
_MscTrkDiscardUnforward_Type = PassportCounter64
_MscTrkDiscardUnforward_Object = MibTableColumn
mscTrkDiscardUnforward = _MscTrkDiscardUnforward_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 107, 1, 5),
    _MscTrkDiscardUnforward_Type()
)
mscTrkDiscardUnforward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkDiscardUnforward.setStatus("mandatory")
_MscTrkDiscardTrunkPktFromIf_Type = Counter32
_MscTrkDiscardTrunkPktFromIf_Object = MibTableColumn
mscTrkDiscardTrunkPktFromIf = _MscTrkDiscardTrunkPktFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 107, 1, 6),
    _MscTrkDiscardTrunkPktFromIf_Type()
)
mscTrkDiscardTrunkPktFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkDiscardTrunkPktFromIf.setStatus("mandatory")
_MscTrkIntPktFromIf_Type = PassportCounter64
_MscTrkIntPktFromIf_Object = MibTableColumn
mscTrkIntPktFromIf = _MscTrkIntPktFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 107, 1, 7),
    _MscTrkIntPktFromIf_Type()
)
mscTrkIntPktFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkIntPktFromIf.setStatus("mandatory")
_MscTrkDiscardIntUnforward_Type = PassportCounter64
_MscTrkDiscardIntUnforward_Object = MibTableColumn
mscTrkDiscardIntUnforward = _MscTrkDiscardIntUnforward_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 107, 1, 8),
    _MscTrkDiscardIntUnforward_Type()
)
mscTrkDiscardIntUnforward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkDiscardIntUnforward.setStatus("mandatory")
_MscTrkStagingAttempts_Type = Counter32
_MscTrkStagingAttempts_Object = MibTableColumn
mscTrkStagingAttempts = _MscTrkStagingAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 107, 1, 9),
    _MscTrkStagingAttempts_Type()
)
mscTrkStagingAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkStagingAttempts.setStatus("mandatory")
_MscTrkDiscardTrunkPktToIf_Type = Counter32
_MscTrkDiscardTrunkPktToIf_Object = MibTableColumn
mscTrkDiscardTrunkPktToIf = _MscTrkDiscardTrunkPktToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 107, 1, 10),
    _MscTrkDiscardTrunkPktToIf_Type()
)
mscTrkDiscardTrunkPktToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkDiscardTrunkPktToIf.setStatus("mandatory")
_MscTrkSpeedReportingTable_Object = MibTable
mscTrkSpeedReportingTable = _MscTrkSpeedReportingTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 109)
)
if mibBuilder.loadTexts:
    mscTrkSpeedReportingTable.setStatus("mandatory")
_MscTrkSpeedReportingEntry_Object = MibTableRow
mscTrkSpeedReportingEntry = _MscTrkSpeedReportingEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 109, 1)
)
mscTrkSpeedReportingEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
)
if mibBuilder.loadTexts:
    mscTrkSpeedReportingEntry.setStatus("mandatory")


class _MscTrkSpeedReportingHoldOff_Type(Unsigned32):
    """Custom type mscTrkSpeedReportingHoldOff based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1200),
    )


_MscTrkSpeedReportingHoldOff_Type.__name__ = "Unsigned32"
_MscTrkSpeedReportingHoldOff_Object = MibTableColumn
mscTrkSpeedReportingHoldOff = _MscTrkSpeedReportingHoldOff_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 109, 1, 2),
    _MscTrkSpeedReportingHoldOff_Type()
)
mscTrkSpeedReportingHoldOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkSpeedReportingHoldOff.setStatus("mandatory")


class _MscTrkLowSpeedAlarmThreshold_Type(Unsigned32):
    """Custom type mscTrkLowSpeedAlarmThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_MscTrkLowSpeedAlarmThreshold_Type.__name__ = "Unsigned32"
_MscTrkLowSpeedAlarmThreshold_Object = MibTableColumn
mscTrkLowSpeedAlarmThreshold = _MscTrkLowSpeedAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 109, 1, 3),
    _MscTrkLowSpeedAlarmThreshold_Type()
)
mscTrkLowSpeedAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkLowSpeedAlarmThreshold.setStatus("mandatory")


class _MscTrkHighSpeedAlarmThreshold_Type(Unsigned32):
    """Custom type mscTrkHighSpeedAlarmThreshold based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MscTrkHighSpeedAlarmThreshold_Type.__name__ = "Unsigned32"
_MscTrkHighSpeedAlarmThreshold_Object = MibTableColumn
mscTrkHighSpeedAlarmThreshold = _MscTrkHighSpeedAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 109, 1, 4),
    _MscTrkHighSpeedAlarmThreshold_Type()
)
mscTrkHighSpeedAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkHighSpeedAlarmThreshold.setStatus("mandatory")
_MscTrkSpdThTable_Object = MibTable
mscTrkSpdThTable = _MscTrkSpdThTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 318)
)
if mibBuilder.loadTexts:
    mscTrkSpdThTable.setStatus("mandatory")
_MscTrkSpdThEntry_Object = MibTableRow
mscTrkSpdThEntry = _MscTrkSpdThEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 318, 1)
)
mscTrkSpdThEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkSpdThValue"),
)
if mibBuilder.loadTexts:
    mscTrkSpdThEntry.setStatus("mandatory")


class _MscTrkSpdThValue_Type(Integer32):
    """Custom type mscTrkSpdThValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_MscTrkSpdThValue_Type.__name__ = "Integer32"
_MscTrkSpdThValue_Object = MibTableColumn
mscTrkSpdThValue = _MscTrkSpdThValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 318, 1, 1),
    _MscTrkSpdThValue_Type()
)
mscTrkSpdThValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkSpdThValue.setStatus("mandatory")
_MscTrkSpdThRowStatus_Type = RowStatus
_MscTrkSpdThRowStatus_Object = MibTableColumn
mscTrkSpdThRowStatus = _MscTrkSpdThRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 318, 1, 2),
    _MscTrkSpdThRowStatus_Type()
)
mscTrkSpdThRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscTrkSpdThRowStatus.setStatus("mandatory")
_MscTrkPktBpTable_Object = MibTable
mscTrkPktBpTable = _MscTrkPktBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 368)
)
if mibBuilder.loadTexts:
    mscTrkPktBpTable.setStatus("mandatory")
_MscTrkPktBpEntry_Object = MibTableRow
mscTrkPktBpEntry = _MscTrkPktBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 368, 1)
)
mscTrkPktBpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkPktBpIndex"),
)
if mibBuilder.loadTexts:
    mscTrkPktBpEntry.setStatus("mandatory")


class _MscTrkPktBpIndex_Type(Integer32):
    """Custom type mscTrkPktBpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ep0", 0),
          ("ep1", 1),
          ("ep2", 2))
    )


_MscTrkPktBpIndex_Type.__name__ = "Integer32"
_MscTrkPktBpIndex_Object = MibTableColumn
mscTrkPktBpIndex = _MscTrkPktBpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 368, 1, 1),
    _MscTrkPktBpIndex_Type()
)
mscTrkPktBpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkPktBpIndex.setStatus("mandatory")
_MscTrkPktBpValue_Type = PassportCounter64
_MscTrkPktBpValue_Object = MibTableColumn
mscTrkPktBpValue = _MscTrkPktBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 368, 1, 2),
    _MscTrkPktBpValue_Type()
)
mscTrkPktBpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPktBpValue.setStatus("mandatory")
_MscTrkDiscBpTable_Object = MibTable
mscTrkDiscBpTable = _MscTrkDiscBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 369)
)
if mibBuilder.loadTexts:
    mscTrkDiscBpTable.setStatus("mandatory")
_MscTrkDiscBpEntry_Object = MibTableRow
mscTrkDiscBpEntry = _MscTrkDiscBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 369, 1)
)
mscTrkDiscBpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkDiscBpIndex"),
)
if mibBuilder.loadTexts:
    mscTrkDiscBpEntry.setStatus("mandatory")


class _MscTrkDiscBpIndex_Type(Integer32):
    """Custom type mscTrkDiscBpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ep0", 0),
          ("ep1", 1),
          ("ep2", 2))
    )


_MscTrkDiscBpIndex_Type.__name__ = "Integer32"
_MscTrkDiscBpIndex_Object = MibTableColumn
mscTrkDiscBpIndex = _MscTrkDiscBpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 369, 1, 1),
    _MscTrkDiscBpIndex_Type()
)
mscTrkDiscBpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkDiscBpIndex.setStatus("mandatory")
_MscTrkDiscBpValue_Type = PassportCounter64
_MscTrkDiscBpValue_Object = MibTableColumn
mscTrkDiscBpValue = _MscTrkDiscBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 369, 1, 2),
    _MscTrkDiscBpValue_Type()
)
mscTrkDiscBpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkDiscBpValue.setStatus("mandatory")
_MscTrkOctBpTable_Object = MibTable
mscTrkOctBpTable = _MscTrkOctBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 370)
)
if mibBuilder.loadTexts:
    mscTrkOctBpTable.setStatus("mandatory")
_MscTrkOctBpEntry_Object = MibTableRow
mscTrkOctBpEntry = _MscTrkOctBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 370, 1)
)
mscTrkOctBpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkOctBpIndex"),
)
if mibBuilder.loadTexts:
    mscTrkOctBpEntry.setStatus("mandatory")


class _MscTrkOctBpIndex_Type(Integer32):
    """Custom type mscTrkOctBpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ep0", 0),
          ("ep1", 1),
          ("ep2", 2))
    )


_MscTrkOctBpIndex_Type.__name__ = "Integer32"
_MscTrkOctBpIndex_Object = MibTableColumn
mscTrkOctBpIndex = _MscTrkOctBpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 370, 1, 1),
    _MscTrkOctBpIndex_Type()
)
mscTrkOctBpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkOctBpIndex.setStatus("mandatory")
_MscTrkOctBpValue_Type = PassportCounter64
_MscTrkOctBpValue_Object = MibTableColumn
mscTrkOctBpValue = _MscTrkOctBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 370, 1, 2),
    _MscTrkOctBpValue_Type()
)
mscTrkOctBpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkOctBpValue.setStatus("mandatory")
_TrunksMIB_ObjectIdentity = ObjectIdentity
trunksMIB = _TrunksMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 43)
)
_TrunksGroup_ObjectIdentity = ObjectIdentity
trunksGroup = _TrunksGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 43, 1)
)
_TrunksGroupCA_ObjectIdentity = ObjectIdentity
trunksGroupCA = _TrunksGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 43, 1, 1)
)
_TrunksGroupCA02_ObjectIdentity = ObjectIdentity
trunksGroupCA02 = _TrunksGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 43, 1, 1, 3)
)
_TrunksGroupCA02A_ObjectIdentity = ObjectIdentity
trunksGroupCA02A = _TrunksGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 43, 1, 1, 3, 2)
)
_TrunksCapabilities_ObjectIdentity = ObjectIdentity
trunksCapabilities = _TrunksCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 43, 3)
)
_TrunksCapabilitiesCA_ObjectIdentity = ObjectIdentity
trunksCapabilitiesCA = _TrunksCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 43, 3, 1)
)
_TrunksCapabilitiesCA02_ObjectIdentity = ObjectIdentity
trunksCapabilitiesCA02 = _TrunksCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 43, 3, 1, 3)
)
_TrunksCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
trunksCapabilitiesCA02A = _TrunksCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 43, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-TrunksMIB",
    **{"mscTrk": mscTrk,
       "mscTrkRowStatusTable": mscTrkRowStatusTable,
       "mscTrkRowStatusEntry": mscTrkRowStatusEntry,
       "mscTrkRowStatus": mscTrkRowStatus,
       "mscTrkComponentName": mscTrkComponentName,
       "mscTrkStorageType": mscTrkStorageType,
       "mscTrkIndex": mscTrkIndex,
       "mscTrkPorsStats": mscTrkPorsStats,
       "mscTrkPorsStatsRowStatusTable": mscTrkPorsStatsRowStatusTable,
       "mscTrkPorsStatsRowStatusEntry": mscTrkPorsStatsRowStatusEntry,
       "mscTrkPorsStatsRowStatus": mscTrkPorsStatsRowStatus,
       "mscTrkPorsStatsComponentName": mscTrkPorsStatsComponentName,
       "mscTrkPorsStatsStorageType": mscTrkPorsStatsStorageType,
       "mscTrkPorsStatsIndex": mscTrkPorsStatsIndex,
       "mscTrkPorsStatsOperTable": mscTrkPorsStatsOperTable,
       "mscTrkPorsStatsOperEntry": mscTrkPorsStatsOperEntry,
       "mscTrkPorsStatsPorsNormPktFromIf": mscTrkPorsStatsPorsNormPktFromIf,
       "mscTrkPorsStatsPorsNormDiscUnforwardFromIf": mscTrkPorsStatsPorsNormDiscUnforwardFromIf,
       "mscTrkPorsStatsPorsNormOctetFromIf": mscTrkPorsStatsPorsNormOctetFromIf,
       "mscTrkPorsStatsPorsIntPktFromIf": mscTrkPorsStatsPorsIntPktFromIf,
       "mscTrkPorsStatsPorsIntDiscUnforwardFromIf": mscTrkPorsStatsPorsIntDiscUnforwardFromIf,
       "mscTrkPorsStatsPorsIntOctetFromIf": mscTrkPorsStatsPorsIntOctetFromIf,
       "mscTrkPorsStatsPktBpTable": mscTrkPorsStatsPktBpTable,
       "mscTrkPorsStatsPktBpEntry": mscTrkPorsStatsPktBpEntry,
       "mscTrkPorsStatsPktBpEpIndex": mscTrkPorsStatsPktBpEpIndex,
       "mscTrkPorsStatsPktBpDpIndex": mscTrkPorsStatsPktBpDpIndex,
       "mscTrkPorsStatsPktBpValue": mscTrkPorsStatsPktBpValue,
       "mscTrkPorsStatsDiscBpTable": mscTrkPorsStatsDiscBpTable,
       "mscTrkPorsStatsDiscBpEntry": mscTrkPorsStatsDiscBpEntry,
       "mscTrkPorsStatsDiscBpEpIndex": mscTrkPorsStatsDiscBpEpIndex,
       "mscTrkPorsStatsDiscBpDpIndex": mscTrkPorsStatsDiscBpDpIndex,
       "mscTrkPorsStatsDiscBpValue": mscTrkPorsStatsDiscBpValue,
       "mscTrkPorsStatsOctBpTable": mscTrkPorsStatsOctBpTable,
       "mscTrkPorsStatsOctBpEntry": mscTrkPorsStatsOctBpEntry,
       "mscTrkPorsStatsOctBpEpIndex": mscTrkPorsStatsOctBpEpIndex,
       "mscTrkPorsStatsOctBpDpIndex": mscTrkPorsStatsOctBpDpIndex,
       "mscTrkPorsStatsOctBpValue": mscTrkPorsStatsOctBpValue,
       "mscTrkFwdStats": mscTrkFwdStats,
       "mscTrkFwdStatsRowStatusTable": mscTrkFwdStatsRowStatusTable,
       "mscTrkFwdStatsRowStatusEntry": mscTrkFwdStatsRowStatusEntry,
       "mscTrkFwdStatsRowStatus": mscTrkFwdStatsRowStatus,
       "mscTrkFwdStatsComponentName": mscTrkFwdStatsComponentName,
       "mscTrkFwdStatsStorageType": mscTrkFwdStatsStorageType,
       "mscTrkFwdStatsIndex": mscTrkFwdStatsIndex,
       "mscTrkFwdStatsOperTable": mscTrkFwdStatsOperTable,
       "mscTrkFwdStatsOperEntry": mscTrkFwdStatsOperEntry,
       "mscTrkFwdStatsFwdPktFromIf": mscTrkFwdStatsFwdPktFromIf,
       "mscTrkFwdStatsFwdDiscUnforwardFromIf": mscTrkFwdStatsFwdDiscUnforwardFromIf,
       "mscTrkFwdStatsFwdOctetFromIf": mscTrkFwdStatsFwdOctetFromIf,
       "mscTrkVnsStats": mscTrkVnsStats,
       "mscTrkVnsStatsRowStatusTable": mscTrkVnsStatsRowStatusTable,
       "mscTrkVnsStatsRowStatusEntry": mscTrkVnsStatsRowStatusEntry,
       "mscTrkVnsStatsRowStatus": mscTrkVnsStatsRowStatus,
       "mscTrkVnsStatsComponentName": mscTrkVnsStatsComponentName,
       "mscTrkVnsStatsStorageType": mscTrkVnsStatsStorageType,
       "mscTrkVnsStatsIndex": mscTrkVnsStatsIndex,
       "mscTrkVnsStatsOperTable": mscTrkVnsStatsOperTable,
       "mscTrkVnsStatsOperEntry": mscTrkVnsStatsOperEntry,
       "mscTrkVnsStatsVnsPktFromIf": mscTrkVnsStatsVnsPktFromIf,
       "mscTrkVnsStatsVnsDiscUnforwardFromIf": mscTrkVnsStatsVnsDiscUnforwardFromIf,
       "mscTrkVnsStatsVnsOctetFromIf": mscTrkVnsStatsVnsOctetFromIf,
       "mscTrkVnsStatsPktBpTable": mscTrkVnsStatsPktBpTable,
       "mscTrkVnsStatsPktBpEntry": mscTrkVnsStatsPktBpEntry,
       "mscTrkVnsStatsPktBpEpIndex": mscTrkVnsStatsPktBpEpIndex,
       "mscTrkVnsStatsPktBpDpIndex": mscTrkVnsStatsPktBpDpIndex,
       "mscTrkVnsStatsPktBpValue": mscTrkVnsStatsPktBpValue,
       "mscTrkVnsStatsDiscBpTable": mscTrkVnsStatsDiscBpTable,
       "mscTrkVnsStatsDiscBpEntry": mscTrkVnsStatsDiscBpEntry,
       "mscTrkVnsStatsDiscBpEpIndex": mscTrkVnsStatsDiscBpEpIndex,
       "mscTrkVnsStatsDiscBpDpIndex": mscTrkVnsStatsDiscBpDpIndex,
       "mscTrkVnsStatsDiscBpValue": mscTrkVnsStatsDiscBpValue,
       "mscTrkVnsStatsOctBpTable": mscTrkVnsStatsOctBpTable,
       "mscTrkVnsStatsOctBpEntry": mscTrkVnsStatsOctBpEntry,
       "mscTrkVnsStatsOctBpEpIndex": mscTrkVnsStatsOctBpEpIndex,
       "mscTrkVnsStatsOctBpDpIndex": mscTrkVnsStatsOctBpDpIndex,
       "mscTrkVnsStatsOctBpValue": mscTrkVnsStatsOctBpValue,
       "mscTrkDprsStats": mscTrkDprsStats,
       "mscTrkDprsStatsRowStatusTable": mscTrkDprsStatsRowStatusTable,
       "mscTrkDprsStatsRowStatusEntry": mscTrkDprsStatsRowStatusEntry,
       "mscTrkDprsStatsRowStatus": mscTrkDprsStatsRowStatus,
       "mscTrkDprsStatsComponentName": mscTrkDprsStatsComponentName,
       "mscTrkDprsStatsStorageType": mscTrkDprsStatsStorageType,
       "mscTrkDprsStatsIndex": mscTrkDprsStatsIndex,
       "mscTrkDprsStatsPktBpTable": mscTrkDprsStatsPktBpTable,
       "mscTrkDprsStatsPktBpEntry": mscTrkDprsStatsPktBpEntry,
       "mscTrkDprsStatsPktBpEpIndex": mscTrkDprsStatsPktBpEpIndex,
       "mscTrkDprsStatsPktBpDpIndex": mscTrkDprsStatsPktBpDpIndex,
       "mscTrkDprsStatsPktBpValue": mscTrkDprsStatsPktBpValue,
       "mscTrkDprsStatsDiscBpTable": mscTrkDprsStatsDiscBpTable,
       "mscTrkDprsStatsDiscBpEntry": mscTrkDprsStatsDiscBpEntry,
       "mscTrkDprsStatsDiscBpEpIndex": mscTrkDprsStatsDiscBpEpIndex,
       "mscTrkDprsStatsDiscBpDpIndex": mscTrkDprsStatsDiscBpDpIndex,
       "mscTrkDprsStatsDiscBpValue": mscTrkDprsStatsDiscBpValue,
       "mscTrkDprsStatsOctBpTable": mscTrkDprsStatsOctBpTable,
       "mscTrkDprsStatsOctBpEntry": mscTrkDprsStatsOctBpEntry,
       "mscTrkDprsStatsOctBpEpIndex": mscTrkDprsStatsOctBpEpIndex,
       "mscTrkDprsStatsOctBpDpIndex": mscTrkDprsStatsOctBpDpIndex,
       "mscTrkDprsStatsOctBpValue": mscTrkDprsStatsOctBpValue,
       "mscTrkAddr": mscTrkAddr,
       "mscTrkAddrRowStatusTable": mscTrkAddrRowStatusTable,
       "mscTrkAddrRowStatusEntry": mscTrkAddrRowStatusEntry,
       "mscTrkAddrRowStatus": mscTrkAddrRowStatus,
       "mscTrkAddrComponentName": mscTrkAddrComponentName,
       "mscTrkAddrStorageType": mscTrkAddrStorageType,
       "mscTrkAddrAddressIndex": mscTrkAddrAddressIndex,
       "mscTrkAddrProvTable": mscTrkAddrProvTable,
       "mscTrkAddrProvEntry": mscTrkAddrProvEntry,
       "mscTrkAddrCost": mscTrkAddrCost,
       "mscTrkIfEntryTable": mscTrkIfEntryTable,
       "mscTrkIfEntryEntry": mscTrkIfEntryEntry,
       "mscTrkIfAdminStatus": mscTrkIfAdminStatus,
       "mscTrkIfIndex": mscTrkIfIndex,
       "mscTrkProvTable": mscTrkProvTable,
       "mscTrkProvEntry": mscTrkProvEntry,
       "mscTrkExpectedRemoteNodeName": mscTrkExpectedRemoteNodeName,
       "mscTrkRemoteValidationAction": mscTrkRemoteValidationAction,
       "mscTrkMaximumExpectedRoundTripDelay": mscTrkMaximumExpectedRoundTripDelay,
       "mscTrkIdleTimeOut": mscTrkIdleTimeOut,
       "mscTrkOverridesTable": mscTrkOverridesTable,
       "mscTrkOverridesEntry": mscTrkOverridesEntry,
       "mscTrkOverrideTransmitSpeed": mscTrkOverrideTransmitSpeed,
       "mscTrkOldOverrideRoundTripDelay": mscTrkOldOverrideRoundTripDelay,
       "mscTrkOverrideRoundTripUsec": mscTrkOverrideRoundTripUsec,
       "mscTrkStateTable": mscTrkStateTable,
       "mscTrkStateEntry": mscTrkStateEntry,
       "mscTrkAdminState": mscTrkAdminState,
       "mscTrkOperationalState": mscTrkOperationalState,
       "mscTrkUsageState": mscTrkUsageState,
       "mscTrkAvailabilityStatus": mscTrkAvailabilityStatus,
       "mscTrkProceduralStatus": mscTrkProceduralStatus,
       "mscTrkControlStatus": mscTrkControlStatus,
       "mscTrkAlarmStatus": mscTrkAlarmStatus,
       "mscTrkStandbyStatus": mscTrkStandbyStatus,
       "mscTrkUnknownStatus": mscTrkUnknownStatus,
       "mscTrkOperStatusTable": mscTrkOperStatusTable,
       "mscTrkOperStatusEntry": mscTrkOperStatusEntry,
       "mscTrkSnmpOperStatus": mscTrkSnmpOperStatus,
       "mscTrkOperTable": mscTrkOperTable,
       "mscTrkOperEntry": mscTrkOperEntry,
       "mscTrkRemoteComponentName": mscTrkRemoteComponentName,
       "mscTrkTransportTable": mscTrkTransportTable,
       "mscTrkTransportEntry": mscTrkTransportEntry,
       "mscTrkMeasuredSpeedToIf": mscTrkMeasuredSpeedToIf,
       "mscTrkMeasuredRoundTripDelay": mscTrkMeasuredRoundTripDelay,
       "mscTrkMaxTxUnit": mscTrkMaxTxUnit,
       "mscTrkMeasuredRoundTripDelayUsec": mscTrkMeasuredRoundTripDelayUsec,
       "mscTrkStatsTable": mscTrkStatsTable,
       "mscTrkStatsEntry": mscTrkStatsEntry,
       "mscTrkAreYouThereModeEntries": mscTrkAreYouThereModeEntries,
       "mscTrkPktFromIf": mscTrkPktFromIf,
       "mscTrkTrunkPktFromIf": mscTrkTrunkPktFromIf,
       "mscTrkTrunkPktToIf": mscTrkTrunkPktToIf,
       "mscTrkDiscardUnforward": mscTrkDiscardUnforward,
       "mscTrkDiscardTrunkPktFromIf": mscTrkDiscardTrunkPktFromIf,
       "mscTrkIntPktFromIf": mscTrkIntPktFromIf,
       "mscTrkDiscardIntUnforward": mscTrkDiscardIntUnforward,
       "mscTrkStagingAttempts": mscTrkStagingAttempts,
       "mscTrkDiscardTrunkPktToIf": mscTrkDiscardTrunkPktToIf,
       "mscTrkSpeedReportingTable": mscTrkSpeedReportingTable,
       "mscTrkSpeedReportingEntry": mscTrkSpeedReportingEntry,
       "mscTrkSpeedReportingHoldOff": mscTrkSpeedReportingHoldOff,
       "mscTrkLowSpeedAlarmThreshold": mscTrkLowSpeedAlarmThreshold,
       "mscTrkHighSpeedAlarmThreshold": mscTrkHighSpeedAlarmThreshold,
       "mscTrkSpdThTable": mscTrkSpdThTable,
       "mscTrkSpdThEntry": mscTrkSpdThEntry,
       "mscTrkSpdThValue": mscTrkSpdThValue,
       "mscTrkSpdThRowStatus": mscTrkSpdThRowStatus,
       "mscTrkPktBpTable": mscTrkPktBpTable,
       "mscTrkPktBpEntry": mscTrkPktBpEntry,
       "mscTrkPktBpIndex": mscTrkPktBpIndex,
       "mscTrkPktBpValue": mscTrkPktBpValue,
       "mscTrkDiscBpTable": mscTrkDiscBpTable,
       "mscTrkDiscBpEntry": mscTrkDiscBpEntry,
       "mscTrkDiscBpIndex": mscTrkDiscBpIndex,
       "mscTrkDiscBpValue": mscTrkDiscBpValue,
       "mscTrkOctBpTable": mscTrkOctBpTable,
       "mscTrkOctBpEntry": mscTrkOctBpEntry,
       "mscTrkOctBpIndex": mscTrkOctBpIndex,
       "mscTrkOctBpValue": mscTrkOctBpValue,
       "trunksMIB": trunksMIB,
       "trunksGroup": trunksGroup,
       "trunksGroupCA": trunksGroupCA,
       "trunksGroupCA02": trunksGroupCA02,
       "trunksGroupCA02A": trunksGroupCA02A,
       "trunksCapabilities": trunksCapabilities,
       "trunksCapabilitiesCA": trunksCapabilitiesCA,
       "trunksCapabilitiesCA02": trunksCapabilitiesCA02,
       "trunksCapabilitiesCA02A": trunksCapabilitiesCA02A}
)
