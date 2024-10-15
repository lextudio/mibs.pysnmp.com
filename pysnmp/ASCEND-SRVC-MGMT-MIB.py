# SNMP MIB module (ASCEND-SRVC-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-SRVC-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:43 2024
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

(srvcMgmtGroup,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "srvcMgmtGroup")

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

_DnisMgmt_ObjectIdentity = ObjectIdentity
dnisMgmt = _DnisMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 26, 1)
)


class _DnisMgmtGlobalEnabled_Type(Integer32):
    """Custom type dnisMgmtGlobalEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_DnisMgmtGlobalEnabled_Type.__name__ = "Integer32"
_DnisMgmtGlobalEnabled_Object = MibScalar
dnisMgmtGlobalEnabled = _DnisMgmtGlobalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 26, 1, 1),
    _DnisMgmtGlobalEnabled_Type()
)
dnisMgmtGlobalEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnisMgmtGlobalEnabled.setStatus("deprecated")
_DnisMgmtGlobalNumEntries_Type = Integer32
_DnisMgmtGlobalNumEntries_Object = MibScalar
dnisMgmtGlobalNumEntries = _DnisMgmtGlobalNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 529, 26, 1, 2),
    _DnisMgmtGlobalNumEntries_Type()
)
dnisMgmtGlobalNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnisMgmtGlobalNumEntries.setStatus("mandatory")
_DnisMgmtGlobalLastChange_Type = TimeTicks
_DnisMgmtGlobalLastChange_Object = MibScalar
dnisMgmtGlobalLastChange = _DnisMgmtGlobalLastChange_Object(
    (1, 3, 6, 1, 4, 1, 529, 26, 1, 3),
    _DnisMgmtGlobalLastChange_Type()
)
dnisMgmtGlobalLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnisMgmtGlobalLastChange.setStatus("mandatory")
_DnisMgmtGlobalTable_Object = MibTable
dnisMgmtGlobalTable = _DnisMgmtGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 26, 1, 4)
)
if mibBuilder.loadTexts:
    dnisMgmtGlobalTable.setStatus("mandatory")
_DnisMgmtGlobalEntry_Object = MibTableRow
dnisMgmtGlobalEntry = _DnisMgmtGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 26, 1, 4, 1)
)
dnisMgmtGlobalEntry.setIndexNames(
    (0, "ASCEND-SRVC-MGMT-MIB", "dnisGlobalPhoneNumber"),
)
if mibBuilder.loadTexts:
    dnisMgmtGlobalEntry.setStatus("mandatory")
_DnisGlobalIndex_Type = Integer32
_DnisGlobalIndex_Object = MibTableColumn
dnisGlobalIndex = _DnisGlobalIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 26, 1, 4, 1, 1),
    _DnisGlobalIndex_Type()
)
dnisGlobalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnisGlobalIndex.setStatus("deprecated")


class _DnisGlobalPhoneNumber_Type(DisplayString):
    """Custom type dnisGlobalPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 24),
    )


_DnisGlobalPhoneNumber_Type.__name__ = "DisplayString"
_DnisGlobalPhoneNumber_Object = MibTableColumn
dnisGlobalPhoneNumber = _DnisGlobalPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 26, 1, 4, 1, 2),
    _DnisGlobalPhoneNumber_Type()
)
dnisGlobalPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnisGlobalPhoneNumber.setStatus("mandatory")


class _DnisGlobalStatus_Type(Integer32):
    """Custom type dnisGlobalStatus based on Integer32"""
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


_DnisGlobalStatus_Type.__name__ = "Integer32"
_DnisGlobalStatus_Object = MibTableColumn
dnisGlobalStatus = _DnisGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 26, 1, 4, 1, 3),
    _DnisGlobalStatus_Type()
)
dnisGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnisGlobalStatus.setStatus("mandatory")
_DnisGlobalCallsAccepted_Type = Counter32
_DnisGlobalCallsAccepted_Object = MibTableColumn
dnisGlobalCallsAccepted = _DnisGlobalCallsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 529, 26, 1, 4, 1, 4),
    _DnisGlobalCallsAccepted_Type()
)
dnisGlobalCallsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnisGlobalCallsAccepted.setStatus("mandatory")
_DnisGlobalCallsDropped_Type = Counter32
_DnisGlobalCallsDropped_Object = MibTableColumn
dnisGlobalCallsDropped = _DnisGlobalCallsDropped_Object(
    (1, 3, 6, 1, 4, 1, 529, 26, 1, 4, 1, 5),
    _DnisGlobalCallsDropped_Type()
)
dnisGlobalCallsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnisGlobalCallsDropped.setStatus("mandatory")


class _DnisGlobalAction_Type(Integer32):
    """Custom type dnisGlobalAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 2),
          ("destroy", 3),
          ("noAction", 1))
    )


_DnisGlobalAction_Type.__name__ = "Integer32"
_DnisGlobalAction_Object = MibTableColumn
dnisGlobalAction = _DnisGlobalAction_Object(
    (1, 3, 6, 1, 4, 1, 529, 26, 1, 4, 1, 6),
    _DnisGlobalAction_Type()
)
dnisGlobalAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnisGlobalAction.setStatus("mandatory")


class _DnisGlobalStatusTimeout_Type(TimeTicks):
    """Custom type dnisGlobalStatusTimeout based on TimeTicks"""
    defaultValue = 360000


_DnisGlobalStatusTimeout_Object = MibTableColumn
dnisGlobalStatusTimeout = _DnisGlobalStatusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 26, 1, 4, 1, 7),
    _DnisGlobalStatusTimeout_Type()
)
dnisGlobalStatusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnisGlobalStatusTimeout.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-SRVC-MGMT-MIB",
    **{"dnisMgmt": dnisMgmt,
       "dnisMgmtGlobalEnabled": dnisMgmtGlobalEnabled,
       "dnisMgmtGlobalNumEntries": dnisMgmtGlobalNumEntries,
       "dnisMgmtGlobalLastChange": dnisMgmtGlobalLastChange,
       "dnisMgmtGlobalTable": dnisMgmtGlobalTable,
       "dnisMgmtGlobalEntry": dnisMgmtGlobalEntry,
       "dnisGlobalIndex": dnisGlobalIndex,
       "dnisGlobalPhoneNumber": dnisGlobalPhoneNumber,
       "dnisGlobalStatus": dnisGlobalStatus,
       "dnisGlobalCallsAccepted": dnisGlobalCallsAccepted,
       "dnisGlobalCallsDropped": dnisGlobalCallsDropped,
       "dnisGlobalAction": dnisGlobalAction,
       "dnisGlobalStatusTimeout": dnisGlobalStatusTimeout}
)
