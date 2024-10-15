# SNMP MIB module (AT-RESOURCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-RESOURCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:31 2024
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

resource = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21)
)
resource.setRevisions(
        ("2012-09-21 00:00",
         "2012-05-22 03:00",
         "2010-06-15 00:15",
         "2009-10-22 23:00",
         "2008-10-20 10:00",
         "1920-08-09 04:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RscBoardTable_Object = MibTable
rscBoardTable = _RscBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1)
)
if mibBuilder.loadTexts:
    rscBoardTable.setStatus("current")
_RscBoardEntry_Object = MibTableRow
rscBoardEntry = _RscBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1)
)
rscBoardEntry.setIndexNames(
    (0, "AT-RESOURCE-MIB", "rscStkId"),
    (0, "AT-RESOURCE-MIB", "rscResourceId"),
)
if mibBuilder.loadTexts:
    rscBoardEntry.setStatus("current")


class _RscStkId_Type(Unsigned32):
    """Custom type rscStkId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_RscStkId_Type.__name__ = "Unsigned32"
_RscStkId_Object = MibTableColumn
rscStkId = _RscStkId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 1),
    _RscStkId_Type()
)
rscStkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rscStkId.setStatus("current")


class _RscResourceId_Type(Unsigned32):
    """Custom type rscResourceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967294),
    )


_RscResourceId_Type.__name__ = "Unsigned32"
_RscResourceId_Object = MibTableColumn
rscResourceId = _RscResourceId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 2),
    _RscResourceId_Type()
)
rscResourceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rscResourceId.setStatus("current")
_RscBoardType_Type = DisplayString
_RscBoardType_Object = MibTableColumn
rscBoardType = _RscBoardType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 3),
    _RscBoardType_Type()
)
rscBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rscBoardType.setStatus("current")
_RscBoardName_Type = DisplayString
_RscBoardName_Object = MibTableColumn
rscBoardName = _RscBoardName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 4),
    _RscBoardName_Type()
)
rscBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rscBoardName.setStatus("current")
_RscBoardID_Type = Unsigned32
_RscBoardID_Object = MibTableColumn
rscBoardID = _RscBoardID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 5),
    _RscBoardID_Type()
)
rscBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rscBoardID.setStatus("current")
_RscBoardBay_Type = DisplayString
_RscBoardBay_Object = MibTableColumn
rscBoardBay = _RscBoardBay_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 6),
    _RscBoardBay_Type()
)
rscBoardBay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rscBoardBay.setStatus("current")


class _RscBoardRevision_Type(DisplayString):
    """Custom type rscBoardRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_RscBoardRevision_Type.__name__ = "DisplayString"
_RscBoardRevision_Object = MibTableColumn
rscBoardRevision = _RscBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 7),
    _RscBoardRevision_Type()
)
rscBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rscBoardRevision.setStatus("current")
_RscBoardSerialNumber_Type = DisplayString
_RscBoardSerialNumber_Object = MibTableColumn
rscBoardSerialNumber = _RscBoardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 8),
    _RscBoardSerialNumber_Type()
)
rscBoardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rscBoardSerialNumber.setStatus("current")
_HostInfoTable_Object = MibTable
hostInfoTable = _HostInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 2)
)
if mibBuilder.loadTexts:
    hostInfoTable.setStatus("current")
_HostInfoEntry_Object = MibTableRow
hostInfoEntry = _HostInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 2, 1)
)
hostInfoEntry.setIndexNames(
    (0, "AT-RESOURCE-MIB", "rscStkId"),
)
if mibBuilder.loadTexts:
    hostInfoEntry.setStatus("current")
_HostInfoDRAM_Type = DisplayString
_HostInfoDRAM_Object = MibTableColumn
hostInfoDRAM = _HostInfoDRAM_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 2, 1, 1),
    _HostInfoDRAM_Type()
)
hostInfoDRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostInfoDRAM.setStatus("current")
_HostInfoFlash_Type = DisplayString
_HostInfoFlash_Object = MibTableColumn
hostInfoFlash = _HostInfoFlash_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 2, 1, 2),
    _HostInfoFlash_Type()
)
hostInfoFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostInfoFlash.setStatus("current")
_HostInfoUptime_Type = DisplayString
_HostInfoUptime_Object = MibTableColumn
hostInfoUptime = _HostInfoUptime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 2, 1, 3),
    _HostInfoUptime_Type()
)
hostInfoUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostInfoUptime.setStatus("current")
_HostInfoBootloaderVersion_Type = DisplayString
_HostInfoBootloaderVersion_Object = MibTableColumn
hostInfoBootloaderVersion = _HostInfoBootloaderVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 2, 1, 4),
    _HostInfoBootloaderVersion_Type()
)
hostInfoBootloaderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostInfoBootloaderVersion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-RESOURCE-MIB",
    **{"resource": resource,
       "rscBoardTable": rscBoardTable,
       "rscBoardEntry": rscBoardEntry,
       "rscStkId": rscStkId,
       "rscResourceId": rscResourceId,
       "rscBoardType": rscBoardType,
       "rscBoardName": rscBoardName,
       "rscBoardID": rscBoardID,
       "rscBoardBay": rscBoardBay,
       "rscBoardRevision": rscBoardRevision,
       "rscBoardSerialNumber": rscBoardSerialNumber,
       "hostInfoTable": hostInfoTable,
       "hostInfoEntry": hostInfoEntry,
       "hostInfoDRAM": hostInfoDRAM,
       "hostInfoFlash": hostInfoFlash,
       "hostInfoUptime": hostInfoUptime,
       "hostInfoBootloaderVersion": hostInfoBootloaderVersion}
)
