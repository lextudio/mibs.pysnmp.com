# SNMP MIB module (NSCDXCDA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NSCDXCDA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:29 2024
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

(nscDx,) = mibBuilder.importSymbols(
    "NSC-MIB",
    "nscDx")

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
 NotificationType,
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
    "NotificationType",
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

_NscDxCda_ObjectIdentity = ObjectIdentity
nscDxCda = _NscDxCda_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3)
)
_NscDxCdaTraceInfoTable_Object = MibTable
nscDxCdaTraceInfoTable = _NscDxCdaTraceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    nscDxCdaTraceInfoTable.setStatus("mandatory")
_NscDxCdaTraceInfoEntry_Object = MibTableRow
nscDxCdaTraceInfoEntry = _NscDxCdaTraceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 1, 1)
)
nscDxCdaTraceInfoEntry.setIndexNames(
    (0, "NSCDXCDA-MIB", "nscDxCdaTraceInfoEntKeyId"),
)
if mibBuilder.loadTexts:
    nscDxCdaTraceInfoEntry.setStatus("mandatory")


class _NscDxCdaTraceInfoEntKeyId_Type(Integer32):
    """Custom type nscDxCdaTraceInfoEntKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NscDxCdaTraceInfoEntKeyId_Type.__name__ = "Integer32"
_NscDxCdaTraceInfoEntKeyId_Object = MibTableColumn
nscDxCdaTraceInfoEntKeyId = _NscDxCdaTraceInfoEntKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 1, 1, 1),
    _NscDxCdaTraceInfoEntKeyId_Type()
)
nscDxCdaTraceInfoEntKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxCdaTraceInfoEntKeyId.setStatus("mandatory")


class _NscDxCdaTraceInfoEntTraceSeverity_Type(Integer32):
    """Custom type nscDxCdaTraceInfoEntTraceSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NscDxCdaTraceInfoEntTraceSeverity_Type.__name__ = "Integer32"
_NscDxCdaTraceInfoEntTraceSeverity_Object = MibTableColumn
nscDxCdaTraceInfoEntTraceSeverity = _NscDxCdaTraceInfoEntTraceSeverity_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 1, 1, 2),
    _NscDxCdaTraceInfoEntTraceSeverity_Type()
)
nscDxCdaTraceInfoEntTraceSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscDxCdaTraceInfoEntTraceSeverity.setStatus("mandatory")
_NscDxCdaTraceInfoEntTraceFacilityMask_Type = Integer32
_NscDxCdaTraceInfoEntTraceFacilityMask_Object = MibTableColumn
nscDxCdaTraceInfoEntTraceFacilityMask = _NscDxCdaTraceInfoEntTraceFacilityMask_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 1, 1, 3),
    _NscDxCdaTraceInfoEntTraceFacilityMask_Type()
)
nscDxCdaTraceInfoEntTraceFacilityMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscDxCdaTraceInfoEntTraceFacilityMask.setStatus("mandatory")


class _NscDxCdaTraceInfoEntTrapSeverity_Type(Integer32):
    """Custom type nscDxCdaTraceInfoEntTrapSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NscDxCdaTraceInfoEntTrapSeverity_Type.__name__ = "Integer32"
_NscDxCdaTraceInfoEntTrapSeverity_Object = MibTableColumn
nscDxCdaTraceInfoEntTrapSeverity = _NscDxCdaTraceInfoEntTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 1, 1, 4),
    _NscDxCdaTraceInfoEntTrapSeverity_Type()
)
nscDxCdaTraceInfoEntTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscDxCdaTraceInfoEntTrapSeverity.setStatus("mandatory")
_NscDxCdaTraceInfoEntTrapFacilityMask_Type = Integer32
_NscDxCdaTraceInfoEntTrapFacilityMask_Object = MibTableColumn
nscDxCdaTraceInfoEntTrapFacilityMask = _NscDxCdaTraceInfoEntTrapFacilityMask_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 1, 1, 5),
    _NscDxCdaTraceInfoEntTrapFacilityMask_Type()
)
nscDxCdaTraceInfoEntTrapFacilityMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscDxCdaTraceInfoEntTrapFacilityMask.setStatus("mandatory")


class _NscDxCdaTraceInfoEntFacility_Type(Integer32):
    """Custom type nscDxCdaTraceInfoEntFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 3),
          ("bus-tag", 20),
          ("console", 1),
          ("device", 19),
          ("dlcx", 5),
          ("escon", 21),
          ("executive", 0),
          ("greenline", 22),
          ("ho15", 23),
          ("isr", 24),
          ("localip", 4),
          ("packets", 2),
          ("session", 18),
          ("xport", 17))
    )


