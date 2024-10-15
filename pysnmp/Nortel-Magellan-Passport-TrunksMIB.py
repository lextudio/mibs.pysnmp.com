# SNMP MIB module (Nortel-Magellan-Passport-TrunksMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-TrunksMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:22 2024
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
 PassportCounter64,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "InterfaceIndex",
    "PassportCounter64",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 FixedPoint1,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "FixedPoint1",
    "NonReplicated")

(components,
 passportMIBs) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "components",
    "passportMIBs")

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

_Trk_ObjectIdentity = ObjectIdentity
trk = _Trk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60)
)
_TrkRowStatusTable_Object = MibTable
trkRowStatusTable = _TrkRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 1)
)
if mibBuilder.loadTexts:
    trkRowStatusTable.setStatus("mandatory")
_TrkRowStatusEntry_Object = MibTableRow
trkRowStatusEntry = _TrkRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 1, 1)
)
trkRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
)
if mibBuilder.loadTexts:
    trkRowStatusEntry.setStatus("mandatory")
_TrkRowStatus_Type = RowStatus
_TrkRowStatus_Object = MibTableColumn
trkRowStatus = _TrkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 1, 1, 1),
    _TrkRowStatus_Type()
)
trkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkRowStatus.setStatus("mandatory")
_TrkComponentName_Type = DisplayString
_TrkComponentName_Object = MibTableColumn
trkComponentName = _TrkComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 1, 1, 2),
    _TrkComponentName_Type()
)
trkComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkComponentName.setStatus("mandatory")
_TrkStorageType_Type = StorageType
_TrkStorageType_Object = MibTableColumn
trkStorageType = _TrkStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 1, 1, 4),
    _TrkStorageType_Type()
)
trkStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkStorageType.setStatus("mandatory")


