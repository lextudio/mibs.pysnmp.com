# SNMP MIB module (Wellfleet-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:22 2024
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

(wfIfGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfIfGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfIf_ObjectIdentity = ObjectIdentity
wfIf = _WfIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 1)
)
_WfIfNumber_Type = Integer32
_WfIfNumber_Object = MibScalar
wfIfNumber = _WfIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 1, 1),
    _WfIfNumber_Type()
)
wfIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfNumber.setStatus("mandatory")


class _WfIfRegistrationMode_Type(Integer32):
    """Custom type wfIfRegistrationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dialcircuitunique", 2),
          ("wellfleetstandard", 1))
    )


_WfIfRegistrationMode_Type.__name__ = "Integer32"
_WfIfRegistrationMode_Object = MibScalar
wfIfRegistrationMode = _WfIfRegistrationMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 1, 2),
    _WfIfRegistrationMode_Type()
)
wfIfRegistrationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfRegistrationMode.setStatus("mandatory")
_WfIfTable_Object = MibTable
wfIfTable = _WfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2)
)
if mibBuilder.loadTexts:
    wfIfTable.setStatus("mandatory")
_WfIfEntry_Object = MibTableRow
wfIfEntry = _WfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1)
)
wfIfEntry.setIndexNames(
    (0, "Wellfleet-IF-MIB", "wfIfIndex"),
)
if mibBuilder.loadTexts:
    wfIfEntry.setStatus("mandatory")
_WfIfIndex_Type = Integer32
_WfIfIndex_Object = MibTableColumn
wfIfIndex = _WfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 1),
    _WfIfIndex_Type()
)
wfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfIndex.setStatus("mandatory")
_WfIfDescr_Type = DisplayString
_WfIfDescr_Object = MibTableColumn
wfIfDescr = _WfIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 2),
    _WfIfDescr_Type()
)
wfIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfDescr.setStatus("mandatory")
_WfIfType_Type = Integer32
_WfIfType_Object = MibTableColumn
wfIfType = _WfIfType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 3),
    _WfIfType_Type()
)
wfIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfType.setStatus("mandatory")
_WfIfMtu_Type = Integer32
_WfIfMtu_Object = MibTableColumn
wfIfMtu = _WfIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 4),
    _WfIfMtu_Type()
)
wfIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfMtu.setStatus("mandatory")
_WfIfSpeed_Type = Gauge32
_WfIfSpeed_Object = MibTableColumn
wfIfSpeed = _WfIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 5),
    _WfIfSpeed_Type()
)
wfIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfSpeed.setStatus("mandatory")
_WfIfPhysAddress_Type = OctetString
_WfIfPhysAddress_Object = MibTableColumn
wfIfPhysAddress = _WfIfPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 6),
    _WfIfPhysAddress_Type()
)
wfIfPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfPhysAddress.setStatus("mandatory")
_WfIfAdminStatus_Type = Integer32
_WfIfAdminStatus_Object = MibTableColumn
wfIfAdminStatus = _WfIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 7),
    _WfIfAdminStatus_Type()
)
wfIfAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfAdminStatus.setStatus("mandatory")
_WfIfOperStatus_Type = Integer32
_WfIfOperStatus_Object = MibTableColumn
wfIfOperStatus = _WfIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 8),
    _WfIfOperStatus_Type()
)
wfIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfOperStatus.setStatus("mandatory")
_WfIfLastChange_Type = TimeTicks
_WfIfLastChange_Object = MibTableColumn
wfIfLastChange = _WfIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 9),
    _WfIfLastChange_Type()
)
wfIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfLastChange.setStatus("mandatory")
_WfIfInOctets_Type = Counter32
_WfIfInOctets_Object = MibTableColumn
wfIfInOctets = _WfIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 10),
    _WfIfInOctets_Type()
)
wfIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfInOctets.setStatus("mandatory")
_WfIfInUcastPkts_Type = Counter32
_WfIfInUcastPkts_Object = MibTableColumn
wfIfInUcastPkts = _WfIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 11),
    _WfIfInUcastPkts_Type()
)
wfIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfInUcastPkts.setStatus("mandatory")
_WfIfInNUCastPkts_Type = Counter32
_WfIfInNUCastPkts_Object = MibTableColumn
wfIfInNUCastPkts = _WfIfInNUCastPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 12),
    _WfIfInNUCastPkts_Type()
)
wfIfInNUCastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfInNUCastPkts.setStatus("mandatory")
_WfIfInDiscards_Type = Counter32
_WfIfInDiscards_Object = MibTableColumn
wfIfInDiscards = _WfIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 13),
    _WfIfInDiscards_Type()
)
wfIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfInDiscards.setStatus("mandatory")
_WfIfInErrors_Type = Counter32
_WfIfInErrors_Object = MibTableColumn
wfIfInErrors = _WfIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 14),
    _WfIfInErrors_Type()
)
wfIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfInErrors.setStatus("mandatory")
_WfIfInUnknownProtos_Type = Counter32
_WfIfInUnknownProtos_Object = MibTableColumn
wfIfInUnknownProtos = _WfIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 15),
    _WfIfInUnknownProtos_Type()
)
wfIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfInUnknownProtos.setStatus("mandatory")
_WfIfOutOctets_Type = Counter32
_WfIfOutOctets_Object = MibTableColumn
wfIfOutOctets = _WfIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 16),
    _WfIfOutOctets_Type()
)
wfIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfOutOctets.setStatus("mandatory")
_WfIfOutUcastPkts_Type = Counter32
_WfIfOutUcastPkts_Object = MibTableColumn
wfIfOutUcastPkts = _WfIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 17),
    _WfIfOutUcastPkts_Type()
)
wfIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfOutUcastPkts.setStatus("mandatory")
_WfIfOutNUcastPkts_Type = Counter32
_WfIfOutNUcastPkts_Object = MibTableColumn
wfIfOutNUcastPkts = _WfIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 18),
    _WfIfOutNUcastPkts_Type()
)
wfIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfOutNUcastPkts.setStatus("mandatory")
_WfIfOutDiscards_Type = Counter32
_WfIfOutDiscards_Object = MibTableColumn
wfIfOutDiscards = _WfIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 19),
    _WfIfOutDiscards_Type()
)
wfIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfOutDiscards.setStatus("mandatory")
_WfIfOutErrors_Type = Counter32
_WfIfOutErrors_Object = MibTableColumn
wfIfOutErrors = _WfIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 20),
    _WfIfOutErrors_Type()
)
wfIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfOutErrors.setStatus("mandatory")
_WfIfOutQLen_Type = Gauge32
_WfIfOutQLen_Object = MibTableColumn
wfIfOutQLen = _WfIfOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 21),
    _WfIfOutQLen_Type()
)
wfIfOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfOutQLen.setStatus("mandatory")
_WfIfSpecific_Type = ObjectIdentifier
_WfIfSpecific_Object = MibTableColumn
wfIfSpecific = _WfIfSpecific_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 22),
    _WfIfSpecific_Type()
)
wfIfSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfSpecific.setStatus("mandatory")
_WfIfCfgTable_Object = MibTable
wfIfCfgTable = _WfIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 3)
)
if mibBuilder.loadTexts:
    wfIfCfgTable.setStatus("mandatory")
_WfIfCfgEntry_Object = MibTableRow
wfIfCfgEntry = _WfIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 3, 1)
)
wfIfCfgEntry.setIndexNames(
    (0, "Wellfleet-IF-MIB", "wfIfCfgIndex"),
)
if mibBuilder.loadTexts:
    wfIfCfgEntry.setStatus("mandatory")


class _WfIfCfgIndex_Type(Integer32):
    """Custom type wfIfCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WfIfCfgIndex_Type.__name__ = "Integer32"