_NscDxCdaTraceInfoEntFacility_Type.__name__ = "Integer32"
_NscDxCdaTraceInfoEntFacility_Object = MibTableColumn
nscDxCdaTraceInfoEntFacility = _NscDxCdaTraceInfoEntFacility_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 1, 1, 6),
    _NscDxCdaTraceInfoEntFacility_Type()
)
nscDxCdaTraceInfoEntFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxCdaTraceInfoEntFacility.setStatus("mandatory")


class _NscDxCdaTraceInfoEntSeverity_Type(Integer32):
    """Custom type nscDxCdaTraceInfoEntSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NscDxCdaTraceInfoEntSeverity_Type.__name__ = "Integer32"
_NscDxCdaTraceInfoEntSeverity_Object = MibTableColumn
nscDxCdaTraceInfoEntSeverity = _NscDxCdaTraceInfoEntSeverity_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 1, 1, 7),
    _NscDxCdaTraceInfoEntSeverity_Type()
)
nscDxCdaTraceInfoEntSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxCdaTraceInfoEntSeverity.setStatus("mandatory")
_NscDxCdaTraceInfoEntMsgnum_Type = Integer32
_NscDxCdaTraceInfoEntMsgnum_Object = MibTableColumn
nscDxCdaTraceInfoEntMsgnum = _NscDxCdaTraceInfoEntMsgnum_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 1, 1, 8),
    _NscDxCdaTraceInfoEntMsgnum_Type()
)
nscDxCdaTraceInfoEntMsgnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxCdaTraceInfoEntMsgnum.setStatus("mandatory")
_NscDxCdaTraceInfoEntTimestamp_Type = Counter32
_NscDxCdaTraceInfoEntTimestamp_Object = MibTableColumn
nscDxCdaTraceInfoEntTimestamp = _NscDxCdaTraceInfoEntTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 1, 1, 9),
    _NscDxCdaTraceInfoEntTimestamp_Type()
)
nscDxCdaTraceInfoEntTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxCdaTraceInfoEntTimestamp.setStatus("mandatory")


class _NscDxCdaTraceInfoEntMsg_Type(DisplayString):
    """Custom type nscDxCdaTraceInfoEntMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NscDxCdaTraceInfoEntMsg_Type.__name__ = "DisplayString"
_NscDxCdaTraceInfoEntMsg_Object = MibTableColumn
nscDxCdaTraceInfoEntMsg = _NscDxCdaTraceInfoEntMsg_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 1, 1, 10),
    _NscDxCdaTraceInfoEntMsg_Type()
)
nscDxCdaTraceInfoEntMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxCdaTraceInfoEntMsg.setStatus("mandatory")
_NscDxCdaTraceTable_Object = MibTable
nscDxCdaTraceTable = _NscDxCdaTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    nscDxCdaTraceTable.setStatus("mandatory")
_NscDxCdaTraceEntry_Object = MibTableRow
nscDxCdaTraceEntry = _NscDxCdaTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 2, 1)
)
nscDxCdaTraceEntry.setIndexNames(
    (0, "NSCDXCDA-MIB", "nscDxCdaTraceEntKeyId"),
    (0, "NSCDXCDA-MIB", "nscDxCdaTraceEntNum"),
)
if mibBuilder.loadTexts:
    nscDxCdaTraceEntry.setStatus("mandatory")