class _TrkIndex_Type(Integer32):
    """Custom type trkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TrkIndex_Type.__name__ = "Integer32"
_TrkIndex_Object = MibTableColumn
trkIndex = _TrkIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 1, 1, 10),
    _TrkIndex_Type()
)
trkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkIndex.setStatus("mandatory")
_TrkPorsStats_ObjectIdentity = ObjectIdentity
trkPorsStats = _TrkPorsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6)
)
_TrkPorsStatsRowStatusTable_Object = MibTable
trkPorsStatsRowStatusTable = _TrkPorsStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 1)
)
if mibBuilder.loadTexts:
    trkPorsStatsRowStatusTable.setStatus("mandatory")
_TrkPorsStatsRowStatusEntry_Object = MibTableRow
trkPorsStatsRowStatusEntry = _TrkPorsStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 1, 1)
)
trkPorsStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkPorsStatsIndex"),
)
if mibBuilder.loadTexts:
    trkPorsStatsRowStatusEntry.setStatus("mandatory")
_TrkPorsStatsRowStatus_Type = RowStatus
_TrkPorsStatsRowStatus_Object = MibTableColumn
trkPorsStatsRowStatus = _TrkPorsStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 1, 1, 1),
    _TrkPorsStatsRowStatus_Type()
)
trkPorsStatsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPorsStatsRowStatus.setStatus("mandatory")
_TrkPorsStatsComponentName_Type = DisplayString
_TrkPorsStatsComponentName_Object = MibTableColumn
trkPorsStatsComponentName = _TrkPorsStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 1, 1, 2),
    _TrkPorsStatsComponentName_Type()
)
trkPorsStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPorsStatsComponentName.setStatus("mandatory")
_TrkPorsStatsStorageType_Type = StorageType
_TrkPorsStatsStorageType_Object = MibTableColumn
trkPorsStatsStorageType = _TrkPorsStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 1, 1, 4),
    _TrkPorsStatsStorageType_Type()
)
trkPorsStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPorsStatsStorageType.setStatus("mandatory")
_TrkPorsStatsIndex_Type = NonReplicated
_TrkPorsStatsIndex_Object = MibTableColumn
trkPorsStatsIndex = _TrkPorsStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 1, 1, 10),
    _TrkPorsStatsIndex_Type()
)
trkPorsStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkPorsStatsIndex.setStatus("mandatory")
_TrkPorsStatsOperTable_Object = MibTable
trkPorsStatsOperTable = _TrkPorsStatsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 10)
)
if mibBuilder.loadTexts:
    trkPorsStatsOperTable.setStatus("mandatory")
_TrkPorsStatsOperEntry_Object = MibTableRow
trkPorsStatsOperEntry = _TrkPorsStatsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 10, 1)
)
trkPorsStatsOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkPorsStatsIndex"),
)
if mibBuilder.loadTexts:
    trkPorsStatsOperEntry.setStatus("mandatory")
_TrkPorsStatsPorsNormPktFromIf_Type = PassportCounter64
_TrkPorsStatsPorsNormPktFromIf_Object = MibTableColumn
trkPorsStatsPorsNormPktFromIf = _TrkPorsStatsPorsNormPktFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 10, 1, 1),
    _TrkPorsStatsPorsNormPktFromIf_Type()
)
trkPorsStatsPorsNormPktFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPorsStatsPorsNormPktFromIf.setStatus("mandatory")
_TrkPorsStatsPorsNormDiscUnforwardFromIf_Type = PassportCounter64
_TrkPorsStatsPorsNormDiscUnforwardFromIf_Object = MibTableColumn
trkPorsStatsPorsNormDiscUnforwardFromIf = _TrkPorsStatsPorsNormDiscUnforwardFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 10, 1, 2),
    _TrkPorsStatsPorsNormDiscUnforwardFromIf_Type()
)
trkPorsStatsPorsNormDiscUnforwardFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPorsStatsPorsNormDiscUnforwardFromIf.setStatus("mandatory")
_TrkPorsStatsPorsNormOctetFromIf_Type = PassportCounter64
_TrkPorsStatsPorsNormOctetFromIf_Object = MibTableColumn
trkPorsStatsPorsNormOctetFromIf = _TrkPorsStatsPorsNormOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 10, 1, 3),
    _TrkPorsStatsPorsNormOctetFromIf_Type()
)
trkPorsStatsPorsNormOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPorsStatsPorsNormOctetFromIf.setStatus("mandatory")
_TrkPorsStatsPorsIntPktFromIf_Type = PassportCounter64
_TrkPorsStatsPorsIntPktFromIf_Object = MibTableColumn
trkPorsStatsPorsIntPktFromIf = _TrkPorsStatsPorsIntPktFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 10, 1, 4),
    _TrkPorsStatsPorsIntPktFromIf_Type()
)
trkPorsStatsPorsIntPktFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPorsStatsPorsIntPktFromIf.setStatus("mandatory")
_TrkPorsStatsPorsIntDiscUnforwardFromIf_Type = PassportCounter64
_TrkPorsStatsPorsIntDiscUnforwardFromIf_Object = MibTableColumn
trkPorsStatsPorsIntDiscUnforwardFromIf = _TrkPorsStatsPorsIntDiscUnforwardFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 10, 1, 5),
    _TrkPorsStatsPorsIntDiscUnforwardFromIf_Type()
)
trkPorsStatsPorsIntDiscUnforwardFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPorsStatsPorsIntDiscUnforwardFromIf.setStatus("mandatory")
_TrkPorsStatsPorsIntOctetFromIf_Type = PassportCounter64
_TrkPorsStatsPorsIntOctetFromIf_Object = MibTableColumn
trkPorsStatsPorsIntOctetFromIf = _TrkPorsStatsPorsIntOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 10, 1, 6),
    _TrkPorsStatsPorsIntOctetFromIf_Type()
)
trkPorsStatsPorsIntOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPorsStatsPorsIntOctetFromIf.setStatus("mandatory")
_TrkPorsStatsPktBpTable_Object = MibTable
trkPorsStatsPktBpTable = _TrkPorsStatsPktBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 371)
)
if mibBuilder.loadTexts:
    trkPorsStatsPktBpTable.setStatus("mandatory")
_TrkPorsStatsPktBpEntry_Object = MibTableRow
trkPorsStatsPktBpEntry = _TrkPorsStatsPktBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 371, 1)
)
trkPorsStatsPktBpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkPorsStatsIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkPorsStatsPktBpEpIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkPorsStatsPktBpDpIndex"),
)
if mibBuilder.loadTexts:
    trkPorsStatsPktBpEntry.setStatus("mandatory")


class _TrkPorsStatsPktBpEpIndex_Type(Integer32):
    """Custom type trkPorsStatsPktBpEpIndex based on Integer32"""
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


_TrkPorsStatsPktBpEpIndex_Type.__name__ = "Integer32"
_TrkPorsStatsPktBpEpIndex_Object = MibTableColumn
trkPorsStatsPktBpEpIndex = _TrkPorsStatsPktBpEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 371, 1, 1),
    _TrkPorsStatsPktBpEpIndex_Type()
)
trkPorsStatsPktBpEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkPorsStatsPktBpEpIndex.setStatus("mandatory")


class _TrkPorsStatsPktBpDpIndex_Type(Integer32):
    """Custom type trkPorsStatsPktBpDpIndex based on Integer32"""
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


_TrkPorsStatsPktBpDpIndex_Type.__name__ = "Integer32"
_TrkPorsStatsPktBpDpIndex_Object = MibTableColumn
trkPorsStatsPktBpDpIndex = _TrkPorsStatsPktBpDpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 371, 1, 2),
    _TrkPorsStatsPktBpDpIndex_Type()
)
trkPorsStatsPktBpDpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkPorsStatsPktBpDpIndex.setStatus("mandatory")
_TrkPorsStatsPktBpValue_Type = PassportCounter64
_TrkPorsStatsPktBpValue_Object = MibTableColumn
trkPorsStatsPktBpValue = _TrkPorsStatsPktBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 371, 1, 3),
    _TrkPorsStatsPktBpValue_Type()
)
trkPorsStatsPktBpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPorsStatsPktBpValue.setStatus("mandatory")
_TrkPorsStatsDiscBpTable_Object = MibTable
trkPorsStatsDiscBpTable = _TrkPorsStatsDiscBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 372)
)
if mibBuilder.loadTexts:
    trkPorsStatsDiscBpTable.setStatus("mandatory")
_TrkPorsStatsDiscBpEntry_Object = MibTableRow
trkPorsStatsDiscBpEntry = _TrkPorsStatsDiscBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 372, 1)
)
trkPorsStatsDiscBpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkPorsStatsIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkPorsStatsDiscBpEpIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkPorsStatsDiscBpDpIndex"),
)
if mibBuilder.loadTexts:
    trkPorsStatsDiscBpEntry.setStatus("mandatory")


class _TrkPorsStatsDiscBpEpIndex_Type(Integer32):
    """Custom type trkPorsStatsDiscBpEpIndex based on Integer32"""
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


_TrkPorsStatsDiscBpEpIndex_Type.__name__ = "Integer32"
_TrkPorsStatsDiscBpEpIndex_Object = MibTableColumn
trkPorsStatsDiscBpEpIndex = _TrkPorsStatsDiscBpEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 372, 1, 1),
    _TrkPorsStatsDiscBpEpIndex_Type()
)
trkPorsStatsDiscBpEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkPorsStatsDiscBpEpIndex.setStatus("mandatory")


class _TrkPorsStatsDiscBpDpIndex_Type(Integer32):
    """Custom type trkPorsStatsDiscBpDpIndex based on Integer32"""
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


_TrkPorsStatsDiscBpDpIndex_Type.__name__ = "Integer32"
_TrkPorsStatsDiscBpDpIndex_Object = MibTableColumn
trkPorsStatsDiscBpDpIndex = _TrkPorsStatsDiscBpDpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 372, 1, 2),
    _TrkPorsStatsDiscBpDpIndex_Type()
)
trkPorsStatsDiscBpDpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkPorsStatsDiscBpDpIndex.setStatus("mandatory")
_TrkPorsStatsDiscBpValue_Type = PassportCounter64
_TrkPorsStatsDiscBpValue_Object = MibTableColumn
trkPorsStatsDiscBpValue = _TrkPorsStatsDiscBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 372, 1, 3),
    _TrkPorsStatsDiscBpValue_Type()
)
trkPorsStatsDiscBpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPorsStatsDiscBpValue.setStatus("mandatory")
_TrkPorsStatsOctBpTable_Object = MibTable
trkPorsStatsOctBpTable = _TrkPorsStatsOctBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 373)
)
if mibBuilder.loadTexts:
    trkPorsStatsOctBpTable.setStatus("mandatory")
_TrkPorsStatsOctBpEntry_Object = MibTableRow
trkPorsStatsOctBpEntry = _TrkPorsStatsOctBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 373, 1)
)
trkPorsStatsOctBpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkPorsStatsIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkPorsStatsOctBpEpIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkPorsStatsOctBpDpIndex"),
)
if mibBuilder.loadTexts:
    trkPorsStatsOctBpEntry.setStatus("mandatory")


class _TrkPorsStatsOctBpEpIndex_Type(Integer32):
    """Custom type trkPorsStatsOctBpEpIndex based on Integer32"""
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


_TrkPorsStatsOctBpEpIndex_Type.__name__ = "Integer32"
_TrkPorsStatsOctBpEpIndex_Object = MibTableColumn
trkPorsStatsOctBpEpIndex = _TrkPorsStatsOctBpEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 373, 1, 1),
    _TrkPorsStatsOctBpEpIndex_Type()
)
trkPorsStatsOctBpEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkPorsStatsOctBpEpIndex.setStatus("mandatory")


class _TrkPorsStatsOctBpDpIndex_Type(Integer32):
    """Custom type trkPorsStatsOctBpDpIndex based on Integer32"""
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


_TrkPorsStatsOctBpDpIndex_Type.__name__ = "Integer32"
_TrkPorsStatsOctBpDpIndex_Object = MibTableColumn
trkPorsStatsOctBpDpIndex = _TrkPorsStatsOctBpDpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 373, 1, 2),
    _TrkPorsStatsOctBpDpIndex_Type()
)
trkPorsStatsOctBpDpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkPorsStatsOctBpDpIndex.setStatus("mandatory")
_TrkPorsStatsOctBpValue_Type = PassportCounter64
_TrkPorsStatsOctBpValue_Object = MibTableColumn
trkPorsStatsOctBpValue = _TrkPorsStatsOctBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 6, 373, 1, 3),
    _TrkPorsStatsOctBpValue_Type()
)
trkPorsStatsOctBpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPorsStatsOctBpValue.setStatus("mandatory")
_TrkFwdStats_ObjectIdentity = ObjectIdentity
trkFwdStats = _TrkFwdStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 7)
)
_TrkFwdStatsRowStatusTable_Object = MibTable
trkFwdStatsRowStatusTable = _TrkFwdStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 7, 1)
)
if mibBuilder.loadTexts:
    trkFwdStatsRowStatusTable.setStatus("mandatory")
_TrkFwdStatsRowStatusEntry_Object = MibTableRow
trkFwdStatsRowStatusEntry = _TrkFwdStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 7, 1, 1)
)
trkFwdStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkFwdStatsIndex"),
)
if mibBuilder.loadTexts:
    trkFwdStatsRowStatusEntry.setStatus("mandatory")
_TrkFwdStatsRowStatus_Type = RowStatus
_TrkFwdStatsRowStatus_Object = MibTableColumn
trkFwdStatsRowStatus = _TrkFwdStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 7, 1, 1, 1),
    _TrkFwdStatsRowStatus_Type()
)
trkFwdStatsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkFwdStatsRowStatus.setStatus("mandatory")
_TrkFwdStatsComponentName_Type = DisplayString
_TrkFwdStatsComponentName_Object = MibTableColumn
trkFwdStatsComponentName = _TrkFwdStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 7, 1, 1, 2),
    _TrkFwdStatsComponentName_Type()
)
trkFwdStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkFwdStatsComponentName.setStatus("mandatory")
_TrkFwdStatsStorageType_Type = StorageType
_TrkFwdStatsStorageType_Object = MibTableColumn
trkFwdStatsStorageType = _TrkFwdStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 7, 1, 1, 4),
    _TrkFwdStatsStorageType_Type()
)
trkFwdStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkFwdStatsStorageType.setStatus("mandatory")
_TrkFwdStatsIndex_Type = NonReplicated
_TrkFwdStatsIndex_Object = MibTableColumn
trkFwdStatsIndex = _TrkFwdStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 7, 1, 1, 10),
    _TrkFwdStatsIndex_Type()
)
trkFwdStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkFwdStatsIndex.setStatus("mandatory")
_TrkFwdStatsOperTable_Object = MibTable
trkFwdStatsOperTable = _TrkFwdStatsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 7, 10)
)
if mibBuilder.loadTexts:
    trkFwdStatsOperTable.setStatus("mandatory")
_TrkFwdStatsOperEntry_Object = MibTableRow
trkFwdStatsOperEntry = _TrkFwdStatsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 7, 10, 1)
)
trkFwdStatsOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkFwdStatsIndex"),
)
if mibBuilder.loadTexts:
    trkFwdStatsOperEntry.setStatus("mandatory")
_TrkFwdStatsFwdPktFromIf_Type = PassportCounter64
_TrkFwdStatsFwdPktFromIf_Object = MibTableColumn
trkFwdStatsFwdPktFromIf = _TrkFwdStatsFwdPktFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 7, 10, 1, 1),
    _TrkFwdStatsFwdPktFromIf_Type()
)
trkFwdStatsFwdPktFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkFwdStatsFwdPktFromIf.setStatus("mandatory")
_TrkFwdStatsFwdDiscUnforwardFromIf_Type = PassportCounter64
_TrkFwdStatsFwdDiscUnforwardFromIf_Object = MibTableColumn
trkFwdStatsFwdDiscUnforwardFromIf = _TrkFwdStatsFwdDiscUnforwardFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 7, 10, 1, 2),
    _TrkFwdStatsFwdDiscUnforwardFromIf_Type()
)
trkFwdStatsFwdDiscUnforwardFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkFwdStatsFwdDiscUnforwardFromIf.setStatus("mandatory")
_TrkFwdStatsFwdOctetFromIf_Type = PassportCounter64
_TrkFwdStatsFwdOctetFromIf_Object = MibTableColumn
trkFwdStatsFwdOctetFromIf = _TrkFwdStatsFwdOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 7, 10, 1, 3),
    _TrkFwdStatsFwdOctetFromIf_Type()
)
trkFwdStatsFwdOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkFwdStatsFwdOctetFromIf.setStatus("mandatory")
_TrkVnsStats_ObjectIdentity = ObjectIdentity
trkVnsStats = _TrkVnsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8)
)
_TrkVnsStatsRowStatusTable_Object = MibTable
trkVnsStatsRowStatusTable = _TrkVnsStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 1)
)
if mibBuilder.loadTexts:
    trkVnsStatsRowStatusTable.setStatus("mandatory")
_TrkVnsStatsRowStatusEntry_Object = MibTableRow
trkVnsStatsRowStatusEntry = _TrkVnsStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 1, 1)
)
trkVnsStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkVnsStatsIndex"),
)
if mibBuilder.loadTexts:
    trkVnsStatsRowStatusEntry.setStatus("mandatory")
_TrkVnsStatsRowStatus_Type = RowStatus
_TrkVnsStatsRowStatus_Object = MibTableColumn
trkVnsStatsRowStatus = _TrkVnsStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 1, 1, 1),
    _TrkVnsStatsRowStatus_Type()
)
trkVnsStatsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkVnsStatsRowStatus.setStatus("mandatory")
_TrkVnsStatsComponentName_Type = DisplayString
_TrkVnsStatsComponentName_Object = MibTableColumn
trkVnsStatsComponentName = _TrkVnsStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 1, 1, 2),
    _TrkVnsStatsComponentName_Type()
)
trkVnsStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkVnsStatsComponentName.setStatus("mandatory")
_TrkVnsStatsStorageType_Type = StorageType
_TrkVnsStatsStorageType_Object = MibTableColumn
trkVnsStatsStorageType = _TrkVnsStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 1, 1, 4),
    _TrkVnsStatsStorageType_Type()
)
trkVnsStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkVnsStatsStorageType.setStatus("mandatory")
_TrkVnsStatsIndex_Type = NonReplicated
_TrkVnsStatsIndex_Object = MibTableColumn
trkVnsStatsIndex = _TrkVnsStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 1, 1, 10),
    _TrkVnsStatsIndex_Type()
)
trkVnsStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkVnsStatsIndex.setStatus("mandatory")
_TrkVnsStatsOperTable_Object = MibTable
trkVnsStatsOperTable = _TrkVnsStatsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 10)
)
if mibBuilder.loadTexts:
    trkVnsStatsOperTable.setStatus("mandatory")
_TrkVnsStatsOperEntry_Object = MibTableRow
trkVnsStatsOperEntry = _TrkVnsStatsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 10, 1)
)
trkVnsStatsOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkVnsStatsIndex"),
)
if mibBuilder.loadTexts:
    trkVnsStatsOperEntry.setStatus("mandatory")
_TrkVnsStatsVnsPktFromIf_Type = PassportCounter64
_TrkVnsStatsVnsPktFromIf_Object = MibTableColumn
trkVnsStatsVnsPktFromIf = _TrkVnsStatsVnsPktFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 10, 1, 1),
    _TrkVnsStatsVnsPktFromIf_Type()
)
trkVnsStatsVnsPktFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkVnsStatsVnsPktFromIf.setStatus("mandatory")
_TrkVnsStatsVnsDiscUnforwardFromIf_Type = PassportCounter64
_TrkVnsStatsVnsDiscUnforwardFromIf_Object = MibTableColumn
trkVnsStatsVnsDiscUnforwardFromIf = _TrkVnsStatsVnsDiscUnforwardFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 10, 1, 2),
    _TrkVnsStatsVnsDiscUnforwardFromIf_Type()
)
trkVnsStatsVnsDiscUnforwardFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkVnsStatsVnsDiscUnforwardFromIf.setStatus("mandatory")
_TrkVnsStatsVnsOctetFromIf_Type = PassportCounter64
_TrkVnsStatsVnsOctetFromIf_Object = MibTableColumn
trkVnsStatsVnsOctetFromIf = _TrkVnsStatsVnsOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 10, 1, 3),
    _TrkVnsStatsVnsOctetFromIf_Type()
)
trkVnsStatsVnsOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkVnsStatsVnsOctetFromIf.setStatus("mandatory")
_TrkVnsStatsPktBpTable_Object = MibTable
trkVnsStatsPktBpTable = _TrkVnsStatsPktBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 377)
)
if mibBuilder.loadTexts:
    trkVnsStatsPktBpTable.setStatus("mandatory")
_TrkVnsStatsPktBpEntry_Object = MibTableRow
trkVnsStatsPktBpEntry = _TrkVnsStatsPktBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 377, 1)
)
trkVnsStatsPktBpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkVnsStatsIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkVnsStatsPktBpEpIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkVnsStatsPktBpDpIndex"),
)
if mibBuilder.loadTexts:
    trkVnsStatsPktBpEntry.setStatus("mandatory")


class _TrkVnsStatsPktBpEpIndex_Type(Integer32):
    """Custom type trkVnsStatsPktBpEpIndex based on Integer32"""
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


_TrkVnsStatsPktBpEpIndex_Type.__name__ = "Integer32"
_TrkVnsStatsPktBpEpIndex_Object = MibTableColumn
trkVnsStatsPktBpEpIndex = _TrkVnsStatsPktBpEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 377, 1, 1),
    _TrkVnsStatsPktBpEpIndex_Type()
)
trkVnsStatsPktBpEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkVnsStatsPktBpEpIndex.setStatus("mandatory")


class _TrkVnsStatsPktBpDpIndex_Type(Integer32):
    """Custom type trkVnsStatsPktBpDpIndex based on Integer32"""
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


_TrkVnsStatsPktBpDpIndex_Type.__name__ = "Integer32"
_TrkVnsStatsPktBpDpIndex_Object = MibTableColumn
trkVnsStatsPktBpDpIndex = _TrkVnsStatsPktBpDpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 377, 1, 2),
    _TrkVnsStatsPktBpDpIndex_Type()
)
trkVnsStatsPktBpDpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkVnsStatsPktBpDpIndex.setStatus("mandatory")
_TrkVnsStatsPktBpValue_Type = PassportCounter64
_TrkVnsStatsPktBpValue_Object = MibTableColumn
trkVnsStatsPktBpValue = _TrkVnsStatsPktBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 377, 1, 3),
    _TrkVnsStatsPktBpValue_Type()
)
trkVnsStatsPktBpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkVnsStatsPktBpValue.setStatus("mandatory")
_TrkVnsStatsDiscBpTable_Object = MibTable
trkVnsStatsDiscBpTable = _TrkVnsStatsDiscBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 378)
)
if mibBuilder.loadTexts:
    trkVnsStatsDiscBpTable.setStatus("mandatory")
_TrkVnsStatsDiscBpEntry_Object = MibTableRow
trkVnsStatsDiscBpEntry = _TrkVnsStatsDiscBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 378, 1)
)
trkVnsStatsDiscBpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkVnsStatsIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkVnsStatsDiscBpEpIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkVnsStatsDiscBpDpIndex"),
)
if mibBuilder.loadTexts:
    trkVnsStatsDiscBpEntry.setStatus("mandatory")


class _TrkVnsStatsDiscBpEpIndex_Type(Integer32):
    """Custom type trkVnsStatsDiscBpEpIndex based on Integer32"""
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


_TrkVnsStatsDiscBpEpIndex_Type.__name__ = "Integer32"
_TrkVnsStatsDiscBpEpIndex_Object = MibTableColumn
trkVnsStatsDiscBpEpIndex = _TrkVnsStatsDiscBpEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 378, 1, 1),
    _TrkVnsStatsDiscBpEpIndex_Type()
)
trkVnsStatsDiscBpEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkVnsStatsDiscBpEpIndex.setStatus("mandatory")


class _TrkVnsStatsDiscBpDpIndex_Type(Integer32):
    """Custom type trkVnsStatsDiscBpDpIndex based on Integer32"""
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


_TrkVnsStatsDiscBpDpIndex_Type.__name__ = "Integer32"
_TrkVnsStatsDiscBpDpIndex_Object = MibTableColumn
trkVnsStatsDiscBpDpIndex = _TrkVnsStatsDiscBpDpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 378, 1, 2),
    _TrkVnsStatsDiscBpDpIndex_Type()
)
trkVnsStatsDiscBpDpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkVnsStatsDiscBpDpIndex.setStatus("mandatory")
_TrkVnsStatsDiscBpValue_Type = PassportCounter64
_TrkVnsStatsDiscBpValue_Object = MibTableColumn
trkVnsStatsDiscBpValue = _TrkVnsStatsDiscBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 378, 1, 3),
    _TrkVnsStatsDiscBpValue_Type()
)
trkVnsStatsDiscBpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkVnsStatsDiscBpValue.setStatus("mandatory")
_TrkVnsStatsOctBpTable_Object = MibTable
trkVnsStatsOctBpTable = _TrkVnsStatsOctBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 379)
)
if mibBuilder.loadTexts:
    trkVnsStatsOctBpTable.setStatus("mandatory")
_TrkVnsStatsOctBpEntry_Object = MibTableRow
trkVnsStatsOctBpEntry = _TrkVnsStatsOctBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 379, 1)
)
trkVnsStatsOctBpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkVnsStatsIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkVnsStatsOctBpEpIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkVnsStatsOctBpDpIndex"),
)
if mibBuilder.loadTexts:
    trkVnsStatsOctBpEntry.setStatus("mandatory")


class _TrkVnsStatsOctBpEpIndex_Type(Integer32):
    """Custom type trkVnsStatsOctBpEpIndex based on Integer32"""
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


_TrkVnsStatsOctBpEpIndex_Type.__name__ = "Integer32"
_TrkVnsStatsOctBpEpIndex_Object = MibTableColumn
trkVnsStatsOctBpEpIndex = _TrkVnsStatsOctBpEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 379, 1, 1),
    _TrkVnsStatsOctBpEpIndex_Type()
)
trkVnsStatsOctBpEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkVnsStatsOctBpEpIndex.setStatus("mandatory")


class _TrkVnsStatsOctBpDpIndex_Type(Integer32):
    """Custom type trkVnsStatsOctBpDpIndex based on Integer32"""
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


_TrkVnsStatsOctBpDpIndex_Type.__name__ = "Integer32"
_TrkVnsStatsOctBpDpIndex_Object = MibTableColumn
trkVnsStatsOctBpDpIndex = _TrkVnsStatsOctBpDpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 379, 1, 2),
    _TrkVnsStatsOctBpDpIndex_Type()
)
trkVnsStatsOctBpDpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkVnsStatsOctBpDpIndex.setStatus("mandatory")
_TrkVnsStatsOctBpValue_Type = PassportCounter64
_TrkVnsStatsOctBpValue_Object = MibTableColumn
trkVnsStatsOctBpValue = _TrkVnsStatsOctBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 8, 379, 1, 3),
    _TrkVnsStatsOctBpValue_Type()
)
trkVnsStatsOctBpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkVnsStatsOctBpValue.setStatus("mandatory")
_TrkDprsStats_ObjectIdentity = ObjectIdentity
trkDprsStats = _TrkDprsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 10)
)
_TrkDprsStatsRowStatusTable_Object = MibTable
trkDprsStatsRowStatusTable = _TrkDprsStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 10, 1)
)
if mibBuilder.loadTexts:
    trkDprsStatsRowStatusTable.setStatus("mandatory")
_TrkDprsStatsRowStatusEntry_Object = MibTableRow
trkDprsStatsRowStatusEntry = _TrkDprsStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 10, 1, 1)
)
trkDprsStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkDprsStatsIndex"),
)
if mibBuilder.loadTexts:
    trkDprsStatsRowStatusEntry.setStatus("mandatory")
_TrkDprsStatsRowStatus_Type = RowStatus
_TrkDprsStatsRowStatus_Object = MibTableColumn
trkDprsStatsRowStatus = _TrkDprsStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 10, 1, 1, 1),
    _TrkDprsStatsRowStatus_Type()
)
trkDprsStatsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkDprsStatsRowStatus.setStatus("mandatory")
_TrkDprsStatsComponentName_Type = DisplayString
_TrkDprsStatsComponentName_Object = MibTableColumn
trkDprsStatsComponentName = _TrkDprsStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 10, 1, 1, 2),
    _TrkDprsStatsComponentName_Type()
)
trkDprsStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkDprsStatsComponentName.setStatus("mandatory")
_TrkDprsStatsStorageType_Type = StorageType
_TrkDprsStatsStorageType_Object = MibTableColumn
trkDprsStatsStorageType = _TrkDprsStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 10, 1, 1, 4),
    _TrkDprsStatsStorageType_Type()
)
trkDprsStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkDprsStatsStorageType.setStatus("mandatory")
_TrkDprsStatsIndex_Type = NonReplicated
_TrkDprsStatsIndex_Object = MibTableColumn
trkDprsStatsIndex = _TrkDprsStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 10, 1, 1, 10),
    _TrkDprsStatsIndex_Type()
)
trkDprsStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkDprsStatsIndex.setStatus("mandatory")
_TrkDprsStatsPktBpTable_Object = MibTable
trkDprsStatsPktBpTable = _TrkDprsStatsPktBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 10, 374)
)
if mibBuilder.loadTexts:
    trkDprsStatsPktBpTable.setStatus("mandatory")
_TrkDprsStatsPktBpEntry_Object = MibTableRow
trkDprsStatsPktBpEntry = _TrkDprsStatsPktBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 10, 374, 1)
)
trkDprsStatsPktBpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkDprsStatsIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkDprsStatsPktBpEpIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkDprsStatsPktBpDpIndex"),
)
if mibBuilder.loadTexts:
    trkDprsStatsPktBpEntry.setStatus("mandatory")


class _TrkDprsStatsPktBpEpIndex_Type(Integer32):
    """Custom type trkDprsStatsPktBpEpIndex based on Integer32"""
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


_TrkDprsStatsPktBpEpIndex_Type.__name__ = "Integer32"
_TrkDprsStatsPktBpEpIndex_Object = MibTableColumn
trkDprsStatsPktBpEpIndex = _TrkDprsStatsPktBpEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 10, 374, 1, 1),
    _TrkDprsStatsPktBpEpIndex_Type()
)
trkDprsStatsPktBpEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkDprsStatsPktBpEpIndex.setStatus("mandatory")


class _TrkDprsStatsPktBpDpIndex_Type(Integer32):
    """Custom type trkDprsStatsPktBpDpIndex based on Integer32"""
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


_TrkDprsStatsPktBpDpIndex_Type.__name__ = "Integer32"
_TrkDprsStatsPktBpDpIndex_Object = MibTableColumn
trkDprsStatsPktBpDpIndex = _TrkDprsStatsPktBpDpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 10, 374, 1, 2),
    _TrkDprsStatsPktBpDpIndex_Type()
)
trkDprsStatsPktBpDpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkDprsStatsPktBpDpIndex.setStatus("mandatory")
_TrkDprsStatsPktBpValue_Type = PassportCounter64
_TrkDprsStatsPktBpValue_Object = MibTableColumn
trkDprsStatsPktBpValue = _TrkDprsStatsPktBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 10, 374, 1, 3),
    _TrkDprsStatsPktBpValue_Type()
)
trkDprsStatsPktBpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkDprsStatsPktBpValue.setStatus("mandatory")
_TrkDprsStatsDiscBpTable_Object = MibTable
trkDprsStatsDiscBpTable = _TrkDprsStatsDiscBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 10, 375)
)
if mibBuilder.loadTexts:
    trkDprsStatsDiscBpTable.setStatus("mandatory")
_TrkDprsStatsDiscBpEntry_Object = MibTableRow
trkDprsStatsDiscBpEntry = _TrkDprsStatsDiscBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 10, 375, 1)
)
trkDprsStatsDiscBpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkDprsStatsIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkDprsStatsDiscBpEpIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkDprsStatsDiscBpDpIndex"),
)
if mibBuilder.loadTexts:
    trkDprsStatsDiscBpEntry.setStatus("mandatory")


class _TrkDprsStatsDiscBpEpIndex_Type(Integer32):
    """Custom type trkDprsStatsDiscBpEpIndex based on Integer32"""
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


_TrkDprsStatsDiscBpEpIndex_Type.__name__ = "Integer32"
_TrkDprsStatsDiscBpEpIndex_Object = MibTableColumn
trkDprsStatsDiscBpEpIndex = _TrkDprsStatsDiscBpEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 10, 375, 1, 1),
    _TrkDprsStatsDiscBpEpIndex_Type()
)
trkDprsStatsDiscBpEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkDprsStatsDiscBpEpIndex.setStatus("mandatory")


class _TrkDprsStatsDiscBpDpIndex_Type(Integer32):
    """Custom type trkDprsStatsDiscBpDpIndex based on Integer32"""
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


_TrkDprsStatsDiscBpDpIndex_Type.__name__ = "Integer32"
_TrkDprsStatsDiscBpDpIndex_Object = MibTableColumn
trkDprsStatsDiscBpDpIndex = _TrkDprsStatsDiscBpDpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 10, 375, 1, 2),
    _TrkDprsStatsDiscBpDpIndex_Type()
)
trkDprsStatsDiscBpDpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkDprsStatsDiscBpDpIndex.setStatus("mandatory")
_TrkDprsStatsDiscBpValue_Type = PassportCounter64
_TrkDprsStatsDiscBpValue_Object = MibTableColumn
trkDprsStatsDiscBpValue = _TrkDprsStatsDiscBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 10, 375, 1, 3),
    _TrkDprsStatsDiscBpValue_Type()
)
trkDprsStatsDiscBpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkDprsStatsDiscBpValue.setStatus("mandatory")
_TrkDprsStatsOctBpTable_Object = MibTable
trkDprsStatsOctBpTable = _TrkDprsStatsOctBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 10, 376)
)
if mibBuilder.loadTexts:
    trkDprsStatsOctBpTable.setStatus("mandatory")
_TrkDprsStatsOctBpEntry_Object = MibTableRow
trkDprsStatsOctBpEntry = _TrkDprsStatsOctBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 10, 376, 1)
)
trkDprsStatsOctBpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkDprsStatsIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkDprsStatsOctBpEpIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkDprsStatsOctBpDpIndex"),
)
if mibBuilder.loadTexts:
    trkDprsStatsOctBpEntry.setStatus("mandatory")


class _TrkDprsStatsOctBpEpIndex_Type(Integer32):
    """Custom type trkDprsStatsOctBpEpIndex based on Integer32"""
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


_TrkDprsStatsOctBpEpIndex_Type.__name__ = "Integer32"
_TrkDprsStatsOctBpEpIndex_Object = MibTableColumn
trkDprsStatsOctBpEpIndex = _TrkDprsStatsOctBpEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 10, 376, 1, 1),
    _TrkDprsStatsOctBpEpIndex_Type()
)
trkDprsStatsOctBpEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkDprsStatsOctBpEpIndex.setStatus("mandatory")


class _TrkDprsStatsOctBpDpIndex_Type(Integer32):
    """Custom type trkDprsStatsOctBpDpIndex based on Integer32"""
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


_TrkDprsStatsOctBpDpIndex_Type.__name__ = "Integer32"
_TrkDprsStatsOctBpDpIndex_Object = MibTableColumn
trkDprsStatsOctBpDpIndex = _TrkDprsStatsOctBpDpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 10, 376, 1, 2),
    _TrkDprsStatsOctBpDpIndex_Type()
)
trkDprsStatsOctBpDpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkDprsStatsOctBpDpIndex.setStatus("mandatory")
_TrkDprsStatsOctBpValue_Type = PassportCounter64
_TrkDprsStatsOctBpValue_Object = MibTableColumn
trkDprsStatsOctBpValue = _TrkDprsStatsOctBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 10, 376, 1, 3),
    _TrkDprsStatsOctBpValue_Type()
)
trkDprsStatsOctBpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkDprsStatsOctBpValue.setStatus("mandatory")
_TrkIfEntryTable_Object = MibTable
trkIfEntryTable = _TrkIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 100)
)
if mibBuilder.loadTexts:
    trkIfEntryTable.setStatus("mandatory")
_TrkIfEntryEntry_Object = MibTableRow
trkIfEntryEntry = _TrkIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 100, 1)
)
trkIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
)
if mibBuilder.loadTexts:
    trkIfEntryEntry.setStatus("mandatory")


class _TrkIfAdminStatus_Type(Integer32):
    """Custom type trkIfAdminStatus based on Integer32"""
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


_TrkIfAdminStatus_Type.__name__ = "Integer32"
_TrkIfAdminStatus_Object = MibTableColumn
trkIfAdminStatus = _TrkIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 100, 1, 1),
    _TrkIfAdminStatus_Type()
)
trkIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkIfAdminStatus.setStatus("mandatory")


class _TrkIfIndex_Type(InterfaceIndex):
    """Custom type trkIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TrkIfIndex_Type.__name__ = "InterfaceIndex"
