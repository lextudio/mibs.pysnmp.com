# SNMP MIB module (ACC-SMDS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-SMDS
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:59 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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

_AccSMDS_ObjectIdentity = ObjectIdentity
accSMDS = _AccSMDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26)
)
_AccSmdsPortTable_Object = MibTable
accSmdsPortTable = _AccSmdsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 1)
)
if mibBuilder.loadTexts:
    accSmdsPortTable.setStatus("mandatory")
_AccSmdsPortEntry_Object = MibTableRow
accSmdsPortEntry = _AccSmdsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 1, 1)
)
accSmdsPortEntry.setIndexNames(
    (0, "ACC-SMDS", "accSmdsPortIndex"),
)
if mibBuilder.loadTexts:
    accSmdsPortEntry.setStatus("mandatory")


class _AccSmdsPortIndex_Type(Integer32):
    """Custom type accSmdsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccSmdsPortIndex_Type.__name__ = "Integer32"
_AccSmdsPortIndex_Object = MibTableColumn
accSmdsPortIndex = _AccSmdsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 1, 1, 1),
    _AccSmdsPortIndex_Type()
)
accSmdsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSmdsPortIndex.setStatus("mandatory")
_AccSmdsPortIA_Type = SmdsAddress
_AccSmdsPortIA_Object = MibTableColumn
accSmdsPortIA = _AccSmdsPortIA_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 1, 1, 2),
    _AccSmdsPortIA_Type()
)
accSmdsPortIA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSmdsPortIA.setStatus("mandatory")


class _AccSmdsPortPollingStatus_Type(Integer32):
    """Custom type accSmdsPortPollingStatus based on Integer32"""
    defaultValue = 2

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


_AccSmdsPortPollingStatus_Type.__name__ = "Integer32"
_AccSmdsPortPollingStatus_Object = MibTableColumn
accSmdsPortPollingStatus = _AccSmdsPortPollingStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 1, 1, 3),
    _AccSmdsPortPollingStatus_Type()
)
accSmdsPortPollingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSmdsPortPollingStatus.setStatus("mandatory")
_AccSipL3Table_Object = MibTable
accSipL3Table = _AccSipL3Table_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 2)
)
if mibBuilder.loadTexts:
    accSipL3Table.setStatus("mandatory")
_AccSipL3Entry_Object = MibTableRow
accSipL3Entry = _AccSipL3Entry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 2, 1)
)
accSipL3Entry.setIndexNames(
    (0, "ACC-SMDS", "accSipL3Index"),
)
if mibBuilder.loadTexts:
    accSipL3Entry.setStatus("mandatory")


class _AccSipL3Index_Type(Integer32):
    """Custom type accSipL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccSipL3Index_Type.__name__ = "Integer32"
_AccSipL3Index_Object = MibTableColumn
accSipL3Index = _AccSipL3Index_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 2, 1, 1),
    _AccSipL3Index_Type()
)
accSipL3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSipL3Index.setStatus("mandatory")
_AccSipL3RcvIAs_Type = Counter32
_AccSipL3RcvIAs_Object = MibTableColumn
accSipL3RcvIAs = _AccSipL3RcvIAs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 2, 1, 2),
    _AccSipL3RcvIAs_Type()
)
accSipL3RcvIAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSipL3RcvIAs.setStatus("mandatory")
_AccSipL3RcvGAs_Type = Counter32
_AccSipL3RcvGAs_Object = MibTableColumn
accSipL3RcvGAs = _AccSipL3RcvGAs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 2, 1, 3),
    _AccSipL3RcvGAs_Type()
)
accSipL3RcvGAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSipL3RcvGAs.setStatus("mandatory")
_AccSipL3UnkIAs_Type = Counter32
_AccSipL3UnkIAs_Object = MibTableColumn
accSipL3UnkIAs = _AccSipL3UnkIAs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 2, 1, 4),
    _AccSipL3UnkIAs_Type()
)
accSipL3UnkIAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSipL3UnkIAs.setStatus("mandatory")
_AccSipL3UnkGAs_Type = Counter32
_AccSipL3UnkGAs_Object = MibTableColumn
accSipL3UnkGAs = _AccSipL3UnkGAs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 2, 1, 5),
    _AccSipL3UnkGAs_Type()
)
accSipL3UnkGAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSipL3UnkGAs.setStatus("mandatory")
_AccSipL3SndIAs_Type = Counter32
_AccSipL3SndIAs_Object = MibTableColumn
accSipL3SndIAs = _AccSipL3SndIAs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 2, 1, 6),
    _AccSipL3SndIAs_Type()
)
accSipL3SndIAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSipL3SndIAs.setStatus("mandatory")
_AccSipL3SndGAs_Type = Counter32
_AccSipL3SndGAs_Object = MibTableColumn
accSipL3SndGAs = _AccSipL3SndGAs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 2, 1, 7),
    _AccSipL3SndGAs_Type()
)
accSipL3SndGAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSipL3SndGAs.setStatus("mandatory")
_AccSipL3Errors_Type = Counter32
_AccSipL3Errors_Object = MibTableColumn
accSipL3Errors = _AccSipL3Errors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 2, 1, 8),
    _AccSipL3Errors_Type()
)
accSipL3Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSipL3Errors.setStatus("mandatory")
_AccSipL3InvAddrs_Type = Counter32
_AccSipL3InvAddrs_Object = MibTableColumn
accSipL3InvAddrs = _AccSipL3InvAddrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 2, 1, 9),
    _AccSipL3InvAddrs_Type()
)
accSipL3InvAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSipL3InvAddrs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-SMDS",
    **{"accSMDS": accSMDS,
       "accSmdsPortTable": accSmdsPortTable,
       "accSmdsPortEntry": accSmdsPortEntry,
       "accSmdsPortIndex": accSmdsPortIndex,
       "accSmdsPortIA": accSmdsPortIA,
       "accSmdsPortPollingStatus": accSmdsPortPollingStatus,
       "accSipL3Table": accSipL3Table,
       "accSipL3Entry": accSipL3Entry,
       "accSipL3Index": accSipL3Index,
       "accSipL3RcvIAs": accSipL3RcvIAs,
       "accSipL3RcvGAs": accSipL3RcvGAs,
       "accSipL3UnkIAs": accSipL3UnkIAs,
       "accSipL3UnkGAs": accSipL3UnkGAs,
       "accSipL3SndIAs": accSipL3SndIAs,
       "accSipL3SndGAs": accSipL3SndGAs,
       "accSipL3Errors": accSipL3Errors,
       "accSipL3InvAddrs": accSipL3InvAddrs}
)
