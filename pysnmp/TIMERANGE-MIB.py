# SNMP MIB module (TIMERANGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMERANGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:20 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swTimeRangeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 50)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwTimeRangeCtrl_ObjectIdentity = ObjectIdentity
swTimeRangeCtrl = _SwTimeRangeCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 50, 1)
)
_SwTimeRangeInfo_ObjectIdentity = ObjectIdentity
swTimeRangeInfo = _SwTimeRangeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 50, 2)
)
_SwTimeRangeMgmt_ObjectIdentity = ObjectIdentity
swTimeRangeMgmt = _SwTimeRangeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 50, 3)
)
_SwTimeRangeMgmtTable_Object = MibTable
swTimeRangeMgmtTable = _SwTimeRangeMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 1)
)
if mibBuilder.loadTexts:
    swTimeRangeMgmtTable.setStatus("current")
_SwTimeRangeMgmtEntry_Object = MibTableRow
swTimeRangeMgmtEntry = _SwTimeRangeMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 1, 1)
)
swTimeRangeMgmtEntry.setIndexNames(
    (0, "TIMERANGE-MIB", "swTimeRangeMgmtRangeName"),
)
if mibBuilder.loadTexts:
    swTimeRangeMgmtEntry.setStatus("current")


class _SwTimeRangeMgmtRangeName_Type(DisplayString):
    """Custom type swTimeRangeMgmtRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwTimeRangeMgmtRangeName_Type.__name__ = "DisplayString"
_SwTimeRangeMgmtRangeName_Object = MibTableColumn
swTimeRangeMgmtRangeName = _SwTimeRangeMgmtRangeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 1, 1, 1),
    _SwTimeRangeMgmtRangeName_Type()
)
swTimeRangeMgmtRangeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTimeRangeMgmtRangeName.setStatus("current")
_SwTimeRangeMgmtSelectDays_Type = DisplayString
_SwTimeRangeMgmtSelectDays_Object = MibTableColumn
swTimeRangeMgmtSelectDays = _SwTimeRangeMgmtSelectDays_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 1, 1, 2),
    _SwTimeRangeMgmtSelectDays_Type()
)
swTimeRangeMgmtSelectDays.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swTimeRangeMgmtSelectDays.setStatus("current")


class _SwTimeRangeMgmtStartTime_Type(DisplayString):
    """Custom type swTimeRangeMgmtStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwTimeRangeMgmtStartTime_Type.__name__ = "DisplayString"
_SwTimeRangeMgmtStartTime_Object = MibTableColumn
swTimeRangeMgmtStartTime = _SwTimeRangeMgmtStartTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 1, 1, 3),
    _SwTimeRangeMgmtStartTime_Type()
)
swTimeRangeMgmtStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swTimeRangeMgmtStartTime.setStatus("current")


class _SwTimeRangeMgmtEndTime_Type(DisplayString):
    """Custom type swTimeRangeMgmtEndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwTimeRangeMgmtEndTime_Type.__name__ = "DisplayString"
_SwTimeRangeMgmtEndTime_Object = MibTableColumn
swTimeRangeMgmtEndTime = _SwTimeRangeMgmtEndTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 1, 1, 4),
    _SwTimeRangeMgmtEndTime_Type()
)
swTimeRangeMgmtEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swTimeRangeMgmtEndTime.setStatus("current")
_SwTimeRangeMgmtStatus_Type = RowStatus
_SwTimeRangeMgmtStatus_Object = MibTableColumn
swTimeRangeMgmtStatus = _SwTimeRangeMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 1, 1, 5),
    _SwTimeRangeMgmtStatus_Type()
)
swTimeRangeMgmtStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swTimeRangeMgmtStatus.setStatus("current")
_SwTimeRangeACLTable_Object = MibTable
swTimeRangeACLTable = _SwTimeRangeACLTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 2)
)
if mibBuilder.loadTexts:
    swTimeRangeACLTable.setStatus("current")
_SwTimeRangeACLEntry_Object = MibTableRow
swTimeRangeACLEntry = _SwTimeRangeACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 2, 1)
)
swTimeRangeACLEntry.setIndexNames(
    (0, "TIMERANGE-MIB", "swTimeRangeACLProfileID"),
    (0, "TIMERANGE-MIB", "swTimeRangeACLAccessID"),
)
if mibBuilder.loadTexts:
    swTimeRangeACLEntry.setStatus("current")
_SwTimeRangeACLProfileID_Type = Integer32
_SwTimeRangeACLProfileID_Object = MibTableColumn
swTimeRangeACLProfileID = _SwTimeRangeACLProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 2, 1, 1),
    _SwTimeRangeACLProfileID_Type()
)
swTimeRangeACLProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTimeRangeACLProfileID.setStatus("current")


class _SwTimeRangeACLAccessID_Type(Integer32):
    """Custom type swTimeRangeACLAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwTimeRangeACLAccessID_Type.__name__ = "Integer32"
