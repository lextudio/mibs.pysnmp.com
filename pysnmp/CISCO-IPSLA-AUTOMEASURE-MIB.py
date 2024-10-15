# SNMP MIB module (CISCO-IPSLA-AUTOMEASURE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IPSLA-AUTOMEASURE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:56 2024
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

(IpSlaOperType,
 IpSlaReactVar) = mibBuilder.importSymbols(
    "CISCO-IPSLA-TC-MIB",
    "IpSlaOperType",
    "IpSlaReactVar")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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

ciscoIpSlaAutoMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 633)
)
ciscoIpSlaAutoMIB.setRevisions(
        ("2007-06-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIpSlaAutoMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIpSlaAutoMIBNotifs = _CiscoIpSlaAutoMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 0)
)
_CiscoIpSlaAutoMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIpSlaAutoMIBObjects = _CiscoIpSlaAutoMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1)
)
_CipslaAutoGroupTable_Object = MibTable
cipslaAutoGroupTable = _CipslaAutoGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1)
)
if mibBuilder.loadTexts:
    cipslaAutoGroupTable.setStatus("current")
_CipslaAutoGroupEntry_Object = MibTableRow
cipslaAutoGroupEntry = _CipslaAutoGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1)
)
cipslaAutoGroupEntry.setIndexNames(
    (0, "CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupName"),
)
if mibBuilder.loadTexts:
    cipslaAutoGroupEntry.setStatus("current")


class _CipslaAutoGroupName_Type(SnmpAdminString):
    """Custom type cipslaAutoGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CipslaAutoGroupName_Type.__name__ = "SnmpAdminString"
_CipslaAutoGroupName_Object = MibTableColumn
cipslaAutoGroupName = _CipslaAutoGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 1),
    _CipslaAutoGroupName_Type()
)
cipslaAutoGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipslaAutoGroupName.setStatus("current")


class _CipslaAutoGroupDescription_Type(SnmpAdminString):
    """Custom type cipslaAutoGroupDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CipslaAutoGroupDescription_Type.__name__ = "SnmpAdminString"
_CipslaAutoGroupDescription_Object = MibTableColumn
cipslaAutoGroupDescription = _CipslaAutoGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 2),
    _CipslaAutoGroupDescription_Type()
)
cipslaAutoGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaAutoGroupDescription.setStatus("current")


class _CipslaAutoGroupDestinationName_Type(SnmpAdminString):
    """Custom type cipslaAutoGroupDestinationName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CipslaAutoGroupDestinationName_Type.__name__ = "SnmpAdminString"
_CipslaAutoGroupDestinationName_Object = MibTableColumn
cipslaAutoGroupDestinationName = _CipslaAutoGroupDestinationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 3),
    _CipslaAutoGroupDestinationName_Type()
)
cipslaAutoGroupDestinationName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaAutoGroupDestinationName.setStatus("current")


class _CipslaAutoGroupADDestPort_Type(InetPortNumber):
    """Custom type cipslaAutoGroupADDestPort based on InetPortNumber"""
    defaultValue = 0


_CipslaAutoGroupADDestPort_Object = MibTableColumn
cipslaAutoGroupADDestPort = _CipslaAutoGroupADDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 4),
    _CipslaAutoGroupADDestPort_Type()
)
cipslaAutoGroupADDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaAutoGroupADDestPort.setStatus("current")


class _CipslaAutoGroupOperTemplateName_Type(SnmpAdminString):
    """Custom type cipslaAutoGroupOperTemplateName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CipslaAutoGroupOperTemplateName_Type.__name__ = "SnmpAdminString"
_CipslaAutoGroupOperTemplateName_Object = MibTableColumn
cipslaAutoGroupOperTemplateName = _CipslaAutoGroupOperTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 5),
    _CipslaAutoGroupOperTemplateName_Type()
)
cipslaAutoGroupOperTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaAutoGroupOperTemplateName.setStatus("current")


