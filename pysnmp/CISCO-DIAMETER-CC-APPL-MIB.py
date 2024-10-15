# SNMP MIB module (CISCO-DIAMETER-CC-APPL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DIAMETER-CC-APPL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:01 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

ciscoDiameterCCAMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 575)
)
ciscoDiameterCCAMIB.setRevisions(
        ("2006-08-23 00:01",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoDiameterCCAMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoDiameterCCAMIBNotifs = _CiscoDiameterCCAMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 0)
)
_CiscoDiameterCCAMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDiameterCCAMIBObjects = _CiscoDiameterCCAMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1)
)
_CdccaHostCfgs_ObjectIdentity = ObjectIdentity
cdccaHostCfgs = _CdccaHostCfgs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 1)
)
_CdccaHostId_Type = SnmpAdminString
_CdccaHostId_Object = MibScalar
cdccaHostId = _CdccaHostId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 1, 1),
    _CdccaHostId_Type()
)
cdccaHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaHostId.setStatus("current")
_CdccaHostIpAddrTable_Object = MibTable
cdccaHostIpAddrTable = _CdccaHostIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cdccaHostIpAddrTable.setStatus("current")
_CdccaHostIpAddrEntry_Object = MibTableRow
cdccaHostIpAddrEntry = _CdccaHostIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 1, 2, 1)
)
cdccaHostIpAddrEntry.setIndexNames(
    (0, "CISCO-DIAMETER-CC-APPL-MIB", "cdccaHostIpAddrIndex"),
)
if mibBuilder.loadTexts:
    cdccaHostIpAddrEntry.setStatus("current")


class _CdccaHostIpAddrIndex_Type(Unsigned32):
    """Custom type cdccaHostIpAddrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdccaHostIpAddrIndex_Type.__name__ = "Unsigned32"
_CdccaHostIpAddrIndex_Object = MibTableColumn
cdccaHostIpAddrIndex = _CdccaHostIpAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 1, 2, 1, 1),
    _CdccaHostIpAddrIndex_Type()
)
cdccaHostIpAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdccaHostIpAddrIndex.setStatus("current")
_CdccaHostIpAddrType_Type = InetAddressType
_CdccaHostIpAddrType_Object = MibTableColumn
cdccaHostIpAddrType = _CdccaHostIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 1, 2, 1, 2),
    _CdccaHostIpAddrType_Type()
)
cdccaHostIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaHostIpAddrType.setStatus("current")
_CdccaHostIpAddress_Type = InetAddress
_CdccaHostIpAddress_Object = MibTableColumn
cdccaHostIpAddress = _CdccaHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 1, 2, 1, 3),
    _CdccaHostIpAddress_Type()
)
cdccaHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaHostIpAddress.setStatus("current")
_CdccaPeerCfgs_ObjectIdentity = ObjectIdentity
cdccaPeerCfgs = _CdccaPeerCfgs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 2)
)
_CdccaPeerTable_Object = MibTable
cdccaPeerTable = _CdccaPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cdccaPeerTable.setStatus("current")
_CdccaPeerEntry_Object = MibTableRow
cdccaPeerEntry = _CdccaPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 2, 1, 1)
)
cdccaPeerEntry.setIndexNames(
    (0, "CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerIndex"),
)
if mibBuilder.loadTexts:
    cdccaPeerEntry.setStatus("current")


class _CdccaPeerIndex_Type(Unsigned32):
    """Custom type cdccaPeerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdccaPeerIndex_Type.__name__ = "Unsigned32"
_CdccaPeerIndex_Object = MibTableColumn
cdccaPeerIndex = _CdccaPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 2, 1, 1, 1),
    _CdccaPeerIndex_Type()
)
cdccaPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdccaPeerIndex.setStatus("current")
_CdccaPeerId_Type = SnmpAdminString
_CdccaPeerId_Object = MibTableColumn
cdccaPeerId = _CdccaPeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 2, 1, 1, 2),
    _CdccaPeerId_Type()
)
cdccaPeerId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdccaPeerId.setStatus("current")


