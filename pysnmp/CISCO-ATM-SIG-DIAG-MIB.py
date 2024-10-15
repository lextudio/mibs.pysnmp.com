# SNMP MIB module (CISCO-ATM-SIG-DIAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ATM-SIG-DIAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:00 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "InterfaceIndexOrZero")

(PnniNodeId,
 PnniPortId,
 ServiceCategory) = mibBuilder.importSymbols(
    "PNNI-MIB",
    "PnniNodeId",
    "PnniPortId",
    "ServiceCategory")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoAtmSigDiagMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 78)
)
ciscoAtmSigDiagMIB.setRevisions(
        ("1997-07-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AtmAddr(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(20, 20),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSigFailMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSigFailMIBObjects = _CiscoSigFailMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1)
)
_CsfBaseGroup_ObjectIdentity = ObjectIdentity
csfBaseGroup = _CsfBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 1)
)


class _CsfFilterControl_Type(Integer32):
    """Custom type csfFilterControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CsfFilterControl_Type.__name__ = "Integer32"
_CsfFilterControl_Object = MibScalar
csfFilterControl = _CsfFilterControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 1, 1),
    _CsfFilterControl_Type()
)
csfFilterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csfFilterControl.setStatus("current")
_CsfFilterGroup_ObjectIdentity = ObjectIdentity
csfFilterGroup = _CsfFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 2)
)
_CsfFilterTable_Object = MibTable
csfFilterTable = _CsfFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 2, 1)
)
if mibBuilder.loadTexts:
    csfFilterTable.setStatus("current")
_CsfFilterEntry_Object = MibTableRow
csfFilterEntry = _CsfFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 2, 1, 1)
)
csfFilterEntry.setIndexNames(
    (0, "CISCO-ATM-SIG-DIAG-MIB", "csfFilterIndex"),
)
if mibBuilder.loadTexts:
    csfFilterEntry.setStatus("current")


class _CsfFilterIndex_Type(Integer32):
    """Custom type csfFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_CsfFilterIndex_Type.__name__ = "Integer32"
_CsfFilterIndex_Object = MibTableColumn
csfFilterIndex = _CsfFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 2, 1, 1, 1),
    _CsfFilterIndex_Type()
)
csfFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csfFilterIndex.setStatus("current")


class _CsfFilterScope_Type(Integer32):
    """Custom type csfFilterScope based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allRejects", 3),
          ("localRejects", 1),
          ("remoteRejects", 2))
    )


_CsfFilterScope_Type.__name__ = "Integer32"
_CsfFilterScope_Object = MibTableColumn
csfFilterScope = _CsfFilterScope_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 2, 1, 1, 2),
    _CsfFilterScope_Type()
)
csfFilterScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csfFilterScope.setStatus("current")


class _CsfFilterConnKind_Type(OctetString):
    """Custom type csfFilterConnKind based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CsfFilterConnKind_Type.__name__ = "OctetString"
_CsfFilterConnKind_Object = MibTableColumn
csfFilterConnKind = _CsfFilterConnKind_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 2, 1, 1, 3),
    _CsfFilterConnKind_Type()
)
csfFilterConnKind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csfFilterConnKind.setStatus("current")


class _CsfFilterConnCastType_Type(OctetString):
    """Custom type csfFilterConnCastType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CsfFilterConnCastType_Type.__name__ = "OctetString"
_CsfFilterConnCastType_Object = MibTableColumn
csfFilterConnCastType = _CsfFilterConnCastType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 2, 1, 1, 4),
    _CsfFilterConnCastType_Type()
)
csfFilterConnCastType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csfFilterConnCastType.setStatus("current")


class _CsfFilterServiceCategory_Type(OctetString):
    """Custom type csfFilterServiceCategory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CsfFilterServiceCategory_Type.__name__ = "OctetString"
_CsfFilterServiceCategory_Object = MibTableColumn
csfFilterServiceCategory = _CsfFilterServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 2, 1, 1, 5),
    _CsfFilterServiceCategory_Type()
)
csfFilterServiceCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csfFilterServiceCategory.setStatus("current")


class _CsfFilterInInterface_Type(InterfaceIndexOrZero):
    """Custom type csfFilterInInterface based on InterfaceIndexOrZero"""
    defaultValue = 0


