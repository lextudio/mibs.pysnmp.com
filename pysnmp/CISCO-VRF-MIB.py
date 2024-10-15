# SNMP MIB module (CISCO-VRF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VRF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:37 2024
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

(InterfaceIndex,
 ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex",
    "ifName")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoVrfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 711)
)
ciscoVrfMIB.setRevisions(
        ("2009-12-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CvVrfIfType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vNETEdge", 2),
          ("vNETTrunkSI", 1),
          ("vrfEdge", 3))
    )



class CvVnetTagOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoVrfMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoVrfMIBNotifs = _CiscoVrfMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 0)
)
_CiscoVrfMIBObjects_ObjectIdentity = ObjectIdentity
ciscoVrfMIBObjects = _CiscoVrfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1)
)
_CvVrf_ObjectIdentity = ObjectIdentity
cvVrf = _CvVrf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 1)
)
_CvVrfTable_Object = MibTable
cvVrfTable = _CvVrfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cvVrfTable.setStatus("current")
_CvVrfEntry_Object = MibTableRow
cvVrfEntry = _CvVrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 1, 1, 1)
)
cvVrfEntry.setIndexNames(
    (0, "CISCO-VRF-MIB", "cvVrfIndex"),
)
if mibBuilder.loadTexts:
    cvVrfEntry.setStatus("current")


class _CvVrfIndex_Type(Unsigned32):
    """Custom type cvVrfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CvVrfIndex_Type.__name__ = "Unsigned32"
_CvVrfIndex_Object = MibTableColumn
cvVrfIndex = _CvVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 1, 1, 1, 1),
    _CvVrfIndex_Type()
)
cvVrfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvVrfIndex.setStatus("current")


class _CvVrfName_Type(SnmpAdminString):
    """Custom type cvVrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CvVrfName_Type.__name__ = "SnmpAdminString"
_CvVrfName_Object = MibTableColumn
cvVrfName = _CvVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 1, 1, 1, 2),
    _CvVrfName_Type()
)
cvVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvVrfName.setStatus("current")


class _CvVrfVnetTag_Type(CvVnetTagOrZero):
    """Custom type cvVrfVnetTag based on CvVnetTagOrZero"""
    defaultValue = 0

    subtypeSpec = CvVnetTagOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4094),
    )


_CvVrfVnetTag_Type.__name__ = "CvVnetTagOrZero"
_CvVrfVnetTag_Object = MibTableColumn
cvVrfVnetTag = _CvVrfVnetTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 1, 1, 1, 3),
    _CvVrfVnetTag_Type()
)
cvVrfVnetTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvVrfVnetTag.setStatus("current")


class _CvVrfOperStatus_Type(Integer32):
    """Custom type cvVrfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CvVrfOperStatus_Type.__name__ = "Integer32"
_CvVrfOperStatus_Object = MibTableColumn
cvVrfOperStatus = _CvVrfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 1, 1, 1, 4),
    _CvVrfOperStatus_Type()
)
cvVrfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVrfOperStatus.setStatus("current")


class _CvVrfRouteDistProt_Type(Bits):
    """Custom type cvVrfRouteDistProt based on Bits"""
    namedValues = NamedValues(
        *(("bgp", 6),
          ("eigrp", 5),
          ("isis", 4),
          ("none", 0),
          ("ospf", 2),
          ("other", 1),
          ("rip", 3))
    )

_CvVrfRouteDistProt_Type.__name__ = "Bits"
_CvVrfRouteDistProt_Object = MibTableColumn
cvVrfRouteDistProt = _CvVrfRouteDistProt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 1, 1, 1, 5),
    _CvVrfRouteDistProt_Type()
)
cvVrfRouteDistProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVrfRouteDistProt.setStatus("current")
_CvVrfStorageType_Type = StorageType
_CvVrfStorageType_Object = MibTableColumn
cvVrfStorageType = _CvVrfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 1, 1, 1, 6),
    _CvVrfStorageType_Type()
)
cvVrfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVrfStorageType.setStatus("current")
_CvVrfRowStatus_Type = RowStatus
_CvVrfRowStatus_Object = MibTableColumn
cvVrfRowStatus = _CvVrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 1, 1, 1, 7),
    _CvVrfRowStatus_Type()
)
cvVrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvVrfRowStatus.setStatus("current")
_CvVrfListTable_Object = MibTable
cvVrfListTable = _CvVrfListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cvVrfListTable.setStatus("current")
_CvVrfListEntry_Object = MibTableRow
cvVrfListEntry = _CvVrfListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 1, 2, 1)
)
cvVrfListEntry.setIndexNames(
    (0, "CISCO-VRF-MIB", "cvVrfListName"),
    (0, "CISCO-VRF-MIB", "cvVrfListVindex"),
)
if mibBuilder.loadTexts:
    cvVrfListEntry.setStatus("current")


class _CvVrfListName_Type(SnmpAdminString):
    """Custom type cvVrfListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CvVrfListName_Type.__name__ = "SnmpAdminString"