class _CdccaPeerFirmwareRevision_Type(Unsigned32):
    """Custom type cdccaPeerFirmwareRevision based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdccaPeerFirmwareRevision_Type.__name__ = "Unsigned32"
_CdccaPeerFirmwareRevision_Object = MibTableColumn
cdccaPeerFirmwareRevision = _CdccaPeerFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 2, 1, 1, 3),
    _CdccaPeerFirmwareRevision_Type()
)
cdccaPeerFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaPeerFirmwareRevision.setStatus("current")


class _CdccaPeerStorageType_Type(StorageType):
    """Custom type cdccaPeerStorageType based on StorageType"""


_CdccaPeerStorageType_Object = MibTableColumn
cdccaPeerStorageType = _CdccaPeerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 2, 1, 1, 4),
    _CdccaPeerStorageType_Type()
)
cdccaPeerStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdccaPeerStorageType.setStatus("current")
_CdccaPeerRowStatus_Type = RowStatus
_CdccaPeerRowStatus_Object = MibTableColumn
cdccaPeerRowStatus = _CdccaPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 2, 1, 1, 5),
    _CdccaPeerRowStatus_Type()
)
cdccaPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdccaPeerRowStatus.setStatus("current")
_CdccaPeerVendorTable_Object = MibTable
cdccaPeerVendorTable = _CdccaPeerVendorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cdccaPeerVendorTable.setStatus("current")
_CdccaPeerVendorEntry_Object = MibTableRow
cdccaPeerVendorEntry = _CdccaPeerVendorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 2, 2, 1)
)
cdccaPeerVendorEntry.setIndexNames(
    (0, "CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerIndex"),
    (0, "CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerVendorIndex"),
)
if mibBuilder.loadTexts:
    cdccaPeerVendorEntry.setStatus("current")


class _CdccaPeerVendorIndex_Type(Unsigned32):
    """Custom type cdccaPeerVendorIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdccaPeerVendorIndex_Type.__name__ = "Unsigned32"
_CdccaPeerVendorIndex_Object = MibTableColumn
cdccaPeerVendorIndex = _CdccaPeerVendorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 2, 2, 1, 1),
    _CdccaPeerVendorIndex_Type()
)
cdccaPeerVendorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdccaPeerVendorIndex.setStatus("current")
_CdccaPeerVendorId_Type = Unsigned32
_CdccaPeerVendorId_Object = MibTableColumn
cdccaPeerVendorId = _CdccaPeerVendorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 2, 2, 1, 2),
    _CdccaPeerVendorId_Type()
)
cdccaPeerVendorId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdccaPeerVendorId.setStatus("current")


class _CdccaPeerVendorStorageType_Type(StorageType):
    """Custom type cdccaPeerVendorStorageType based on StorageType"""


_CdccaPeerVendorStorageType_Object = MibTableColumn
cdccaPeerVendorStorageType = _CdccaPeerVendorStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 2, 2, 1, 3),
    _CdccaPeerVendorStorageType_Type()
)
cdccaPeerVendorStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdccaPeerVendorStorageType.setStatus("current")
_CdccaPeerVendorRowStatus_Type = RowStatus
_CdccaPeerVendorRowStatus_Object = MibTableColumn
cdccaPeerVendorRowStatus = _CdccaPeerVendorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 2, 2, 1, 4),
    _CdccaPeerVendorRowStatus_Type()
)
cdccaPeerVendorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdccaPeerVendorRowStatus.setStatus("current")
_CdccaPeerStats_ObjectIdentity = ObjectIdentity
cdccaPeerStats = _CdccaPeerStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 3)
)
_CdccaPeerStatsTable_Object = MibTable
cdccaPeerStatsTable = _CdccaPeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cdccaPeerStatsTable.setStatus("current")
_CdccaPeerStatsEntry_Object = MibTableRow
cdccaPeerStatsEntry = _CdccaPeerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 3, 1, 1)
)
cdccaPeerStatsEntry.setIndexNames(
    (0, "CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerIndex"),
)
if mibBuilder.loadTexts:
    cdccaPeerStatsEntry.setStatus("current")
_CdccaPeerStatsCCRIn_Type = Counter32
_CdccaPeerStatsCCRIn_Object = MibTableColumn
cdccaPeerStatsCCRIn = _CdccaPeerStatsCCRIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 3, 1, 1, 1),
    _CdccaPeerStatsCCRIn_Type()
)
cdccaPeerStatsCCRIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaPeerStatsCCRIn.setStatus("current")
if mibBuilder.loadTexts:
    cdccaPeerStatsCCRIn.setUnits("messages")