_CsfFilterInInterface_Object = MibTableColumn
csfFilterInInterface = _CsfFilterInInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 2, 1, 1, 6),
    _CsfFilterInInterface_Type()
)
csfFilterInInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csfFilterInInterface.setStatus("current")


class _CsfFilterOutInterface_Type(InterfaceIndexOrZero):
    """Custom type csfFilterOutInterface based on InterfaceIndexOrZero"""
    defaultValue = 0


_CsfFilterOutInterface_Object = MibTableColumn
csfFilterOutInterface = _CsfFilterOutInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 2, 1, 1, 7),
    _CsfFilterOutInterface_Type()
)
csfFilterOutInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csfFilterOutInterface.setStatus("current")


class _CsfFilterCause_Type(Integer32):
    """Custom type csfFilterCause based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CsfFilterCause_Type.__name__ = "Integer32"
_CsfFilterCause_Object = MibTableColumn
csfFilterCause = _CsfFilterCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 2, 1, 1, 8),
    _CsfFilterCause_Type()
)
csfFilterCause.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csfFilterCause.setStatus("current")
_CsfFilterCallingParty_Type = AtmAddr
_CsfFilterCallingParty_Object = MibTableColumn
csfFilterCallingParty = _CsfFilterCallingParty_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 2, 1, 1, 9),
    _CsfFilterCallingParty_Type()
)
csfFilterCallingParty.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csfFilterCallingParty.setStatus("current")


class _CsfFilterCallingPartyMask_Type(OctetString):
    """Custom type csfFilterCallingPartyMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CsfFilterCallingPartyMask_Type.__name__ = "OctetString"
_CsfFilterCallingPartyMask_Object = MibTableColumn
csfFilterCallingPartyMask = _CsfFilterCallingPartyMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 2, 1, 1, 10),
    _CsfFilterCallingPartyMask_Type()
)
csfFilterCallingPartyMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csfFilterCallingPartyMask.setStatus("current")
_CsfFilterCalledParty_Type = AtmAddr
_CsfFilterCalledParty_Object = MibTableColumn
csfFilterCalledParty = _CsfFilterCalledParty_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 2, 1, 1, 11),
    _CsfFilterCalledParty_Type()
)
csfFilterCalledParty.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csfFilterCalledParty.setStatus("current")


class _CsfFilterCalledPartyMask_Type(OctetString):
    """Custom type csfFilterCalledPartyMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CsfFilterCalledPartyMask_Type.__name__ = "OctetString"
_CsfFilterCalledPartyMask_Object = MibTableColumn
csfFilterCalledPartyMask = _CsfFilterCalledPartyMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 2, 1, 1, 12),
    _CsfFilterCalledPartyMask_Type()
)
csfFilterCalledPartyMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csfFilterCalledPartyMask.setStatus("current")


class _CsfFilterMaxRecords_Type(Integer32):
    """Custom type csfFilterMaxRecords based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 214783647),
    )


_CsfFilterMaxRecords_Type.__name__ = "Integer32"
_CsfFilterMaxRecords_Object = MibTableColumn
csfFilterMaxRecords = _CsfFilterMaxRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 2, 1, 1, 13),
    _CsfFilterMaxRecords_Type()
)
csfFilterMaxRecords.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csfFilterMaxRecords.setStatus("current")


class _CsfFilterAgeTimeout_Type(Integer32):
    """Custom type csfFilterAgeTimeout based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_CsfFilterAgeTimeout_Type.__name__ = "Integer32"
_CsfFilterAgeTimeout_Object = MibTableColumn
csfFilterAgeTimeout = _CsfFilterAgeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 2, 1, 1, 14),
    _CsfFilterAgeTimeout_Type()
)
csfFilterAgeTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csfFilterAgeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    csfFilterAgeTimeout.setUnits("seconds")


class _CsfFilterPurge_Type(Integer32):
    """Custom type csfFilterPurge based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 2),
          ("purge", 1))
    )