class _CipslaAutoGroupSchedulerId_Type(SnmpAdminString):
    """Custom type cipslaAutoGroupSchedulerId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CipslaAutoGroupSchedulerId_Type.__name__ = "SnmpAdminString"
_CipslaAutoGroupSchedulerId_Object = MibTableColumn
cipslaAutoGroupSchedulerId = _CipslaAutoGroupSchedulerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 6),
    _CipslaAutoGroupSchedulerId_Type()
)
cipslaAutoGroupSchedulerId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaAutoGroupSchedulerId.setStatus("current")


class _CipslaAutoGroupQoSEnable_Type(TruthValue):
    """Custom type cipslaAutoGroupQoSEnable based on TruthValue"""


_CipslaAutoGroupQoSEnable_Object = MibTableColumn
cipslaAutoGroupQoSEnable = _CipslaAutoGroupQoSEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 7),
    _CipslaAutoGroupQoSEnable_Type()
)
cipslaAutoGroupQoSEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaAutoGroupQoSEnable.setStatus("current")
_CipslaAutoGroupOperType_Type = IpSlaOperType
_CipslaAutoGroupOperType_Object = MibTableColumn
cipslaAutoGroupOperType = _CipslaAutoGroupOperType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 8),
    _CipslaAutoGroupOperType_Type()
)
cipslaAutoGroupOperType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaAutoGroupOperType.setStatus("current")


class _CipslaAutoGroupDestIPADEnable_Type(TruthValue):
    """Custom type cipslaAutoGroupDestIPADEnable based on TruthValue"""


_CipslaAutoGroupDestIPADEnable_Object = MibTableColumn
cipslaAutoGroupDestIPADEnable = _CipslaAutoGroupDestIPADEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 9),
    _CipslaAutoGroupDestIPADEnable_Type()
)
cipslaAutoGroupDestIPADEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaAutoGroupDestIPADEnable.setStatus("current")


class _CipslaAutoGroupADMeasureRetry_Type(Unsigned32):
    """Custom type cipslaAutoGroupADMeasureRetry based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_CipslaAutoGroupADMeasureRetry_Type.__name__ = "Unsigned32"
_CipslaAutoGroupADMeasureRetry_Object = MibTableColumn
cipslaAutoGroupADMeasureRetry = _CipslaAutoGroupADMeasureRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 10),
    _CipslaAutoGroupADMeasureRetry_Type()
)
cipslaAutoGroupADMeasureRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaAutoGroupADMeasureRetry.setStatus("current")


class _CipslaAutoGroupADDestIPAgeout_Type(Unsigned32):
    """Custom type cipslaAutoGroupADDestIPAgeout based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CipslaAutoGroupADDestIPAgeout_Type.__name__ = "Unsigned32"
_CipslaAutoGroupADDestIPAgeout_Object = MibTableColumn
cipslaAutoGroupADDestIPAgeout = _CipslaAutoGroupADDestIPAgeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 11),
    _CipslaAutoGroupADDestIPAgeout_Type()
)
cipslaAutoGroupADDestIPAgeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaAutoGroupADDestIPAgeout.setStatus("current")
if mibBuilder.loadTexts:
    cipslaAutoGroupADDestIPAgeout.setUnits("seconds")


class _CipslaAutoGroupStorageType_Type(StorageType):
    """Custom type cipslaAutoGroupStorageType based on StorageType"""


_CipslaAutoGroupStorageType_Object = MibTableColumn
cipslaAutoGroupStorageType = _CipslaAutoGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 12),
    _CipslaAutoGroupStorageType_Type()
)
cipslaAutoGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaAutoGroupStorageType.setStatus("current")
_CipslaAutoGroupRowStatus_Type = RowStatus
_CipslaAutoGroupRowStatus_Object = MibTableColumn
cipslaAutoGroupRowStatus = _CipslaAutoGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 13),
    _CipslaAutoGroupRowStatus_Type()
)
cipslaAutoGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaAutoGroupRowStatus.setStatus("current")
_CipslaAutoGroupDestTable_Object = MibTable
cipslaAutoGroupDestTable = _CipslaAutoGroupDestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 2)
)
if mibBuilder.loadTexts:
    cipslaAutoGroupDestTable.setStatus("current")
_CipslaAutoGroupDestEntry_Object = MibTableRow
cipslaAutoGroupDestEntry = _CipslaAutoGroupDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 2, 1)
)
cipslaAutoGroupDestEntry.setIndexNames(
    (0, "CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupDestName"),
    (0, "CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupDestIpAddrType"),
    (0, "CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupDestIpAddr"),
    (0, "CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupDestPort"),
)
if mibBuilder.loadTexts:
    cipslaAutoGroupDestEntry.setStatus("current")


class _CipslaAutoGroupDestName_Type(SnmpAdminString):
    """Custom type cipslaAutoGroupDestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CipslaAutoGroupDestName_Type.__name__ = "SnmpAdminString"