_CdccaPeerStatsCCROut_Type = Counter32
_CdccaPeerStatsCCROut_Object = MibTableColumn
cdccaPeerStatsCCROut = _CdccaPeerStatsCCROut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 3, 1, 1, 2),
    _CdccaPeerStatsCCROut_Type()
)
cdccaPeerStatsCCROut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaPeerStatsCCROut.setStatus("current")
if mibBuilder.loadTexts:
    cdccaPeerStatsCCROut.setUnits("messages")
_CdccaPeerStatsCCRDropped_Type = Counter32
_CdccaPeerStatsCCRDropped_Object = MibTableColumn
cdccaPeerStatsCCRDropped = _CdccaPeerStatsCCRDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 3, 1, 1, 3),
    _CdccaPeerStatsCCRDropped_Type()
)
cdccaPeerStatsCCRDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaPeerStatsCCRDropped.setStatus("current")
if mibBuilder.loadTexts:
    cdccaPeerStatsCCRDropped.setUnits("messages")
_CdccaPeerStatsCCAIn_Type = Counter32
_CdccaPeerStatsCCAIn_Object = MibTableColumn
cdccaPeerStatsCCAIn = _CdccaPeerStatsCCAIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 3, 1, 1, 4),
    _CdccaPeerStatsCCAIn_Type()
)
cdccaPeerStatsCCAIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaPeerStatsCCAIn.setStatus("current")
if mibBuilder.loadTexts:
    cdccaPeerStatsCCAIn.setUnits("messages")
_CdccaPeerStatsCCAOut_Type = Counter32
_CdccaPeerStatsCCAOut_Object = MibTableColumn
cdccaPeerStatsCCAOut = _CdccaPeerStatsCCAOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 3, 1, 1, 5),
    _CdccaPeerStatsCCAOut_Type()
)
cdccaPeerStatsCCAOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaPeerStatsCCAOut.setStatus("current")
if mibBuilder.loadTexts:
    cdccaPeerStatsCCAOut.setUnits("messages")
_CdccaPeerStatsCCADropped_Type = Counter32
_CdccaPeerStatsCCADropped_Object = MibTableColumn
cdccaPeerStatsCCADropped = _CdccaPeerStatsCCADropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 3, 1, 1, 6),
    _CdccaPeerStatsCCADropped_Type()
)
cdccaPeerStatsCCADropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaPeerStatsCCADropped.setStatus("current")
if mibBuilder.loadTexts:
    cdccaPeerStatsCCADropped.setUnits("messages")
_CdccaPeerStatsRARIn_Type = Counter32
_CdccaPeerStatsRARIn_Object = MibTableColumn
cdccaPeerStatsRARIn = _CdccaPeerStatsRARIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 3, 1, 1, 7),
    _CdccaPeerStatsRARIn_Type()
)
cdccaPeerStatsRARIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaPeerStatsRARIn.setStatus("current")
if mibBuilder.loadTexts:
    cdccaPeerStatsRARIn.setUnits("messages")
_CdccaPeerStatsRARDropped_Type = Counter32
_CdccaPeerStatsRARDropped_Object = MibTableColumn
cdccaPeerStatsRARDropped = _CdccaPeerStatsRARDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 3, 1, 1, 8),
    _CdccaPeerStatsRARDropped_Type()
)
cdccaPeerStatsRARDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaPeerStatsRARDropped.setStatus("current")
if mibBuilder.loadTexts:
    cdccaPeerStatsRARDropped.setUnits("messages")
_CdccaPeerStatsRAAOut_Type = Counter32
_CdccaPeerStatsRAAOut_Object = MibTableColumn
cdccaPeerStatsRAAOut = _CdccaPeerStatsRAAOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 3, 1, 1, 9),
    _CdccaPeerStatsRAAOut_Type()
)
cdccaPeerStatsRAAOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaPeerStatsRAAOut.setStatus("current")
if mibBuilder.loadTexts:
    cdccaPeerStatsRAAOut.setUnits("messages")
_CdccaPeerStatsRAADropped_Type = Counter32
_CdccaPeerStatsRAADropped_Object = MibTableColumn
cdccaPeerStatsRAADropped = _CdccaPeerStatsRAADropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 3, 1, 1, 10),
    _CdccaPeerStatsRAADropped_Type()
)
cdccaPeerStatsRAADropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaPeerStatsRAADropped.setStatus("current")
if mibBuilder.loadTexts:
    cdccaPeerStatsRAADropped.setUnits("messages")