_CsfFilterPurge_Type.__name__ = "Integer32"
_CsfFilterPurge_Object = MibTableColumn
csfFilterPurge = _CsfFilterPurge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 2, 1, 1, 15),
    _CsfFilterPurge_Type()
)
csfFilterPurge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csfFilterPurge.setStatus("current")
_CsfFilterNumMatches_Type = Counter32
_CsfFilterNumMatches_Object = MibTableColumn
csfFilterNumMatches = _CsfFilterNumMatches_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 2, 1, 1, 16),
    _CsfFilterNumMatches_Type()
)
csfFilterNumMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfFilterNumMatches.setStatus("current")
_CsfFilterRowStatus_Type = RowStatus
_CsfFilterRowStatus_Object = MibTableColumn
csfFilterRowStatus = _CsfFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 2, 1, 1, 17),
    _CsfFilterRowStatus_Type()
)
csfFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csfFilterRowStatus.setStatus("current")
_CsfRecordGroup_ObjectIdentity = ObjectIdentity
csfRecordGroup = _CsfRecordGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3)
)
_CsfRecordTable_Object = MibTable
csfRecordTable = _CsfRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 1)
)
if mibBuilder.loadTexts:
    csfRecordTable.setStatus("current")
_CsfRecordEntry_Object = MibTableRow
csfRecordEntry = _CsfRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 1, 1)
)
csfRecordEntry.setIndexNames(
    (0, "CISCO-ATM-SIG-DIAG-MIB", "csfFilterIndex"),
    (0, "CISCO-ATM-SIG-DIAG-MIB", "csfRecordIndex"),
)
if mibBuilder.loadTexts:
    csfRecordEntry.setStatus("current")


class _CsfRecordIndex_Type(Integer32):
    """Custom type csfRecordIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CsfRecordIndex_Type.__name__ = "Integer32"
_CsfRecordIndex_Object = MibTableColumn
csfRecordIndex = _CsfRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 1, 1, 1),
    _CsfRecordIndex_Type()
)
csfRecordIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csfRecordIndex.setStatus("current")


class _CsfRecordScope_Type(Integer32):
    """Custom type csfRecordScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localReject", 1),
          ("remoteReject", 2))
    )


_CsfRecordScope_Type.__name__ = "Integer32"
_CsfRecordScope_Object = MibTableColumn
csfRecordScope = _CsfRecordScope_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 1, 1, 2),
    _CsfRecordScope_Type()
)
csfRecordScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfRecordScope.setStatus("current")


class _CsfRecordConnKind_Type(Integer32):
    """Custom type csfRecordConnKind based on Integer32"""
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
        *(("softPvcc", 1),
          ("softPvpc", 2),
          ("switchedVcc", 3),
          ("switchedVpc", 4))
    )


_CsfRecordConnKind_Type.__name__ = "Integer32"
_CsfRecordConnKind_Object = MibTableColumn
csfRecordConnKind = _CsfRecordConnKind_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 1, 1, 3),
    _CsfRecordConnKind_Type()
)
csfRecordConnKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfRecordConnKind.setStatus("current")


class _CsfRecordConnCastType_Type(Integer32):
    """Custom type csfRecordConnCastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("p2mp", 2),
          ("p2p", 1))
    )


_CsfRecordConnCastType_Type.__name__ = "Integer32"
_CsfRecordConnCastType_Object = MibTableColumn
csfRecordConnCastType = _CsfRecordConnCastType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 1, 1, 4),
    _CsfRecordConnCastType_Type()
)
csfRecordConnCastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfRecordConnCastType.setStatus("current")


class _CsfRecordConnIndicator_Type(Integer32):
    """Custom type csfRecordConnIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addPartyReject", 1),
          ("setupReject", 2))
    )


_CsfRecordConnIndicator_Type.__name__ = "Integer32"
_CsfRecordConnIndicator_Object = MibTableColumn
csfRecordConnIndicator = _CsfRecordConnIndicator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 1, 1, 5),
    _CsfRecordConnIndicator_Type()
)
csfRecordConnIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfRecordConnIndicator.setStatus("current")
_CsfRecordServiceCategory_Type = ServiceCategory
_CsfRecordServiceCategory_Object = MibTableColumn
csfRecordServiceCategory = _CsfRecordServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 1, 1, 6),
    _CsfRecordServiceCategory_Type()
)
csfRecordServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfRecordServiceCategory.setStatus("current")