_CipslaAutoGroupDestName_Object = MibTableColumn
cipslaAutoGroupDestName = _CipslaAutoGroupDestName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 2, 1, 1),
    _CipslaAutoGroupDestName_Type()
)
cipslaAutoGroupDestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipslaAutoGroupDestName.setStatus("current")
_CipslaAutoGroupDestIpAddrType_Type = InetAddressType
_CipslaAutoGroupDestIpAddrType_Object = MibTableColumn
cipslaAutoGroupDestIpAddrType = _CipslaAutoGroupDestIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 2, 1, 2),
    _CipslaAutoGroupDestIpAddrType_Type()
)
cipslaAutoGroupDestIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipslaAutoGroupDestIpAddrType.setStatus("current")
_CipslaAutoGroupDestIpAddr_Type = InetAddress
_CipslaAutoGroupDestIpAddr_Object = MibTableColumn
cipslaAutoGroupDestIpAddr = _CipslaAutoGroupDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 2, 1, 3),
    _CipslaAutoGroupDestIpAddr_Type()
)
cipslaAutoGroupDestIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipslaAutoGroupDestIpAddr.setStatus("current")
_CipslaAutoGroupDestPort_Type = InetPortNumber
_CipslaAutoGroupDestPort_Object = MibTableColumn
cipslaAutoGroupDestPort = _CipslaAutoGroupDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 2, 1, 4),
    _CipslaAutoGroupDestPort_Type()
)
cipslaAutoGroupDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipslaAutoGroupDestPort.setStatus("current")


class _CipslaAutoGroupDestStorageType_Type(StorageType):
    """Custom type cipslaAutoGroupDestStorageType based on StorageType"""


_CipslaAutoGroupDestStorageType_Object = MibTableColumn
cipslaAutoGroupDestStorageType = _CipslaAutoGroupDestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 2, 1, 5),
    _CipslaAutoGroupDestStorageType_Type()
)
cipslaAutoGroupDestStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaAutoGroupDestStorageType.setStatus("current")
_CipslaAutoGroupDestRowStatus_Type = RowStatus
_CipslaAutoGroupDestRowStatus_Object = MibTableColumn
cipslaAutoGroupDestRowStatus = _CipslaAutoGroupDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 2, 1, 6),
    _CipslaAutoGroupDestRowStatus_Type()
)
cipslaAutoGroupDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaAutoGroupDestRowStatus.setStatus("current")
_CipslaReactTable_Object = MibTable
cipslaReactTable = _CipslaReactTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 3)
)
if mibBuilder.loadTexts:
    cipslaReactTable.setStatus("current")
_CipslaReactEntry_Object = MibTableRow
cipslaReactEntry = _CipslaReactEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 3, 1)
)
cipslaReactEntry.setIndexNames(
    (0, "CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupOperType"),
    (0, "CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaReactConfigIndex"),
    (0, "CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupOperTemplateName"),
)
if mibBuilder.loadTexts:
    cipslaReactEntry.setStatus("current")


class _CipslaReactConfigIndex_Type(Unsigned32):
    """Custom type cipslaReactConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CipslaReactConfigIndex_Type.__name__ = "Unsigned32"
_CipslaReactConfigIndex_Object = MibTableColumn
cipslaReactConfigIndex = _CipslaReactConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 3, 1, 1),
    _CipslaReactConfigIndex_Type()
)
cipslaReactConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipslaReactConfigIndex.setStatus("current")
_CipslaReactVar_Type = IpSlaReactVar
_CipslaReactVar_Object = MibTableColumn
cipslaReactVar = _CipslaReactVar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 3, 1, 2),
    _CipslaReactVar_Type()
)
cipslaReactVar.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaReactVar.setStatus("current")


class _CipslaReactThresholdType_Type(Integer32):
    """Custom type cipslaReactThresholdType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("average", 5),
          ("consecutive", 3),
          ("immediate", 2),
          ("never", 1),
          ("xOfy", 4))
    )


_CipslaReactThresholdType_Type.__name__ = "Integer32"
_CipslaReactThresholdType_Object = MibTableColumn
cipslaReactThresholdType = _CipslaReactThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 3, 1, 3),
    _CipslaReactThresholdType_Type()
)
cipslaReactThresholdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaReactThresholdType.setStatus("current")