_WfIfCfgIndex_Object = MibTableColumn
wfIfCfgIndex = _WfIfCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 3, 1, 1),
    _WfIfCfgIndex_Type()
)
wfIfCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfCfgIndex.setStatus("mandatory")


class _WfIfCfgConformanceTesting_Type(Integer32):
    """Custom type wfIfCfgConformanceTesting based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIfCfgConformanceTesting_Type.__name__ = "Integer32"
_WfIfCfgConformanceTesting_Object = MibTableColumn
wfIfCfgConformanceTesting = _WfIfCfgConformanceTesting_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 3, 1, 2),
    _WfIfCfgConformanceTesting_Type()
)
wfIfCfgConformanceTesting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfCfgConformanceTesting.setStatus("mandatory")


class _WfIfCfgSparseTableAdminStatus_Type(Integer32):
    """Custom type wfIfCfgSparseTableAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("zerofill", 2))
    )


_WfIfCfgSparseTableAdminStatus_Type.__name__ = "Integer32"
_WfIfCfgSparseTableAdminStatus_Object = MibTableColumn
wfIfCfgSparseTableAdminStatus = _WfIfCfgSparseTableAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 3, 1, 3),
    _WfIfCfgSparseTableAdminStatus_Type()
)
wfIfCfgSparseTableAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfCfgSparseTableAdminStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-IF-MIB",
    **{"wfIf": wfIf,
       "wfIfNumber": wfIfNumber,
       "wfIfRegistrationMode": wfIfRegistrationMode,
       "wfIfTable": wfIfTable,
       "wfIfEntry": wfIfEntry,
       "wfIfIndex": wfIfIndex,
       "wfIfDescr": wfIfDescr,
       "wfIfType": wfIfType,
       "wfIfMtu": wfIfMtu,
       "wfIfSpeed": wfIfSpeed,
       "wfIfPhysAddress": wfIfPhysAddress,
       "wfIfAdminStatus": wfIfAdminStatus,
       "wfIfOperStatus": wfIfOperStatus,
       "wfIfLastChange": wfIfLastChange,
       "wfIfInOctets": wfIfInOctets,
       "wfIfInUcastPkts": wfIfInUcastPkts,
       "wfIfInNUCastPkts": wfIfInNUCastPkts,
       "wfIfInDiscards": wfIfInDiscards,
       "wfIfInErrors": wfIfInErrors,
       "wfIfInUnknownProtos": wfIfInUnknownProtos,
       "wfIfOutOctets": wfIfOutOctets,
       "wfIfOutUcastPkts": wfIfOutUcastPkts,
       "wfIfOutNUcastPkts": wfIfOutNUcastPkts,
       "wfIfOutDiscards": wfIfOutDiscards,
       "wfIfOutErrors": wfIfOutErrors,
       "wfIfOutQLen": wfIfOutQLen,
       "wfIfSpecific": wfIfSpecific,
       "wfIfCfgTable": wfIfCfgTable,
       "wfIfCfgEntry": wfIfCfgEntry,
       "wfIfCfgIndex": wfIfCfgIndex,
       "wfIfCfgConformanceTesting": wfIfCfgConformanceTesting,
       "wfIfCfgSparseTableAdminStatus": wfIfCfgSparseTableAdminStatus}
)