class _CsfRecordInInterface_Type(Integer32):
    """Custom type csfRecordInInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CsfRecordInInterface_Type.__name__ = "Integer32"
_CsfRecordInInterface_Object = MibTableColumn
csfRecordInInterface = _CsfRecordInInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 1, 1, 7),
    _CsfRecordInInterface_Type()
)
csfRecordInInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfRecordInInterface.setStatus("current")
_CsfRecordOutInterface_Type = InterfaceIndexOrZero
_CsfRecordOutInterface_Object = MibTableColumn
csfRecordOutInterface = _CsfRecordOutInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 1, 1, 8),
    _CsfRecordOutInterface_Type()
)
csfRecordOutInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfRecordOutInterface.setStatus("current")


class _CsfRecordCause_Type(Integer32):
    """Custom type csfRecordCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CsfRecordCause_Type.__name__ = "Integer32"
_CsfRecordCause_Object = MibTableColumn
csfRecordCause = _CsfRecordCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 1, 1, 9),
    _CsfRecordCause_Type()
)
csfRecordCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfRecordCause.setStatus("current")


class _CsfRecordDiags_Type(OctetString):
    """Custom type csfRecordDiags based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_CsfRecordDiags_Type.__name__ = "OctetString"
_CsfRecordDiags_Object = MibTableColumn
csfRecordDiags = _CsfRecordDiags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 1, 1, 10),
    _CsfRecordDiags_Type()
)
csfRecordDiags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfRecordDiags.setStatus("current")
_CsfRecordCallingParty_Type = AtmAddr
_CsfRecordCallingParty_Object = MibTableColumn
csfRecordCallingParty = _CsfRecordCallingParty_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 1, 1, 11),
    _CsfRecordCallingParty_Type()
)
csfRecordCallingParty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfRecordCallingParty.setStatus("current")
_CsfRecordCallingPartySubAddress_Type = AtmAddr
_CsfRecordCallingPartySubAddress_Object = MibTableColumn
csfRecordCallingPartySubAddress = _CsfRecordCallingPartySubAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 1, 1, 12),
    _CsfRecordCallingPartySubAddress_Type()
)
csfRecordCallingPartySubAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfRecordCallingPartySubAddress.setStatus("current")
_CsfRecordCalledParty_Type = AtmAddr
_CsfRecordCalledParty_Object = MibTableColumn
csfRecordCalledParty = _CsfRecordCalledParty_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 1, 1, 13),
    _CsfRecordCalledParty_Type()
)
csfRecordCalledParty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfRecordCalledParty.setStatus("current")
_CsfRecordCalledPartySubAddress_Type = AtmAddr
_CsfRecordCalledPartySubAddress_Object = MibTableColumn
csfRecordCalledPartySubAddress = _CsfRecordCalledPartySubAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 1, 1, 14),
    _CsfRecordCalledPartySubAddress_Type()
)
csfRecordCalledPartySubAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfRecordCalledPartySubAddress.setStatus("current")


class _CsfRecordCrankBackTransitType_Type(Integer32):
    """Custom type csfRecordCrankBackTransitType based on Integer32"""
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
        *(("blockedIncomingPort", 1),
          ("blockedLink", 3),
          ("blockedNode", 2),
          ("noCrankBack", 4))
    )


_CsfRecordCrankBackTransitType_Type.__name__ = "Integer32"
_CsfRecordCrankBackTransitType_Object = MibTableColumn
csfRecordCrankBackTransitType = _CsfRecordCrankBackTransitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 1, 1, 15),
    _CsfRecordCrankBackTransitType_Type()
)
csfRecordCrankBackTransitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfRecordCrankBackTransitType.setStatus("current")
_CsfRecordCrankBackNodeId_Type = PnniNodeId
_CsfRecordCrankBackNodeId_Object = MibTableColumn
csfRecordCrankBackNodeId = _CsfRecordCrankBackNodeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 1, 1, 16),
    _CsfRecordCrankBackNodeId_Type()
)
csfRecordCrankBackNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfRecordCrankBackNodeId.setStatus("current")
_CsfRecordCrankBackPortId_Type = PnniPortId
_CsfRecordCrankBackPortId_Object = MibTableColumn
csfRecordCrankBackPortId = _CsfRecordCrankBackPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 1, 1, 17),
    _CsfRecordCrankBackPortId_Type()
)
csfRecordCrankBackPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfRecordCrankBackPortId.setStatus("current")
_CsfRecordCrankBackSucceedingNodeId_Type = PnniNodeId
_CsfRecordCrankBackSucceedingNodeId_Object = MibTableColumn
csfRecordCrankBackSucceedingNodeId = _CsfRecordCrankBackSucceedingNodeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 1, 1, 18),
    _CsfRecordCrankBackSucceedingNodeId_Type()
)
csfRecordCrankBackSucceedingNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfRecordCrankBackSucceedingNodeId.setStatus("current")
_CsfRecordTimeStamp_Type = TimeStamp
_CsfRecordTimeStamp_Object = MibTableColumn
csfRecordTimeStamp = _CsfRecordTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 1, 1, 19),
    _CsfRecordTimeStamp_Type()
)
csfRecordTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfRecordTimeStamp.setStatus("current")
_CsfDtlTable_Object = MibTable
csfDtlTable = _CsfDtlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 2)
)
if mibBuilder.loadTexts:
    csfDtlTable.setStatus("current")
_CsfDtlEntry_Object = MibTableRow
csfDtlEntry = _CsfDtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 2, 1)
)
csfDtlEntry.setIndexNames(
    (0, "CISCO-ATM-SIG-DIAG-MIB", "csfFilterIndex"),
    (0, "CISCO-ATM-SIG-DIAG-MIB", "csfRecordIndex"),
    (0, "CISCO-ATM-SIG-DIAG-MIB", "csfDtlEntryIndex"),
)
if mibBuilder.loadTexts:
    csfDtlEntry.setStatus("current")


class _CsfDtlEntryIndex_Type(Integer32):
    """Custom type csfDtlEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_CsfDtlEntryIndex_Type.__name__ = "Integer32"