_TrkIfIndex_Object = MibTableColumn
trkIfIndex = _TrkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 100, 1, 2),
    _TrkIfIndex_Type()
)
trkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkIfIndex.setStatus("mandatory")
_TrkProvTable_Object = MibTable
trkProvTable = _TrkProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 101)
)
if mibBuilder.loadTexts:
    trkProvTable.setStatus("mandatory")
_TrkProvEntry_Object = MibTableRow
trkProvEntry = _TrkProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 101, 1)
)
trkProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
)
if mibBuilder.loadTexts:
    trkProvEntry.setStatus("mandatory")


class _TrkExpectedRemoteNodeName_Type(AsciiString):
    """Custom type trkExpectedRemoteNodeName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_TrkExpectedRemoteNodeName_Type.__name__ = "AsciiString"
_TrkExpectedRemoteNodeName_Object = MibTableColumn
trkExpectedRemoteNodeName = _TrkExpectedRemoteNodeName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 101, 1, 1),
    _TrkExpectedRemoteNodeName_Type()
)
trkExpectedRemoteNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkExpectedRemoteNodeName.setStatus("mandatory")


class _TrkRemoteValidationAction_Type(Integer32):
    """Custom type trkRemoteValidationAction based on Integer32"""
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


_TrkRemoteValidationAction_Type.__name__ = "Integer32"
_TrkRemoteValidationAction_Object = MibTableColumn
trkRemoteValidationAction = _TrkRemoteValidationAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 101, 1, 2),
    _TrkRemoteValidationAction_Type()
)
trkRemoteValidationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkRemoteValidationAction.setStatus("mandatory")


class _TrkMaximumExpectedRoundTripDelay_Type(Unsigned32):
    """Custom type trkMaximumExpectedRoundTripDelay based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1500),
    )