class _NscDxCdaTraceEntKeyId_Type(Integer32):
    """Custom type nscDxCdaTraceEntKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NscDxCdaTraceEntKeyId_Type.__name__ = "Integer32"
_NscDxCdaTraceEntKeyId_Object = MibTableColumn
nscDxCdaTraceEntKeyId = _NscDxCdaTraceEntKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 2, 1, 1),
    _NscDxCdaTraceEntKeyId_Type()
)
nscDxCdaTraceEntKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxCdaTraceEntKeyId.setStatus("mandatory")
_NscDxCdaTraceEntNum_Type = Integer32
_NscDxCdaTraceEntNum_Object = MibTableColumn
nscDxCdaTraceEntNum = _NscDxCdaTraceEntNum_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 2, 1, 2),
    _NscDxCdaTraceEntNum_Type()
)
nscDxCdaTraceEntNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxCdaTraceEntNum.setStatus("mandatory")


class _NscDxCdaTraceEntFacility_Type(Integer32):
    """Custom type nscDxCdaTraceEntFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 3),
          ("bus-tag", 20),
          ("console", 1),
          ("device", 19),
          ("dlcx", 5),
          ("escon", 21),
          ("executive", 0),
          ("greenline", 22),
          ("ho15", 23),
          ("isr", 24),
          ("localip", 4),
          ("packets", 2),
          ("session", 18),
          ("xport", 17))
    )


_NscDxCdaTraceEntFacility_Type.__name__ = "Integer32"
_NscDxCdaTraceEntFacility_Object = MibTableColumn
nscDxCdaTraceEntFacility = _NscDxCdaTraceEntFacility_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 2, 1, 3),
    _NscDxCdaTraceEntFacility_Type()
)
nscDxCdaTraceEntFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxCdaTraceEntFacility.setStatus("mandatory")


class _NscDxCdaTraceEntSeverity_Type(Integer32):
    """Custom type nscDxCdaTraceEntSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NscDxCdaTraceEntSeverity_Type.__name__ = "Integer32"
_NscDxCdaTraceEntSeverity_Object = MibTableColumn
nscDxCdaTraceEntSeverity = _NscDxCdaTraceEntSeverity_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 2, 1, 4),
    _NscDxCdaTraceEntSeverity_Type()
)
nscDxCdaTraceEntSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxCdaTraceEntSeverity.setStatus("mandatory")
_NscDxCdaTraceEntMsgnum_Type = Integer32
_NscDxCdaTraceEntMsgnum_Object = MibTableColumn
nscDxCdaTraceEntMsgnum = _NscDxCdaTraceEntMsgnum_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 2, 1, 5),
    _NscDxCdaTraceEntMsgnum_Type()
)
nscDxCdaTraceEntMsgnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxCdaTraceEntMsgnum.setStatus("mandatory")
_NscDxCdaTraceEntTimestamp_Type = Counter32
_NscDxCdaTraceEntTimestamp_Object = MibTableColumn
nscDxCdaTraceEntTimestamp = _NscDxCdaTraceEntTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 2, 1, 6),
    _NscDxCdaTraceEntTimestamp_Type()
)
nscDxCdaTraceEntTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxCdaTraceEntTimestamp.setStatus("mandatory")


class _NscDxCdaTraceEntMsg_Type(DisplayString):
    """Custom type nscDxCdaTraceEntMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NscDxCdaTraceEntMsg_Type.__name__ = "DisplayString"
_NscDxCdaTraceEntMsg_Object = MibTableColumn
nscDxCdaTraceEntMsg = _NscDxCdaTraceEntMsg_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 2, 1, 7),
    _NscDxCdaTraceEntMsg_Type()
)
nscDxCdaTraceEntMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxCdaTraceEntMsg.setStatus("mandatory")
_NscDxCdaProfilesTable_Object = MibTable
nscDxCdaProfilesTable = _NscDxCdaProfilesTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 3)
)
if mibBuilder.loadTexts:
    nscDxCdaProfilesTable.setStatus("mandatory")