class _CipslaReactActionType_Type(Integer32):
    """Custom type cipslaReactActionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("notificationOnly", 2))
    )


_CipslaReactActionType_Type.__name__ = "Integer32"
_CipslaReactActionType_Object = MibTableColumn
cipslaReactActionType = _CipslaReactActionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 3, 1, 4),
    _CipslaReactActionType_Type()
)
cipslaReactActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaReactActionType.setStatus("current")
_CipslaReactThresholdRising_Type = Unsigned32
_CipslaReactThresholdRising_Object = MibTableColumn
cipslaReactThresholdRising = _CipslaReactThresholdRising_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 3, 1, 5),
    _CipslaReactThresholdRising_Type()
)
cipslaReactThresholdRising.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaReactThresholdRising.setStatus("current")
_CipslaReactThresholdFalling_Type = Unsigned32
_CipslaReactThresholdFalling_Object = MibTableColumn
cipslaReactThresholdFalling = _CipslaReactThresholdFalling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 3, 1, 6),
    _CipslaReactThresholdFalling_Type()
)
cipslaReactThresholdFalling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaReactThresholdFalling.setStatus("current")


class _CipslaReactThresholdCountX_Type(Unsigned32):
    """Custom type cipslaReactThresholdCountX based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CipslaReactThresholdCountX_Type.__name__ = "Unsigned32"
_CipslaReactThresholdCountX_Object = MibTableColumn
cipslaReactThresholdCountX = _CipslaReactThresholdCountX_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 3, 1, 7),
    _CipslaReactThresholdCountX_Type()
)
cipslaReactThresholdCountX.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaReactThresholdCountX.setStatus("current")


class _CipslaReactThresholdCountY_Type(Unsigned32):
    """Custom type cipslaReactThresholdCountY based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CipslaReactThresholdCountY_Type.__name__ = "Unsigned32"
_CipslaReactThresholdCountY_Object = MibTableColumn
cipslaReactThresholdCountY = _CipslaReactThresholdCountY_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 3, 1, 8),
    _CipslaReactThresholdCountY_Type()
)
cipslaReactThresholdCountY.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaReactThresholdCountY.setStatus("current")


class _CipslaReactStorageType_Type(StorageType):
    """Custom type cipslaReactStorageType based on StorageType"""


_CipslaReactStorageType_Object = MibTableColumn
cipslaReactStorageType = _CipslaReactStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 3, 1, 9),
    _CipslaReactStorageType_Type()
)
cipslaReactStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaReactStorageType.setStatus("current")
_CipslaReactRowStatus_Type = RowStatus
_CipslaReactRowStatus_Object = MibTableColumn
cipslaReactRowStatus = _CipslaReactRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 3, 1, 10),
    _CipslaReactRowStatus_Type()
)
cipslaReactRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaReactRowStatus.setStatus("current")
_CipslaAutoGroupSchedTable_Object = MibTable
cipslaAutoGroupSchedTable = _CipslaAutoGroupSchedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 4)
)
if mibBuilder.loadTexts:
    cipslaAutoGroupSchedTable.setStatus("current")
_CipslaAutoGroupSchedEntry_Object = MibTableRow
cipslaAutoGroupSchedEntry = _CipslaAutoGroupSchedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 4, 1)
)
cipslaAutoGroupSchedEntry.setIndexNames(
    (0, "CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupSchedId"),
)
if mibBuilder.loadTexts:
    cipslaAutoGroupSchedEntry.setStatus("current")


class _CipslaAutoGroupSchedId_Type(SnmpAdminString):
    """Custom type cipslaAutoGroupSchedId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CipslaAutoGroupSchedId_Type.__name__ = "SnmpAdminString"
_CipslaAutoGroupSchedId_Object = MibTableColumn
cipslaAutoGroupSchedId = _CipslaAutoGroupSchedId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 4, 1, 1),
    _CipslaAutoGroupSchedId_Type()
)
cipslaAutoGroupSchedId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipslaAutoGroupSchedId.setStatus("current")