_SwTimeRangeACLAccessID_Object = MibTableColumn
swTimeRangeACLAccessID = _SwTimeRangeACLAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 2, 1, 2),
    _SwTimeRangeACLAccessID_Type()
)
swTimeRangeACLAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTimeRangeACLAccessID.setStatus("current")


class _SwTimeRangeACLTimeRangeName_Type(DisplayString):
    """Custom type swTimeRangeACLTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwTimeRangeACLTimeRangeName_Type.__name__ = "DisplayString"
_SwTimeRangeACLTimeRangeName_Object = MibTableColumn
swTimeRangeACLTimeRangeName = _SwTimeRangeACLTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 2, 1, 3),
    _SwTimeRangeACLTimeRangeName_Type()
)
swTimeRangeACLTimeRangeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTimeRangeACLTimeRangeName.setStatus("current")
_SwTimeRangeCPUACLTable_Object = MibTable
swTimeRangeCPUACLTable = _SwTimeRangeCPUACLTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 3)
)
if mibBuilder.loadTexts:
    swTimeRangeCPUACLTable.setStatus("current")
_SwTimeRangeCPUACLEntry_Object = MibTableRow
swTimeRangeCPUACLEntry = _SwTimeRangeCPUACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 3, 1)
)
swTimeRangeCPUACLEntry.setIndexNames(
    (0, "TIMERANGE-MIB", "swTimeRangeCPUACLProfileID"),
    (0, "TIMERANGE-MIB", "swTimeRangeCPUACLAccessID"),
)
if mibBuilder.loadTexts:
    swTimeRangeCPUACLEntry.setStatus("current")
_SwTimeRangeCPUACLProfileID_Type = Integer32
_SwTimeRangeCPUACLProfileID_Object = MibTableColumn
swTimeRangeCPUACLProfileID = _SwTimeRangeCPUACLProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 3, 1, 1),
    _SwTimeRangeCPUACLProfileID_Type()
)
swTimeRangeCPUACLProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTimeRangeCPUACLProfileID.setStatus("current")


class _SwTimeRangeCPUACLAccessID_Type(Integer32):
    """Custom type swTimeRangeCPUACLAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwTimeRangeCPUACLAccessID_Type.__name__ = "Integer32"
_SwTimeRangeCPUACLAccessID_Object = MibTableColumn
swTimeRangeCPUACLAccessID = _SwTimeRangeCPUACLAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 3, 1, 2),
    _SwTimeRangeCPUACLAccessID_Type()
)
swTimeRangeCPUACLAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTimeRangeCPUACLAccessID.setStatus("current")


class _SwTimeRangeCPUACLTimeRangeName_Type(DisplayString):
    """Custom type swTimeRangeCPUACLTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwTimeRangeCPUACLTimeRangeName_Type.__name__ = "DisplayString"
_SwTimeRangeCPUACLTimeRangeName_Object = MibTableColumn
swTimeRangeCPUACLTimeRangeName = _SwTimeRangeCPUACLTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 3, 1, 3),
    _SwTimeRangeCPUACLTimeRangeName_Type()
)
swTimeRangeCPUACLTimeRangeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTimeRangeCPUACLTimeRangeName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMERANGE-MIB",
    **{"swTimeRangeMIB": swTimeRangeMIB,
       "swTimeRangeCtrl": swTimeRangeCtrl,
       "swTimeRangeInfo": swTimeRangeInfo,
       "swTimeRangeMgmt": swTimeRangeMgmt,
       "swTimeRangeMgmtTable": swTimeRangeMgmtTable,
       "swTimeRangeMgmtEntry": swTimeRangeMgmtEntry,
       "swTimeRangeMgmtRangeName": swTimeRangeMgmtRangeName,
       "swTimeRangeMgmtSelectDays": swTimeRangeMgmtSelectDays,
       "swTimeRangeMgmtStartTime": swTimeRangeMgmtStartTime,
       "swTimeRangeMgmtEndTime": swTimeRangeMgmtEndTime,
       "swTimeRangeMgmtStatus": swTimeRangeMgmtStatus,
       "swTimeRangeACLTable": swTimeRangeACLTable,
       "swTimeRangeACLEntry": swTimeRangeACLEntry,
       "swTimeRangeACLProfileID": swTimeRangeACLProfileID,
       "swTimeRangeACLAccessID": swTimeRangeACLAccessID,
       "swTimeRangeACLTimeRangeName": swTimeRangeACLTimeRangeName,
       "swTimeRangeCPUACLTable": swTimeRangeCPUACLTable,
       "swTimeRangeCPUACLEntry": swTimeRangeCPUACLEntry,
       "swTimeRangeCPUACLProfileID": swTimeRangeCPUACLProfileID,
       "swTimeRangeCPUACLAccessID": swTimeRangeCPUACLAccessID,
       "swTimeRangeCPUACLTimeRangeName": swTimeRangeCPUACLTimeRangeName}
)