_CvVrfListName_Object = MibTableColumn
cvVrfListName = _CvVrfListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 1, 2, 1, 1),
    _CvVrfListName_Type()
)
cvVrfListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvVrfListName.setStatus("current")


class _CvVrfListVindex_Type(Unsigned32):
    """Custom type cvVrfListVindex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CvVrfListVindex_Type.__name__ = "Unsigned32"
_CvVrfListVindex_Object = MibTableColumn
cvVrfListVindex = _CvVrfListVindex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 1, 2, 1, 2),
    _CvVrfListVindex_Type()
)
cvVrfListVindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvVrfListVindex.setStatus("current")


class _CvVrfListVrfIndex_Type(Unsigned32):
    """Custom type cvVrfListVrfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CvVrfListVrfIndex_Type.__name__ = "Unsigned32"
_CvVrfListVrfIndex_Object = MibTableColumn
cvVrfListVrfIndex = _CvVrfListVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 1, 2, 1, 3),
    _CvVrfListVrfIndex_Type()
)
cvVrfListVrfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvVrfListVrfIndex.setStatus("current")
_CvVrfListStorageType_Type = StorageType
_CvVrfListStorageType_Object = MibTableColumn
cvVrfListStorageType = _CvVrfListStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 1, 2, 1, 4),
    _CvVrfListStorageType_Type()
)
cvVrfListStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVrfListStorageType.setStatus("current")
_CvVrfListRowStatus_Type = RowStatus
_CvVrfListRowStatus_Object = MibTableColumn
cvVrfListRowStatus = _CvVrfListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 1, 2, 1, 5),
    _CvVrfListRowStatus_Type()
)
cvVrfListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvVrfListRowStatus.setStatus("current")
_CvInterface_ObjectIdentity = ObjectIdentity
cvInterface = _CvInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 2)
)
_CvVrfInterfaceTable_Object = MibTable
cvVrfInterfaceTable = _CvVrfInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cvVrfInterfaceTable.setStatus("current")
_CvVrfInterfaceEntry_Object = MibTableRow
cvVrfInterfaceEntry = _CvVrfInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 2, 1, 1)
)
cvVrfInterfaceEntry.setIndexNames(
    (0, "CISCO-VRF-MIB", "cvVrfIndex"),
    (0, "CISCO-VRF-MIB", "cvVrfInterfaceIndex"),
)
if mibBuilder.loadTexts:
    cvVrfInterfaceEntry.setStatus("current")