_CdccaPeerStatsSTROut_Type = Counter32
_CdccaPeerStatsSTROut_Object = MibTableColumn
cdccaPeerStatsSTROut = _CdccaPeerStatsSTROut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 3, 1, 1, 11),
    _CdccaPeerStatsSTROut_Type()
)
cdccaPeerStatsSTROut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaPeerStatsSTROut.setStatus("current")
if mibBuilder.loadTexts:
    cdccaPeerStatsSTROut.setUnits("messages")
_CdccaPeerStatsSTRDropped_Type = Counter32
_CdccaPeerStatsSTRDropped_Object = MibTableColumn
cdccaPeerStatsSTRDropped = _CdccaPeerStatsSTRDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 3, 1, 1, 12),
    _CdccaPeerStatsSTRDropped_Type()
)
cdccaPeerStatsSTRDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaPeerStatsSTRDropped.setStatus("current")
if mibBuilder.loadTexts:
    cdccaPeerStatsSTRDropped.setUnits("messages")
_CdccaPeerStatsSTAIn_Type = Counter32
_CdccaPeerStatsSTAIn_Object = MibTableColumn
cdccaPeerStatsSTAIn = _CdccaPeerStatsSTAIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 3, 1, 1, 13),
    _CdccaPeerStatsSTAIn_Type()
)
cdccaPeerStatsSTAIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaPeerStatsSTAIn.setStatus("current")
if mibBuilder.loadTexts:
    cdccaPeerStatsSTAIn.setUnits("messages")
_CdccaPeerStatsSTADropped_Type = Counter32
_CdccaPeerStatsSTADropped_Object = MibTableColumn
cdccaPeerStatsSTADropped = _CdccaPeerStatsSTADropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 3, 1, 1, 14),
    _CdccaPeerStatsSTADropped_Type()
)
cdccaPeerStatsSTADropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaPeerStatsSTADropped.setStatus("current")
if mibBuilder.loadTexts:
    cdccaPeerStatsSTADropped.setUnits("messages")
_CdccaPeerStatsAAROut_Type = Counter32
_CdccaPeerStatsAAROut_Object = MibTableColumn
cdccaPeerStatsAAROut = _CdccaPeerStatsAAROut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 3, 1, 1, 15),
    _CdccaPeerStatsAAROut_Type()
)
cdccaPeerStatsAAROut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaPeerStatsAAROut.setStatus("current")
if mibBuilder.loadTexts:
    cdccaPeerStatsAAROut.setUnits("messages")
_CdccaPeerStatsAARDropped_Type = Counter32
_CdccaPeerStatsAARDropped_Object = MibTableColumn
cdccaPeerStatsAARDropped = _CdccaPeerStatsAARDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 3, 1, 1, 16),
    _CdccaPeerStatsAARDropped_Type()
)
cdccaPeerStatsAARDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaPeerStatsAARDropped.setStatus("current")
if mibBuilder.loadTexts:
    cdccaPeerStatsAARDropped.setUnits("messages")
_CdccaPeerStatsAAAIn_Type = Counter32
_CdccaPeerStatsAAAIn_Object = MibTableColumn
cdccaPeerStatsAAAIn = _CdccaPeerStatsAAAIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 3, 1, 1, 17),
    _CdccaPeerStatsAAAIn_Type()
)
cdccaPeerStatsAAAIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaPeerStatsAAAIn.setStatus("current")
if mibBuilder.loadTexts:
    cdccaPeerStatsAAAIn.setUnits("messages")
_CdccaPeerStatsAAADropped_Type = Counter32
_CdccaPeerStatsAAADropped_Object = MibTableColumn
cdccaPeerStatsAAADropped = _CdccaPeerStatsAAADropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 3, 1, 1, 18),
    _CdccaPeerStatsAAADropped_Type()
)
cdccaPeerStatsAAADropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaPeerStatsAAADropped.setStatus("current")
if mibBuilder.loadTexts:
    cdccaPeerStatsAAADropped.setUnits("messages")