_NscDxCdaProfilesEntry_Object = MibTableRow
nscDxCdaProfilesEntry = _NscDxCdaProfilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 3, 1)
)
nscDxCdaProfilesEntry.setIndexNames(
    (0, "NSCDXCDA-MIB", "nscDxCdaProfilesEntKeyId"),
)
if mibBuilder.loadTexts:
    nscDxCdaProfilesEntry.setStatus("mandatory")


class _NscDxCdaProfilesEntKeyId_Type(Integer32):
    """Custom type nscDxCdaProfilesEntKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NscDxCdaProfilesEntKeyId_Type.__name__ = "Integer32"
_NscDxCdaProfilesEntKeyId_Object = MibTableColumn
nscDxCdaProfilesEntKeyId = _NscDxCdaProfilesEntKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 3, 1, 1),
    _NscDxCdaProfilesEntKeyId_Type()
)
nscDxCdaProfilesEntKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxCdaProfilesEntKeyId.setStatus("mandatory")
_NscDxCdaProfilesEntDateWritten_Type = Integer32
_NscDxCdaProfilesEntDateWritten_Object = MibTableColumn
nscDxCdaProfilesEntDateWritten = _NscDxCdaProfilesEntDateWritten_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 3, 1, 2),
    _NscDxCdaProfilesEntDateWritten_Type()
)
nscDxCdaProfilesEntDateWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxCdaProfilesEntDateWritten.setStatus("mandatory")
_NscDxCdaProfilesEntTimeWritten_Type = Integer32
_NscDxCdaProfilesEntTimeWritten_Object = MibTableColumn
nscDxCdaProfilesEntTimeWritten = _NscDxCdaProfilesEntTimeWritten_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 3, 1, 3),
    _NscDxCdaProfilesEntTimeWritten_Type()
)
nscDxCdaProfilesEntTimeWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxCdaProfilesEntTimeWritten.setStatus("mandatory")


class _NscDxCdaProfilesEntName_Type(DisplayString):
    """Custom type nscDxCdaProfilesEntName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NscDxCdaProfilesEntName_Type.__name__ = "DisplayString"
_NscDxCdaProfilesEntName_Object = MibTableColumn
nscDxCdaProfilesEntName = _NscDxCdaProfilesEntName_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 3, 1, 4),
    _NscDxCdaProfilesEntName_Type()
)
nscDxCdaProfilesEntName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscDxCdaProfilesEntName.setStatus("mandatory")