class _CvVrfInterfaceIndex_Type(InterfaceIndex):
    """Custom type cvVrfInterfaceIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvVrfInterfaceIndex_Type.__name__ = "InterfaceIndex"
_CvVrfInterfaceIndex_Object = MibTableColumn
cvVrfInterfaceIndex = _CvVrfInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 2, 1, 1, 1),
    _CvVrfInterfaceIndex_Type()
)
cvVrfInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvVrfInterfaceIndex.setStatus("current")
_CvVrfInterfaceType_Type = CvVrfIfType
_CvVrfInterfaceType_Object = MibTableColumn
cvVrfInterfaceType = _CvVrfInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 2, 1, 1, 2),
    _CvVrfInterfaceType_Type()
)
cvVrfInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVrfInterfaceType.setStatus("current")


class _CvVrfInterfaceVnetTagOverride_Type(CvVnetTagOrZero):
    """Custom type cvVrfInterfaceVnetTagOverride based on CvVnetTagOrZero"""
    defaultValue = 0

    subtypeSpec = CvVnetTagOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4094),
    )


_CvVrfInterfaceVnetTagOverride_Type.__name__ = "CvVnetTagOrZero"
_CvVrfInterfaceVnetTagOverride_Object = MibTableColumn
cvVrfInterfaceVnetTagOverride = _CvVrfInterfaceVnetTagOverride_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 2, 1, 1, 3),
    _CvVrfInterfaceVnetTagOverride_Type()
)
cvVrfInterfaceVnetTagOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvVrfInterfaceVnetTagOverride.setStatus("current")
_CvVrfInterfaceStorageType_Type = StorageType
_CvVrfInterfaceStorageType_Object = MibTableColumn
cvVrfInterfaceStorageType = _CvVrfInterfaceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 2, 1, 1, 4),
    _CvVrfInterfaceStorageType_Type()
)
cvVrfInterfaceStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVrfInterfaceStorageType.setStatus("current")
_CvVrfInterfaceRowStatus_Type = RowStatus
_CvVrfInterfaceRowStatus_Object = MibTableColumn
cvVrfInterfaceRowStatus = _CvVrfInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 2, 1, 1, 5),
    _CvVrfInterfaceRowStatus_Type()
)
cvVrfInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvVrfInterfaceRowStatus.setStatus("current")
_CvInterfaceTable_Object = MibTable
cvInterfaceTable = _CvInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cvInterfaceTable.setStatus("current")
_CvInterfaceEntry_Object = MibTableRow
cvInterfaceEntry = _CvInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 2, 2, 1)
)
cvInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cvInterfaceEntry.setStatus("current")


class _CvInterfaceVnetTrunkEnabled_Type(TruthValue):
    """Custom type cvInterfaceVnetTrunkEnabled based on TruthValue"""


_CvInterfaceVnetTrunkEnabled_Object = MibTableColumn
cvInterfaceVnetTrunkEnabled = _CvInterfaceVnetTrunkEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 2, 2, 1, 1),
    _CvInterfaceVnetTrunkEnabled_Type()
)
cvInterfaceVnetTrunkEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvInterfaceVnetTrunkEnabled.setStatus("current")


class _CvInterfaceVnetVrfList_Type(SnmpAdminString):
    """Custom type cvInterfaceVnetVrfList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )


_CvInterfaceVnetVrfList_Type.__name__ = "SnmpAdminString"
_CvInterfaceVnetVrfList_Object = MibTableColumn
cvInterfaceVnetVrfList = _CvInterfaceVnetVrfList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 2, 2, 1, 2),
    _CvInterfaceVnetVrfList_Type()
)
cvInterfaceVnetVrfList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvInterfaceVnetVrfList.setStatus("current")
_CvNotifCntl_ObjectIdentity = ObjectIdentity
cvNotifCntl = _CvNotifCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 3)
)


class _CvVrfIfNotifEnable_Type(TruthValue):
    """Custom type cvVrfIfNotifEnable based on TruthValue"""


_CvVrfIfNotifEnable_Object = MibScalar
cvVrfIfNotifEnable = _CvVrfIfNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 3, 1),
    _CvVrfIfNotifEnable_Type()
)
cvVrfIfNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVrfIfNotifEnable.setStatus("current")


class _CvVnetTrunkNotifEnable_Type(TruthValue):
    """Custom type cvVnetTrunkNotifEnable based on TruthValue"""