_CdccaPeerStatsASRIn_Type = Counter32
_CdccaPeerStatsASRIn_Object = MibTableColumn
cdccaPeerStatsASRIn = _CdccaPeerStatsASRIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 3, 1, 1, 19),
    _CdccaPeerStatsASRIn_Type()
)
cdccaPeerStatsASRIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaPeerStatsASRIn.setStatus("current")
if mibBuilder.loadTexts:
    cdccaPeerStatsASRIn.setUnits("messages")
_CdccaPeerStatsASRDropped_Type = Counter32
_CdccaPeerStatsASRDropped_Object = MibTableColumn
cdccaPeerStatsASRDropped = _CdccaPeerStatsASRDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 3, 1, 1, 20),
    _CdccaPeerStatsASRDropped_Type()
)
cdccaPeerStatsASRDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaPeerStatsASRDropped.setStatus("current")
if mibBuilder.loadTexts:
    cdccaPeerStatsASRDropped.setUnits("messages")
_CdccaPeerStatsASAOut_Type = Counter32
_CdccaPeerStatsASAOut_Object = MibTableColumn
cdccaPeerStatsASAOut = _CdccaPeerStatsASAOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 3, 1, 1, 21),
    _CdccaPeerStatsASAOut_Type()
)
cdccaPeerStatsASAOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaPeerStatsASAOut.setStatus("current")
if mibBuilder.loadTexts:
    cdccaPeerStatsASAOut.setUnits("messages")
_CdccaPeerStatsASADropped_Type = Counter32
_CdccaPeerStatsASADropped_Object = MibTableColumn
cdccaPeerStatsASADropped = _CdccaPeerStatsASADropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 1, 3, 1, 1, 22),
    _CdccaPeerStatsASADropped_Type()
)
cdccaPeerStatsASADropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdccaPeerStatsASADropped.setStatus("current")
if mibBuilder.loadTexts:
    cdccaPeerStatsASADropped.setUnits("messages")
_CiscoDiameterCCAMIBConform_ObjectIdentity = ObjectIdentity
ciscoDiameterCCAMIBConform = _CiscoDiameterCCAMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 2)
)
_CiscoDiameterCCAMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDiameterCCAMIBCompliances = _CiscoDiameterCCAMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 2, 1)
)
_CiscoDiameterCCAMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDiameterCCAMIBGroups = _CiscoDiameterCCAMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 2, 2)
)

# Managed Objects groups

ciscoDiameterCCAHostCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 2, 2, 1)
)
ciscoDiameterCCAHostCfgGroup.setObjects(
      *(("CISCO-DIAMETER-CC-APPL-MIB", "cdccaHostIpAddrType"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaHostIpAddress"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaHostId"))
)
if mibBuilder.loadTexts:
    ciscoDiameterCCAHostCfgGroup.setStatus("current")

ciscoDiameterCCAPeerCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 2, 2, 2)
)
ciscoDiameterCCAPeerCfgGroup.setObjects(
      *(("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerId"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerVendorId"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerStorageType"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerVendorStorageType"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerFirmwareRevision"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerRowStatus"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerVendorRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoDiameterCCAPeerCfgGroup.setStatus("current")

ciscoDiameterCCAPeerStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 2, 2, 3)
)
ciscoDiameterCCAPeerStatsGroup.setObjects(
      *(("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerStatsCCRIn"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerStatsCCROut"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerStatsCCRDropped"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerStatsCCAIn"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerStatsCCAOut"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerStatsCCADropped"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerStatsRARIn"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerStatsRARDropped"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerStatsRAAOut"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerStatsRAADropped"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerStatsSTROut"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerStatsSTRDropped"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerStatsSTAIn"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerStatsSTADropped"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerStatsAAROut"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerStatsAARDropped"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerStatsAAAIn"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerStatsAAADropped"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerStatsASRIn"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerStatsASRDropped"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerStatsASAOut"),
        ("CISCO-DIAMETER-CC-APPL-MIB", "cdccaPeerStatsASADropped"))
)
if mibBuilder.loadTexts:
    ciscoDiameterCCAPeerStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoDiameterCCAMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 575, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDiameterCCAMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DIAMETER-CC-APPL-MIB",
    **{"ciscoDiameterCCAMIB": ciscoDiameterCCAMIB,
       "ciscoDiameterCCAMIBNotifs": ciscoDiameterCCAMIBNotifs,
       "ciscoDiameterCCAMIBObjects": ciscoDiameterCCAMIBObjects,
       "cdccaHostCfgs": cdccaHostCfgs,
       "cdccaHostId": cdccaHostId,
       "cdccaHostIpAddrTable": cdccaHostIpAddrTable,
       "cdccaHostIpAddrEntry": cdccaHostIpAddrEntry,
       "cdccaHostIpAddrIndex": cdccaHostIpAddrIndex,
       "cdccaHostIpAddrType": cdccaHostIpAddrType,
       "cdccaHostIpAddress": cdccaHostIpAddress,
       "cdccaPeerCfgs": cdccaPeerCfgs,
       "cdccaPeerTable": cdccaPeerTable,
       "cdccaPeerEntry": cdccaPeerEntry,
       "cdccaPeerIndex": cdccaPeerIndex,
       "cdccaPeerId": cdccaPeerId,
       "cdccaPeerFirmwareRevision": cdccaPeerFirmwareRevision,
       "cdccaPeerStorageType": cdccaPeerStorageType,
       "cdccaPeerRowStatus": cdccaPeerRowStatus,
       "cdccaPeerVendorTable": cdccaPeerVendorTable,
       "cdccaPeerVendorEntry": cdccaPeerVendorEntry,
       "cdccaPeerVendorIndex": cdccaPeerVendorIndex,
       "cdccaPeerVendorId": cdccaPeerVendorId,
       "cdccaPeerVendorStorageType": cdccaPeerVendorStorageType,
       "cdccaPeerVendorRowStatus": cdccaPeerVendorRowStatus,
       "cdccaPeerStats": cdccaPeerStats,
       "cdccaPeerStatsTable": cdccaPeerStatsTable,
       "cdccaPeerStatsEntry": cdccaPeerStatsEntry,
       "cdccaPeerStatsCCRIn": cdccaPeerStatsCCRIn,
       "cdccaPeerStatsCCROut": cdccaPeerStatsCCROut,
       "cdccaPeerStatsCCRDropped": cdccaPeerStatsCCRDropped,
       "cdccaPeerStatsCCAIn": cdccaPeerStatsCCAIn,
       "cdccaPeerStatsCCAOut": cdccaPeerStatsCCAOut,
       "cdccaPeerStatsCCADropped": cdccaPeerStatsCCADropped,
       "cdccaPeerStatsRARIn": cdccaPeerStatsRARIn,
       "cdccaPeerStatsRARDropped": cdccaPeerStatsRARDropped,
       "cdccaPeerStatsRAAOut": cdccaPeerStatsRAAOut,
       "cdccaPeerStatsRAADropped": cdccaPeerStatsRAADropped,
       "cdccaPeerStatsSTROut": cdccaPeerStatsSTROut,
       "cdccaPeerStatsSTRDropped": cdccaPeerStatsSTRDropped,
       "cdccaPeerStatsSTAIn": cdccaPeerStatsSTAIn,
       "cdccaPeerStatsSTADropped": cdccaPeerStatsSTADropped,
       "cdccaPeerStatsAAROut": cdccaPeerStatsAAROut,
       "cdccaPeerStatsAARDropped": cdccaPeerStatsAARDropped,
       "cdccaPeerStatsAAAIn": cdccaPeerStatsAAAIn,
       "cdccaPeerStatsAAADropped": cdccaPeerStatsAAADropped,
       "cdccaPeerStatsASRIn": cdccaPeerStatsASRIn,
       "cdccaPeerStatsASRDropped": cdccaPeerStatsASRDropped,
       "cdccaPeerStatsASAOut": cdccaPeerStatsASAOut,
       "cdccaPeerStatsASADropped": cdccaPeerStatsASADropped,
       "ciscoDiameterCCAMIBConform": ciscoDiameterCCAMIBConform,
       "ciscoDiameterCCAMIBCompliances": ciscoDiameterCCAMIBCompliances,
       "ciscoDiameterCCAMIBCompliance": ciscoDiameterCCAMIBCompliance,
       "ciscoDiameterCCAMIBGroups": ciscoDiameterCCAMIBGroups,
       "ciscoDiameterCCAHostCfgGroup": ciscoDiameterCCAHostCfgGroup,
       "ciscoDiameterCCAPeerCfgGroup": ciscoDiameterCCAPeerCfgGroup,
       "ciscoDiameterCCAPeerStatsGroup": ciscoDiameterCCAPeerStatsGroup}
)