class _NscDxCdaProfilesEntSaveProfiles_Type(Integer32):
    """Custom type nscDxCdaProfilesEntSaveProfiles based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modified", 1),
          ("up-to-date", 2))
    )


_NscDxCdaProfilesEntSaveProfiles_Type.__name__ = "Integer32"
_NscDxCdaProfilesEntSaveProfiles_Object = MibTableColumn
nscDxCdaProfilesEntSaveProfiles = _NscDxCdaProfilesEntSaveProfiles_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 3, 1, 5),
    _NscDxCdaProfilesEntSaveProfiles_Type()
)
nscDxCdaProfilesEntSaveProfiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscDxCdaProfilesEntSaveProfiles.setStatus("mandatory")
_NscDxCdaProfilesEntProcessorSpecific_Type = ObjectIdentifier
_NscDxCdaProfilesEntProcessorSpecific_Object = MibTableColumn
nscDxCdaProfilesEntProcessorSpecific = _NscDxCdaProfilesEntProcessorSpecific_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 3, 3, 1, 6),
    _NscDxCdaProfilesEntProcessorSpecific_Type()
)
nscDxCdaProfilesEntProcessorSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxCdaProfilesEntProcessorSpecific.setStatus("mandatory")

# Managed Objects groups


# Notification objects

nscDxTrace = NotificationType(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 0, 1)
)
nscDxTrace.setObjects(
      *(("NSCDXCDA-MIB", "nscDxCdaTraceInfoEntKeyId"),
        ("NSCDXCDA-MIB", "nscDxCdaTraceInfoEntFacility"),
        ("NSCDXCDA-MIB", "nscDxCdaTraceInfoEntSeverity"),
        ("NSCDXCDA-MIB", "nscDxCdaTraceInfoEntMsgnum"),
        ("NSCDXCDA-MIB", "nscDxCdaTraceInfoEntTimestamp"),
        ("NSCDXCDA-MIB", "nscDxCdaTraceInfoEntMsg"))
)
if mibBuilder.loadTexts:
    nscDxTrace.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCDXCDA-MIB",
    **{"nscDxTrace": nscDxTrace,
       "nscDxCda": nscDxCda,
       "nscDxCdaTraceInfoTable": nscDxCdaTraceInfoTable,
       "nscDxCdaTraceInfoEntry": nscDxCdaTraceInfoEntry,
       "nscDxCdaTraceInfoEntKeyId": nscDxCdaTraceInfoEntKeyId,
       "nscDxCdaTraceInfoEntTraceSeverity": nscDxCdaTraceInfoEntTraceSeverity,
       "nscDxCdaTraceInfoEntTraceFacilityMask": nscDxCdaTraceInfoEntTraceFacilityMask,
       "nscDxCdaTraceInfoEntTrapSeverity": nscDxCdaTraceInfoEntTrapSeverity,
       "nscDxCdaTraceInfoEntTrapFacilityMask": nscDxCdaTraceInfoEntTrapFacilityMask,
       "nscDxCdaTraceInfoEntFacility": nscDxCdaTraceInfoEntFacility,
       "nscDxCdaTraceInfoEntSeverity": nscDxCdaTraceInfoEntSeverity,
       "nscDxCdaTraceInfoEntMsgnum": nscDxCdaTraceInfoEntMsgnum,
       "nscDxCdaTraceInfoEntTimestamp": nscDxCdaTraceInfoEntTimestamp,
       "nscDxCdaTraceInfoEntMsg": nscDxCdaTraceInfoEntMsg,
       "nscDxCdaTraceTable": nscDxCdaTraceTable,
       "nscDxCdaTraceEntry": nscDxCdaTraceEntry,
       "nscDxCdaTraceEntKeyId": nscDxCdaTraceEntKeyId,
       "nscDxCdaTraceEntNum": nscDxCdaTraceEntNum,
       "nscDxCdaTraceEntFacility": nscDxCdaTraceEntFacility,
       "nscDxCdaTraceEntSeverity": nscDxCdaTraceEntSeverity,
       "nscDxCdaTraceEntMsgnum": nscDxCdaTraceEntMsgnum,
       "nscDxCdaTraceEntTimestamp": nscDxCdaTraceEntTimestamp,
       "nscDxCdaTraceEntMsg": nscDxCdaTraceEntMsg,
       "nscDxCdaProfilesTable": nscDxCdaProfilesTable,
       "nscDxCdaProfilesEntry": nscDxCdaProfilesEntry,
       "nscDxCdaProfilesEntKeyId": nscDxCdaProfilesEntKeyId,
       "nscDxCdaProfilesEntDateWritten": nscDxCdaProfilesEntDateWritten,
       "nscDxCdaProfilesEntTimeWritten": nscDxCdaProfilesEntTimeWritten,
       "nscDxCdaProfilesEntName": nscDxCdaProfilesEntName,
       "nscDxCdaProfilesEntSaveProfiles": nscDxCdaProfilesEntSaveProfiles,
       "nscDxCdaProfilesEntProcessorSpecific": nscDxCdaProfilesEntProcessorSpecific}
)