_CvVnetTrunkNotifEnable_Object = MibScalar
cvVnetTrunkNotifEnable = _CvVnetTrunkNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 1, 3, 2),
    _CvVnetTrunkNotifEnable_Type()
)
cvVnetTrunkNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVnetTrunkNotifEnable.setStatus("current")
_CiscoVrfMIBConform_ObjectIdentity = ObjectIdentity
ciscoVrfMIBConform = _CiscoVrfMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 2)
)
_CvMIBGroups_ObjectIdentity = ObjectIdentity
cvMIBGroups = _CvMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 2, 1)
)
_CvMIBCompliances_ObjectIdentity = ObjectIdentity
cvMIBCompliances = _CvMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 2, 2)
)

# Managed Objects groups

cvMIBVrfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 2, 1, 1)
)
cvMIBVrfGroup.setObjects(
      *(("CISCO-VRF-MIB", "cvVrfOperStatus"),
        ("CISCO-VRF-MIB", "cvVrfStorageType"),
        ("CISCO-VRF-MIB", "cvVrfRowStatus"),
        ("CISCO-VRF-MIB", "cvVrfRouteDistProt"),
        ("CISCO-VRF-MIB", "cvVrfInterfaceType"),
        ("CISCO-VRF-MIB", "cvVrfInterfaceStorageType"),
        ("CISCO-VRF-MIB", "cvVrfInterfaceRowStatus"),
        ("CISCO-VRF-MIB", "cvVrfIfNotifEnable"),
        ("CISCO-VRF-MIB", "cvVrfName"))
)
if mibBuilder.loadTexts:
    cvMIBVrfGroup.setStatus("current")

cvMIBVnetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 2, 1, 3)
)
cvMIBVnetGroup.setObjects(
      *(("CISCO-VRF-MIB", "cvVrfVnetTag"),
        ("CISCO-VRF-MIB", "cvVrfListVrfIndex"),
        ("CISCO-VRF-MIB", "cvVrfListStorageType"),
        ("CISCO-VRF-MIB", "cvVrfListRowStatus"),
        ("CISCO-VRF-MIB", "cvVrfInterfaceVnetTagOverride"),
        ("CISCO-VRF-MIB", "cvInterfaceVnetTrunkEnabled"),
        ("CISCO-VRF-MIB", "cvInterfaceVnetVrfList"),
        ("CISCO-VRF-MIB", "cvVnetTrunkNotifEnable"))
)
if mibBuilder.loadTexts:
    cvMIBVnetGroup.setStatus("current")


# Notification objects

cvVrfIfUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 0, 1)
)
cvVrfIfUp.setObjects(
      *(("IF-MIB", "ifName"),
        ("CISCO-VRF-MIB", "cvVrfName"),
        ("CISCO-VRF-MIB", "cvVrfOperStatus"))
)
if mibBuilder.loadTexts:
    cvVrfIfUp.setStatus(
        "current"
    )

cvVrfIfDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 0, 2)
)
cvVrfIfDown.setObjects(
      *(("IF-MIB", "ifName"),
        ("CISCO-VRF-MIB", "cvVrfName"),
        ("CISCO-VRF-MIB", "cvVrfOperStatus"))
)
if mibBuilder.loadTexts:
    cvVrfIfDown.setStatus(
        "current"
    )

cvVnetTrunkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 0, 3)
)
cvVnetTrunkUp.setObjects(
    ("IF-MIB", "ifName")
)
if mibBuilder.loadTexts:
    cvVnetTrunkUp.setStatus(
        "current"
    )

cvVnetTrunkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 0, 4)
)
cvVnetTrunkDown.setObjects(
    ("IF-MIB", "ifName")
)
if mibBuilder.loadTexts:
    cvVnetTrunkDown.setStatus(
        "current"
    )


# Notifications groups

cvMIBVrfNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 2, 1, 2)
)
cvMIBVrfNotifGroup.setObjects(
      *(("CISCO-VRF-MIB", "cvVrfIfUp"),
        ("CISCO-VRF-MIB", "cvVrfIfDown"))
)
if mibBuilder.loadTexts:
    cvMIBVrfNotifGroup.setStatus(
        "current"
    )

cvMIBVnetNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 2, 1, 4)
)
cvMIBVnetNotifGroup.setObjects(
      *(("CISCO-VRF-MIB", "cvVnetTrunkUp"),
        ("CISCO-VRF-MIB", "cvVnetTrunkDown"))
)
if mibBuilder.loadTexts:
    cvMIBVnetNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cvMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 711, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cvMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VRF-MIB",
    **{"CvVrfIfType": CvVrfIfType,
       "CvVnetTagOrZero": CvVnetTagOrZero,
       "ciscoVrfMIB": ciscoVrfMIB,
       "ciscoVrfMIBNotifs": ciscoVrfMIBNotifs,
       "cvVrfIfUp": cvVrfIfUp,
       "cvVrfIfDown": cvVrfIfDown,
       "cvVnetTrunkUp": cvVnetTrunkUp,
       "cvVnetTrunkDown": cvVnetTrunkDown,
       "ciscoVrfMIBObjects": ciscoVrfMIBObjects,
       "cvVrf": cvVrf,
       "cvVrfTable": cvVrfTable,
       "cvVrfEntry": cvVrfEntry,
       "cvVrfIndex": cvVrfIndex,
       "cvVrfName": cvVrfName,
       "cvVrfVnetTag": cvVrfVnetTag,
       "cvVrfOperStatus": cvVrfOperStatus,
       "cvVrfRouteDistProt": cvVrfRouteDistProt,
       "cvVrfStorageType": cvVrfStorageType,
       "cvVrfRowStatus": cvVrfRowStatus,
       "cvVrfListTable": cvVrfListTable,
       "cvVrfListEntry": cvVrfListEntry,
       "cvVrfListName": cvVrfListName,
       "cvVrfListVindex": cvVrfListVindex,
       "cvVrfListVrfIndex": cvVrfListVrfIndex,
       "cvVrfListStorageType": cvVrfListStorageType,
       "cvVrfListRowStatus": cvVrfListRowStatus,
       "cvInterface": cvInterface,
       "cvVrfInterfaceTable": cvVrfInterfaceTable,
       "cvVrfInterfaceEntry": cvVrfInterfaceEntry,
       "cvVrfInterfaceIndex": cvVrfInterfaceIndex,
       "cvVrfInterfaceType": cvVrfInterfaceType,
       "cvVrfInterfaceVnetTagOverride": cvVrfInterfaceVnetTagOverride,
       "cvVrfInterfaceStorageType": cvVrfInterfaceStorageType,
       "cvVrfInterfaceRowStatus": cvVrfInterfaceRowStatus,
       "cvInterfaceTable": cvInterfaceTable,
       "cvInterfaceEntry": cvInterfaceEntry,
       "cvInterfaceVnetTrunkEnabled": cvInterfaceVnetTrunkEnabled,
       "cvInterfaceVnetVrfList": cvInterfaceVnetVrfList,
       "cvNotifCntl": cvNotifCntl,
       "cvVrfIfNotifEnable": cvVrfIfNotifEnable,
       "cvVnetTrunkNotifEnable": cvVnetTrunkNotifEnable,
       "ciscoVrfMIBConform": ciscoVrfMIBConform,
       "cvMIBGroups": cvMIBGroups,
       "cvMIBVrfGroup": cvMIBVrfGroup,
       "cvMIBVrfNotifGroup": cvMIBVrfNotifGroup,
       "cvMIBVnetGroup": cvMIBVnetGroup,
       "cvMIBVnetNotifGroup": cvMIBVnetNotifGroup,
       "cvMIBCompliances": cvMIBCompliances,
       "cvMIBCompliance": cvMIBCompliance}
)