_TrkMaximumExpectedRoundTripDelay_Type.__name__ = "Unsigned32"
_TrkMaximumExpectedRoundTripDelay_Object = MibTableColumn
trkMaximumExpectedRoundTripDelay = _TrkMaximumExpectedRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 101, 1, 3),
    _TrkMaximumExpectedRoundTripDelay_Type()
)
trkMaximumExpectedRoundTripDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkMaximumExpectedRoundTripDelay.setStatus("mandatory")


class _TrkIdleTimeOut_Type(Unsigned32):
    """Custom type trkIdleTimeOut based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_TrkIdleTimeOut_Type.__name__ = "Unsigned32"
_TrkIdleTimeOut_Object = MibTableColumn
trkIdleTimeOut = _TrkIdleTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 101, 1, 4),
    _TrkIdleTimeOut_Type()
)
trkIdleTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkIdleTimeOut.setStatus("mandatory")
_TrkOverridesTable_Object = MibTable
trkOverridesTable = _TrkOverridesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 102)
)
if mibBuilder.loadTexts:
    trkOverridesTable.setStatus("mandatory")
_TrkOverridesEntry_Object = MibTableRow
trkOverridesEntry = _TrkOverridesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 102, 1)
)
trkOverridesEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
)
if mibBuilder.loadTexts:
    trkOverridesEntry.setStatus("mandatory")


class _TrkOverrideTransmitSpeed_Type(Gauge32):
    """Custom type trkOverrideTransmitSpeed based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1000, 4294967295),
    )