class _CipslaAutoGroupSchedPeriod_Type(Unsigned32):
    """Custom type cipslaAutoGroupSchedPeriod based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 99000),
    )


_CipslaAutoGroupSchedPeriod_Type.__name__ = "Unsigned32"
_CipslaAutoGroupSchedPeriod_Object = MibTableColumn
cipslaAutoGroupSchedPeriod = _CipslaAutoGroupSchedPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 4, 1, 2),
    _CipslaAutoGroupSchedPeriod_Type()
)
cipslaAutoGroupSchedPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaAutoGroupSchedPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cipslaAutoGroupSchedPeriod.setUnits("seconds")


class _CipslaAutoGroupSchedInterval_Type(Unsigned32):
    """Custom type cipslaAutoGroupSchedInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_CipslaAutoGroupSchedInterval_Type.__name__ = "Unsigned32"
_CipslaAutoGroupSchedInterval_Object = MibTableColumn
cipslaAutoGroupSchedInterval = _CipslaAutoGroupSchedInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 4, 1, 3),
    _CipslaAutoGroupSchedInterval_Type()
)
cipslaAutoGroupSchedInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaAutoGroupSchedInterval.setStatus("current")
if mibBuilder.loadTexts:
    cipslaAutoGroupSchedInterval.setUnits("seconds")


class _CipslaAutoGroupSchedLife_Type(Unsigned32):
    """Custom type cipslaAutoGroupSchedLife based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CipslaAutoGroupSchedLife_Type.__name__ = "Unsigned32"
_CipslaAutoGroupSchedLife_Object = MibTableColumn
cipslaAutoGroupSchedLife = _CipslaAutoGroupSchedLife_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 4, 1, 4),
    _CipslaAutoGroupSchedLife_Type()
)
cipslaAutoGroupSchedLife.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaAutoGroupSchedLife.setStatus("current")
if mibBuilder.loadTexts:
    cipslaAutoGroupSchedLife.setUnits("seconds")


class _CipslaAutoGroupSchedAgeout_Type(Unsigned32):
    """Custom type cipslaAutoGroupSchedAgeout based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2073600),
    )


_CipslaAutoGroupSchedAgeout_Type.__name__ = "Unsigned32"
_CipslaAutoGroupSchedAgeout_Object = MibTableColumn
cipslaAutoGroupSchedAgeout = _CipslaAutoGroupSchedAgeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 4, 1, 5),
    _CipslaAutoGroupSchedAgeout_Type()
)
cipslaAutoGroupSchedAgeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaAutoGroupSchedAgeout.setStatus("current")
if mibBuilder.loadTexts:
    cipslaAutoGroupSchedAgeout.setUnits("seconds")


class _CipslaAutoGroupSchedMaxInterval_Type(Unsigned32):
    """Custom type cipslaAutoGroupSchedMaxInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_CipslaAutoGroupSchedMaxInterval_Type.__name__ = "Unsigned32"
_CipslaAutoGroupSchedMaxInterval_Object = MibTableColumn
cipslaAutoGroupSchedMaxInterval = _CipslaAutoGroupSchedMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 4, 1, 6),
    _CipslaAutoGroupSchedMaxInterval_Type()
)
cipslaAutoGroupSchedMaxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaAutoGroupSchedMaxInterval.setStatus("current")
if mibBuilder.loadTexts:
    cipslaAutoGroupSchedMaxInterval.setUnits("seconds")


class _CipslaAutoGroupSchedMinInterval_Type(Unsigned32):
    """Custom type cipslaAutoGroupSchedMinInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_CipslaAutoGroupSchedMinInterval_Type.__name__ = "Unsigned32"
_CipslaAutoGroupSchedMinInterval_Object = MibTableColumn
cipslaAutoGroupSchedMinInterval = _CipslaAutoGroupSchedMinInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 4, 1, 7),
    _CipslaAutoGroupSchedMinInterval_Type()
)
cipslaAutoGroupSchedMinInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaAutoGroupSchedMinInterval.setStatus("current")
if mibBuilder.loadTexts:
    cipslaAutoGroupSchedMinInterval.setUnits("seconds")