_CsfDtlEntryIndex_Object = MibTableColumn
csfDtlEntryIndex = _CsfDtlEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 2, 1, 1),
    _CsfDtlEntryIndex_Type()
)
csfDtlEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csfDtlEntryIndex.setStatus("current")
_CsfDtlNodeId_Type = PnniNodeId
_CsfDtlNodeId_Object = MibTableColumn
csfDtlNodeId = _CsfDtlNodeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 2, 1, 2),
    _CsfDtlNodeId_Type()
)
csfDtlNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfDtlNodeId.setStatus("current")
_CsfDtlPortId_Type = PnniPortId
_CsfDtlPortId_Object = MibTableColumn
csfDtlPortId = _CsfDtlPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 2, 1, 3),
    _CsfDtlPortId_Type()
)
csfDtlPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfDtlPortId.setStatus("current")


class _CsfDtlLinkType_Type(Integer32):
    """Custom type csfDtlLinkType based on Integer32"""
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
        *(("horizontal", 2),
          ("invalid", 1),
          ("last", 4),
          ("uplink", 3))
    )


_CsfDtlLinkType_Type.__name__ = "Integer32"
_CsfDtlLinkType_Object = MibTableColumn
csfDtlLinkType = _CsfDtlLinkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 1, 3, 2, 1, 4),
    _CsfDtlLinkType_Type()
)
csfDtlLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfDtlLinkType.setStatus("current")
_CiscoSigFailMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSigFailMIBConformance = _CiscoSigFailMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 3)
)
_CiscoSigFailMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSigFailMIBCompliances = _CiscoSigFailMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 3, 1)
)
_CiscoSigFailMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSigFailMIBGroups = _CiscoSigFailMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 3, 2)
)

# Managed Objects groups

ciscoSigFailGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 3, 2, 1)
)
ciscoSigFailGeneralGroup.setObjects(
    ("CISCO-ATM-SIG-DIAG-MIB", "csfFilterControl")
)
if mibBuilder.loadTexts:
    ciscoSigFailGeneralGroup.setStatus("current")

ciscoSigFailMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 3, 2, 2)
)
ciscoSigFailMIBGroup.setObjects(
      *(("CISCO-ATM-SIG-DIAG-MIB", "csfFilterScope"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfFilterConnKind"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfFilterConnCastType"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfFilterServiceCategory"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfFilterInInterface"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfFilterOutInterface"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfFilterCause"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfFilterCallingParty"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfFilterCallingPartyMask"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfFilterCalledParty"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfFilterCalledPartyMask"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfFilterMaxRecords"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfFilterAgeTimeout"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfFilterPurge"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfFilterNumMatches"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfFilterRowStatus"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfRecordScope"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfRecordConnKind"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfRecordConnCastType"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfRecordConnIndicator"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfRecordServiceCategory"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfRecordInInterface"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfRecordOutInterface"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfRecordCause"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfRecordDiags"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfRecordCallingParty"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfRecordCallingPartySubAddress"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfRecordCalledParty"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfRecordCalledPartySubAddress"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfRecordCrankBackTransitType"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfRecordCrankBackNodeId"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfRecordCrankBackSucceedingNodeId"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfRecordCrankBackPortId"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfRecordTimeStamp"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfDtlNodeId"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfDtlPortId"),
        ("CISCO-ATM-SIG-DIAG-MIB", "csfDtlLinkType"))
)
if mibBuilder.loadTexts:
    ciscoSigFailMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoSigFailMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 78, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSigFailMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-SIG-DIAG-MIB",
    **{"AtmAddr": AtmAddr,
       "ciscoAtmSigDiagMIB": ciscoAtmSigDiagMIB,
       "ciscoSigFailMIBObjects": ciscoSigFailMIBObjects,
       "csfBaseGroup": csfBaseGroup,
       "csfFilterControl": csfFilterControl,
       "csfFilterGroup": csfFilterGroup,
       "csfFilterTable": csfFilterTable,
       "csfFilterEntry": csfFilterEntry,
       "csfFilterIndex": csfFilterIndex,
       "csfFilterScope": csfFilterScope,
       "csfFilterConnKind": csfFilterConnKind,
       "csfFilterConnCastType": csfFilterConnCastType,
       "csfFilterServiceCategory": csfFilterServiceCategory,
       "csfFilterInInterface": csfFilterInInterface,
       "csfFilterOutInterface": csfFilterOutInterface,
       "csfFilterCause": csfFilterCause,
       "csfFilterCallingParty": csfFilterCallingParty,
       "csfFilterCallingPartyMask": csfFilterCallingPartyMask,
       "csfFilterCalledParty": csfFilterCalledParty,
       "csfFilterCalledPartyMask": csfFilterCalledPartyMask,
       "csfFilterMaxRecords": csfFilterMaxRecords,
       "csfFilterAgeTimeout": csfFilterAgeTimeout,
       "csfFilterPurge": csfFilterPurge,
       "csfFilterNumMatches": csfFilterNumMatches,
       "csfFilterRowStatus": csfFilterRowStatus,
       "csfRecordGroup": csfRecordGroup,
       "csfRecordTable": csfRecordTable,
       "csfRecordEntry": csfRecordEntry,
       "csfRecordIndex": csfRecordIndex,
       "csfRecordScope": csfRecordScope,
       "csfRecordConnKind": csfRecordConnKind,
       "csfRecordConnCastType": csfRecordConnCastType,
       "csfRecordConnIndicator": csfRecordConnIndicator,
       "csfRecordServiceCategory": csfRecordServiceCategory,
       "csfRecordInInterface": csfRecordInInterface,
       "csfRecordOutInterface": csfRecordOutInterface,
       "csfRecordCause": csfRecordCause,
       "csfRecordDiags": csfRecordDiags,
       "csfRecordCallingParty": csfRecordCallingParty,
       "csfRecordCallingPartySubAddress": csfRecordCallingPartySubAddress,
       "csfRecordCalledParty": csfRecordCalledParty,
       "csfRecordCalledPartySubAddress": csfRecordCalledPartySubAddress,
       "csfRecordCrankBackTransitType": csfRecordCrankBackTransitType,
       "csfRecordCrankBackNodeId": csfRecordCrankBackNodeId,
       "csfRecordCrankBackPortId": csfRecordCrankBackPortId,
       "csfRecordCrankBackSucceedingNodeId": csfRecordCrankBackSucceedingNodeId,
       "csfRecordTimeStamp": csfRecordTimeStamp,
       "csfDtlTable": csfDtlTable,
       "csfDtlEntry": csfDtlEntry,
       "csfDtlEntryIndex": csfDtlEntryIndex,
       "csfDtlNodeId": csfDtlNodeId,
       "csfDtlPortId": csfDtlPortId,
       "csfDtlLinkType": csfDtlLinkType,
       "ciscoSigFailMIBConformance": ciscoSigFailMIBConformance,
       "ciscoSigFailMIBCompliances": ciscoSigFailMIBCompliances,
       "ciscoSigFailMIBCompliance": ciscoSigFailMIBCompliance,
       "ciscoSigFailMIBGroups": ciscoSigFailMIBGroups,
       "ciscoSigFailGeneralGroup": ciscoSigFailGeneralGroup,
       "ciscoSigFailMIBGroup": ciscoSigFailMIBGroup}
)