_TrkOverrideTransmitSpeed_Type.__name__ = "Gauge32"
_TrkOverrideTransmitSpeed_Object = MibTableColumn
trkOverrideTransmitSpeed = _TrkOverrideTransmitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 102, 1, 1),
    _TrkOverrideTransmitSpeed_Type()
)
trkOverrideTransmitSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkOverrideTransmitSpeed.setStatus("mandatory")


class _TrkOldOverrideRoundTripDelay_Type(Gauge32):
    """Custom type trkOldOverrideRoundTripDelay based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_TrkOldOverrideRoundTripDelay_Type.__name__ = "Gauge32"
_TrkOldOverrideRoundTripDelay_Object = MibTableColumn
trkOldOverrideRoundTripDelay = _TrkOldOverrideRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 102, 1, 2),
    _TrkOldOverrideRoundTripDelay_Type()
)
trkOldOverrideRoundTripDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkOldOverrideRoundTripDelay.setStatus("obsolete")


class _TrkOverrideRoundTripUsec_Type(FixedPoint1):
    """Custom type trkOverrideRoundTripUsec based on FixedPoint1"""
    defaultValue = 0

    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_TrkOverrideRoundTripUsec_Type.__name__ = "FixedPoint1"
_TrkOverrideRoundTripUsec_Object = MibTableColumn
trkOverrideRoundTripUsec = _TrkOverrideRoundTripUsec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 102, 1, 3),
    _TrkOverrideRoundTripUsec_Type()
)
trkOverrideRoundTripUsec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkOverrideRoundTripUsec.setStatus("mandatory")
_TrkStateTable_Object = MibTable
trkStateTable = _TrkStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 103)
)
if mibBuilder.loadTexts:
    trkStateTable.setStatus("mandatory")
_TrkStateEntry_Object = MibTableRow
trkStateEntry = _TrkStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 103, 1)
)
trkStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
)
if mibBuilder.loadTexts:
    trkStateEntry.setStatus("mandatory")


class _TrkAdminState_Type(Integer32):
    """Custom type trkAdminState based on Integer32"""
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


_TrkAdminState_Type.__name__ = "Integer32"
_TrkAdminState_Object = MibTableColumn
trkAdminState = _TrkAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 103, 1, 1),
    _TrkAdminState_Type()
)
trkAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkAdminState.setStatus("mandatory")


class _TrkOperationalState_Type(Integer32):
    """Custom type trkOperationalState based on Integer32"""
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


_TrkOperationalState_Type.__name__ = "Integer32"
_TrkOperationalState_Object = MibTableColumn
trkOperationalState = _TrkOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 103, 1, 2),
    _TrkOperationalState_Type()
)
trkOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkOperationalState.setStatus("mandatory")


class _TrkUsageState_Type(Integer32):
    """Custom type trkUsageState based on Integer32"""
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


_TrkUsageState_Type.__name__ = "Integer32"
_TrkUsageState_Object = MibTableColumn
trkUsageState = _TrkUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 103, 1, 3),
    _TrkUsageState_Type()
)
trkUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUsageState.setStatus("mandatory")


class _TrkAvailabilityStatus_Type(OctetString):
    """Custom type trkAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_TrkAvailabilityStatus_Type.__name__ = "OctetString"
_TrkAvailabilityStatus_Object = MibTableColumn
trkAvailabilityStatus = _TrkAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 103, 1, 4),
    _TrkAvailabilityStatus_Type()
)
trkAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkAvailabilityStatus.setStatus("mandatory")


class _TrkProceduralStatus_Type(OctetString):
    """Custom type trkProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_TrkProceduralStatus_Type.__name__ = "OctetString"
_TrkProceduralStatus_Object = MibTableColumn
trkProceduralStatus = _TrkProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 103, 1, 5),
    _TrkProceduralStatus_Type()
)
trkProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkProceduralStatus.setStatus("mandatory")


class _TrkControlStatus_Type(OctetString):
    """Custom type trkControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_TrkControlStatus_Type.__name__ = "OctetString"
_TrkControlStatus_Object = MibTableColumn
trkControlStatus = _TrkControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 103, 1, 6),
    _TrkControlStatus_Type()
)
trkControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkControlStatus.setStatus("mandatory")


class _TrkAlarmStatus_Type(OctetString):
    """Custom type trkAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_TrkAlarmStatus_Type.__name__ = "OctetString"
_TrkAlarmStatus_Object = MibTableColumn
trkAlarmStatus = _TrkAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 103, 1, 7),
    _TrkAlarmStatus_Type()
)
trkAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkAlarmStatus.setStatus("mandatory")


class _TrkStandbyStatus_Type(Integer32):
    """Custom type trkStandbyStatus based on Integer32"""
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


_TrkStandbyStatus_Type.__name__ = "Integer32"
_TrkStandbyStatus_Object = MibTableColumn
trkStandbyStatus = _TrkStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 103, 1, 8),
    _TrkStandbyStatus_Type()
)
trkStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkStandbyStatus.setStatus("mandatory")


class _TrkUnknownStatus_Type(Integer32):
    """Custom type trkUnknownStatus based on Integer32"""
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


_TrkUnknownStatus_Type.__name__ = "Integer32"
_TrkUnknownStatus_Object = MibTableColumn
trkUnknownStatus = _TrkUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 103, 1, 9),
    _TrkUnknownStatus_Type()
)
trkUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnknownStatus.setStatus("mandatory")
_TrkOperStatusTable_Object = MibTable
trkOperStatusTable = _TrkOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 104)
)
if mibBuilder.loadTexts:
    trkOperStatusTable.setStatus("mandatory")
_TrkOperStatusEntry_Object = MibTableRow
trkOperStatusEntry = _TrkOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 104, 1)
)
trkOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
)
if mibBuilder.loadTexts:
    trkOperStatusEntry.setStatus("mandatory")


class _TrkSnmpOperStatus_Type(Integer32):
    """Custom type trkSnmpOperStatus based on Integer32"""
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


_TrkSnmpOperStatus_Type.__name__ = "Integer32"
_TrkSnmpOperStatus_Object = MibTableColumn
trkSnmpOperStatus = _TrkSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 104, 1, 1),
    _TrkSnmpOperStatus_Type()
)
trkSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkSnmpOperStatus.setStatus("mandatory")
_TrkOperTable_Object = MibTable
trkOperTable = _TrkOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 105)
)
if mibBuilder.loadTexts:
    trkOperTable.setStatus("mandatory")
_TrkOperEntry_Object = MibTableRow
trkOperEntry = _TrkOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 105, 1)
)
trkOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
)
if mibBuilder.loadTexts:
    trkOperEntry.setStatus("mandatory")


class _TrkRemoteComponentName_Type(AsciiString):
    """Custom type trkRemoteComponentName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 27),
    )


