# SNMP MIB module (AT-XEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-XEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:38 2024
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

(sysinfo,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "sysinfo")

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

xem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11)
)
xem.setRevisions(
        ("2010-09-07 00:00",
         "2010-06-15 00:15",
         "2009-07-15 00:00",
         "2008-02-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XemTraps_ObjectIdentity = ObjectIdentity
xemTraps = _XemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 0)
)


class _XemNumOfXem_Type(Unsigned32):
    """Custom type xemNumOfXem based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_XemNumOfXem_Type.__name__ = "Unsigned32"
_XemNumOfXem_Object = MibScalar
xemNumOfXem = _XemNumOfXem_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 1),
    _XemNumOfXem_Type()
)
xemNumOfXem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xemNumOfXem.setStatus("current")
_XemInfoTable_Object = MibTable
xemInfoTable = _XemInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2)
)
if mibBuilder.loadTexts:
    xemInfoTable.setStatus("current")
_XemInfoEntry_Object = MibTableRow
xemInfoEntry = _XemInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1)
)
xemInfoEntry.setIndexNames(
    (0, "AT-XEM-MIB", "xemInfoMemberId"),
    (0, "AT-XEM-MIB", "xemInfoBayId"),
)
if mibBuilder.loadTexts:
    xemInfoEntry.setStatus("current")


class _XemInfoMemberId_Type(Unsigned32):
    """Custom type xemInfoMemberId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_XemInfoMemberId_Type.__name__ = "Unsigned32"
_XemInfoMemberId_Object = MibTableColumn
xemInfoMemberId = _XemInfoMemberId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 1),
    _XemInfoMemberId_Type()
)
xemInfoMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xemInfoMemberId.setStatus("current")


class _XemInfoBayId_Type(Unsigned32):
    """Custom type xemInfoBayId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_XemInfoBayId_Type.__name__ = "Unsigned32"
_XemInfoBayId_Object = MibTableColumn
xemInfoBayId = _XemInfoBayId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 2),
    _XemInfoBayId_Type()
)
xemInfoBayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xemInfoBayId.setStatus("current")


class _XemInfoXemId_Type(Unsigned32):
    """Custom type xemInfoXemId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XemInfoXemId_Type.__name__ = "Unsigned32"
_XemInfoXemId_Object = MibTableColumn
xemInfoXemId = _XemInfoXemId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 3),
    _XemInfoXemId_Type()
)
xemInfoXemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xemInfoXemId.setStatus("current")
_XemInfoBoardType_Type = DisplayString
_XemInfoBoardType_Object = MibTableColumn
xemInfoBoardType = _XemInfoBoardType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 4),
    _XemInfoBoardType_Type()
)
xemInfoBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xemInfoBoardType.setStatus("current")


class _XemInfoBoardName_Type(DisplayString):
    """Custom type xemInfoBoardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_XemInfoBoardName_Type.__name__ = "DisplayString"
_XemInfoBoardName_Object = MibTableColumn
xemInfoBoardName = _XemInfoBoardName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 5),
    _XemInfoBoardName_Type()
)
xemInfoBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xemInfoBoardName.setStatus("current")


class _XemInfoRevision_Type(DisplayString):
    """Custom type xemInfoRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_XemInfoRevision_Type.__name__ = "DisplayString"
_XemInfoRevision_Object = MibTableColumn
xemInfoRevision = _XemInfoRevision_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 6),
    _XemInfoRevision_Type()
)
xemInfoRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xemInfoRevision.setStatus("current")


class _XemInfoSerialNumber_Type(DisplayString):
    """Custom type xemInfoSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_XemInfoSerialNumber_Type.__name__ = "DisplayString"
_XemInfoSerialNumber_Object = MibTableColumn
xemInfoSerialNumber = _XemInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 7),
    _XemInfoSerialNumber_Type()
)
xemInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xemInfoSerialNumber.setStatus("current")

# Managed Objects groups


# Notification objects

xemInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 0, 1)
)
xemInserted.setObjects(
      *(("AT-XEM-MIB", "xemInfoMemberId"),
        ("AT-XEM-MIB", "xemInfoBayId"))
)
if mibBuilder.loadTexts:
    xemInserted.setStatus(
        "current"
    )

xemRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 0, 2)
)
xemRemoved.setObjects(
      *(("AT-XEM-MIB", "xemInfoMemberId"),
        ("AT-XEM-MIB", "xemInfoBayId"))
)
if mibBuilder.loadTexts:
    xemRemoved.setStatus(
        "current"
    )

xemInsertedFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 0, 3)
)
xemInsertedFail.setObjects(
      *(("AT-XEM-MIB", "xemInfoMemberId"),
        ("AT-XEM-MIB", "xemInfoBayId"))
)
if mibBuilder.loadTexts:
    xemInsertedFail.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-XEM-MIB",
    **{"xem": xem,
       "xemTraps": xemTraps,
       "xemInserted": xemInserted,
       "xemRemoved": xemRemoved,
       "xemInsertedFail": xemInsertedFail,
       "xemNumOfXem": xemNumOfXem,
       "xemInfoTable": xemInfoTable,
       "xemInfoEntry": xemInfoEntry,
       "xemInfoMemberId": xemInfoMemberId,
       "xemInfoBayId": xemInfoBayId,
       "xemInfoXemId": xemInfoXemId,
       "xemInfoBoardType": xemInfoBoardType,
       "xemInfoBoardName": xemInfoBoardName,
       "xemInfoRevision": xemInfoRevision,
       "xemInfoSerialNumber": xemInfoSerialNumber}
)