class _CipslaAutoGroupSchedStartTime_Type(Unsigned32):
    """Custom type cipslaAutoGroupSchedStartTime based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_CipslaAutoGroupSchedStartTime_Type.__name__ = "Unsigned32"
_CipslaAutoGroupSchedStartTime_Object = MibTableColumn
cipslaAutoGroupSchedStartTime = _CipslaAutoGroupSchedStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 4, 1, 8),
    _CipslaAutoGroupSchedStartTime_Type()
)
cipslaAutoGroupSchedStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaAutoGroupSchedStartTime.setStatus("current")
if mibBuilder.loadTexts:
    cipslaAutoGroupSchedStartTime.setUnits("seconds")


class _CipslaAutoGroupSchedStorageType_Type(StorageType):
    """Custom type cipslaAutoGroupSchedStorageType based on StorageType"""


_CipslaAutoGroupSchedStorageType_Object = MibTableColumn
cipslaAutoGroupSchedStorageType = _CipslaAutoGroupSchedStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 4, 1, 9),
    _CipslaAutoGroupSchedStorageType_Type()
)
cipslaAutoGroupSchedStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaAutoGroupSchedStorageType.setStatus("current")
_CipslaAutoGroupSchedRowStatus_Type = RowStatus
_CipslaAutoGroupSchedRowStatus_Object = MibTableColumn
cipslaAutoGroupSchedRowStatus = _CipslaAutoGroupSchedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 4, 1, 10),
    _CipslaAutoGroupSchedRowStatus_Type()
)
cipslaAutoGroupSchedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaAutoGroupSchedRowStatus.setStatus("current")
_CiscoIpSlaAutoMIBConform_ObjectIdentity = ObjectIdentity
ciscoIpSlaAutoMIBConform = _CiscoIpSlaAutoMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 2)
)
_CiscoIpSlaAutoMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIpSlaAutoMIBCompliances = _CiscoIpSlaAutoMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 2, 1)
)
_CiscoIpSlaAutoMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIpSlaAutoMIBGroups = _CiscoIpSlaAutoMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 2, 2)
)

# Managed Objects groups

ciscoIpSlaAutoGroupConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 2, 2, 1)
)
ciscoIpSlaAutoGroupConfGroup.setObjects(
      *(("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupDescription"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupDestinationName"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupADDestPort"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupOperTemplateName"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupSchedulerId"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupQoSEnable"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupOperType"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupDestIPADEnable"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupADMeasureRetry"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupADDestIPAgeout"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupStorageType"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoIpSlaAutoGroupConfGroup.setStatus("current")

ciscoIpSlaAutoGroupDestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 2, 2, 2)
)
ciscoIpSlaAutoGroupDestGroup.setObjects(
      *(("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupDestStorageType"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupDestRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoIpSlaAutoGroupDestGroup.setStatus("current")

ciscoIpSlaAutoGroupReactGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 2, 2, 3)
)
ciscoIpSlaAutoGroupReactGroup.setObjects(
      *(("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaReactVar"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaReactThresholdType"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaReactActionType"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaReactThresholdRising"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaReactThresholdFalling"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaReactThresholdCountX"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaReactThresholdCountY"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaReactStorageType"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaReactRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoIpSlaAutoGroupReactGroup.setStatus("current")

ciscoIpSlaAutoGroupSchedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 2, 2, 4)
)
ciscoIpSlaAutoGroupSchedGroup.setObjects(
      *(("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupSchedPeriod"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupSchedInterval"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupSchedLife"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupSchedAgeout"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupSchedMaxInterval"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupSchedMinInterval"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupSchedStartTime"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupSchedStorageType"),
        ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupSchedRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoIpSlaAutoGroupSchedGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoIpSlaAutoMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 633, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIpSlaAutoMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IPSLA-AUTOMEASURE-MIB",
    **{"ciscoIpSlaAutoMIB": ciscoIpSlaAutoMIB,
       "ciscoIpSlaAutoMIBNotifs": ciscoIpSlaAutoMIBNotifs,
       "ciscoIpSlaAutoMIBObjects": ciscoIpSlaAutoMIBObjects,
       "cipslaAutoGroupTable": cipslaAutoGroupTable,
       "cipslaAutoGroupEntry": cipslaAutoGroupEntry,
       "cipslaAutoGroupName": cipslaAutoGroupName,
       "cipslaAutoGroupDescription": cipslaAutoGroupDescription,
       "cipslaAutoGroupDestinationName": cipslaAutoGroupDestinationName,
       "cipslaAutoGroupADDestPort": cipslaAutoGroupADDestPort,
       "cipslaAutoGroupOperTemplateName": cipslaAutoGroupOperTemplateName,
       "cipslaAutoGroupSchedulerId": cipslaAutoGroupSchedulerId,
       "cipslaAutoGroupQoSEnable": cipslaAutoGroupQoSEnable,
       "cipslaAutoGroupOperType": cipslaAutoGroupOperType,
       "cipslaAutoGroupDestIPADEnable": cipslaAutoGroupDestIPADEnable,
       "cipslaAutoGroupADMeasureRetry": cipslaAutoGroupADMeasureRetry,
       "cipslaAutoGroupADDestIPAgeout": cipslaAutoGroupADDestIPAgeout,
       "cipslaAutoGroupStorageType": cipslaAutoGroupStorageType,
       "cipslaAutoGroupRowStatus": cipslaAutoGroupRowStatus,
       "cipslaAutoGroupDestTable": cipslaAutoGroupDestTable,
       "cipslaAutoGroupDestEntry": cipslaAutoGroupDestEntry,
       "cipslaAutoGroupDestName": cipslaAutoGroupDestName,
       "cipslaAutoGroupDestIpAddrType": cipslaAutoGroupDestIpAddrType,
       "cipslaAutoGroupDestIpAddr": cipslaAutoGroupDestIpAddr,
       "cipslaAutoGroupDestPort": cipslaAutoGroupDestPort,
       "cipslaAutoGroupDestStorageType": cipslaAutoGroupDestStorageType,
       "cipslaAutoGroupDestRowStatus": cipslaAutoGroupDestRowStatus,
       "cipslaReactTable": cipslaReactTable,
       "cipslaReactEntry": cipslaReactEntry,
       "cipslaReactConfigIndex": cipslaReactConfigIndex,
       "cipslaReactVar": cipslaReactVar,
       "cipslaReactThresholdType": cipslaReactThresholdType,
       "cipslaReactActionType": cipslaReactActionType,
       "cipslaReactThresholdRising": cipslaReactThresholdRising,
       "cipslaReactThresholdFalling": cipslaReactThresholdFalling,
       "cipslaReactThresholdCountX": cipslaReactThresholdCountX,
       "cipslaReactThresholdCountY": cipslaReactThresholdCountY,
       "cipslaReactStorageType": cipslaReactStorageType,
       "cipslaReactRowStatus": cipslaReactRowStatus,
       "cipslaAutoGroupSchedTable": cipslaAutoGroupSchedTable,
       "cipslaAutoGroupSchedEntry": cipslaAutoGroupSchedEntry,
       "cipslaAutoGroupSchedId": cipslaAutoGroupSchedId,
       "cipslaAutoGroupSchedPeriod": cipslaAutoGroupSchedPeriod,
       "cipslaAutoGroupSchedInterval": cipslaAutoGroupSchedInterval,
       "cipslaAutoGroupSchedLife": cipslaAutoGroupSchedLife,
       "cipslaAutoGroupSchedAgeout": cipslaAutoGroupSchedAgeout,
       "cipslaAutoGroupSchedMaxInterval": cipslaAutoGroupSchedMaxInterval,
       "cipslaAutoGroupSchedMinInterval": cipslaAutoGroupSchedMinInterval,
       "cipslaAutoGroupSchedStartTime": cipslaAutoGroupSchedStartTime,
       "cipslaAutoGroupSchedStorageType": cipslaAutoGroupSchedStorageType,
       "cipslaAutoGroupSchedRowStatus": cipslaAutoGroupSchedRowStatus,
       "ciscoIpSlaAutoMIBConform": ciscoIpSlaAutoMIBConform,
       "ciscoIpSlaAutoMIBCompliances": ciscoIpSlaAutoMIBCompliances,
       "ciscoIpSlaAutoMIBCompliance": ciscoIpSlaAutoMIBCompliance,
       "ciscoIpSlaAutoMIBGroups": ciscoIpSlaAutoMIBGroups,
       "ciscoIpSlaAutoGroupConfGroup": ciscoIpSlaAutoGroupConfGroup,
       "ciscoIpSlaAutoGroupDestGroup": ciscoIpSlaAutoGroupDestGroup,
       "ciscoIpSlaAutoGroupReactGroup": ciscoIpSlaAutoGroupReactGroup,
       "ciscoIpSlaAutoGroupSchedGroup": ciscoIpSlaAutoGroupSchedGroup}
)