_TrkRemoteComponentName_Type.__name__ = "AsciiString"
_TrkRemoteComponentName_Object = MibTableColumn
trkRemoteComponentName = _TrkRemoteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 105, 1, 1),
    _TrkRemoteComponentName_Type()
)
trkRemoteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkRemoteComponentName.setStatus("mandatory")
_TrkTransportTable_Object = MibTable
trkTransportTable = _TrkTransportTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 106)
)
if mibBuilder.loadTexts:
    trkTransportTable.setStatus("mandatory")
_TrkTransportEntry_Object = MibTableRow
trkTransportEntry = _TrkTransportEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 106, 1)
)
trkTransportEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
)
if mibBuilder.loadTexts:
    trkTransportEntry.setStatus("mandatory")


class _TrkMeasuredSpeedToIf_Type(Gauge32):
    """Custom type trkMeasuredSpeedToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TrkMeasuredSpeedToIf_Type.__name__ = "Gauge32"
_TrkMeasuredSpeedToIf_Object = MibTableColumn
trkMeasuredSpeedToIf = _TrkMeasuredSpeedToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 106, 1, 1),
    _TrkMeasuredSpeedToIf_Type()
)
trkMeasuredSpeedToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkMeasuredSpeedToIf.setStatus("mandatory")


class _TrkMeasuredRoundTripDelay_Type(Gauge32):
    """Custom type trkMeasuredRoundTripDelay based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_TrkMeasuredRoundTripDelay_Type.__name__ = "Gauge32"
_TrkMeasuredRoundTripDelay_Object = MibTableColumn
trkMeasuredRoundTripDelay = _TrkMeasuredRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 106, 1, 2),
    _TrkMeasuredRoundTripDelay_Type()
)
trkMeasuredRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkMeasuredRoundTripDelay.setStatus("obsolete")


class _TrkMaxTxUnit_Type(Gauge32):
    """Custom type trkMaxTxUnit based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TrkMaxTxUnit_Type.__name__ = "Gauge32"
_TrkMaxTxUnit_Object = MibTableColumn
trkMaxTxUnit = _TrkMaxTxUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 106, 1, 3),
    _TrkMaxTxUnit_Type()
)
trkMaxTxUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkMaxTxUnit.setStatus("mandatory")


class _TrkMeasuredRoundTripDelayUsec_Type(FixedPoint1):
    """Custom type trkMeasuredRoundTripDelayUsec based on FixedPoint1"""
    defaultValue = 0

    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_TrkMeasuredRoundTripDelayUsec_Type.__name__ = "FixedPoint1"
_TrkMeasuredRoundTripDelayUsec_Object = MibTableColumn
trkMeasuredRoundTripDelayUsec = _TrkMeasuredRoundTripDelayUsec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 106, 1, 4),
    _TrkMeasuredRoundTripDelayUsec_Type()
)
trkMeasuredRoundTripDelayUsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkMeasuredRoundTripDelayUsec.setStatus("mandatory")
_TrkStatsTable_Object = MibTable
trkStatsTable = _TrkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 107)
)
if mibBuilder.loadTexts:
    trkStatsTable.setStatus("mandatory")
_TrkStatsEntry_Object = MibTableRow
trkStatsEntry = _TrkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 107, 1)
)
trkStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
)
if mibBuilder.loadTexts:
    trkStatsEntry.setStatus("mandatory")
_TrkAreYouThereModeEntries_Type = Counter32
_TrkAreYouThereModeEntries_Object = MibTableColumn
trkAreYouThereModeEntries = _TrkAreYouThereModeEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 107, 1, 1),
    _TrkAreYouThereModeEntries_Type()
)
trkAreYouThereModeEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkAreYouThereModeEntries.setStatus("mandatory")
_TrkPktFromIf_Type = PassportCounter64
_TrkPktFromIf_Object = MibTableColumn
trkPktFromIf = _TrkPktFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 107, 1, 2),
    _TrkPktFromIf_Type()
)
trkPktFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPktFromIf.setStatus("mandatory")
_TrkTrunkPktFromIf_Type = Counter32
_TrkTrunkPktFromIf_Object = MibTableColumn
trkTrunkPktFromIf = _TrkTrunkPktFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 107, 1, 3),
    _TrkTrunkPktFromIf_Type()
)
trkTrunkPktFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkTrunkPktFromIf.setStatus("mandatory")
_TrkTrunkPktToIf_Type = Counter32
_TrkTrunkPktToIf_Object = MibTableColumn
trkTrunkPktToIf = _TrkTrunkPktToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 107, 1, 4),
    _TrkTrunkPktToIf_Type()
)
trkTrunkPktToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkTrunkPktToIf.setStatus("mandatory")
_TrkDiscardUnforward_Type = PassportCounter64
_TrkDiscardUnforward_Object = MibTableColumn
trkDiscardUnforward = _TrkDiscardUnforward_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 107, 1, 5),
    _TrkDiscardUnforward_Type()
)
trkDiscardUnforward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkDiscardUnforward.setStatus("mandatory")
_TrkDiscardTrunkPktFromIf_Type = Counter32
_TrkDiscardTrunkPktFromIf_Object = MibTableColumn
trkDiscardTrunkPktFromIf = _TrkDiscardTrunkPktFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 107, 1, 6),
    _TrkDiscardTrunkPktFromIf_Type()
)
trkDiscardTrunkPktFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkDiscardTrunkPktFromIf.setStatus("mandatory")
_TrkIntPktFromIf_Type = PassportCounter64
_TrkIntPktFromIf_Object = MibTableColumn
trkIntPktFromIf = _TrkIntPktFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 107, 1, 7),
    _TrkIntPktFromIf_Type()
)
trkIntPktFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkIntPktFromIf.setStatus("mandatory")
_TrkDiscardIntUnforward_Type = PassportCounter64
_TrkDiscardIntUnforward_Object = MibTableColumn
trkDiscardIntUnforward = _TrkDiscardIntUnforward_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 107, 1, 8),
    _TrkDiscardIntUnforward_Type()
)
trkDiscardIntUnforward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkDiscardIntUnforward.setStatus("mandatory")
_TrkStagingAttempts_Type = Counter32
_TrkStagingAttempts_Object = MibTableColumn
trkStagingAttempts = _TrkStagingAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 107, 1, 9),
    _TrkStagingAttempts_Type()
)
trkStagingAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkStagingAttempts.setStatus("mandatory")
_TrkDiscardTrunkPktToIf_Type = Counter32
_TrkDiscardTrunkPktToIf_Object = MibTableColumn
trkDiscardTrunkPktToIf = _TrkDiscardTrunkPktToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 107, 1, 10),
    _TrkDiscardTrunkPktToIf_Type()
)
trkDiscardTrunkPktToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkDiscardTrunkPktToIf.setStatus("mandatory")


class _TrkUtilization_Type(Gauge32):
    """Custom type trkUtilization based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_TrkUtilization_Type.__name__ = "Gauge32"
_TrkUtilization_Object = MibTableColumn
trkUtilization = _TrkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 107, 1, 11),
    _TrkUtilization_Type()
)
trkUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUtilization.setStatus("mandatory")
_TrkSpeedReportingTable_Object = MibTable
trkSpeedReportingTable = _TrkSpeedReportingTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 109)
)
if mibBuilder.loadTexts:
    trkSpeedReportingTable.setStatus("mandatory")
_TrkSpeedReportingEntry_Object = MibTableRow
trkSpeedReportingEntry = _TrkSpeedReportingEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 109, 1)
)
trkSpeedReportingEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
)
if mibBuilder.loadTexts:
    trkSpeedReportingEntry.setStatus("mandatory")


class _TrkSpeedReportingHoldOff_Type(Unsigned32):
    """Custom type trkSpeedReportingHoldOff based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1200),
    )


_TrkSpeedReportingHoldOff_Type.__name__ = "Unsigned32"
_TrkSpeedReportingHoldOff_Object = MibTableColumn
trkSpeedReportingHoldOff = _TrkSpeedReportingHoldOff_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 109, 1, 2),
    _TrkSpeedReportingHoldOff_Type()
)
trkSpeedReportingHoldOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkSpeedReportingHoldOff.setStatus("mandatory")


class _TrkLowSpeedAlarmThreshold_Type(Unsigned32):
    """Custom type trkLowSpeedAlarmThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_TrkLowSpeedAlarmThreshold_Type.__name__ = "Unsigned32"
_TrkLowSpeedAlarmThreshold_Object = MibTableColumn
trkLowSpeedAlarmThreshold = _TrkLowSpeedAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 109, 1, 3),
    _TrkLowSpeedAlarmThreshold_Type()
)
trkLowSpeedAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkLowSpeedAlarmThreshold.setStatus("mandatory")


class _TrkHighSpeedAlarmThreshold_Type(Unsigned32):
    """Custom type trkHighSpeedAlarmThreshold based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TrkHighSpeedAlarmThreshold_Type.__name__ = "Unsigned32"
_TrkHighSpeedAlarmThreshold_Object = MibTableColumn
trkHighSpeedAlarmThreshold = _TrkHighSpeedAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 109, 1, 4),
    _TrkHighSpeedAlarmThreshold_Type()
)
trkHighSpeedAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkHighSpeedAlarmThreshold.setStatus("mandatory")
_TrkSpdThTable_Object = MibTable
trkSpdThTable = _TrkSpdThTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 318)
)
if mibBuilder.loadTexts:
    trkSpdThTable.setStatus("mandatory")
_TrkSpdThEntry_Object = MibTableRow
trkSpdThEntry = _TrkSpdThEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 318, 1)
)
trkSpdThEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkSpdThValue"),
)
if mibBuilder.loadTexts:
    trkSpdThEntry.setStatus("mandatory")


class _TrkSpdThValue_Type(Integer32):
    """Custom type trkSpdThValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_TrkSpdThValue_Type.__name__ = "Integer32"
_TrkSpdThValue_Object = MibTableColumn
trkSpdThValue = _TrkSpdThValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 318, 1, 1),
    _TrkSpdThValue_Type()
)
trkSpdThValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkSpdThValue.setStatus("mandatory")
_TrkSpdThRowStatus_Type = RowStatus
_TrkSpdThRowStatus_Object = MibTableColumn
trkSpdThRowStatus = _TrkSpdThRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 318, 1, 2),
    _TrkSpdThRowStatus_Type()
)
trkSpdThRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    trkSpdThRowStatus.setStatus("mandatory")
_TrkPktBpTable_Object = MibTable
trkPktBpTable = _TrkPktBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 368)
)
if mibBuilder.loadTexts:
    trkPktBpTable.setStatus("mandatory")
_TrkPktBpEntry_Object = MibTableRow
trkPktBpEntry = _TrkPktBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 368, 1)
)
trkPktBpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkPktBpIndex"),
)
if mibBuilder.loadTexts:
    trkPktBpEntry.setStatus("mandatory")


class _TrkPktBpIndex_Type(Integer32):
    """Custom type trkPktBpIndex based on Integer32"""
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


_TrkPktBpIndex_Type.__name__ = "Integer32"
_TrkPktBpIndex_Object = MibTableColumn
trkPktBpIndex = _TrkPktBpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 368, 1, 1),
    _TrkPktBpIndex_Type()
)
trkPktBpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkPktBpIndex.setStatus("mandatory")
_TrkPktBpValue_Type = PassportCounter64
_TrkPktBpValue_Object = MibTableColumn
trkPktBpValue = _TrkPktBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 368, 1, 2),
    _TrkPktBpValue_Type()
)
trkPktBpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPktBpValue.setStatus("mandatory")
_TrkDiscBpTable_Object = MibTable
trkDiscBpTable = _TrkDiscBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 369)
)
if mibBuilder.loadTexts:
    trkDiscBpTable.setStatus("mandatory")
_TrkDiscBpEntry_Object = MibTableRow
trkDiscBpEntry = _TrkDiscBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 369, 1)
)
trkDiscBpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkDiscBpIndex"),
)
if mibBuilder.loadTexts:
    trkDiscBpEntry.setStatus("mandatory")


class _TrkDiscBpIndex_Type(Integer32):
    """Custom type trkDiscBpIndex based on Integer32"""
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


_TrkDiscBpIndex_Type.__name__ = "Integer32"
_TrkDiscBpIndex_Object = MibTableColumn
trkDiscBpIndex = _TrkDiscBpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 369, 1, 1),
    _TrkDiscBpIndex_Type()
)
trkDiscBpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkDiscBpIndex.setStatus("mandatory")
_TrkDiscBpValue_Type = PassportCounter64
_TrkDiscBpValue_Object = MibTableColumn
trkDiscBpValue = _TrkDiscBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 369, 1, 2),
    _TrkDiscBpValue_Type()
)
trkDiscBpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkDiscBpValue.setStatus("mandatory")
_TrkOctBpTable_Object = MibTable
trkOctBpTable = _TrkOctBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 370)
)
if mibBuilder.loadTexts:
    trkOctBpTable.setStatus("mandatory")
_TrkOctBpEntry_Object = MibTableRow
trkOctBpEntry = _TrkOctBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 370, 1)
)
trkOctBpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkOctBpIndex"),
)
if mibBuilder.loadTexts:
    trkOctBpEntry.setStatus("mandatory")


class _TrkOctBpIndex_Type(Integer32):
    """Custom type trkOctBpIndex based on Integer32"""
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


_TrkOctBpIndex_Type.__name__ = "Integer32"
_TrkOctBpIndex_Object = MibTableColumn
trkOctBpIndex = _TrkOctBpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 370, 1, 1),
    _TrkOctBpIndex_Type()
)
trkOctBpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkOctBpIndex.setStatus("mandatory")
_TrkOctBpValue_Type = PassportCounter64
_TrkOctBpValue_Object = MibTableColumn
trkOctBpValue = _TrkOctBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 370, 1, 2),
    _TrkOctBpValue_Type()
)
trkOctBpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkOctBpValue.setStatus("mandatory")
_TrunksMIB_ObjectIdentity = ObjectIdentity
trunksMIB = _TrunksMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 43)
)
_TrunksGroup_ObjectIdentity = ObjectIdentity
trunksGroup = _TrunksGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 43, 1)
)
_TrunksGroupBE_ObjectIdentity = ObjectIdentity
trunksGroupBE = _TrunksGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 43, 1, 5)
)
_TrunksGroupBE00_ObjectIdentity = ObjectIdentity
trunksGroupBE00 = _TrunksGroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 43, 1, 5, 1)
)
_TrunksGroupBE00A_ObjectIdentity = ObjectIdentity
trunksGroupBE00A = _TrunksGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 43, 1, 5, 1, 2)
)
_TrunksCapabilities_ObjectIdentity = ObjectIdentity
trunksCapabilities = _TrunksCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 43, 3)
)
_TrunksCapabilitiesBE_ObjectIdentity = ObjectIdentity
trunksCapabilitiesBE = _TrunksCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 43, 3, 5)
)
_TrunksCapabilitiesBE00_ObjectIdentity = ObjectIdentity
trunksCapabilitiesBE00 = _TrunksCapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 43, 3, 5, 1)
)
_TrunksCapabilitiesBE00A_ObjectIdentity = ObjectIdentity
trunksCapabilitiesBE00A = _TrunksCapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 43, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-TrunksMIB",
    **{"trk": trk,
       "trkRowStatusTable": trkRowStatusTable,
       "trkRowStatusEntry": trkRowStatusEntry,
       "trkRowStatus": trkRowStatus,
       "trkComponentName": trkComponentName,
       "trkStorageType": trkStorageType,
       "trkIndex": trkIndex,
       "trkPorsStats": trkPorsStats,
       "trkPorsStatsRowStatusTable": trkPorsStatsRowStatusTable,
       "trkPorsStatsRowStatusEntry": trkPorsStatsRowStatusEntry,
       "trkPorsStatsRowStatus": trkPorsStatsRowStatus,
       "trkPorsStatsComponentName": trkPorsStatsComponentName,
       "trkPorsStatsStorageType": trkPorsStatsStorageType,
       "trkPorsStatsIndex": trkPorsStatsIndex,
       "trkPorsStatsOperTable": trkPorsStatsOperTable,
       "trkPorsStatsOperEntry": trkPorsStatsOperEntry,
       "trkPorsStatsPorsNormPktFromIf": trkPorsStatsPorsNormPktFromIf,
       "trkPorsStatsPorsNormDiscUnforwardFromIf": trkPorsStatsPorsNormDiscUnforwardFromIf,
       "trkPorsStatsPorsNormOctetFromIf": trkPorsStatsPorsNormOctetFromIf,
       "trkPorsStatsPorsIntPktFromIf": trkPorsStatsPorsIntPktFromIf,
       "trkPorsStatsPorsIntDiscUnforwardFromIf": trkPorsStatsPorsIntDiscUnforwardFromIf,
       "trkPorsStatsPorsIntOctetFromIf": trkPorsStatsPorsIntOctetFromIf,
       "trkPorsStatsPktBpTable": trkPorsStatsPktBpTable,
       "trkPorsStatsPktBpEntry": trkPorsStatsPktBpEntry,
       "trkPorsStatsPktBpEpIndex": trkPorsStatsPktBpEpIndex,
       "trkPorsStatsPktBpDpIndex": trkPorsStatsPktBpDpIndex,
       "trkPorsStatsPktBpValue": trkPorsStatsPktBpValue,
       "trkPorsStatsDiscBpTable": trkPorsStatsDiscBpTable,
       "trkPorsStatsDiscBpEntry": trkPorsStatsDiscBpEntry,
       "trkPorsStatsDiscBpEpIndex": trkPorsStatsDiscBpEpIndex,
       "trkPorsStatsDiscBpDpIndex": trkPorsStatsDiscBpDpIndex,
       "trkPorsStatsDiscBpValue": trkPorsStatsDiscBpValue,
       "trkPorsStatsOctBpTable": trkPorsStatsOctBpTable,
       "trkPorsStatsOctBpEntry": trkPorsStatsOctBpEntry,
       "trkPorsStatsOctBpEpIndex": trkPorsStatsOctBpEpIndex,
       "trkPorsStatsOctBpDpIndex": trkPorsStatsOctBpDpIndex,
       "trkPorsStatsOctBpValue": trkPorsStatsOctBpValue,
       "trkFwdStats": trkFwdStats,
       "trkFwdStatsRowStatusTable": trkFwdStatsRowStatusTable,
       "trkFwdStatsRowStatusEntry": trkFwdStatsRowStatusEntry,
       "trkFwdStatsRowStatus": trkFwdStatsRowStatus,
       "trkFwdStatsComponentName": trkFwdStatsComponentName,
       "trkFwdStatsStorageType": trkFwdStatsStorageType,
       "trkFwdStatsIndex": trkFwdStatsIndex,
       "trkFwdStatsOperTable": trkFwdStatsOperTable,
       "trkFwdStatsOperEntry": trkFwdStatsOperEntry,
       "trkFwdStatsFwdPktFromIf": trkFwdStatsFwdPktFromIf,
       "trkFwdStatsFwdDiscUnforwardFromIf": trkFwdStatsFwdDiscUnforwardFromIf,
       "trkFwdStatsFwdOctetFromIf": trkFwdStatsFwdOctetFromIf,
       "trkVnsStats": trkVnsStats,
       "trkVnsStatsRowStatusTable": trkVnsStatsRowStatusTable,
       "trkVnsStatsRowStatusEntry": trkVnsStatsRowStatusEntry,
       "trkVnsStatsRowStatus": trkVnsStatsRowStatus,
       "trkVnsStatsComponentName": trkVnsStatsComponentName,
       "trkVnsStatsStorageType": trkVnsStatsStorageType,
       "trkVnsStatsIndex": trkVnsStatsIndex,
       "trkVnsStatsOperTable": trkVnsStatsOperTable,
       "trkVnsStatsOperEntry": trkVnsStatsOperEntry,
       "trkVnsStatsVnsPktFromIf": trkVnsStatsVnsPktFromIf,
       "trkVnsStatsVnsDiscUnforwardFromIf": trkVnsStatsVnsDiscUnforwardFromIf,
       "trkVnsStatsVnsOctetFromIf": trkVnsStatsVnsOctetFromIf,
       "trkVnsStatsPktBpTable": trkVnsStatsPktBpTable,
       "trkVnsStatsPktBpEntry": trkVnsStatsPktBpEntry,
       "trkVnsStatsPktBpEpIndex": trkVnsStatsPktBpEpIndex,
       "trkVnsStatsPktBpDpIndex": trkVnsStatsPktBpDpIndex,
       "trkVnsStatsPktBpValue": trkVnsStatsPktBpValue,
       "trkVnsStatsDiscBpTable": trkVnsStatsDiscBpTable,
       "trkVnsStatsDiscBpEntry": trkVnsStatsDiscBpEntry,
       "trkVnsStatsDiscBpEpIndex": trkVnsStatsDiscBpEpIndex,
       "trkVnsStatsDiscBpDpIndex": trkVnsStatsDiscBpDpIndex,
       "trkVnsStatsDiscBpValue": trkVnsStatsDiscBpValue,
       "trkVnsStatsOctBpTable": trkVnsStatsOctBpTable,
       "trkVnsStatsOctBpEntry": trkVnsStatsOctBpEntry,
       "trkVnsStatsOctBpEpIndex": trkVnsStatsOctBpEpIndex,
       "trkVnsStatsOctBpDpIndex": trkVnsStatsOctBpDpIndex,
       "trkVnsStatsOctBpValue": trkVnsStatsOctBpValue,
       "trkDprsStats": trkDprsStats,
       "trkDprsStatsRowStatusTable": trkDprsStatsRowStatusTable,
       "trkDprsStatsRowStatusEntry": trkDprsStatsRowStatusEntry,
       "trkDprsStatsRowStatus": trkDprsStatsRowStatus,
       "trkDprsStatsComponentName": trkDprsStatsComponentName,
       "trkDprsStatsStorageType": trkDprsStatsStorageType,
       "trkDprsStatsIndex": trkDprsStatsIndex,
       "trkDprsStatsPktBpTable": trkDprsStatsPktBpTable,
       "trkDprsStatsPktBpEntry": trkDprsStatsPktBpEntry,
       "trkDprsStatsPktBpEpIndex": trkDprsStatsPktBpEpIndex,
       "trkDprsStatsPktBpDpIndex": trkDprsStatsPktBpDpIndex,
       "trkDprsStatsPktBpValue": trkDprsStatsPktBpValue,
       "trkDprsStatsDiscBpTable": trkDprsStatsDiscBpTable,
       "trkDprsStatsDiscBpEntry": trkDprsStatsDiscBpEntry,
       "trkDprsStatsDiscBpEpIndex": trkDprsStatsDiscBpEpIndex,
       "trkDprsStatsDiscBpDpIndex": trkDprsStatsDiscBpDpIndex,
       "trkDprsStatsDiscBpValue": trkDprsStatsDiscBpValue,
       "trkDprsStatsOctBpTable": trkDprsStatsOctBpTable,
       "trkDprsStatsOctBpEntry": trkDprsStatsOctBpEntry,
       "trkDprsStatsOctBpEpIndex": trkDprsStatsOctBpEpIndex,
       "trkDprsStatsOctBpDpIndex": trkDprsStatsOctBpDpIndex,
       "trkDprsStatsOctBpValue": trkDprsStatsOctBpValue,
       "trkIfEntryTable": trkIfEntryTable,
       "trkIfEntryEntry": trkIfEntryEntry,
       "trkIfAdminStatus": trkIfAdminStatus,
       "trkIfIndex": trkIfIndex,
       "trkProvTable": trkProvTable,
       "trkProvEntry": trkProvEntry,
       "trkExpectedRemoteNodeName": trkExpectedRemoteNodeName,
       "trkRemoteValidationAction": trkRemoteValidationAction,
       "trkMaximumExpectedRoundTripDelay": trkMaximumExpectedRoundTripDelay,
       "trkIdleTimeOut": trkIdleTimeOut,
       "trkOverridesTable": trkOverridesTable,
       "trkOverridesEntry": trkOverridesEntry,
       "trkOverrideTransmitSpeed": trkOverrideTransmitSpeed,
       "trkOldOverrideRoundTripDelay": trkOldOverrideRoundTripDelay,
       "trkOverrideRoundTripUsec": trkOverrideRoundTripUsec,
       "trkStateTable": trkStateTable,
       "trkStateEntry": trkStateEntry,
       "trkAdminState": trkAdminState,
       "trkOperationalState": trkOperationalState,
       "trkUsageState": trkUsageState,
       "trkAvailabilityStatus": trkAvailabilityStatus,
       "trkProceduralStatus": trkProceduralStatus,
       "trkControlStatus": trkControlStatus,
       "trkAlarmStatus": trkAlarmStatus,
       "trkStandbyStatus": trkStandbyStatus,
       "trkUnknownStatus": trkUnknownStatus,
       "trkOperStatusTable": trkOperStatusTable,
       "trkOperStatusEntry": trkOperStatusEntry,
       "trkSnmpOperStatus": trkSnmpOperStatus,
       "trkOperTable": trkOperTable,
       "trkOperEntry": trkOperEntry,
       "trkRemoteComponentName": trkRemoteComponentName,
       "trkTransportTable": trkTransportTable,
       "trkTransportEntry": trkTransportEntry,
       "trkMeasuredSpeedToIf": trkMeasuredSpeedToIf,
       "trkMeasuredRoundTripDelay": trkMeasuredRoundTripDelay,
       "trkMaxTxUnit": trkMaxTxUnit,
       "trkMeasuredRoundTripDelayUsec": trkMeasuredRoundTripDelayUsec,
       "trkStatsTable": trkStatsTable,
       "trkStatsEntry": trkStatsEntry,
       "trkAreYouThereModeEntries": trkAreYouThereModeEntries,
       "trkPktFromIf": trkPktFromIf,
       "trkTrunkPktFromIf": trkTrunkPktFromIf,
       "trkTrunkPktToIf": trkTrunkPktToIf,
       "trkDiscardUnforward": trkDiscardUnforward,
       "trkDiscardTrunkPktFromIf": trkDiscardTrunkPktFromIf,
       "trkIntPktFromIf": trkIntPktFromIf,
       "trkDiscardIntUnforward": trkDiscardIntUnforward,
       "trkStagingAttempts": trkStagingAttempts,
       "trkDiscardTrunkPktToIf": trkDiscardTrunkPktToIf,
       "trkUtilization": trkUtilization,
       "trkSpeedReportingTable": trkSpeedReportingTable,
       "trkSpeedReportingEntry": trkSpeedReportingEntry,
       "trkSpeedReportingHoldOff": trkSpeedReportingHoldOff,
       "trkLowSpeedAlarmThreshold": trkLowSpeedAlarmThreshold,
       "trkHighSpeedAlarmThreshold": trkHighSpeedAlarmThreshold,
       "trkSpdThTable": trkSpdThTable,
       "trkSpdThEntry": trkSpdThEntry,
       "trkSpdThValue": trkSpdThValue,
       "trkSpdThRowStatus": trkSpdThRowStatus,
       "trkPktBpTable": trkPktBpTable,
       "trkPktBpEntry": trkPktBpEntry,
       "trkPktBpIndex": trkPktBpIndex,
       "trkPktBpValue": trkPktBpValue,
       "trkDiscBpTable": trkDiscBpTable,
       "trkDiscBpEntry": trkDiscBpEntry,
       "trkDiscBpIndex": trkDiscBpIndex,
       "trkDiscBpValue": trkDiscBpValue,
       "trkOctBpTable": trkOctBpTable,
       "trkOctBpEntry": trkOctBpEntry,
       "trkOctBpIndex": trkOctBpIndex,
       "trkOctBpValue": trkOctBpValue,
       "trunksMIB": trunksMIB,
       "trunksGroup": trunksGroup,
       "trunksGroupBE": trunksGroupBE,
       "trunksGroupBE00": trunksGroupBE00,
       "trunksGroupBE00A": trunksGroupBE00A,
       "trunksCapabilities": trunksCapabilities,
       "trunksCapabilitiesBE": trunksCapabilitiesBE,
       "trunksCapabilitiesBE00": trunksCapabilitiesBE00,
       "trunksCapabilitiesBE00A": trunksCapabilitiesBE00A}
)
